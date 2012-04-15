%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 4
%define libname %mklibname xfcegui4_ %{major}
%define develname %mklibname xfcegui4 -d

Summary:	Various GTK+ widgets for Xfce desktop environment
Name:		libxfcegui4
Version:	4.9.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfcegui4/%{url_ver}/%{name}-%{version}.tar.bz2
#(tpg) http://bugzilla.xfce.org/show_bug.cgi?id=3614
Patch0:		%{name}-4.4.2-extension-strip.patch
Patch1:		%{name}-4.4.2-use-thunar.patch
Patch2:		%{name}-4.4.2-fix-underlinking.patch
Patch3:		libxfcegui4-fix-4.10.patch
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	startup-notification-devel
BuildRequires:	gettext-devel
BuildRequires:	xfce4-dev-tools >= 4.9.0
BuildRequires:	libglade2.0-devel
BuildRequires:	glade3-devel
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	gtk-doc

%description
Various GTK+ widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Obsoletes:	libxfcegui4-plugins < 4.5.91
Provides:	libxfcegui4-plugins
Requires:	librsvg2
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	%mklibname xfcegui4 4

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package common
Summary:	Translations for %{name}
Group:		Graphical desktop/Xfce
BuildArch:	noarch
Conflicts:	%{_lib}xfcegui4_4 < 4.8.1-5

%description common
This package contains common files for %{name}.

%package -n %{name}-glade
Summary:        Glade modules for %{name}
Group:          Graphical desktop/Xfce
Requires:	glade3
Conflicts:	%{_lib}xfcegui4_4 < 4.8.1-4

%description -n %{name}-glade
This package provides a catalog for Glade which allows the use of the
provided Xfce widgets in Glade.


%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	xfce4-dev-tools
Requires:	libglade2.0-devel
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
%patch3 -p1

%build
# (tpg) needed for patch 2
NOCONFIGURE=1 xdt-autogen

%configure2_5x \
	--disable-static \
	--enable-startup-notification \
	--enable-gladeui

%make

%install
%makeinstall_std

# %{tpg} drop libtool files
find %{buildroot} -name "*.la" -delete

%find_lang %{name} %{name}.lang

%files common -f %{name}.lang
%{_iconsdir}/hicolor/*/apps/xfce*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/libglade/2.0/libxfce4.so

%files -n %{name}-glade
%{_libdir}/glade3/modules/libgladexfce4.so
%{_datadir}/glade3/catalogs/xfce4.xml
%{_datadir}/glade3/catalogs/xfce4.xml.in
%{_datadir}/glade3/pixmaps/hicolor/*/actions/*.png

%files -n %{develname}
%doc AUTHORS ChangeLog README NEWS
%doc %{_datadir}/gtk-doc/html/libxfcegui4/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*
