#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-uopz
Version  : 6.1.1
Release  : 3
URL      : https://pecl.php.net/get/uopz-6.1.1.tgz
Source0  : https://pecl.php.net/get/uopz-6.1.1.tgz
Summary  : User Operations for Zend
Group    : Development/Tools
License  : PHP-3.01
Requires: php-uopz-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
UOPZ
====
*User Operations for Zend*
[![Build Status](https://travis-ci.org/krakjoe/uopz.svg?branch=master)](https://travis-ci.org/krakjoe/uopz)
[![Coverage Status](https://coveralls.io/repos/github/krakjoe/uopz/badge.svg?branch=master)](https://coveralls.io/github/krakjoe/uopz?branch=master)

%package lib
Summary: lib components for the php-uopz package.
Group: Libraries

%description lib
lib components for the php-uopz package.


%prep
%setup -q -n uopz-6.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/uopz.so
