# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspicker
Version:        0.4.7
Release:        0.1.20261017gitfa99785%{?dist}
Summary:        Wayland color picker for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPicker
Source0:        https://github.com/AbyssWM/AbyssPicker/archive/fa997857bfc513c240f8b442802dee64d15e1759.tar.gz
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
printf '%s  %s\n' '18bc8ada83a3cd912140ae7f8bf825f55ffb6ee441b9ad0f267381222319955a' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPicker-fa997857bfc513c240f8b442802dee64d15e1759

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysspicker
%{_mandir}/man1/*
