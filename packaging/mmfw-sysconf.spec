Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.1.8
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
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
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/mmfw-sysconf
mkdir -p %{buildroot}/opt/etc/mmfw-sysconf

mkdir -p %{buildroot}%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-simulator
cp -rf  mmfw-sysconf-simulator/etc/* %{buildroot}%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-simulator/

mkdir -p %{buildroot}/opt/etc/mmfw-sysconf/mmfw-sysconf-simulator
cp -rf  mmfw-sysconf-simulator/opt/etc/* %{buildroot}/opt/etc/mmfw-sysconf/mmfw-sysconf-simulator/

mkdir -p %{buildroot}%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-cleansdk-target
cp -rf  mmfw-sysconf-simulator/etc/* %{buildroot}%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-cleansdk-target/

mkdir -p %{buildroot}/opt/etc/mmfw-sysconf/mmfw-sysconf-cleansdk-target
cp -rf  mmfw-sysconf-simulator/opt/etc/* %{buildroot}/opt/etc/mmfw-sysconf/mmfw-sysconf-cleansdk-target/

%post simulator
rm -f %{_sysconfdir}/asound.conf
ln -s %{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-simulator/asound.conf %{_sysconfdir}/asound.conf

rm -f /opt/etc/mmfw_camcorder.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_pri.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_sec.ini
rm -f /opt/etc/mmfw_player.ini

ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-simulator/mmfw_camcorder.ini /opt/etc/mmfw_camcorder.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-simulator/mmfw_camcorder_dev_video_pri.ini /opt/etc/mmfw_camcorder_dev_video_pri.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-simulator/mmfw_camcorder_dev_video_sec.ini /opt/etc/mmfw_camcorder_dev_video_sec.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-simulator/mmfw_player.ini /opt/etc/mmfw_player.ini

%post cleansdk-target
rm -f %{_sysconfdir}/asound.conf
ln -s %{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-cleansdk-target/asound.conf %{_sysconfdir}/asound.conf

rm -f /opt/etc/mmfw_camcorder.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_pri.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_sec.ini
rm -f /opt/etc/mmfw_player.ini

ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-cleansdk-target/mmfw_camcorder.ini /opt/etc/mmfw_camcorder.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-cleansdk-target/mmfw_camcorder_dev_video_pri.ini /opt/etc/mmfw_camcorder_dev_video_pri.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-cleansdk-target/mmfw_camcorder_dev_video_sec.ini /opt/etc/mmfw_camcorder_dev_video_sec.ini
ln -s /opt/etc/mmfw-sysonf/mmfw-sysconf-cleansdk-target/mmfw_player.ini /opt/etc/mmfw_player.ini


%postun simulator
rm -f %{_sysconfdir}/asound.conf
rm -f /opt/etc/mmfw_camcorder.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_pri.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_sec.ini
rm -f /opt/etc/mmfw_player.ini

%postun cleansdk-target
rm -f %{_sysconfdir}/asound.conf
rm -f /opt/etc/mmfw_camcorder.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_pri.ini
rm -f /opt/etc/mmfw_camcorder_dev_video_sec.ini
rm -f /opt/etc/mmfw_player.ini


%files simulator
%defattr(-,root,root,-)
%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-simulator/*
/opt/etc/mmfw-sysconf/mmfw-sysconf-simulator/*

%files cleansdk-target
%defattr(-,root,root,-)
%{_sysconfdir}/mmfw-sysconf/mmfw-sysconf-cleansdk-target/*
/opt/etc/mmfw-sysconf/mmfw-sysconf-cleansdk-target/*
