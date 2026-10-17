# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysscursor
Version:        0.1.13
Release:        0.1.20261017git6a762ed%{?dist}
Summary:        Cursor library and theme tools for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abysscursor
Source0:        https://github.com/AbyssWM/Abysscursor/archive/6a762edb75677f8cc46a20cb26b615bbabb5155a.tar.gz
BuildRequires:  abyssparse-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(tomlplusplus)

%description
Cursor library and theme tools for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssparse-devel
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libzip)
Requires:       pkgconfig(tomlplusplus)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' 'a18b616212a28339358fdf84158ecf0ac0163e61d4d194bda6776a91a79586b5' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abysscursor-6a762edb75677f8cc46a20cb26b615bbabb5155a

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabysscursor.so.*
%{_bindir}/abysscursor-util

%files devel
%{_includedir}/*
%{_libdir}/libabysscursor.so
%{_libdir}/pkgconfig/*
