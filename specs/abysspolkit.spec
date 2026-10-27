# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspolkit
Version:        0.2.0
Release:        0.1.20261027gitb3a214b%{?dist}
Summary:        Polkit authentication agent for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPolkit
Source0:        https://github.com/AbyssWM/AbyssPolkit/archive/b3a214b1948dcebd2f5f0f6cab2e6fdddf7cd486.tar.gz
BuildRequires:  abyssgraphics-devel
BuildRequires:  abyssparse-devel
BuildRequires:  abysstoolkit-devel
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sdbus-c++)
Requires:       polkit

%description
Polkit authentication agent for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '9802a003f2dec0fb8b73adedf2d770a548a20e46d416b77b884768a21e1195dd' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPolkit-b3a214b1948dcebd2f5f0f6cab2e6fdddf7cd486

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libexecdir}/abyss-polkit-agent
%{_userunitdir}/abyss-polkit-agent.service
%{_datadir}/dbus-1/services/org.abyssland.AbyssPolkitAgent.service
