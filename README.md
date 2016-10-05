# hansel-api
A backend API for use with the hansel iOS App


To develop locally:

 - Make sure you have `python3` and `venv` package.
 - `echo 'PRODUCTION = False' > api/ignored.py`
 - `pyvenev env`
 - `pip install -r requirements.txt`
 - `./manage.py migrate`
 - `./manage.py createsuperuser`
 - `./manage.py runserver`
 
 Read the [restless docs](http://restless.readthedocs.io/).
