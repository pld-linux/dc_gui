Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.48
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://ac2i.tzo.com/dctc/
Requires:	dctc >= 0.74
BuildRequires:	dctc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/

gzip -9nf README ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/dc_gui
%attr(644,root,root) %{_applnkdir}/Network/Misc/*
