Summary:	rpm helloworld
Name:		helloworld
Version:	1.0.1
Release:	2%{?dist}
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
* Wed Oct 14 2020 Li xin <601998977@qq.com> 1.0.1
- add 1 line
