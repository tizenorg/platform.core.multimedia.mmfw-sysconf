Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.2.0
Release:    0
Group:      Multimedia/Configuration
License:    Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz

%description
Multimedia Framework system configuration package

%ifarch %{arm}

%package target-c210
Summary: Multimedia Framework system configuration package for C210
Group: Multimedia/Configuration
License: Apache-2.0

%description target-c210
Multimedia Framework system configuration package for C210


%package target-e4412
Summary: Multimedia Framework system configuration package for Exynos4412
Group: Multimedia/Configuration
License: Apache-2.0

%description target-e4412
Multimedia Framework system configuration package for Exynos4412


%package target-u3
Summary: Multimedia Framework system configuration package for u3
Group: Multimedia/Configuration
License: Apache-2.0

%description target-u3
Multimedia Framework system configuration package for u3

%else

%package simulator
Summary: Multimedia Framework system configuration package for simulator
Group: Multimedia/Configuration
License: Apache-2.0

%description simulator
Multimedia Framework system configuration package for simulator

%endif


%prep
%setup -q -n %{name}-%{version}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr

%ifarch %{arm}

mkdir -p %{buildroot}/%{name}-target-c210
cp -arf %{name}-target-c210/* %{buildroot}/%{name}-target-c210
mkdir -p %{buildroot}/%{name}-target-c210/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}/%{name}-target-c210/usr/share/license/%{name}-target-c210
cat LICENSE.LGPLv2.1 >> %{buildroot}/%{name}-target-c210/usr/share/license/%{name}-target-c210
mkdir -p %{buildroot}/%{name}-target-e4412
cp -arf %{name}-target-e4412/* %{buildroot}/%{name}-target-e4412
mkdir -p %{buildroot}/%{name}-target-e4412/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}/%{name}-target-e4412/usr/share/license/%{name}-target-e4412
cat LICENSE.LGPLv2.1 >> %{buildroot}/%{name}-target-e4412/usr/share/license/%{name}-target-e4412
mkdir -p %{buildroot}/%{name}-target-u3
cp -arf %{name}-target-u3/* %{buildroot}/%{name}-target-u3
mkdir -p %{buildroot}/%{name}-target-u3/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}/%{name}-target-u3/usr/share/license/%{name}-target-u3
cat LICENSE.LGPLv2.1 >> %{buildroot}/%{name}-target-u3/usr/share/license/%{name}-target-u3

%else

mkdir -p %{buildroot}/%{name}-simulator
cp -arf %{name}-simulator/* %{buildroot}/%{name}-simulator
mkdir -p %{buildroot}/%{name}-simulator/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}/%{name}-simulator/usr/share/license/%{name}-simulator
cat LICENSE.LGPLv2.1 >> %{buildroot}/%{name}-simulator/usr/share/license/%{name}-simulator

%endif


%ifarch %{arm}

%post target-c210
cp -arf /mmfw-sysconf-target-c210/* /
rm -rf /mmfw-sysconf-target-c210

%post target-e4412
cp -arf /mmfw-sysconf-target-e4412/* /
rm -rf /mmfw-sysconf-target-e4412

%post target-u3
cp -arf /mmfw-sysconf-target-u3/* /
rm -rf /mmfw-sysconf-target-u3

%else

%post simulator
cp -arf /mmfw-sysconf-simulator/* /
rm -rf /mmfw-sysconf-simulator

%endif


%postun 


%ifarch %{arm}

%files target-c210
%manifest mmfw-sysconf-target-c210.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-target-c210/etc/asound.conf
/mmfw-sysconf-target-c210/etc/pulse/*
/mmfw-sysconf-target-c210/usr/etc/*.ini
/mmfw-sysconf-target-c210/usr/etc/gst-openmax.conf
/mmfw-sysconf-target-c210/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-target-c210/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-target-c210/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-target-c210/usr/share/license/mmfw-sysconf-target-c210

%files target-e4412
%manifest mmfw-sysconf-target-e4412.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-target-e4412/etc/asound.conf
/mmfw-sysconf-target-e4412/etc/pulse/*
/mmfw-sysconf-target-e4412/usr/etc/*.ini
/mmfw-sysconf-target-e4412/usr/etc/gst-openmax.conf
/mmfw-sysconf-target-e4412/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-target-e4412/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-target-e4412/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-target-e4412/usr/share/license/mmfw-sysconf-target-e4412

%files target-u3
%manifest mmfw-sysconf-target-u3.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-target-u3/etc/asound.conf
/mmfw-sysconf-target-u3/etc/pulse/*
/mmfw-sysconf-target-u3/usr/etc/*.ini
/mmfw-sysconf-target-u3/usr/etc/gst-openmax.conf
/mmfw-sysconf-target-u3/usr/etc/gst-tz-openmax.conf
/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-target-u3/opt/system/*
/mmfw-sysconf-target-u3/usr/share/license/mmfw-sysconf-target-u3

%else

%files simulator
%manifest mmfw-sysconf-simulator.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-simulator/etc/asound.conf
/mmfw-sysconf-simulator/etc/pulse/*
/mmfw-sysconf-simulator/usr/etc/*.ini
/mmfw-sysconf-simulator/usr/etc/gst-openmax.conf
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-simulator/usr/share/license/mmfw-sysconf-simulator

%endif

