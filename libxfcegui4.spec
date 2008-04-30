%define major 4
%define libname %mklibname xfcegui4_ %{major}
%define develname %mklibname xfcegui4 -d

Summary:	Various GTK+ widgets for Xfce desktop environment
Name:		libxfcegui4
Version: 	4.4.2
Release: 	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
#(tpg) http://bugzilla.xfce.org/show_bug.cgi?id=3614
Patch0:		%{name}-4.4.2-extension-strip.patch
Patch1:		%{name}-4.4.2-use-thunar.patch
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	startup-notification-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Various GTK+ widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Obsoletes:	libxfcegui4-plugins
Provides:	libxfcegui4-plugins
Requires:	librsvg2
Obsoletes:	%mklibname xfcegui4 4

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libxfce4gui-devel = %{version}-%{release}
Obsoletes:	%mklibname xfcegui4_ 4 -d

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q
%patch0 -p1 -b .icons
%patch1 -p1 -b .thunar

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11 \
	--disable-static \
	--enable-startup-notification

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
%{_iconsdir}/*/*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/*
%{_datadir}/gtk-doc/html/libxfcegui4/*
