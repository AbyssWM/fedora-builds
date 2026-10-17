# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           xdg-desktop-portal-abyss
Version:        1.4.1
Release:        0.1.20261017gitc4e1197%{?dist}
Summary:        Desktop portal and screen sharing picker for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Xdg-desktop-portal-abyss
Source0:        https://github.com/AbyssWM/Xdg-desktop-portal-abyss/archive/c4e1197e9aaed10773d0d142d13d40223a92b0eb.tar.gz
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
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
Requires:       xdg-desktop-portal
Requires:       qt6-qtwayland

%description
Desktop portal and screen sharing picker for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '962d8e61267e48b3e5d2c84e9104cb0a0a93a0f893781626d7eb072a5848b5ae' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Xdg-desktop-portal-abyss-c4e1197e9aaed10773d0d142d13d40223a92b0eb

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON -DSYSTEMD_SERVICES=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abyss-share-picker
%{_libexecdir}/xdg-desktop-portal-abyss
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.abyss.service
%{_datadir}/xdg-desktop-portal/portals/abyss.portal
%{_userunitdir}/xdg-desktop-portal-abyss.service
