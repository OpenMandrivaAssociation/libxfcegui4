%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 4
%define libname %mklibname xfcegui4_ %{major}
%define develname %mklibname xfcegui4 -d

Summary:	Various GTK+ widgets for Xfce desktop environment
Name:		libxfcegui4
Version:	4.10.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfcegui4/%{url_ver}/%{name}-%{version}.tar.bz2
#(tpg) http://bugzilla.xfce.org/show_bug.cgi?id=3614
Patch0:		%{name}-4.4.2-extension-strip.patch
BuildRequires:	pkgconfig(gdk-2.0) >= 2.0.6
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.10.0
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	gettext-devel
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gladeui-1.0)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.10.0
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

%build
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


%changelog
* Sat May 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 799656
- drop patch 1 and 2
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-1
+ Revision: 791111
- drop patch 3, applied by upstream
- update to new version 4.9.0

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-6
+ Revision: 789812
- Patch3: add support for xfce-4.10
- spec file clean
- add gtk-doc as a br
- rebuild

* Tue Dec 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-5
+ Revision: 745800
- move locales and other blob files from libname to a common subpackage
- spec file clean
- drop la files

* Thu Nov 17 2011 Crispin Boylan <crisb@mandriva.org> 4.8.1-4
+ Revision: 731432
- Fix requires

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-3
+ Revision: 700910
- rebuild for new libpng15

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 4.8.1-2
+ Revision: 640876
- rebuild

* Sat Feb 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 637382
- update to new version 4.8.1

* Thu Jan 20 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 631891
- update to new version 4.8.0

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 4.7.0-2mdv2011.0
+ Revision: 622588
- rebuild for new libgladeui

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.0-1mdv2011.0
+ Revision: 609459
- update to new version 4.7.0
- drop pacthes 3 and 4
- fix file list

* Fri Sep 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.4-3mdv2011.0
+ Revision: 579287
- rebuild

* Sun Aug 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.4-2mdv2011.0
+ Revision: 564180
- Patch4: fix overflow

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.4-1mdv2011.0
+ Revision: 553738
- update to new version 4.6.4

* Thu Mar 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-2mdv2011.0
+ Revision: 525125
- Patch3: replace invalid client ids (xfce upstream bug #6317)

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-1mdv2010.1
+ Revision: 495488
- update to new version 4.6.3

* Wed Jan 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2010.1
+ Revision: 486968
- update to new version 4.6.2
- update url for Source0

* Sun Jun 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.0
+ Revision: 385897
- Patch0: strip jpg icon extension too

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368571
- update to new version 4.6.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 349163
- rebuild whole xfce

* Sat Feb 28 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 346116
- fix file list

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345685
- Add files
- New upstream release

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333891
- update to new version 4.5.99.1

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329536
- update to new version 4.5.93

* Fri Dec 19 2008 Funda Wang <fwang@mandriva.org> 4.5.92-2mdv2009.1
+ Revision: 316053
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303489
- exclude xfce4-keyboard-shortcuts.xml as it should be in mandriva-xfce-config
- versionate buildrequires on xfconf-devel
- add buildrequires on xfconf-devel
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-3mdv2009.1
+ Revision: 302316
- rebuild

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-2mdv2009.1
+ Revision: 302169
- add buildrequires on glade3-devel

* Wed Oct 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294068
- Xfce4.6 beta1 is landing on cooker

* Sun Oct 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-11mdv2009.1
+ Revision: 292979
- use patch to fix underlinking
- Patch0: fix patch (#44001 OO.o icons were not displayed)

* Fri Aug 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-10mdv2009.0
+ Revision: 268290
- fix underlinking issue in a real bad way ;)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-9mdv2009.0
+ Revision: 205573
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Wed Apr 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-8mdv2009.0
+ Revision: 199472
- Patch0: this one should be better

* Wed Apr 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-7mdv2009.0
+ Revision: 199451
- Patch1: don't call xftree4 which is long time ago depreciated

* Fri Mar 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-6mdv2008.1
+ Revision: 189380
- Patch0: fix entension stripping for icons (Xfce upstream bug #3614)

* Tue Jan 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-5mdv2008.1
+ Revision: 156274
- fix libification, broken in last release

* Tue Jan 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2008.1
+ Revision: 156000
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2008.1
+ Revision: 113989
- update to the latest tarball

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 110092
- remove not needed buildrequires
- move docs to the devel package

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109929
- new version
- correct the license
- move docs to the devel package

* Thu Nov 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.1
+ Revision: 104399
- requires librsvg
- new license policy
- update description
- SILET remove it

* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 44109
- new devel library policy
- disable building of static files rather deleting them
- correct provides/obsoletes
- fix file list
- add translations

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32580
- bump release tag
- drop __libtoolize and __cputoolize
- spec file clean

* Wed Apr 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 14558
- New release 4.4.1


* Tue Jan 23 2007 plouf <plouf> 4.4.0-1mdv2007.0
+ Revision: 112307
- New release 4.4.0

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 4.3.99.2-1mdv2007.1
+ Revision: 91726
- New release 4.3.99.2
- Import libxfcegui4

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 4.3.90.2-1mdv2007.0
- 4.3.90.2 (Xfce-4.4 beta2)

* Wed Apr 26 2006 Jerome Soyer <saispo@mandriva.org> 4.3.90.1-1mdk
- Tue Apr 18 2006 trem <trem@mandriva.org> 4.3.90.1-1mdk
- 4.3.90.1

* Tue Mar 07 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r20246.1mdk
- svn release r20246
- drop plugin package

* Sat Feb 04 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r19739.1mdk 
- 4.3.0 svn r19739
- new major
- don't run libtoolize
- update filelist
- ignore 4.3.7 version

* Fri Jan 13 2006 Marcel Pol <mpol@mandriva.org> 4.2.3-1mdk
- 4.2.3
- drop P0, merged upstream

* Tue Oct 11 2005 Marcel Pol <mpol@mandriva.org> 4.2.2-2mdk
- From Cris Boylan <cris@mandriva.org>
  - Patch for gtk2.8 (fixes taskbar titles overflow, bug #18594)

* Wed May 25 2005 Marcel Pol <mpol@mandriva.org> 4.2.2-1mdk
- 4.2.2
- %%mkrel

* Wed Mar 16 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.1-1mdk
- 4.2.1

* Sat Jan 22 2005 Marcel Pol <mpol@mandrake.org> 4.2.0-2mdk
- group: Graphical desktop/Xfce

* Tue Jan 18 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.0-1mdk
- 4.2.0 Final

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.3-1mdk
- 4.1.99.3 (4.2.0 RC 3)
- remove unneeded devel files

* Sun Dec 12 2004 Charles A Edwards <eslrahc@mandrake.org> 4.1.99.2-1mdk
- 4.1.99.2 (4.2.0 RC 2)

* Thu Nov 18 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.1-2mdk
- buildrequires libxml2-devel

* Tue Nov 16 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.1-1mdk
- 4.1.99.1
- s/XFce/Xfce
- add buildrequires dbh-devel startup-notification-devel
- adjust soname major
- add plugins package for Xfce-utils and Xffm
- add locale files

* Tue Jul 13 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.6-1mdk
- 4.0.6
- reenable libtoolize

* Sun Apr 18 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.5-1mdk
- 4.0.5

* Sat Apr 10 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.4-1mdk
- 4.0.4

