Summary:	xnc - a file manager for Linux
Summary(pl.UTF-8):   xnc - zarządca plików dla Linuksa
Name:		xnc
Version:	5.0.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.xnc.dubna.su/src-5/%{name}-%{version}.src.tar.gz
# Source0-md5:	62446cdfdf5730f125fb351a658c0bd3
Patch0:		%{name}-Makefile_in.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.xnc.dubna.su/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
xnc is a file manager for Linux.

%description -l pl.UTF-8
xnc jest zarządcą plików dla Linuksa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{sr,sr@Latn}.po
mv -f po/{sp,sr}.po
%{__perl} -pi -e 's/sr sp/sr sr\@Latn/' po/LINGUAS

rm -rf jpeg

%build
cp -f /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README* TODO WHATS_NEW
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xnc
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
