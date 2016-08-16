# Requirements
+ Vagrant 1.7.4
+ VirtualBox 5.0.0

# Vagrant
1 run: `vagrant up`

2 setup: `vagrant provision`

3 connect: `vagrant ssh`

# Install dependencies
```cd /vagrant 
sudo pip install -r requirements.txt```

# Run app
    `python manage.py runserver --host 0.0.0.0 --port 5000 (vagrant corre con 0.0.0.0 como localhost)`

# Postgres
Init DB: `python manage.py setup_nomad`
Connect to db: `\connect dbname`
Show tables: `\dt`



-------

Included in validation:
- Coffee Shop Manager form
- Clients form
- WEB (landing page)
- CMS coffee shops and clients
