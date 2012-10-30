Name:           chrpath
Version:        0.13
Release:        3
License:        GPL+
Summary:        Modify rpath of compiled programs
Url:            http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
Group:          Development/Tools
Source0:        http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/%{name}-%{version}.tar.gz

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q


%build

%configure --disable-static
# Call make instruction with smp support
make %{?_smp_mflags}

%install
%make_install

rm -fr %{buildroot}/usr/doc

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/chrpath
%doc %{_mandir}/man1/chrpath.1*


