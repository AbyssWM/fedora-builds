# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspicker
Version:        0.4.7
Release:        0.1.20261027git9724004%{?dist}
Summary:        Wayland color picker for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPicker
Source0:        https://github.com/AbyssWM/AbyssPicker/archive/97240042de866686f1da1db3847ddd5f37603e27.tar.gz
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
printf '%s  %s\n' 'e20ff9b5596a8db82b9a979c633ee92f04f70c31b3f875bf8305a2c44322519f' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPicker-97240042de866686f1da1db3847ddd5f37603e27

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysspicker
%{_mandir}/man1/*
