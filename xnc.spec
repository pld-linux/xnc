Summary:	xnc is a file manager for Linux
Summary(pl):	xnc jest zarz�dc� plik�w pod Linuksa
Name:		xnc
Version:	4.4.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xnc.dubna.su/src/xnc-4.4.7.src.tar.gz
Patch0:		%{name}-configure.patch
Patch1:		%{name}-destdir.patch
URL:		http://www.xnc.dubna.su
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
xnc is a file manager for Linux

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
aclocal
%{__autoconf}

rm -rf jpeg
%configure2_13    
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE AUTHORS ABOUT-NLS README TODO WHATS_NEW
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root)%{_libdir}/xnc/*
%{_mandir}/man1/*
