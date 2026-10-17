# Abyss Fedora builds

Experimental RPM definitions for all 17 Abyss repositories. These are development
snapshots. Native Fedora builds and installation tests are **not yet validated**.
This repository is independent of Fedora's official package collection.

Sources are pinned in `sources.json`. `specs/` contains one spec per repository;
libraries have `-devel` subpackages. The compositor uses the public default
configuration and explicitly checksummed Glaze/udis86 archives. No build-time
Git fallback or personal user config is required.

The intended COPR owner is `bb8therobot1717`; a project named `abyss` still needs
to be created. With COPR's Git SCM source method, select this repository,
the `main` branch, and the **make srpm** build method. For each package set the
spec path to `specs/PACKAGE.spec`. `.copr/Makefile` calls the source-RPM helper.
Build in the order listed in `sources.json`; dependencies must be available in
the COPR project before dependent packages are submitted. No automatic builds
have been enabled or submitted by this repository.

To prepare one source RPM locally on Fedora:

```sh
python3 tools/srpm.py --spec specs/abyssutils.spec --outdir out
```

`--prepare-only` verifies and stages sources without invoking rpmbuild.
The actual build still needs native dependency resolution and RPM validation.
Choose supported Fedora chroots only after verifying the compiler and dependency
versions. No COPR credentials or signing keys belong in this repository.

Maintainer: bb8TheRobot <bb8therobot85@gmail.com>. Packaging: 0BSD.
The sources retain their own licenses and original notices; the separate upstream
attribution audit remains a release prerequisite.
