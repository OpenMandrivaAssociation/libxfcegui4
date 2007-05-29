%define major 4
%define libname %mklibname xfcegui4_ %{major}

Summary:	Various GTK+ widgets for Xfce
Name:		libxfcegui4
Version: 	4.4.1
Release: 	%mkrel 2
License:	LGPL
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	dbh-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Various GTK+ widgets for Xfce.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Obsoletes:	libxfcegui4-plugins
Provides:	libxfcegui4-plugins

%description -n %{libname}
Gui libraries for Xfce.

%package -n %{libname}-devel
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	libxfcegui4-devel

%description -n %{libname}-devel
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/xfce4/modules/*.a
rm -f %{buildroot}/%{_datadir}/xfce4/xfce-svg-test.svg
rm -rf %{buildroot}/%{_datadir}/locale
#%%find_lang %name

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.%{major}*
%{_datadir}/gtk-doc/html/libxfcegui4/*
%{_iconsdir}/*/*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*
