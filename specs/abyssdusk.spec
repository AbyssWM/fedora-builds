# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssdusk
Version:        0.4.0
Release:        0.1.20261027gitb383b37%{?dist}
Summary:        Display color temperature manager for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssDusk
Source0:        https://github.com/AbyssWM/AbyssDusk/archive/b383b3706c40b8b6c0c76ec359ca4b89652f9b46.tar.gz
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
printf '%s  %s\n' '7cabb12e3d8eb24cad418a17b1e498f18a9e501066426131ad3a698c6608019a' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssDusk-b383b3706c40b8b6c0c76ec359ca4b89652f9b46

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abyssdusk
%{_userunitdir}/abyssdusk.service
