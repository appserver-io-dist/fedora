%define         _unpackaged_files_terminate_build 0
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:       ${build.name.prefix}dist
Version:    ${appserver.src.version}
Release:    ${appserver.src.suffix}${build.number}${build.name.suffix}
Summary:    appserver.io provides a multithreaded application server for PHP.
Group:      System Environment/Base
License:    OSL 3.0
Vendor:     Bernhard Wick bw@appserver.io
URL:        http://appserver.io
requires:   appserver-runtime
Provides:   appserver-dist

%description
%{summary}

%prep

%build

%clean

%files
/opt/appserver/*
/lib/systemd/system/*

%post

# Reload shared library list
ldconfig

# Set needed files as accessable for the configured user
chown -R nobody:nobody /opt/appserver/var
chown -R nobody:nobody /opt/appserver/webapps
chown -R nobody:nobody /opt/appserver/deploy

# Make the link to our system systemd file
ln -sf /lib/systemd/system/appserver.service /etc/systemd/system/appserver.service
ln -sf /lib/systemd/system/appserver-watcher.service /etc/systemd/system/appserver-watcher.service
ln -sf /lib/systemd/system/appserver-php5-fpm.service /etc/systemd/system/appserver-php5-fpm.service

# Create composer symlink
ln -sf /opt/appserver/bin/composer.phar /opt/appserver/bin/composer

# Reload the systemd daemon
systemctl daemon-reload

# run postinstall script from appserver-io/appserver composer package
# to set correct path for specific startup scripts
cd /opt/appserver
./bin/php ./bin/composer.phar run-script post-install-cmd 1>&2 >> /tmp/test.txt

# Start the appserver + watcher + fpm
systemctl start appserver.service
systemctl start appserver-watcher.service
systemctl start appserver-php5-fpm.service

%preun
# Stop the appserver + watcher + fpm
systemctl stop appserver.service
systemctl stop appserver-watcher.service
systemctl stop appserver-php5-fpm.service

%postun
# Reload shared library list
ldconfig