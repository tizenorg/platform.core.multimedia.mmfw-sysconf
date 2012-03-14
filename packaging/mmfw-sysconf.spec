Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.1.22
Release:    1
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz

%description
Multimedia Framework system configuration package


%package simulator
Summary:    Multimedia Framework system configuration package for simulator
Group:      TO_BE/FILLED_IN

%description simulator
Multimedia Framework system configuration package for simulator


%prep
%setup -q 

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/
cp -rf  mmfw-sysconf-simulator/etc/* %{buildroot}%{_sysconfdir}/

mkdir -p %{buildroot}/opt/etc/mmfw-sysconf/mmfw-sysconf-simulator
cp -rf  mmfw-sysconf-simulator/opt/etc/* %{buildroot}/opt/etc/


%files simulator
%{_sysconfdir}/asound.conf
/opt/etc/*
/etc/pulse/*
