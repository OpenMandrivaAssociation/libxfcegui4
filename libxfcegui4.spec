%define major 4
%define libname %mklibname xfcegui4_ %{major}
%define develname %mklibname xfcegui4 -d

Summary:	Various GTK+ widgets for Xfce desktop environment
Name:		libxfcegui4
Version: 	4.6.1
Release: 	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
#(tpg) http://bugzilla.xfce.org/show_bug.cgi?id=3614
Patch0:		%{name}-4.4.2-extension-strip.patch
Patch1:		%{name}-4.4.2-use-thunar.patch
Patch2:		%{name}-4.4.2-fix-underlinking.patch
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= 4.6.0
BuildRequires:	startup-notification-devel
BuildRequires:	gettext-devel
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	libglade2-devel
BuildRequires:	glade3-devel
BuildRequires:	xfconf-devel >= 4.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Various GTK+ widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Obsoletes:	libxfcegui4-plugins < 4.5.91
Provides:	libxfcegui4-plugins
Requires:	librsvg2
Obsoletes:	%mklibname xfcegui4 4

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	xfce4-dev-tools
Requires:	libglade2-devel
Requires:	glade3-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libxfce4gui-devel = %{version}-%{release}
Obsoletes:	%mklibname xfcegui4_ 4 -d

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q
%patch0 -p1 -b .icons
%patch1 -p1 -b .thunar
%patch2 -p1

%build
# (tpg) needed for patch 2
NOCONFIGURE=1 xdt-autogen

%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--disable-static \
	--enable-startup-notification

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%exclude %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_libdir}/lib*.so.%{major}*
%{_libdir}/libglade/2.0/libxfce4.la
%{_libdir}/libglade/2.0/libxfce4.so
%{_iconsdir}/*/*
%{_libdir}/glade3/modules/libgladexfce4.la
%{_libdir}/glade3/modules/libgladexfce4.so
%{_datadir}/glade3/catalogs/xfce4.xml
%{_datadir}/glade3/catalogs/xfce4.xml.in
%{_datadir}/glade3/pixmaps/hicolor/*/actions/*.png
%{_libdir}/libxfce4kbd-private.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*
%{_datadir}/gtk-doc/html/libxfcegui4/*
