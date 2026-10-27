# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyss-guiutils
Version:        0.2.2
Release:        0.1.20261027git0afda1e%{?dist}
Summary:        Dialogs and application tools for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyss-guiutils
Source0:        https://github.com/AbyssWM/Abyss-guiutils/archive/0afda1ef922bbdf63c74042642cf12a69a449320.tar.gz
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
printf '%s  %s\n' '7ad0ced7f29b6e7c8b9c07541c77465bf56a17acb8be76a2565cc36bfe4febd5' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyss-guiutils-0afda1ef922bbdf63c74042642cf12a69a449320

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/*
