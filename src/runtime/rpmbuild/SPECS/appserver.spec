%define         _unpackaged_files_terminate_build 0
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:       ${build.name.prefix}runtime
Version:    ${appserver.runtime.version}
Release:    ${build.name.suffix}
Summary:    appserver.io provides a multithreaded application server for PHP.
Group:      System Environment/Base
License:    OSL 3.0
Vendor:     Bernhard Wick bw@appserver.io
URL:        http://appserver.io
requires:   git, libmcrypt
Provides:   appserver-runtime

%description
%{summary}

%prep

%build

%clean

%files
/opt/appserver/*

%changelog

%post
# Reload shared library list
ldconfig

# Create composer symlink
ln -s /opt/appserver/bin/composer.phar /opt/appserver/bin/composer

%postun
# Reload shared library list
ldconfig