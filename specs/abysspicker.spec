# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspicker
Version:        0.4.7
Release:        0.1.20261027git6a4a1cc%{?dist}
Summary:        Wayland color picker for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPicker
Source0:        https://github.com/AbyssWM/AbyssPicker/archive/6a4a1ccf9de9b8c9a803f75e6e4829e907a08568.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
Wayland color picker for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '9fa5bd0c913e4cfff6e1e1b7d2d0161afb4c0310e77df161b9a9e4fd3db6bba2' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPicker-6a4a1ccf9de9b8c9a803f75e6e4829e907a08568

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysspicker
%{_mandir}/man1/*
