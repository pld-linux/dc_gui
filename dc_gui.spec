Summary:	GUI for dctc
Summary(pl):	GUI do dctc
Name:		dc_gui
Version:	0.34
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
URL:		http://ac2i.tzo.com/dctc/
Requires:	dctc >= 0.60
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
dctc GUI.

%description -l pl
Graficzny interfejs u¿ytkownika do dctc.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README COPYING ChangeLog INSTALL ABOUT-NLS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/dc_gui
