Steps to run app:

Inside vagrant:

Install dependencies:

    sudo pip install -r requirements.txt

Init db:

    python manage.py setup_nomad

Run app:

    python manage.py runserver --host 0.0.0.0 --port 5000 (vagrant corre con 0.0.0.0 como localhost)


Postgres:
\connect dbname
\dt show tables