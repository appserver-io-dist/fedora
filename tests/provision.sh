#!/bin/sh

# install ant and other dependencies
yum -y install ant ant-contrib git;

# download jmeter and make it usable
wget ${jmeter.download.url};
tar -xvzf ./${jmeter.package.name} ${jmeter.vagrant.dir}