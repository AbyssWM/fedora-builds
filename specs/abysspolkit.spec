# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspolkit
Version:        0.2.0
Release:        0.1.20261027gitd9bc965%{?dist}
Summary:        Polkit authentication agent for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPolkit
Source0:        https://github.com/AbyssWM/AbyssPolkit/archive/d9bc965683bb4b0b90d6039b22fbd39423a37c86.tar.gz
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
printf '%s  %s\n' 'a5e5d65028067d7b57faa44b82a026cd371009d054cf5fde91751a1e4faaedeb' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPolkit-d9bc965683bb4b0b90d6039b22fbd39423a37c86

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
