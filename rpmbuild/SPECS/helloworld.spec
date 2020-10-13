Summary:	rpm helloworld
Name:		helloworld
Version:	1.0.0
Release:	1%{?dist}
License:	GPL
#URL:
Source0:	%{name}-%{version}.tar.gz
#BuildRequires:
#Requires:  

%description
print helloworld

%prep
%autosetup


%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp $RPM_BUILD_DIR/%{name}-%{version}/helloworld $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf %RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/bin/helloworld



%changelog
