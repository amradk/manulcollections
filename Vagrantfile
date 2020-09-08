# -*- mode: ruby -*-
# vi: set ft=ruby :
vms = [
  {:v_name => 'bookshelf', :v_mem => 2048, :v_cpu => 2, :v_ip => '192.168.20.110'},
]

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "20200807.0.0"
  config.ssh.shell = "bash"
  config.vm.boot_timeout = 420
  config.ssh.insert_key = true


  vms.each do |i|
    config.vm.define i[:v_name] do |machine|
      machine.vm.provider "virtualbox" do |vbox|
        vbox.memory = i[:v_mem]
        vbox.name = i[:v_name]
      end

      machine.vm.hostname = i[:v_name]
      machine.vm.network 'private_network', ip: i[:v_ip], netmask: '255.255.255.0'
      machine.vm.provision :hosts, :sync_hosts => true
    end

    config.vm.provision "ansible" do |ansible|
      ansible.galaxy_role_file = "requirements.yaml"
      ansible.playbook = "bootstrap.yaml"
    end

    #config.vm.provision :shell do |sh|
    #   sh.path = "bootstrap.sh"
    #   sh.args = ["-h","localhost","-P","3306","-u","root","-p","Str0ngP@ss"]
    #end

  end

end
