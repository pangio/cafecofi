#!/bin/sh

PACKAGES="
  redis-server
  redis-tools
"

###############################################################################

echo "--<< Redis: Install packages"

for pkg in ${PACKAGES}; do
  # Skip empty lines
  [ -z "${pkg}" ] && continue
  # Install the package if missing
  [ -z "$(dpkg -l ${pkg} 2>/dev/null)" ] && \
    sudo apt-get install -y ${pkg}
done

redis-cli ping

echo "--<< Redis: Done"

