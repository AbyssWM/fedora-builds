# COPR publication

One public project, `bb8therobot1717/abyss`, is intended to contain all 17
primary packages and the seven library development subpackages. Separate COPR
projects per executable are unnecessary. Programs supplied together by an
upstream project remain in the corresponding RPM.

Homepage: https://abysswm.github.io/

## Description

```text
the complete abyss wayland ecosystem for fedora

a dynamic tiling compositor with its own libraries desktop portal and companion tools
built around abyssland and configured in c++
```

## Instructions

Once the packages have successfully built and been published, Fedora users can run:

```sh
sudo dnf copr enable bb8therobot1717/abyss
sudo dnf install abyssland
```

Other tools can be installed individually using the package names below.
These commands are for Fedora users; they are not host setup commands for Void.

## Package coverage

| Primary RPM | Programs | Additional RPM |
|---|---|---|
| `abyssutils` | Shared library / protocol data | `abyssutils-devel` |
| `abyss-scanner` | `abyss-scanner` | — |
| `abyssland-protocols` | Shared library / protocol data | — |
| `abyssparse` | Shared library / protocol data | `abyssparse-devel` |
| `abysswire` | `abysswire-scanner` | `abysswire-devel` |
| `abyssgraphics` | Shared library / protocol data | `abyssgraphics-devel` |
| `abyssal` | Shared library / protocol data | `abyssal-devel` |
| `abysstoolkit` | `abyss-preprocess` | `abysstoolkit-devel` |
| `abysscursor` | `abysscursor-util` | `abysscursor-devel` |
| `abyssland` | `start-abyssland`, `abyssctl`, `Abyssland` | — |
| `abyss-guiutils` | `abyss-welcome`, `abyss-update-screen`, `abyss-run`, `abyss-donate-screen`, `abyss-dialog` | — |
| `xdg-desktop-portal-abyss` | `xdg-desktop-portal-abyss`, `abyss-share-picker` | — |
| `abysspicker` | `abysspicker` | — |
| `abyssdusk` | `abyssdusk` | — |
| `abysspaper` | `abysspaper` | — |
| `abysslock` | `abysslock` | — |
| `abysspolkit` | `abyss-polkit-agent` | — |

Executable coverage was checked against the actual Void package artifacts and
the Fedora spec file lists. This confirms intended packaging coverage, not
successful Fedora builds. The libraries also provide shared objects.

## Build and publication status

The Git recipes are public; a COPR project/build is not created by a Git push.
Create the project in COPR, select the Fedora x86_64 chroot being targeted, then
use SCM/Git with `https://github.com/AbyssWM/fedora-builds.git`, branch `main`,
no subdirectory, `specs/PACKAGE.spec`, and the **make srpm** method.

Build in `sources.json` dependency order and wait for dependencies to be available
before submitting dependants. `abyssland-protocols` can serve as the first
independent build to verify this setup. All 17 projects remain in scope.
Successful COPR builds publish RPMs in the project repository. Session/hardware
tests are performed by Raphi after COPR publication.

References: [COPR SCM builds](https://docs.copr.fedorainfracloud.org/user_documentation.html#scm),
[COPR setup](https://docs.copr.fedorainfracloud.org/screenshots_tutorial.html).
