# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssal
Version:        0.15.0
Release:        0.1.20261017git95bbf98%{?dist}
Summary:        Rendering and display backend library for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyssal
Source0:        https://github.com/AbyssWM/Abyssal/archive/95bbf980b4c704b517d557038ba4460080847314.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
Rendering and display backend library for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssutils-devel
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(hwdata)
Requires:       pkgconfig(libdisplay-info)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libseat)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-egl)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-server)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' '269bdf8c8bced938de0c772fa90907a4e82d08a3cb8e9e1a16a3da8006e653d0' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssal-95bbf980b4c704b517d557038ba4460080847314

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabyssal.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssal.so
%{_libdir}/pkgconfig/*
