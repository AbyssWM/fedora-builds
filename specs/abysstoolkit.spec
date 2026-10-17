# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abysstoolkit
Version:        0.6.0
Release:        0.1.20261017git9a095e0%{?dist}
Summary:        Native graphical toolkit and config preprocessor for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abysstoolkit
Source0:        https://github.com/AbyssWM/Abysstoolkit/archive/9a095e013abdd600b617e912f207430eaeafda18.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssal-devel
BuildRequires:  abyssgraphics-devel
BuildRequires:  abyssparse-devel
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(absl_flat_hash_map)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       python3

%description
Native graphical toolkit and config preprocessor for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssal-devel
Requires:       abyssgraphics-devel
Requires:       abyssparse-devel
Requires:       abyssutils-devel
Requires:       pkgconfig(absl_flat_hash_map)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(iniparser)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-egl)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-server)
Requires:       pkgconfig(xkbcommon)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' '61622f6f4ae903e5e991d9d555b12207c97cf274def0b7934b348628f531b156' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abysstoolkit-9a095e013abdd600b617e912f207430eaeafda18

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabysstoolkit.so.*
%{_bindir}/abyss-preprocess

%files devel
%{_includedir}/*
%{_libdir}/libabysstoolkit.so
%{_libdir}/pkgconfig/*
%{_datadir}/abysstoolkit/cmake/
