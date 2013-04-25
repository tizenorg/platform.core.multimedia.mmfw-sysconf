Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.1.66
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz
ExcludeArch: %{ix86}
ExcludeArch: %{arm}

%description
Multimedia Framework system configuration package for simulator

%prep
%setup -q -n mmfw-sysconf-%{version} 

%build

%install

%post 

%postun 

%files
%defattr(-,root,root,-)
