Summary:	xnc is a file manager for Linux
Summary(pl):	xnc jest zarz±dc± plików dla Linuksa
Name:		xnc
Version:	5.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xnc.dubna.su/src-5/%{name}-%{version}.src.tar.gz
# Source0-md5:	d702945813df0e483bf4c0630cfc355a
Patch0:		%{name}-configure.patch
URL:		http://www.xnc.dubna.su/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
xnc is a file manager for Linux.

%description -l pl
xnc jest zarz±dc± plików dla Linuksa.

%prep
%setup -q
%patch0 -p1

rm -rf jpeg

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTMAN=%{_mandir}/man1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README* TODO WHATS_NEW
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xnc
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
