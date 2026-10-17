# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysspaper
Version:        0.8.4
Release:        0.1.20261017git4e06e75%{?dist}
Summary:        Wallpaper manager for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/AbyssPaper
Source0:        https://github.com/AbyssWM/AbyssPaper/archive/4e06e7590cd135fc7592e60b469699a641bec47c.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssparse-devel
BuildRequires:  abysstoolkit-devel
BuildRequires:  abyssutils-devel
BuildRequires:  abysswire-devel
Patch0:         0001-find-installed-config-module.patch
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)

%description
Wallpaper manager for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '2576e4c28a2edba50de600ccb6e4567486e9190528e43a30f6074f6903b06682' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n AbyssPaper-4e06e7590cd135fc7592e60b469699a641bec47c

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON -DABYSS_CONFIG_DIR=%{_builddir}/empty-config
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abysspaper
%{_userunitdir}/abysspaper.service
