# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssparse
Version:        0.6.8
Release:        0.1.20261017gitdcd10ad%{?dist}
Summary:        Configuration parsing library for Abyss
License:        LGPL-3.0-only
URL:            https://github.com/AbyssWM/Abyssparse
Source0:        https://github.com/AbyssWM/Abyssparse/archive/dcd10adbf858a4f0128a04938878844d935298d9.tar.gz
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
printf '%s  %s\n' 'cedd57c46b449d5ba8998020d458cc9a6a9394759225342aa1048964125cf685' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssparse-dcd10adbf858a4f0128a04938878844d935298d9

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabyssparse.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssparse.so
%{_libdir}/pkgconfig/*
