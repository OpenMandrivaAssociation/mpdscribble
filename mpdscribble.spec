Summary:	Mpd client which submits information about tracks being played to Lastfm
Name:		mpdscribble
Version:	0.17
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Url:		http://mpd.wikia.com/wiki/Client:Mpdscribble
Source0:	http://downloads.sourceforge.net/musicpd/mpdscribble-0.17.tar.bz2
Patch0:		mpdscribble-0.17-format-not-a-string-literal.patch
Requires:	mpd
BuildRequires:	libsoup-2.4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch0 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/var/cache/mpdscribble/
touch %{buildroot}/var/cache/mpdscribble/cache

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS
%{_bindir}/mpdscribble
%{_mandir}/*/*
%{_sysconfdir}/mpdscribble.conf
%attr(0600,mpd,audio) %dir /var/cache/mpdscribble
%attr(0600,mpd,audio) /var/cache/mpdscribble/cache


