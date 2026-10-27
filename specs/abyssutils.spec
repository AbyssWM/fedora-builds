# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssutils
Version:        0.14.2
Release:        0.1.20261027gitf1f540b%{?dist}
Summary:        Utility library for the Abyss ecosystem
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyssutils
Source0:        https://github.com/AbyssWM/Abyssutils/archive/f1f540b7121f6db3c0bb8518a072c1a79755cd82.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(pixman-1)

%description
Utility library for the Abyss ecosystem.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(pixman-1)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' '7a579a81abc1dce8ba65e14ffde83f15acd03aa4b07788c5d03a764cce2a7462' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssutils-f1f540b7121f6db3c0bb8518a072c1a79755cd82

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabyssutils.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssutils.so
%{_libdir}/pkgconfig/*
