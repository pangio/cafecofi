#!/bin/sh

#curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -

#sudo apt-get install -y nodejs

echo "--<< NODEJS: installing NVM"
cat <<EOF | sudo -s
su vagrant
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash
. ~/.nvm/nvm.sh
nvm install 4.2.2
nvm use 4.2.2
nvm alias default 4.2.2
cd ~ && sudo cp -r .nvm/versions/node/v4.2.2/bin/node /usr/bin
npm install npm@2.14.7 -g
EOF



