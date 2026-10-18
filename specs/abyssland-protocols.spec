# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssland-protocols
Version:        0.7.0
Release:        0.1.20261017git23246e7%{?dist}
Summary:        Wayland protocol extensions for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyssland-protocols
Source0:        https://github.com/AbyssWM/Abyssland-protocols/archive/23246e7462e75bc07a04e62b1edc68b68770f73e.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config

%description
Wayland protocol extensions for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '1cbc35cfa275eaae72614897d2b1b0ebe2af5708e383b4aa1fbdc88df3542822' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssland-protocols-23246e7462e75bc07a04e62b1edc68b68770f73e

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_datadir}/abyssland-protocols/
%{_datadir}/pkgconfig/abyssland-protocols.pc
