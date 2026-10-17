# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyss-guiutils
Version:        0.2.2
Release:        0.1.20261017gitda66469%{?dist}
Summary:        Dialogs and application tools for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyss-guiutils
Source0:        https://github.com/AbyssWM/Abyss-guiutils/archive/da6646906dab8557440ed8f5cca4157452105fc2.tar.gz
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
printf '%s  %s\n' 'f2eb180c298dc718b8e3b144c9f114a05e4e9aacd852d01864162dda65a06d48' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyss-guiutils-da6646906dab8557440ed8f5cca4157452105fc2

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/*
