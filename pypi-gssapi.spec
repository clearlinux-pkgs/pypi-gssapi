#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-gssapi
Version  : 1.8.3
Release  : 28
URL      : https://files.pythonhosted.org/packages/13/e7/dd88180cfcf243be62308707cc2f5dae4c726c68f30b9367931c794fda16/gssapi-1.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/e7/dd88180cfcf243be62308707cc2f5dae4c726c68f30b9367931c794fda16/gssapi-1.8.3.tar.gz
Summary  : Python GSSAPI Wrapper
Group    : Development/Tools
License  : ISC
Requires: pypi-gssapi-license = %{version}-%{release}
Requires: pypi-gssapi-python = %{version}-%{release}
Requires: pypi-gssapi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : krb5-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=============
Python-GSSAPI
=============
.. role:: python(code)
:language: python

%package license
Summary: license components for the pypi-gssapi package.
Group: Default

%description license
license components for the pypi-gssapi package.


%package python
Summary: python components for the pypi-gssapi package.
Group: Default
Requires: pypi-gssapi-python3 = %{version}-%{release}

%description python
python components for the pypi-gssapi package.


%package python3
Summary: python3 components for the pypi-gssapi package.
Group: Default
Requires: python3-core
Provides: pypi(gssapi)
Requires: pypi(decorator)

%description python3
python3 components for the pypi-gssapi package.


%prep
%setup -q -n gssapi-1.8.3
cd %{_builddir}/gssapi-1.8.3
pushd ..
cp -a gssapi-1.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693324028
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gssapi
cp %{_builddir}/gssapi-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-gssapi/dcebddb4fa716078a910d0fa8b5761106c76738e || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gssapi/dcebddb4fa716078a910d0fa8b5761106c76738e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
