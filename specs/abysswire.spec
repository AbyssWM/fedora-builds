# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysswire
Version:        0.3.1
Release:        0.1.20261017git5556523%{?dist}
Summary:        IPC wire protocol library and scanner for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abysswire
Source0:        https://github.com/AbyssWM/Abysswire/archive/55565230b6ac2fbdf9fbeb23f074d4c006715d69.tar.gz
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(pugixml)

%description
IPC wire protocol library and scanner for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssutils-devel
Requires:       pkgconfig(libffi)
Requires:       pkgconfig(pugixml)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' 'f392a31c4693f2a3297bb796304cdab4cefe05666b840b12048e06a4cd221b42' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abysswire-55565230b6ac2fbdf9fbeb23f074d4c006715d69

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabysswire.so.*
%{_bindir}/abysswire-scanner

%files devel
%{_includedir}/*
%{_libdir}/libabysswire.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/abysswire-scanner/
