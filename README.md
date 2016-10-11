# hansel-api
A backend API for use with the hansel iOS App


To develop locally:

 - Make sure you have `python3` and `venv` package.
 - `echo $'PRODUCTION = False\nTOP_SECRET_KEY="092h30f9hw0ihsofjsoif4ijfpij2"' > api/ignored.py`
 - `pyvenev env`
 - `source env/bin/activate`
 - `pip install -r requirements.txt`
 - `./manage.py migrate`
 - `./manage.py createsuperuser`
 - `./manage.py runserver`
 
 Read the [restless docs](http://restless.readthedocs.io/).
