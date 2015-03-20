%define         _unpackaged_files_terminate_build 0
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:       ${build.name.prefix}runtime
Version:    ${appserver.runtime.version}
Release:    ${appserver.runtime.build}%{?dist}
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
/opt/appserver/bin/*
/opt/appserver/include/*
/opt/appserver/lib/*
/opt/appserver/php/*
/opt/appserver/sbin/*
/opt/appserver/var/*
%config(noreplace) /opt/appserver/etc/*

%post
# Reload shared library list
ldconfig

%postun
# Reload shared library list
ldconfig