Name:           oogradient
Version:        0.2.0
Release:        1%{?dist}
Summary:        Applies smooth TrueColor color gradient interpolation across lines of text.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oogradient
Source0:        oogradient-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oogradient is a sovereign, capability-bounded TEXT GRADIENT written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oogradient
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oogradient-uninstall

%files
/usr/bin/oogradient
/usr/bin/oogradient-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate oogradient to v0.2.0 (pure openOODA, MCP, tri-dist packaging)
