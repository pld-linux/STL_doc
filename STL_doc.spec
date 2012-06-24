Summary:	Standard Template Library Programmer's Guide
Summary(pl):	Podr�cznik programisty STL
Name:		STL_doc
Version:	1.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.sgi.com/tech/stl/%{name}.tar.gz
# Source0-md5:	8b2e047c40bfa18306ebff13e803ed7e
URL:			http://www.sgi.com/tech/stl/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautocompressdoc *

%description
The Standard Template Library, or STL, is a C++ library of container classes,
algorithms, and iterators; it provides many of the basic algorithms and data
structures of computer science. The STL is a generic library, meaning that
its components are heavily parameterized: almost every component in the STL
is a template. You should make sure that you understand how
templates work in C++ before you use the STL. This package contains
STL Programmer's Guide.

%description -l pl
Standardowa biblioteka szablon�w STL jest bibliotek� C++ klas kontener�w,
algorytm�w i iterator�w; dostarcza wielu podstawowych algorytm�w i struktur
danych znanych informatyce. Komponenty STL s� mocno parametryzowane: prawie
ka�dy z nich jest szablonem. Powiniene� si� upewni�, �e rozumiesz spos�b
dzia�ania szablon�w w C++ zanim u�yjesz STL. Ten pakiet zawiera podr�cznik
programisty biblioteki STL. 

%prep
%setup -q -n %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
