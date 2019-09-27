# Ayasakura

Program Silab.

## Installation

1. Default environment is `Development`, if you want to change to `Production` change environment setting on `wsgi.py` and `manage.py` to `Ayasakura.settings.production`, or you can add your own environment in `Ayasakura/Ayasakura/settings/`.

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Nymphaea dependencies.

```bash
pip install script/requirements.txt
```

3. Migrate all tables to database, make sure you configure `your environment` first before do this part.

```bash
python manage.py migrate
```

## Usage

1. For development .

```bash
python manage.py runserver
```

2. For Production (with gunicorn)

```bash
gunicorn Ayasakura.wsgi -w <number or workers> --bind <ip_address>:<port_destination> &
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
1. Fork this git .
2. Make a *branch* what-a-feature   : `git checkout -b my-new-feature`
3. *Commit* changes                 : `git commit -am 'Add some features'`
4. *Push* branch to *remote*        : `git push origin my-new-feature`
5. Make a *pull request*

Please make sure to update tests as appropriate.

## Changelog
[Read Changelog](https://github.com/aldamr01/Ayasakura/blob/master/changelog.md)

## License
[GNU GPL V3.0](https://github.com/aldamr01/Ayasakura/license.txt)

