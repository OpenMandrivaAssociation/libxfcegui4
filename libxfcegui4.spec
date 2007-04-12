%define lib_major       4
%define lib_name        %mklibname xfcegui4_ %{lib_major}
%define version		4.4.0
%define rel		1
%define __libtoolize	/bin/true
%define __cputoolize	/bin/true


Summary: 	Various GTK+ widgets for Xfce
Name: 		libxfcegui4
Version: 	%{version}
Release: 	%mkrel 1
License:	LGPL
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.bz2
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	dbh-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxml2-devel

%description
Various GTK+ widgets for Xfce.

%package -n %{lib_name}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Obsoletes:	libxfcegui4-plugins
Provides:	libxfcegui4-plugins

%description -n %{lib_name}
Gui libraries for Xfce.

%package -n %{lib_name}-devel
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{lib_name} = %{version}
Provides:	libxfcegui4-devel

%description -n %{lib_name}-devel
Libraries and header files for the %{name} library.

%prep
%setup -q -n %{name}-%{version}

%build
# xinerama needs testing, see README
%configure2_5x --enable-xinerama --sysconfdir=%_sysconfdir/X11
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/xfce4/modules/*.a
rm -f %{buildroot}/%{_datadir}/xfce4/xfce-svg-test.svg
rm -rf %{buildroot}/%{_datadir}/locale
#%%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig


%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*
%{_datadir}/gtk-doc/html/libxfcegui4/*
%{_iconsdir}/*/*
%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*


