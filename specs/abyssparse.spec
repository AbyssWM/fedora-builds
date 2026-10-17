# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssparse
Version:        0.6.8
Release:        0.2.20261017git45d399e%{?dist}
Summary:        Configuration parsing library for Abyss
License:        LGPL-3.0-only
URL:            https://github.com/AbyssWM/Abyssparse
Source0:        https://github.com/AbyssWM/Abyssparse/archive/45d399ec11762312395d62f1e66f6d3c4b53c482.tar.gz
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config

%description
Configuration parsing library for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssutils-devel

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' 'b3b43a824e8a6112c7a62534536f712146ea27daea77ff6afe06179d536e47c4' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssparse-45d399ec11762312395d62f1e66f6d3c4b53c482

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE COPYING COPYRIGHT
%{_libdir}/libabyssparse.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssparse.so
%{_libdir}/pkgconfig/*
