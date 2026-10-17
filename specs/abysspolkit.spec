# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspolkit
Version:        0.2.0
Release:        0.1.20261017gitf121b36%{?dist}
Summary:        Polkit authentication agent for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPolkit
Source0:        https://github.com/AbyssWM/AbyssPolkit/archive/f121b36311c1d4cd1382fe29704d353d203a49a0.tar.gz
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
printf '%s  %s\n' 'f33d4b688692f37c7e1e8a0ef288e24d0d211ca73c69cc061ea20b489208db7f' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPolkit-f121b36311c1d4cd1382fe29704d353d203a49a0

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
