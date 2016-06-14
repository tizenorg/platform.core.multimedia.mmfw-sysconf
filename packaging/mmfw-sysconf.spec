Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.2.70
Release:    0
Group:      Multimedia/Configuration
License:    LGPL-2.1+ and Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz

%description
Multimedia Framework system configuration package including ini, conf and etc files.


%ifarch %arm aarch64

%package target-u3
Summary: Multimedia Framework system configuration package for u3
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-u3
Multimedia Framework system configuration package including ini, conf and etc files for u3 target.

%package target-n4
Summary: Multimedia Framework system configuration package for n4
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-n4
Multimedia Framework system configuration package including ini, conf and etc files for n4 target.

%package target-hawkp
Summary: Multimedia Framework system configuration package for hawkp
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-hawkp
Multimedia Framework system configuration package including ini, conf and etc files for hawkp target.

%package target-tm1
Summary: Multimedia Framework system configuration package for tm1
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-tm1
Multimedia Framework system configuration package including ini, conf and etc files for tm1 target.

%package target-tw1
Summary: Multimedia Framework system configuration package for tw1
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-tw1
Multimedia Framework system configuration package including ini, conf and etc files for tw1 target.

%package target-artik10
Summary: Multimedia Framework system configuration package for artik 10
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

%description target-artik10
Multimedia Framework system configuration package including ini, conf and etc files for artik 10 target.


%else

%package simulator
Summary: Multimedia Framework system configuration package for simulator
Group: Multimedia/Configuration
License: LGPL-2.1+ and Apache-2.0

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

mkdir -p %{buildroot}%{_datadir}/%{name}-target-u3%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-u3%{_datadir}/license/%{name}-target-u3
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-u3%{_datadir}/license/%{name}-target-u3

mkdir -p %{buildroot}%{_datadir}/%{name}-target-n4
cp -arf %{name}-target-n4/* %{buildroot}%{_datadir}/%{name}-target-n4

mkdir -p %{buildroot}%{_datadir}/%{name}-target-n4%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-n4%{_datadir}/license/%{name}-target-n4
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-n4%{_datadir}/license/%{name}-target-n4

mkdir -p %{buildroot}%{_datadir}/%{name}-target-hawkp
cp -arf %{name}-target-hawkp/* %{buildroot}%{_datadir}/%{name}-target-hawkp

mkdir -p %{buildroot}%{_datadir}/%{name}-target-hawkp%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-hawkp%{_datadir}/license/%{name}-target-hawkp
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-hawkp%{_datadir}/license/%{name}-target-hawkp

mkdir -p %{buildroot}%{_datadir}/%{name}-target-tm1
cp -arf %{name}-target-tm1/* %{buildroot}%{_datadir}/%{name}-target-tm1

mkdir -p %{buildroot}%{_datadir}/%{name}-target-tm1%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-tm1%{_datadir}/license/%{name}-target-tm1
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-tm1%{_datadir}/license/%{name}-target-tm1

mkdir -p %{buildroot}%{_datadir}/%{name}-target-tw1
cp -arf %{name}-target-tw1/* %{buildroot}%{_datadir}/%{name}-target-tw1

mkdir -p %{buildroot}%{_datadir}/%{name}-target-tw1%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-tw1%{_datadir}/license/%{name}-target-tw1
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-tw1%{_datadir}/license/%{name}-target-tw1

mkdir -p %{buildroot}%{_datadir}/%{name}-target-artik10
cp -arf %{name}-target-artik10/* %{buildroot}%{_datadir}/%{name}-target-artik10
mkdir -p %{buildroot}%{_datadir}/%{name}-target-artik10%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-target-artik10%{_datadir}/license/%{name}-target-artik10
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-target-artik10%{_datadir}/license/%{name}-target-artik10

%else

mkdir -p %{buildroot}%{_datadir}/%{name}-simulator
cp -arf %{name}-simulator/* %{buildroot}%{_datadir}/%{name}-simulator

mkdir -p %{buildroot}%{_datadir}/%{name}-simulator%{_datadir}/license
cp LICENSE.APLv2.0 %{buildroot}%{_datadir}/%{name}-simulator%{_datadir}/license/%{name}-simulator
cat LICENSE.LGPLv2.1 >> %{buildroot}%{_datadir}/%{name}-simulator%{_datadir}/license/%{name}-simulator

%endif


%ifarch %arm aarch64

%post target-u3
cp -arf %{_datadir}/mmfw-sysconf-target-u3/* /
rm -rf %{_datadir}/mmfw-sysconf-target-u3

%post target-n4
cp -arf %{_datadir}/mmfw-sysconf-target-n4/* /
rm -rf %{_datadir}/mmfw-sysconf-target-n4

%post target-hawkp
cp -arf %{_datadir}/mmfw-sysconf-target-hawkp/* /
rm -rf %{_datadir}/mmfw-sysconf-target-hawkp

%post target-tm1
cp -arf %{_datadir}/mmfw-sysconf-target-tm1/* /
rm -rf %{_datadir}/mmfw-sysconf-target-tm1

%post target-tw1
cp -arf %{_datadir}/mmfw-sysconf-target-tw1/* /
rm -rf %{_datadir}/mmfw-sysconf-target-tw1

%post target-artik10
cp -arf %{_datadir}/mmfw-sysconf-target-artik10/* /
rm -rf %{_datadir}/mmfw-sysconf-target-artik10

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
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-u3%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-u3%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-u3%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-u3%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-u3%{_datadir}/license/mmfw-sysconf-target-u3

%files target-n4
%manifest mmfw-sysconf-target-n4.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-n4%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-n4%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-n4%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-n4%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-n4%{_datadir}/license/mmfw-sysconf-target-n4

%files target-hawkp
%manifest mmfw-sysconf-target-hawkp.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-hawkp%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-hawkp%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-hawkp%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-hawkp%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-hawkp%{_datadir}/license/mmfw-sysconf-target-hawkp

%files target-tm1
%manifest mmfw-sysconf-target-tm1.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-tm1%{_sysconfdir}/multimedia/audio_hw.xml
%{_datadir}/mmfw-sysconf-target-tm1%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-tm1%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-tm1%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-tm1%{_datadir}/license/mmfw-sysconf-target-tm1

%files target-tw1
%manifest mmfw-sysconf-target-tw1.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-tw1%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-tw1%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-tw1%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-tw1%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-tw1%{_datadir}/license/mmfw-sysconf-target-tw1

%files target-artik10
%manifest mmfw-sysconf-target-artik10.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-target-artik10%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-target-artik10%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-target-artik10%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-target-artik10%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-target-artik10%{_datadir}/license/mmfw-sysconf-target-artik10

%else

%files simulator
%manifest mmfw-sysconf-simulator.manifest
%defattr(-,root,root,-)
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/asound.conf
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/pulse/*
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/murphy/*
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/profile.d/*
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/multimedia/*.ini
%{_datadir}/mmfw-sysconf-simulator%{_sysconfdir}/multimedia/*.conf
%{_datadir}/mmfw-sysconf-simulator%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/mmfw-sysconf-simulator%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/mmfw-sysconf-simulator%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
%{_datadir}/mmfw-sysconf-simulator%{_datadir}/license/mmfw-sysconf-simulator

%endif
