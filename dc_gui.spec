Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.77
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ac2i.tzo.com/dctc/%{name}2-%{version}.tar.gz
# Source0-md5:	45108ef6caa9d79c56392f0a5442707b
Patch0:		%{name}-home_etc.patch
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	dctc >= 0.85.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel
Requires:	dctc >= 0.85.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Direct Connect client (dctc) GUI.

%description -l pl
Graficzny interfejs u¿ytkownika do dctc (Direct Connect).

%prep
%setup -q -n %{name}2-%{version}
#%patch0 -p1

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

# dc_gui2.mo, but gnome/help/dc_gui

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/dc_gui2
%{_pixmapsdir}/dc_gui2.xpm
