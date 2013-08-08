Name:       mmfw-sysconf-simulator
Summary:    Multimedia Framework system configuration package
Version:    0.1.66
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz
Source1001: %{name}.manifest
ExclusiveArch:  %{ix86}

%description
Multimedia Framework system configuration package for simulator

%prep
%setup -q -n mmfw-sysconf-%{version} 
cp %{SOURCE1001} .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr
cp -arf mmfw-sysconf-simulator/* %{buildroot}

%post 

%postun 

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
/etc/asound.conf
/etc/pulse/*
/usr/etc/*.ini
/usr/etc/gst-openmax.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.common
/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
