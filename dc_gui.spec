Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.56
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	db3-devel
BuildRequires:	dctc >= 0.81
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
Requires:	dctc >= 0.81
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Direct Connect client (dctc) GUI.

%description -l pl
Graficzny interfejs użytkownika do dctc (Direct Connect).

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

gzip -9nf README ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/dc_gui
%attr(644,root,root) %{_applnkdir}/Network/Communications/*
