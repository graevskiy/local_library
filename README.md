# local_library

Local library is a Django tutorial project from MDN located at
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

## Instalation

First you need Python 3 and probably pip installed. We created it using 3.7.2 version.

It's highly recommended to install virtualenv and install all packages in it.

If you don't have virtualenv installed do following:

```bash
pip install virtualenv
```

Once done, activate it and go to project root directory.

Install packages located in requirements.txt.

Project uses SQLite DB in development.

```bash
pip install -r requirements.txt
```

Once you have all your packages installed you need to create db.sqlite3 file.
