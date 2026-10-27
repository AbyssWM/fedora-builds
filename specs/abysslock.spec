# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysslock
Version:        0.9.6
Release:        0.1.20261027gitce1058c%{?dist}
Summary:        Wayland session lock for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssLock
Source0:        https://github.com/AbyssWM/AbyssLock/archive/ce1058c6dc4f994af77a9974cb5928ff0222bb2a.tar.gz
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
printf '%s  %s\n' '6ac29dd099a1e20eed031da1adf6acd10b8f6ebe165bd6ff9027a1e19becd12b' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssLock-ce1058c6dc4f994af77a9974cb5928ff0222bb2a

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysslock
%config(noreplace) %{_sysconfdir}/pam.d/abysslock
%{_datadir}/abyss/abysslock.conf
