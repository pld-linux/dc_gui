Summary:	GUI for dctc (Direct Connect)
Summary(pl):	GUI do dctc (Direct Connect)
Name:		dc_gui
Version:	0.69
Release:	1.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ac2i.tzo.com/dctc/%{name}2-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-home_etc.patch
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	db-devel
BuildRequires:	dctc >= 0.83.7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	imlib-devel
BuildRequires:	libgnomeui-devel
Requires:	dctc >= 0.83.7
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
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
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

%find_lang %{name}2 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}2.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/dc_gui2
%attr(644,root,root) %{_applnkdir}/Network/Communications/*
%{_pixmapsdir}/dc_gui2
%{_datadir}/gnome/help/dc_gui/C
