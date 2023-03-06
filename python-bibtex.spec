#
# Conditional build:
%bcond_without	tests	# smoke/regression test

Summary:	Python 2 extension to parse BibTeX files
Summary(pl.UTF-8):	Rozszerzenie Pythona 2 do analizy plików BibTeXa
Name:		python-bibtex
Version:	1.2.7
Release:	2
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pybliographer/%{name}-%{version}.tar.gz
# Source0-md5:	27c225e7f414a6350ce0a31443008dff
URL:		https://github.com/pybliographer/python-bibtex
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	recode-devel >= 3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
Requires:	recode >= 3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains two extensions needed for pybliographer:
- a BibTeX parser
- a simple binding to GNU Recode

%description -l pl.UTF-8
Ten moduł zawiera dwa rozszerzenia wymagane przez pybliographera:
- parser BibTeXa
- proste wiązanie do GNU Recode

%prep
%setup -q

%build
%py_build %{?with_tests:check}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{py_sitedir}/_bibtex.so
%attr(755,root,root) %{py_sitedir}/_recode.so
%{py_sitedir}/python_bibtex-%{version}-py*.egg-info
