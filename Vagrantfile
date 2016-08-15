VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box      = 'ubuntu/trusty64'
  config.vm.hostname = 'nomad'

  config.vm.network 'forwarded_port', guest: 5000,  host: 5000
  config.vm.network 'forwarded_port', guest: 5432,  host: 2345
  config.vm.network 'forwarded_port', guest: 6379,  host: 7890
  
  config.vm.network 'private_network', ip: '192.168.255.201'

  config.vm.provider :virtualbox do |vb|
    vb.gui = false
    vb.customize [ 'modifyvm', :id, '--memory', '2048' ]
    vb.customize [ 'modifyvm', :id, '--nictype1', 'virtio' ]
    vb.customize [ 'modifyvm', :id, '--natdnshostresolver1', 'on' ]
    vb.customize [ 'modifyvm', :id, '--natdnsproxy1', 'on' ]
  end
      
  config.vm.provision 'shell', inline: 'apt-get update'
  config.vm.provision 'shell', path:   'provisioning/postgresql.sh'
  config.vm.provision 'shell', path:   'provisioning/postgresql_test.sh'
  config.vm.provision 'shell', path:   'provisioning/redis.sh'
  config.vm.provision 'shell', path:   'provisioning/nomad-reqs.sh'
  config.vm.provision 'shell', path:   'provisioning/nodejs.sh'

end
  
# vi:ts=2:sw=2:et:ft=ruby:
