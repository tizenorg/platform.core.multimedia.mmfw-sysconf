Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.1.41
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz

%description
Multimedia Framework system configuration package

%ifarch %{arm}
%package -n mmfw-sysconf-cleansdk-target
Summary:    Multimedia Framework system configuration package for clean SDK target binary
Group:      TO_BE/FILLED_IN

%description -n mmfw-sysconf-cleansdk-target
Multimedia Framework system configuration package for clean SDK target binary

%else

%package -n mmfw-sysconf-simulator
Summary:    Multimedia Framework system configuration package for simulator
Group:      TO_BE/FILLED_IN

%description -n mmfw-sysconf-simulator
Multimedia Framework system configuration package for simulator
%endif



%prep
%setup -q 

%build

%install
rm -rf %{buildroot}

%ifarch %{arm}
	mkdir -p %{buildroot}/opt/etc/mmfw-sysconf
	cp -arf mmfw-sysconf-cleansdk-target/* %{buildroot}
%else
	mkdir -p %{buildroot}/opt/etc/mmfw-sysconf
	cp -arf mmfw-sysconf-simulator/* %{buildroot}
%endif

%post 

%postun 

%ifarch %{arm}
%files -n mmfw-sysconf-cleansdk-target
%defattr(-,root,root,-)
/etc/asound.conf
/etc/pulse/*
/usr/etc/*.ini
/usr/etc/gst-openmax.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.common
/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
%else
%files -n mmfw-sysconf-simulator
%defattr(-,root,root,-)
/etc/asound.conf
/etc/pulse/*
/usr/etc/*.ini
/usr/etc/gst-openmax.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.common
/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
%endif

