SETUP:

Requirements:
+ Vagrant 1.7.4
+ VirtualBox 5.0.0

In the main directory:
    vagrant up
    vagrant provision

Connect to vagrant:
    vagrant ssh

Install dependencies:
    cd /vagrant

    Run: sudo pip install -r requirements.txt

Init db:

    python manage.py setup_nomad

Run app:

    python manage.py runserver --host 0.0.0.0 --port 5000 (vagrant corre con 0.0.0.0 como localhost)


Postgres:
Connect to db: \connect dbname
Show tables: \dt



-------

Included in validation:
- Coffee Shop Manager form
- Clients form
- WEB (landing page)
- CMS coffee shops and clients
