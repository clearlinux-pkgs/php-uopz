#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-uopz
Version  : 7.1.1
Release  : 72
URL      : https://pecl.php.net/get/uopz-7.1.1.tgz
Source0  : https://pecl.php.net/get/uopz-7.1.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-uopz-lib = %{version}-%{release}
Requires: php-uopz-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
UOPZ
====
*User Operations for Zend*
[![Build and Test](https://github.com/krakjoe/uopz/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/krakjoe/uopz/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/krakjoe/uopz/badge.svg?branch=master)](https://coveralls.io/github/krakjoe/uopz?branch=master)

%package lib
Summary: lib components for the php-uopz package.
Group: Libraries
Requires: php-uopz-license = %{version}-%{release}

%description lib
lib components for the php-uopz package.


%package license
Summary: license components for the php-uopz package.
Group: Default

%description license
license components for the php-uopz package.


%prep
%setup -q -n uopz-7.1.1
cd %{_builddir}/uopz-7.1.1
pushd ..
cp -a uopz-7.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-uopz
cp %{_builddir}/uopz-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-uopz/ec8f10e892d180cc3930ca693908076a326520f0 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/uopz.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-uopz/ec8f10e892d180cc3930ca693908076a326520f0
