%define name xmms-speex
%define version 0.9.1
%define release %mkrel 4

Summary: Speex support for XMMS
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sound
URL: http://jzb.rapanden.dk/projects/speex-xmms
Source: http://jzb.rapanden.dk/pub/speex-xmms-0.9.1.tar.bz2
Patch: speex-xmms-0.9.1-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: xmms 
BuildRequires: xmms-devel libspeex-devel
BuildRequires: libogg-devel

%define _xmmsinputdir %(xmms-config --input-plugin-dir)

%description
Speex is a free codec specialized for speech and voice. Install
this package to be able to read speex media files in XMMS.

%prep
%setup -q -n speex-xmms
%patch -p1

%build
make CFLAGS="-fPIC $RPM_OPT_FLAGS -I%_includedir/speex"

%install
mkdir -p %{buildroot}/%{_xmmsinputdir}
install libspeex.so %{buildroot}/%{_xmmsinputdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README 
%{_xmmsinputdir}/*.so


