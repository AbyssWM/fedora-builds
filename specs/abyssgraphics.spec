# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssgraphics
Version:        0.5.1
Release:        0.1.20261027git5f590f2%{?dist}
Summary:        Graphics and resource library for Abyss
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyssgraphics
Source0:        https://github.com/AbyssWM/Abyssgraphics/archive/5f590f21086f9c1fbb0ca1b0c1d7ffebdfb60945.tar.gz
BuildRequires:  abyssutils-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)

%description
Graphics and resource library for Abyss.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       abyssutils-devel
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libheif)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libjxl)
Requires:       pkgconfig(libmagic)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libwebp)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' '5a191c008e3f2719fbd10633e48fa1b40bbf9742593b7f7e5e043c3a0972458d' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssgraphics-5f590f21086f9c1fbb0ca1b0c1d7ffebdfb60945

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabyssgraphics.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssgraphics.so
%{_libdir}/pkgconfig/*
