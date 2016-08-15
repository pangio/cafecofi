#!/bin/sh

NOMAD_DB=nomad
NOMAD_USER=nomad
NOMAD_PASS=nomadpass
NOMAD_DUMP=/vagrant/provisioning/nomad_database.sql.gz

PACKAGES="
  postgresql-client-9.4
  postgresql-contrib-9.4
  postgresql-server-dev-9.4
  postgresql-9.4
  libpq-dev
"

###############################################################################

echo "--<< Postgres: Install packages"
> /etc/apt/sources.list.d/pgdg.list
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list.d/pgdg.list

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  sudo apt-key add -
sudo apt-get update

for pkg in ${PACKAGES}; do
  # Skip empty lines
  [ -z "${pkg}" ] && continue
  # Install the package if missing
  [ -z "$(dpkg -l ${pkg} 2>/dev/null)" ] && \
    sudo apt-get install -y ${pkg}
done

echo "--<< Postgres: Create role and database"

cat <<EOF | sudo -u postgres psql
\c template1
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
\c postgres
CREATE USER ${NOMAD_USER} WITH ENCRYPTED PASSWORD '${NOMAD_PASS}';
CREATE DATABASE ${NOMAD_DB} with OWNER ${NOMAD_USER};
EOF

echo "--<< Postgres: Create pgpass"

echo "localhost:5432:${NOMAD_DB}:${NOMAD_USER}:${NOMAD_PASS}" | tee ~/.pgpass /home/vagrant/.pgpass

chmod 600 /root/.pgpass
chmod 600 /home/vagrant/.pgpass
chown vagrant: /home/vagrant/.pgpass

echo "--<< Postgres: Import data"

gunzip -c ${NOMAD_DUMP} | psql -U ${NOMAD_USER} -d ${NOMAD_DB} -h localhost

echo "--<< Postgres: Fix external connection"

sed -ire "s/^#\(listen_addresses\).*$/\1 = '*'/" /etc/postgresql/9.4/main/postgresql.conf

cat <<EOF >> /etc/postgresql/9.4/main/pg_hba.conf
host    all             all             0.0.0.0/0               md5
EOF

service postgresql restart

cat <<EOF | psql -h localhost -d ${NOMAD_USER}  -U ${NOMAD_USER}
CREATE SCHEMA ${NOMAD_DB} AUTHORIZATION ${NOMAD_USER};
EOF

echo "--<< Postgres: Done"

