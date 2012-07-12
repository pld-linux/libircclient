Summary:	Small but extremely powerful library which implements the IRC protocol
Name:		libircclient
Version:	1.6
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libircclient/%{name}-%{version}.tar.gz
# Source0-md5:	eb6a2c4e91862cc10de3b13b198cfa23
Patch0:		opt.patch
Patch1:		soname.patch
Patch2:		install.patch
URL:		http://www.ulduzsoft.com/libircclient/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libircclient is a small but powerful library, which implements
client-server IRC protocol. It has all features needed to create
your own IRC client or bot, including multi-threading support,
sync and async interfaces, CTCP/DCC support, colors, SSL connections
and so on.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--enable-shared \
	--enable-threads \
	--enable-ipv6 \
	--enable-openssl

%{__make} \
	LDFLAGS=%{rpmldflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p doc/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README THANKS
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html doc/rfc1459.txt
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
