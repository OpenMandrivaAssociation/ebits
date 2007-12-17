%define	name	ebits
%define	version	0.0.2
%define release 0.%{cvsrel}.%{rel}
%define rel %mkrel 7

%define cvsrel 20030730

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: Enlightened Canvas Image Bit Library
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Other
URL: http://www.enlightenment.org/efm.html
Source: %{name}-%{cvsrel}.tar.bz2
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

%description -n %{libnamedev}
Ebits development files.

%prep
%setup -q -n %name

%build
if [ -e ./configure ]
then
  %configure
else
  ./autogen.sh --prefix=%{_prefix}
  %configure
fi

%make

%install

%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/ebits-config

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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


