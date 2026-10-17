# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssutils
Version:        0.14.2
Release:        0.1.20261017gitb423270%{?dist}
Summary:        Utility library for the Abyss ecosystem
License:        BSD-3-Clause
URL:            https://github.com/AbyssWM/Abyssutils
Source0:        https://github.com/AbyssWM/Abyssutils/archive/b423270d43764d3b0f74584fa4a9c61ab1c9b9aa.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(pixman-1)

%description
Utility library for the Abyss ecosystem.
Pinned experimental source snapshot maintained by AbyssWM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(pixman-1)

%description devel
Headers and build metadata for %{name}.

%prep
printf '%s  %s\n' '42a8e2d5fbac0bb9c1837b94b22ce3d491e05159fb1f64258b25fe2fd106d02e' '%{SOURCE0}' | sha256sum --check --status
%autosetup -p1 -n Abyssutils-b423270d43764d3b0f74584fa4a9c61ab1c9b9aa

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libabyssutils.so.*

%files devel
%{_includedir}/*
%{_libdir}/libabyssutils.so
%{_libdir}/pkgconfig/*
