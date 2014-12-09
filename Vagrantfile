# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "python2-sandbox" do |sandbox|
    sandbox.vm.box = "ubuntu/trusty64"
    sandbox.vm.hostname = "python2-sandbox.dev"
    sandbox.vm.network "private_network", ip: "192.168.100.102"
    sandbox.vm.synced_folder "./python2",  "/home/vagrant/python2"
    sandbox.vm.provider "virtualbox" do |vb|
      vb.name = "python2-sandbox"
      vb.memory = 512
      vb.cpus = 1
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
    end
    sandbox.vm.provision :shell, :path => "provision.sh"
  end
end
