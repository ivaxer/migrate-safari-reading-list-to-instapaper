import sys
import plistlib
import os.path

import click
import requests

@click.command()
@click.option("-u", "--username", prompt="Enter your Instapaper username or email",
	help="An Instapaper user account.")
@click.option("-p", "--password", help="Account's password.")
@click.option("-f", "--plist", type=click.Path(readable=True, resolve_path=True),
	help="Path to Safari's Bookmarks.plist, which located in ~/Library/Safari.")
def migrate(username, password, plist):
	if plist is None:
		plist = os.path.join(os.path.expanduser('~'), "Library/Safari/Bookmarks.plist")
	root = plistlib.load(open(plist, "rb"))
	readingList = findReadingList(root)
	if not readingList:
		click.secho("Nothing to migrate: reading list empty or not available.", err=True, fg="red")
		return
	for child in reversed(readingList["Children"]):
		add(username, password, child["URLString"])

def findReadingList(root):
	for child in root["Children"]:
		if child["Title"] == "com.apple.ReadingList":
			return child

errors = {
	400: "Bad request",
	403: "Invalid username or password",
	500: "The service encountered an error. Please try again later",
}

def add(username, password, url, title=None, selection=None):
	payload = {'url': url}
	if title:
		payload['title'] = title
	if selection:
		payload['selection'] = selection

	r = requests.post("https://www.instapaper.com/api/add", params=payload,
		auth=(username, password))
	if r.status_code == 201:
		click.secho("Added {0}...".format(url), err=True, fg="green")
		return
	msg = errors.get(r.status_code, "Unknown error")
	click.secho("Failed to add url: {0}: [{1}] {2}".format(url, r.status_code, msg), err=True, fg="red")
	sys.exit(1)


if __name__ == '__main__':
	migrate()