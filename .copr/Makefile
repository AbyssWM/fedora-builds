srpm:
	dnf -y install rpm-build python3 systemd-rpm-macros cmake-rpm-macros meson-rpm-macros
	python3 tools/srpm.py --spec "$(spec)" --outdir "$(outdir)"
