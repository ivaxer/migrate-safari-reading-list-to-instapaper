# Safari Reading List to Instapaper migrator

To migrate your Reading List from Safari to Instapaper run:

    git clone https://github.com/ivaxer/migrate-safari-reading-list-to-instapaper.git
    cd migrate-safari-reading-list-to-instapaper
    virtualenv --python=python3 env
    . env/bin/activate
    python setup.py install
    migrate --help
    migrate -u instapaper_account # -p password if set

Script uses only [Instapaper's Simple API](https://www.instapaper.com/api/simple), which doesn't require premium account. Therefore `migrate` can't sync read/unread statuses and skip already added articles.
