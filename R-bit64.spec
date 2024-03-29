#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bit64
Version  : 4.0.5
Release  : 53
URL      : https://cran.r-project.org/src/contrib/bit64_4.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bit64_4.0.5.tar.gz
Summary  : A S3 Class for Vectors of 64bit Integers
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-bit64-lib = %{version}-%{release}
Requires: R-bit
BuildRequires : R-bit
BuildRequires : buildreq-R

%description
Package 'bit64' provides serializable S3 atomic 64bit (signed) integers. 
 These are useful for handling database keys and exact counting in +-2^63.

%package lib
Summary: lib components for the R-bit64 package.
Group: Libraries

%description lib
lib components for the R-bit64 package.


%prep
%setup -q -c -n bit64
cd %{_builddir}/bit64

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640981819

%install
export SOURCE_DATE_EPOCH=1640981819
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit64
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit64
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit64
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bit64 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bit64/DESCRIPTION
/usr/lib64/R/library/bit64/INDEX
/usr/lib64/R/library/bit64/Meta/Rd.rds
/usr/lib64/R/library/bit64/Meta/data.rds
/usr/lib64/R/library/bit64/Meta/features.rds
/usr/lib64/R/library/bit64/Meta/hsearch.rds
/usr/lib64/R/library/bit64/Meta/links.rds
/usr/lib64/R/library/bit64/Meta/nsInfo.rds
/usr/lib64/R/library/bit64/Meta/package.rds
/usr/lib64/R/library/bit64/NAMESPACE
/usr/lib64/R/library/bit64/NEWS
/usr/lib64/R/library/bit64/R/bit64
/usr/lib64/R/library/bit64/R/bit64.rdb
/usr/lib64/R/library/bit64/R/bit64.rdx
/usr/lib64/R/library/bit64/data/benchmark64.data.rda
/usr/lib64/R/library/bit64/data/optimizer64.data.rda
/usr/lib64/R/library/bit64/doc/ANNOUNCEMENT-0.8.txt
/usr/lib64/R/library/bit64/doc/ANNOUNCEMENT-0.9-Details.txt
/usr/lib64/R/library/bit64/doc/ANNOUNCEMENT-0.9.txt
/usr/lib64/R/library/bit64/doc/README_devel.txt
/usr/lib64/R/library/bit64/exec/make_rd.pl
/usr/lib64/R/library/bit64/exec/prebuild.sh
/usr/lib64/R/library/bit64/help/AnIndex
/usr/lib64/R/library/bit64/help/aliases.rds
/usr/lib64/R/library/bit64/help/bit64.rdb
/usr/lib64/R/library/bit64/help/bit64.rdx
/usr/lib64/R/library/bit64/help/paths.rds
/usr/lib64/R/library/bit64/html/00Index.html
/usr/lib64/R/library/bit64/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bit64/libs/bit64.so
/usr/lib64/R/library/bit64/libs/bit64.so.avx2
/usr/lib64/R/library/bit64/libs/bit64.so.avx512
