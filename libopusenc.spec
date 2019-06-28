%define major		0
%define libname		%mklibname opusenc %{major}
%define develname	%mklibname opusenc -d

Name:		libopusenc
Version:	0.2.1
Release:	%mkrel 1
Summary:	A library that provides an easy way to encode Ogg Opus files
Group:		System/Libraries
License:	BSD
URL:		https://opus-codec.org/
Source0:	https://ftp.osuosl.org/pub/xiph/releases/opus/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	doxygen
BuildRequires:	pkgconfig(opus)

%description
A library that provides an easy way to encode Ogg Opus files.

%package -n	%{libname}
Summary:	A library that provides an easy way to encode Ogg Opus files
Group:		System/Libraries

%description -n	%{libname}
A library that provides an easy way to encode Ogg Opus files.

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_datadir}/doc/%{name}/

%check
make check V=1

%files -n %{libname}
%license COPYING
%{_libdir}/%{name}.so.%{major}{,.*}

%files -n %{develname}
%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Apr 14 2019 daviddavid <daviddavid> 0.2.1-1.mga7
+ Revision: 1389928
- initial package libopusenc

