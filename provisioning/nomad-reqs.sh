#!/bin/sh

PREFIX=/vagrant/

APT_PACKAGES="
  gcc
  git
  python2.7
  python-dev
  python-pip
  libtiff4-dev
  libjpeg8-dev
  zlib1g-dev
  libfreetype6-dev
  liblcms2-dev
  libwebp-dev
  tcl8.5-dev
  tk8.5-dev
  python-tk
  "

PIP_PACKAGES="
  psycopg2
  uwsgi
  "

###############################################################################

echo "--<< NOMAD: install package dependencies"

unset packages
for pkg in ${APT_PACKAGES}; do
  [ -z "${pkg}" ] && continue 
  [ -z "$(dpkg -l ${pkg} 2>/dev/null | grep '^ii')" ] && packages="${packages} ${pkg}"
done

sudo apt-get update
sudo apt-get install -y ${packages}

echo "--<< NOMAD: install pip predependencies"

for pkg in ${PIP_PACKAGES}; do
  sudo pip install ${pkg}
done

echo "--<< NOMAD: install pip requirements"

cd ${PREFIX} && sudo pip install -r requirements.txt && cd -

echo "--<< Logs"

mkdir -p /opt/data

echo "--<< Symlinks"

if [ ! -d "/opt/nomad/vagrant" ]; then
  mkdir -p /opt/nomad && ln -s /vagrant/nomad /opt/nomad/vagrant
fi



