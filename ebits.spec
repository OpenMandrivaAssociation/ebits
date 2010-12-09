%define	name	ebits
%define	version	0.0.2
%define rel 0.%{cvsrel}.11

%define cvsrel 20030730

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: Enlightened Canvas Image Bit Library
Name: %{name}
Version: %{version}
Release: %mkrel %rel
License: BSD
Group: Development/Other
URL: http://www.enlightenment.org/efm.html
Source: %{name}-%{cvsrel}.tar.bz2
Patch: ebits-use-pkgconfig.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: evas-devel, edb-devel, freetype2-devel
Buildrequires: MesaGLU-devel X11-devel jpeg-devel

%description
The Ebits library provides layout functionality for 
graphical elements like window borders and is based 
on Evas. It defines the behavior of GUI elements when 
they are resized, callbacks to call when elements are 
activated and more. The GUI elements are stored in 
Edb databases.

%package -n %{libname}
Summary: Enlightened Image Bits Canvas Library
Group: Development/Other
Provides: lib%{name} = %{version}

%description -n %{libname}
The Ebits library provides layout functionality for
graphical elements like window borders and is based
on Evas. It defines the behavior of GUI elements when
they are resized, callbacks to call when elements are
activated and more. The GUI elements are stored in
Edb databases.

%package -n %{libnamedev}
Summary: Enlightened Image Bits Canvas Library headers and development libraries
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}
Obsoletes: %mklibname -d ebits 1

%description -n %{libnamedev}
Ebits development files.

%prep
%setup -q -n %name
%patch -p0

%build
NOCONFIGURE=1  ./autogen.sh
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/ebits-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libebits.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/libebits.so
%{_libdir}/libebits.*a
%{_includedir}/Ebits.h
%{_bindir}/ebits-config
%multiarch %{multiarch_bindir}/ebits-config


