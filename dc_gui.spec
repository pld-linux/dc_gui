Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.39
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://ac2i.tzo.com/dctc/
Requires:	dctc >= 0.65
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Direct Connect client (dctc) GUI.

%description -l pl
Graficzny interfejs u¿ytkownika do dctc (Direct Connect).

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/dc_gui
