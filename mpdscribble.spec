Summary:	Mpd client which submits information about tracks being played to Lastfm
Name:		mpdscribble
Version:	0.26
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://mpd.wikia.com/wiki/Client:Mpdscribble
Source0:	https://www.musicpd.org/download/mpdscribble/%{version}/%{name}-%{version}.tar.xz
BuildRequires: meson >= 1.2
BuildRequires: mpd
BuildRequires: ninja
BuildRequires: boost-devel
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libmpdclient) >= 2.2
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(systemd)
Requires:	mpd

%description
Mpdscribble is a music player daemon client which submits information about
tracks being played to Last.fm (formerly audioscrobbler), with the following
features:
* written in C, consumes very little memory and CPU;
* full support for MPD's "idle" mode;
* last.fm protocol 1.2 (including "now playing") supports seeking, crossfading
   and repeated songs.

%files
%doc README.rst AUTHORS COPYING NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix FSF address and make rpmlint happy
sed -i 's/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA/31 Milk Street, # 960789, Boston, MA 02196, USA/g' COPYING


%build
%meson
%meson_build


%install
%meson_install

# Fix rpmlint error
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf
