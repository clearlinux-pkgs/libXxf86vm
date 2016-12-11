#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXxf86vm
Version  : 1.1.4
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-1.1.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-1.1.4.tar.gz
Summary  : XFree86 Video Mode Extension Library
Group    : Development/Tools
License  : MIT
Requires: libXxf86vm-lib
Requires: libXxf86vm-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xf86vidmodeproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xf86vidmodeproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
libXxf86vm - Extension library for the XFree86-VidMode X extension
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libXxf86vm package.
Group: Development
Requires: libXxf86vm-lib
Provides: libXxf86vm-devel

%description dev
dev components for the libXxf86vm package.


%package dev32
Summary: dev32 components for the libXxf86vm package.
Group: Default
Requires: libXxf86vm-lib32

%description dev32
dev32 components for the libXxf86vm package.


%package doc
Summary: doc components for the libXxf86vm package.
Group: Documentation

%description doc
doc components for the libXxf86vm package.


%package lib
Summary: lib components for the libXxf86vm package.
Group: Libraries

%description lib
lib components for the libXxf86vm package.


%package lib32
Summary: lib32 components for the libXxf86vm package.
Group: Default

%description lib32
lib32 components for the libXxf86vm package.


%prep
%setup -q -n libXxf86vm-1.1.4
pushd ..
cp -a libXxf86vm-1.1.4 build32
popd

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xf86vmode.h
/usr/lib64/libXxf86vm.so
/usr/lib64/pkgconfig/xxf86vm.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXxf86vm.so
/usr/lib32/pkgconfig/32xxf86vm.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXxf86vm.so.1
/usr/lib64/libXxf86vm.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXxf86vm.so.1
/usr/lib32/libXxf86vm.so.1.0.0
