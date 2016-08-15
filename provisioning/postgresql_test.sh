#!/bin/sh
NOMAD_TEST_DB=nomad_test
NOMAD_TEST_USER=nomad_test
NOMAD_TEST_PASS=nomad_test

###############################################################################

echo "--<< Postgres: Create role and database"

cat <<EOF | sudo -u postgres psql
\c template1
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
\c postgres
CREATE USER ${NOMAD_TEST_USER} WITH ENCRYPTED PASSWORD '${NOMAD_TEST_PASS}';
CREATE DATABASE ${NOMAD_TEST_DB} with OWNER ${NOMAD_TEST_USER};
EOF

echo "--<< Postgres: Create pgpass"

echo "localhost:5432:${NOMAD_TEST_DB}:${NOMAD_TEST_USER}:${NOMAD_TEST_PASS}" | tee ~/.pgpass /home/vagrant/.pgpass

service postgresql restart

cat <<EOF | psql -h localhost -d ${NOMAD_TEST_USER}  -U ${NOMAD_TEST_USER}
CREATE SCHEMA ${NOMAD_TEST_DB} AUTHORIZATION ${NOMAD_TEST_USER};
EOF

echo "--<< Postgres: Done"

