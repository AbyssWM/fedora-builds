# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssdusk
Version:        0.4.0
Release:        0.1.20261027git6c58248%{?dist}
Summary:        Display color temperature manager for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssDusk
Source0:        https://github.com/AbyssWM/AbyssDusk/archive/6c58248dbd91d392fde18aa7764181b80b2da539.tar.gz
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
printf '%s  %s\n' '9cced56fb5bc428081dddb36293241fd9ef6d006aa5e63a34881742ebb9dc077' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssDusk-6c58248dbd91d392fde18aa7764181b80b2da539

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abyssdusk
%{_userunitdir}/abyssdusk.service
