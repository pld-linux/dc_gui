Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.74
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ac2i.tzo.com/dctc/%{name}2-%{version}.tar.gz
# Source0-md5:	427356dc0e5f8cdcdbec06c06eecc6f6
Patch0:		%{name}-home_etc.patch
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	db-devel
BuildRequires:	dctc >= 0.85.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:  alsa-lib-devel
Requires:	dctc >= 0.85.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Direct Connect client (dctc) GUI.

%description -l pl
Graficzny interfejs u¿ytkownika do dctc (Direct Connect).

%prep
%setup -q -n %{name}2-%{version}
%patch0 -p1

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}2 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}2.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/dc_gui2
%{_pixmapsdir}/dc_gui2.xpm
%{_datadir}/gnome/help/dc_gui
