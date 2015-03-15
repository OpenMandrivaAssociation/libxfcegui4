%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 4
%define libname %mklibname xfcegui4_ %{major}
%define devname %mklibname xfcegui4 -d

Summary:	Various GTK+ widgets for Xfce desktop environment
Name:		libxfcegui4
Version:	4.10.0
Release:	7.1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfcegui4/%{url_ver}/%{name}-%{version}.tar.bz2
#(tpg) http://bugzilla.xfce.org/show_bug.cgi?id=3614
Patch0:		%{name}-4.4.2-extension-strip.patch
Patch1:		libxfcegui4-4.10.0-no-xfce_setenv.patch
BuildRequires:	gtk-doc
BuildRequires:	xfce4-dev-tools >= 4.12
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(gladeui-1.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.12
Conflicts:	%{_lib}xfcegui4_4 < 4.10.0-5

%description
Various GTK+ widgets for Xfce desktop environment.

%files
%{_libdir}/libglade/2.0/libxfce4.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Provides:	libxfcegui4-plugins = %{EVRD}
Requires:	librsvg2
Requires:	%{name} >= %{EVRD}
Requires:	%{name}-common >= %{EVRD}

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%files -n %{libname}
%{_libdir}/libxfcegui4.so.%{major}*

#----------------------------------------------------------------------------

%package common
Summary:	Translations for %{name}
Group:		Graphical desktop/Xfce
BuildArch:	noarch

%description common
This package contains common files for %{name}.

%files common -f %{name}.lang
%{_iconsdir}/hicolor/*/apps/xfce*

#----------------------------------------------------------------------------

%package glade
Summary:	Glade modules for %{name}
Group:		Graphical desktop/Xfce
Requires:	glade3

%description glade
This package provides a catalog for Glade which allows the use of the
provided Xfce widgets in Glade.

%files glade
%{_libdir}/glade3/modules/libgladexfce4.so
%{_datadir}/glade3/catalogs/xfce4.xml
%{_datadir}/glade3/catalogs/xfce4.xml.in
%{_datadir}/glade3/pixmaps/hicolor/*/actions/*.png

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	xfce4-dev-tools
Requires:	pkgconfig(gladeui-1.0)
Requires:	pkgconfig(libglade-2.0)
Provides:	%{name}-devel = %{EVRD}
Provides:	libxfce4gui-devel = %{EVRD}

%description -n %{devname}
Libraries and header files for the %{name} library.

%files -n %{devname}
%doc AUTHORS ChangeLog README NEWS
%doc %{_datadir}/gtk-doc/html/libxfcegui4/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .icons
%patch1 -p0 -b .setenv

%build
%configure2_5x \
	--disable-static \
	--enable-startup-notification \
	--enable-gladeui

%make

%install
%makeinstall_std

%find_lang %{name}
