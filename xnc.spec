Summary:	xnc is a file manager for Linux
Summary(pl):	xnc jest zarz±dc± plików dla Linuksa
Name:		xnc
Version:	4.4.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xnc.dubna.su/src/xnc-4.4.7.src.tar.gz
# Source0-md5:	5f6a6a95aa83c35268c2d339bbd3ef83
Patch0:		%{name}-configure.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-gcc33.patch
URL:		http://www.xnc.dubna.su/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
xnc is a file manager for Linux.

%description -l pl
xnc jest zarz±dc± plików dla Linuksa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
	INSTMAN=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO WHATS_NEW
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xnc
%{_mandir}/man1/*
