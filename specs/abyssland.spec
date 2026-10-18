# SPDX-License-Identifier: 0BSD
# Experimental pinned snapshot; native Fedora build validation pending.
Name:           abyssland
Version:        0.56.2
Release:        0.1.20261018gitc30ad2a%{?dist}
Summary:        Dynamic tiling Wayland compositor with C++ configuration
License:        BSD-3-Clause AND MIT AND BSD-2-Clause
URL:            https://github.com/AbyssWM/Abyssland
Source0:        https://github.com/AbyssWM/Abyssland/archive/c30ad2a50fc41b2025280ded8b54effb87624480.tar.gz
Source1:        https://github.com/stephenberry/glaze/archive/refs/tags/v7.2.0.tar.gz
Source2:        https://github.com/canihavesomecoffee/udis86/archive/5336633af70f3917760a6d441ff02d93477b0c86.tar.gz
BuildRequires:  abyss-scanner
BuildRequires:  abyssal-devel
BuildRequires:  abysscursor-devel
BuildRequires:  abyssgraphics-devel
BuildRequires:  abyssland-protocols
BuildRequires:  abyssutils-devel
BuildRequires:  abysswire-devel
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3
Requires:       dbus
Requires:       xorg-x11-server-Xwayland

%description
Dynamic tiling Wayland compositor with C++ configuration.
Pinned experimental source snapshot maintained by AbyssWM.

%prep
printf '%s  %s\n' '70aff89b07756f52f8a776ab3f89ed9dab2614ce97635d0e7630773525873497' '%{SOURCE0}' | sha256sum --check --status
printf '%s  %s\n' '17dba19ae63ae48f94994f00d49d5cb3c8f1306db1046c534c4828662490b7d4' '%{SOURCE1}' | sha256sum --check --status
printf '%s  %s\n' '2f459fafa19535ef1be417bf7614e4f92475e5787d7ba76df20287cc29d1b5a9' '%{SOURCE2}' | sha256sum --check --status
%setup -q -n Abyssland-c30ad2a50fc41b2025280ded8b54effb87624480 -a1 -a2
install -d subprojects/udis86
cp -a udis86-5336633af70f3917760a6d441ff02d93477b0c86/. subprojects/udis86/
cp -p glaze-7.2.0/LICENSE LICENSE.glaze
cp -p udis86-5336633af70f3917760a6d441ff02d93477b0c86/LICENSE LICENSE.udis86

%build
%cmake -DBUILD_TESTING=OFF -DFETCHCONTENT_FULLY_DISCONNECTED=ON -DNO_SYSTEMD=OFF -DNO_UWSM=ON -DABYSS_CONFIG=%{_builddir}/Abyssland-c30ad2a50fc41b2025280ded8b54effb87624480/config.def.hpp -DFETCHCONTENT_SOURCE_DIR_GLAZE=%{_builddir}/Abyssland-c30ad2a50fc41b2025280ded8b54effb87624480/glaze-7.2.0
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%license LICENSE.glaze LICENSE.udis86
%{_bindir}/*
%{_includedir}/abyssland/
%{_datadir}/abyss/
%{_datadir}/pkgconfig/abyssland.pc
%{_datadir}/wayland-sessions/*
%{_prefix}/lib/systemd/user/abyssland-session.target
%{_datadir}/xdg-desktop-portal/*
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/abyssctl
%{_datadir}/fish/vendor_completions.d/abyssctl.fish
%{_datadir}/zsh/site-functions/_abyssctl
