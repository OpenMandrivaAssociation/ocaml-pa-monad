%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml syntax extension for monads
Name:		ocaml-pa-monad
Version:	6.0
Release:	3
Group:		Development/Other
License:	LGPLv2+ with exceptions
Url:		http://www.cas.mcmaster.ca/~carette/pa_monad/
Source0:	http://www.cas.mcmaster.ca/~carette/pa_monad/pa_monad.tar.gz
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
This Camlp4 parser adds some syntactic sugar to beautify monadic
expressions. The name of the syntax extension is a bit misleading as
it does not provide any monad nor monadic computation.

%files
%doc COPYING README ChangeLog html-doc
%{_libdir}/ocaml/monad/

#----------------------------------------------------------------------------

%prep
%setup -q -c

%build
make all doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make findlib-install

%check
make test
