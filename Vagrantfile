# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Configure the actual windows machine
    config.vm.define "${vagrant-box.name}" do |fedora|

        # Basic default configuration used for intial setup of box.
        # Please use if packaged boxes are unavailable or unwelcome
        # fedora.vm.box = "chef/fedora-${target-os.version}"
        # fedora.vm.box_url = "https://vagrantcloud.com/chef/boxes/fedora-${target-os.version}"

        # Box name and location
        fedora.vm.box = "${vagrant-box.name}"
        fedora.vm.box_url = "${vagrant-box.baseurl}/${vagrant-box.name}.box"

        # Basic network configuration
        fedora.vm.host_name = "${vagrant-box.name}"
        # Required for NFS to work, pick any local IP. Disabled due to errors with network configuration at Fedora 21+ boxes.
        # Please enable at times and add a ", nfs: true" at the end of each folder sync
        # fedora.vm.network :private_network, ip: '192.168.50.50'

        # Share some needed folders
        fedora.vm.synced_folder "${build.dir}", "${vagrant-build.dir}"
        fedora.vm.synced_folder "${reports.dir}", "${vagrant-reports.dir}"
        fedora.vm.synced_folder "${src.dir}", "${vagrant-src.dir}"

        # Shell provisioning used for intial setup of box.
        # Please use if packaged boxes are unavailable or unwelcome
        # fedora.vm.provision "shell", path: "provision.sh"

        # Extend the timeout for initial connection
        fedora.vm.boot_timeout = 600

        # Make some provider specific configuration changes
        fedora.vm.provider "virtualbox" do |vb|
            host = RbConfig::CONFIG['host_os']

            # Give VM 2Gb system memory & access to 2 cpu cores on the host
            vb.customize ["modifyvm", :id, "--memory", "2048"]
            vb.customize ["modifyvm", :id, "--cpus", "2"]
            vb.customize ["modifyvm", :id, "--cpuexecutioncap", "90"]
        end
    end
end
