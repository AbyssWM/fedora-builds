srpm:
	dnf -y install --skip-unavailable rpm-build python3 systemd-rpm-macros cmake-rpm-macros
	python3 tools/srpm.py --spec "$(spec)" --outdir "$(outdir)"
