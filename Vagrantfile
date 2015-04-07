# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Basic default configuration
  config.vm.box = "chef/fedora-${target-os.version}"
  config.vm.box_url = "https://vagrantcloud.com/chef/boxes/fedora-${target-os.version}"

  # Basic network configuration
  config.vm.host_name = "${vagrant-box.name}"

  # Shell provisioning
  config.vm.provision "shell", path: "provision.sh"

  # Share the build folder as read only
  config.vm.synced_folder "${build.dir}", "${vagrant-build.dir}"
  config.vm.synced_folder "${reports.dir}", "${vagrant-reports.dir}"

  # Extend the timeout for initial connection
  config.vm.boot_timeout = 1200

  config.vm.provider "virtualbox" do |vb|
    host = RbConfig::CONFIG['host_os']

    # Give VM 1/3 system memory & access to all cpu cores on the host
    if host =~ /darwin/
      cpus = `sysctl -n hw.ncpu`.to_i
      # sysctl returns Bytes and we need to convert to MB
      mem = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 3
    elsif host =~ /linux/
      cpus = `nproc`.to_i
      # meminfo shows KB and we need to convert to MB
      mem = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 3
    else # sorry Windows folks, I can't help you
      cpus = 2
      mem = 1024
    end

    vb.customize ["modifyvm", :id, "--memory", mem]
    vb.customize ["modifyvm", :id, "--cpus", cpus]
  end

  config.vm.define :${vagrant-box.name} do |t|
    end
end