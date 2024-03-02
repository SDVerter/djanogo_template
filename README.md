# djanogo_template


python -m venv .venv --prompt djtempl
. .venv/bin/activate
pip install -r requirements.txt
django-admin startproject home .
django-admin startapp  app 
python manage.py migrate
python manage.py createsuperuser
