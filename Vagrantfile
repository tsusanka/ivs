# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

	# All Vagrant configuration is done here. The most common configuration
	# options are documented and commented below. For a complete reference,
	# please see the online documentation at vagrantup.com.

	# Every Vagrant virtual environment requires a box to build off of.
	config.vm.box = "baseubuntu14.04-32b"

	# The url from where the 'config.vm.box' box will be fetched if it
	# doesn't already exist on the user's system.
	config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"
	
	# The hostname of the computer
	config.vm.hostname = "vagrant"

	# Create a private network, which allows host-only access to the machine
	# using a specific IP.
	config.vm.network :private_network, ip: "10.11.12.13"

	# Increase system's memory
	config.vm.provider "virtualbox" do |v|
		v.memory = 2048
	end

	# Share an additional folder to the guest VM. The first argument is
	# the path on the host to the actual folder. The second argument is
	# the path on the guest to mount the folder. And the optional third
	# argument is a set of non-required options.
#	config.vm.synced_folder config.user.work.folder, "/mnt", type: "nfs", nfs_version: "4", nfs_udp: false, mount_options: ['nolock,noatime']  # nfs should be ignored on Windows
	config.vm.synced_folder config.user.work.folder, "/mnt"

end
