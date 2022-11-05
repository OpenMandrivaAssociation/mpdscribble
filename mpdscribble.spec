Summary:	Mpd client which submits information about tracks being played to Lastfm
Name:		mpdscribble
Version:	0.24
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://mpd.wikia.com/wiki/Client:Mpdscribble
Source0:	http://www.musicpd.org/download/mpdscribble/%{version}/%{name}-%{version}.tar.xz
BuildRequires: meson
BuildRequires: mpd
BuildRequires: boost-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libmpdclient)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(systemd)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	mpd

%description
Mpdscribble is a music player daemon client which submits information about
tracks being played to Last.fm (formerly audioscrobbler), with the following
features:
* written in C, consumes very little memory and CPU
* full support for MPD's "idle" mode
* last.fm protocol 1.2 (including "now playing") supports seeking, crossfading,
* repeated songs 

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install


%files
%defattr(-,root,root)
%doc README.rst AUTHORS COPYING NEWS
%{_bindir}/mpdscribble
%{_mandir}/*/*
%{_sysconfdir}/mpdscribble.conf
%{_prefix}/lib/systemd/system/mpdscribble.service
%{_prefix}/lib/systemd/user/mpdscribble.service



%changelog
* Fri Dec 23 2011 Andrey Bondrov <abondrov@mandriva.org> 0.22-3mdv2011.0
+ Revision: 744855
- Fix BuildRequires (as libsoup Provides changed)
- Bump release
- New version 0.22, update BuildRequires

* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 0.20-1mdv2011.0
+ Revision: 585866
- bump release

* Sun Aug 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.18.1-1mdv2010.0
+ Revision: 422455
- Update to new version 0.18.1
- Remove format string patch: not needed anymore

* Wed May 13 2009 Rémy Clouard <shikamaru@mandriva.org> 0.17-2mdv2010.0
+ Revision: 375216
- fix wrong dependency that prevents installing the package on x86_64
- fix a warning in rpmlint (summary too long)

* Wed Mar 18 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.17-1mdv2009.1
+ Revision: 357401
- Fixed summary.
- Fixed license.
- import mpdscribble


