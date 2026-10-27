# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyss-guiutils
Version:        0.2.2
Release:        0.1.20261027gitb25e097%{?dist}
Summary:        Dialogs and application tools for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyss-guiutils
Source0:        https://github.com/AbyssWM/Abyss-guiutils/archive/b25e0974ae580c63aa23252c4170eb7adf60f98d.tar.gz
BuildRequires:  abyssparse-devel
BuildRequires:  abysstoolkit-devel
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xkbcommon)

%description
Dialogs and application tools for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '13382fa09aa13f7c1d17462f638937be5212e2c6ec99aab39aef647a191b5eba' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyss-guiutils-b25e0974ae580c63aa23252c4170eb7adf60f98d

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/*
