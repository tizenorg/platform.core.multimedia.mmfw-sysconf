%bcond_with wayland

Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.2.2
Release:    0
Group:      Multimedia/Configuration
License:    Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz

%description
Multimedia Framework system configuration package including ini, conf and etc files.


%ifarch %arm aarch64

%package target-u3
Summary: Multimedia Framework system configuration package for u3
Group: Multimedia/Configuration
License: Apache-2.0

%description target-u3
Multimedia Framework system configuration package including ini, conf and etc files for u3 target.

%else

%package simulator
Summary: Multimedia Framework system configuration package for simulator
Group: Multimedia/Configuration
License: Apache-2.0

%description simulator
Multimedia Framework system configuration package including ini, conf and etc files for simulator.

%endif


%prep
%setup -q -n %{name}-%{version}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}


%ifarch %arm aarch64

mkdir -p %{buildroot}%{_datadir}/%{name}-target-u3
cp -arf %{name}-target-u3/* %{buildroot}%{_datadir}/%{name}-target-u3
%if %{with wayland}
mv %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini.wayland %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini
mv %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini.wayland %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini
rm %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini.x
rm %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini.x
%else
mv %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini.x %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini
mv %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini.x %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini
rm %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_player.ini.wayland
rm %{buildroot}%{_datadir}/%{name}-target-u3/usr/etc/mmfw_camcorder.ini.wayland
%endif
mkdir -p %{buildroot}%{_datadir}/%{name}-target-u3/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-u3/usr/share/license/%{name}-target-u3
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-u3/usr/share/license/%{name}-target-u3

%else

mkdir -p %{buildroot}%{_datadir}/%{name}-simulator
cp -arf %{name}-simulator/* %{buildroot}%{_datadir}/%{name}-simulator
%if %{with wayland}
mv %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini.wayland %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini
mv %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini.wayland %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini
rm %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini.x
rm %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini.x
%else
mv %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini.x %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini
mv %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini.x %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini
rm %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_player.ini.wayland
rm %{buildroot}%{_datadir}/%{name}-simulator/usr/etc/mmfw_camcorder.ini.wayland
%endif
mkdir -p %{buildroot}%{_datadir}/%{name}-simulator/usr/share/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-simulator/usr/share/license/%{name}-simulator
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-simulator/usr/share/license/%{name}-simulator

%endif


%ifarch %arm aarch64

%post target-u3
cp -arf %{_datadir}/mmfw-sysconf-target-u3/* /
rm -rf %{_datadir}/mmfw-sysconf-target-u3

%else

%post simulator
cp -arf %{_datadir}/mmfw-sysconf-simulator/* /
rm -rf %{_datadir}/mmfw-sysconf-simulator

%endif


%postun


%ifarch %arm aarch64

%files target-u3
%manifest mmfw-sysconf-target-u3.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-u3/etc/asound.conf
%{_datadir}/mmfw-sysconf-target-u3/etc/pulse/*
%{_datadir}/mmfw-sysconf-target-u3/usr/etc/*.ini
%{_datadir}/mmfw-sysconf-target-u3/usr/etc/gst-openmax.conf
%{_datadir}/mmfw-sysconf-target-u3/usr/etc/gst-tz-openmax.conf
%{_datadir}/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-u3/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-u3/opt/system/*
%{_datadir}/mmfw-sysconf-target-u3/usr/share/license/mmfw-sysconf-target-u3

%else

%files simulator
%manifest mmfw-sysconf-simulator.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-simulator/etc/asound.conf
%{_datadir}/mmfw-sysconf-simulator/etc/pulse/*
%{_datadir}/mmfw-sysconf-simulator/usr/etc/*.ini
%{_datadir}/mmfw-sysconf-simulator/usr/etc/gst-openmax.conf
%{_datadir}/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-simulator/usr/share/license/mmfw-sysconf-simulator

%endif

