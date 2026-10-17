#!/usr/bin/env python3
"""Assemble a pinned source RPM without publishing it or reading credentials."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import urllib.request
from urllib.parse import urlsplit

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--spec", type=Path, required=True)
parser.add_argument("--outdir", type=Path, required=True)
parser.add_argument("--cache", type=Path)
parser.add_argument("--prepare-only", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
spec = args.spec.resolve()
if spec.parent != root / "specs" or spec.suffix != ".spec":
    parser.error("--spec must select a spec in this repository's specs directory")
sources = json.loads((root / "sources.json").read_text())
catalog = json.loads((root / "catalog.json").read_text())
source = next((p for p in sources["packages"] if catalog["packages"][p["repo"]]["name"] == spec.stem), None)
if source is None:
    parser.error("unknown package")
selected = [source]
if spec.stem == "abyssland":
    selected += [sources["extras"]["glaze"], sources["extras"]["udis86"]]
topdir = args.outdir.resolve() / (spec.stem + "-srpm")
for directory in ["BUILD", "BUILDROOT", "RPMS", "SOURCES", "SPECS", "SRPMS"]:
    (topdir / directory).mkdir(parents=True, exist_ok=True)
for item in selected:
    destination = topdir / "SOURCES" / Path(urlsplit(item["url"]).path).name
    cached = args.cache / item["filename"] if args.cache else None
    if cached is not None and cached.is_file():
        shutil.copy2(cached, destination)
    elif not destination.is_file():
        with urllib.request.urlopen(item["url"], timeout=120) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output)
    if hashlib.sha256(destination.read_bytes()).hexdigest() != item["sha256"]:
        raise SystemExit(f"checksum mismatch: {destination.name}")
for patch in catalog["packages"][source["repo"]].get("patches", []):
    shutil.copy2(root / "patches" / spec.stem / patch, topdir / "SOURCES" / patch)
shutil.copy2(spec, topdir / "SPECS" / spec.name)
print(f"Verified source RPM inputs in {topdir}")
if not args.prepare_only:
    subprocess.run(["rpmbuild", "-bs", "--define", f"_topdir {topdir}",
                    str(topdir / "SPECS" / spec.name)], check=True)
    args.outdir.mkdir(parents=True, exist_ok=True)
    for srpm in (topdir / "SRPMS").glob("*.src.rpm"):
        shutil.copy2(srpm, args.outdir / srpm.name)
