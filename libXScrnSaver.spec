Summary: X.Org X11 libXss runtime library
Name: libXScrnSaver
Version: 1.2.0
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel >= 7.0-9
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
X.Org X11 libXss runtime library

%package devel
Summary: X.Org X11 libXScrnSaver development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXss development package

%prep
%setup -q

# Disable static library creation by default.
%define with_static 0

%build
# FIXME: XScrnSaver.c:429: warning: dereferencing type-punned pointer will break strict-aliasing rules
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
%if ! %{with_static}
	--disable-static
%endif
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXss.so.1
%{_libdir}/libXss.so.1.0.0

%files devel
%defattr(-,root,root,-)
%if %{with_static}
%{_libdir}/libXss.a
%endif
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
#%dir %{_mandir}/man3x
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/scrnsaver.h

%changelog
* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.0-1
- libXScrnSaver 1.2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.1.3-4
- Un-require xorg-x11-filesystem

* Sun Jun 14 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1.3-3
- Don't claim ownership of %%_libdir/pkgconfig/ (#499660)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 04 2008 Adam Jackson <ajax@redhat.com> 1.1.3-1
- libXScrnSaver 1.1.3

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.1.2-5
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.2-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.1.2-3
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.1.2-2
- Don't install INSTALL

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1.1.2-1
- Update to 1.1.2

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.1.1-1
- Update to 1.1.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.1.0-3.1
- rebuild

* Wed Jun 07 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-3
- Update build dep to "xorg-x11-proto-devel >= 7.0-9" for scrnsaverproto 1.1
- Added "Requires: xorg-x11-proto-devel >= 7.0-9" to devel package, to match
  what is listed as required in xscrnsaver.pc

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-2
- Added "BuildRequires: pkgconfig" for (#193424)
- Replace "makeinstall" with "make install DESTDIR=..."
- Remove package ownership of mandir/libdir/etc.

* Fri May 12 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0, new Suspend request.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated libXScrnSaver to version 1.0.1 from X11R7.0

* Mon Jan 16 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Added "Requires: libX11-devel, libXext-devel" to work around bug (#176674).

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXScrnSaver to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libXScrnSaver to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-4
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Wed Nov 2 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-3
- Actually spell RPM_OPT_FLAGS correctly this time.

* Mon Oct 31 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Build with -fno-strict-aliasing to work around possible pointer aliasing
  issue

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXScrnSaver to version 0.99.2 from X11R7 RC1
- Updated file manifest to find manpages in "man3x"

* Mon Oct  3 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated to new upstream libXScrnSaver-0.99.1 which changes the .so name back
  to libXss, but keeps the inconsistent package name.  This may change again
  in the future.

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
