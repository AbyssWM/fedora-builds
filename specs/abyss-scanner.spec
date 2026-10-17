# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyss-scanner
Version:        0.4.5
Release:        0.1.20261017git84f54bf%{?dist}
Summary:        C++ Wayland protocol scanner for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyss-scanner
Source0:        https://github.com/AbyssWM/Abyss-scanner/archive/84f54bf0d3074ef8700d3e89699181accdd28cba.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(pugixml)

%description
C++ Wayland protocol scanner for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '82528be339b642f28a38ca495a6388300313dce37e624d67ae2c88e3992a1255' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyss-scanner-84f54bf0d3074ef8700d3e89699181accdd28cba

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/abyss-scanner
%{_libdir}/pkgconfig/abyss-scanner.pc
%{_libdir}/cmake/abyss-scanner/
