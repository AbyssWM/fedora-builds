# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssdusk
Version:        0.4.0
Release:        0.1.20261017git01ad76f%{?dist}
Summary:        Display color temperature manager for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssDusk
Source0:        https://github.com/AbyssWM/AbyssDusk/archive/01ad76f953f8d5139b5e03cd7cfaaf9342667f0b.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssland-protocols
BuildRequires:  abyssparse-devel
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
Display color temperature manager for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '1870725946980001ea426c8723cfb7b3c0f2536673049a25a0762b8b59ef6b8c' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssDusk-01ad76f953f8d5139b5e03cd7cfaaf9342667f0b

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abyssdusk
%{_userunitdir}/abyssdusk.service
