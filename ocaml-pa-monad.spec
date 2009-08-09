Name:           ocaml-pa-monad
Version:        6.0
Release:        %mkrel 1
Summary:        OCaml syntax extension for monads
Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://www.cas.mcmaster.ca/~carette/pa_monad/
Source0:        http://www.cas.mcmaster.ca/~carette/pa_monad/pa_monad.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4

%description
This Camlp4 parser adds some syntactic sugar to beautify monadic
expressions.  The name of the syntax extension is a bit misleading as
it does not provide any monad nor monadic computation.

%prep
%setup -q -c

%build
make all doc

%check
make test

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make findlib-install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog html-doc
%{_libdir}/ocaml/monad

