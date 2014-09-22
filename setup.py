from setuptools import setup

setup(
    name='migrate',
    version='0.1',
    py_modules=['migrate'],
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        migrate=migrate:migrate
    ''',
)
