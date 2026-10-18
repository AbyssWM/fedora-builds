<div align="center">

<img src="https://github.com/AbyssWM.png?size=200" width="140" alt="Abyss logo">

# 🎩 Abyss for Fedora

**RPM specs for the complete Abyss Wayland ecosystem — built on COPR.**

[![COPR](https://img.shields.io/badge/COPR-bb8therobot1717%2FAbyss-51a2da?style=flat-square&logo=fedora&logoColor=white)](https://copr.fedorainfracloud.org/coprs/bb8therobot1717/Abyss/) [![Fedora](https://img.shields.io/badge/fedora-44%20%7C%2045-294172?style=flat-square&logo=fedora&logoColor=white)](https://fedoraproject.org/) [![Packages](https://img.shields.io/badge/packages-17-7c3aed?style=flat-square)](#-packages) [![Packaging license](https://img.shields.io/badge/packaging-0BSD-blue?style=flat-square)](LICENSE)

[🌐 Website](https://abysswm.github.io/) · [📖 Install guide](https://abysswm.github.io/wiki/getting-started) · [🌊 Abyss on GitHub](https://github.com/AbyssWM)

</div>

---

> [!WARNING]
> **Experimental, pre-1.0.** All packages build on Fedora 44 and 45, but no session or hardware tests have been done yet.

## 🚀 Install

```sh
sudo dnf copr enable bb8therobot1717/Abyss
sudo dnf install abyssland
```

Add the tools you want:

```sh
sudo dnf install xdg-desktop-portal-abyss abysslock abysspaper abysspolkit abyssdusk abysspicker abyss-guiutils
```

Then pick **Abyssland** in your display manager, or run `start-abyssland` from a TTY.

## 🔨 How it builds

COPR builds straight from this repository: **SCM → Git**, branch `main`, spec `specs/<package>.spec`, method **make srpm**.
[`.copr/Makefile`](.copr/Makefile) runs [`tools/srpm.py`](tools/srpm.py), which downloads the pinned source archive, checks it against
[`sources.json`](sources.json) and assembles the source RPM. No network access is needed during the binary build.

Prepare a source RPM locally:

```sh
python3 tools/srpm.py --spec specs/abyssutils.spec --outdir out
```

`--prepare-only` only verifies and stages the sources.

<details>
<summary>Build results</summary>

All 17 packages succeeded on `fedora-44-x86_64` and `fedora-45-x86_64` (2026-10-18).
Fixes found along the way: an invalid `meson-rpm-macros` build dependency, the AbyssLock PAM file path,
packaging the `abyssctl` shell completions and the bundled Glaze / udis86 license files.
Full project details: [COPR.md](COPR.md).

</details>

## 📋 Packages

Listed in build order — every package only depends on the ones above it.

| # | Package | Development package |
|---|---|---|
| 1 | [`abyssutils`](specs/abyssutils.spec) | `abyssutils-devel` |
| 2 | [`abyss-scanner`](specs/abyss-scanner.spec) | — |
| 3 | [`abyssland-protocols`](specs/abyssland-protocols.spec) | — |
| 4 | [`abyssparse`](specs/abyssparse.spec) | `abyssparse-devel` |
| 5 | [`abysswire`](specs/abysswire.spec) | `abysswire-devel` |
| 6 | [`abyssgraphics`](specs/abyssgraphics.spec) | `abyssgraphics-devel` |
| 7 | [`abyssal`](specs/abyssal.spec) | `abyssal-devel` |
| 8 | [`abysstoolkit`](specs/abysstoolkit.spec) | `abysstoolkit-devel` |
| 9 | [`abysscursor`](specs/abysscursor.spec) | `abysscursor-devel` |
| 10 | [`abyssland`](specs/abyssland.spec) | — |
| 11 | [`abyss-guiutils`](specs/abyss-guiutils.spec) | — |
| 12 | [`xdg-desktop-portal-abyss`](specs/xdg-desktop-portal-abyss.spec) | — |
| 13 | [`abysspicker`](specs/abysspicker.spec) | — |
| 14 | [`abyssdusk`](specs/abyssdusk.spec) | — |
| 15 | [`abysspaper`](specs/abysspaper.spec) | — |
| 16 | [`abysslock`](specs/abysslock.spec) | — |
| 17 | [`abysspolkit`](specs/abysspolkit.spec) | — |

## ⚖️ License

The packaging in this repository is **0BSD** ([LICENSE](LICENSE)). The packaged software keeps its own licenses — see [LICENSES.md](LICENSES.md).

Maintainer: bb8TheRobot &lt;bb8therobot85@gmail.com&gt;
