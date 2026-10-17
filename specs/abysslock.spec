# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysslock
Version:        0.9.6
Release:        0.1.20261017git651a5ec%{?dist}
Summary:        Wayland session lock for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssLock
Source0:        https://github.com/AbyssWM/AbyssLock/archive/651a5ecf43b742965bca25e99056cf8e7cf83aa3.tar.gz
Patch0:         0001-install-pam-in-sysconfdir.patch
BuildRequires:  abyss-scanner
BuildRequires:  abyssgraphics-devel
BuildRequires:  abyssparse-devel
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pam-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
Wayland session lock for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '86e77468c4b4c4e598a5a933c16b7436fd3348e02bf0392400838f3c8097f926' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssLock-651a5ecf43b742965bca25e99056cf8e7cf83aa3

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysslock
%config(noreplace) %{_sysconfdir}/pam.d/abysslock
%{_datadir}/abyss/abysslock.conf
