%define debug_package %{nil}

Name:          nitrokey-udev-rules
Version:       1.1.1
Release:       %autorelease
Summary:       udev rules for Nitrokey devices

License:       CC0-1.0
URL:           https://github.com/Nitrokey/nitrokey-udev-rules/
Source0:       %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: python3
BuildRequires: systemd-rpm-macros
BuildRequires: systemd-udev

ExclusiveArch: noarch

%description
%{Summary}.

%prep
%autosetup


%build
%python3 generate.py v%{version} devices.toml 41-nitrokey.rules


%install
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0755 41-nitrokey.rules %{buildroot}%{_udevrulesdir}/41-nitrokey.rules


%check
udevadm verify 41-nitrokey.rules


%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/41-nitrokey.rules


%changelog
%autochangelog
