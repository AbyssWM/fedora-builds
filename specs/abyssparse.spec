# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssparse
Version:        0.6.8
Release:        0.2.20261027git6c3c77e%{?dist}
Summary:        Configuration parsing library for Abyss
License:        LGPL-3.0-only
URL:            https://github.com/AbyssWM/Abyssparse
Source0:        https://github.com/AbyssWM/Abyssparse/archive/6c3c77e8a029e46d7416b84f67aff833f9beedd2.tar.gz
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
printf '%s  %s\n' '87ba448e0e84a56dd0785b7136b831e82c6895ddedad041a92cc7bad360db651' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssparse-6c3c77e8a029e46d7416b84f67aff833f9beedd2

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
