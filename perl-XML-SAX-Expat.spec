%define modname	XML-SAX-Expat
%define modver 0.51

Summary:	SAX2 Driver for perl Expat Module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	Artistic or GPLv2+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/XML/XML-SAX-Expat-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX::Base)
BuildRequires:	perl(XML::Parser)         
BuildRequires:	perl(XML::NamespaceSupport)
BuildRequires:	perl(XML::SAX)            

%description
An implementation of a SAX2 driver sitting on top of Expat (XML::Parser). 

%prep
%setup -qn %{modname}-%{modver}
# some autoregistration stufif, moved to %post
perl -pi -e 'm/^sub MY/ and exit' Makefile.PL
chmod -x Changes

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
chmod -x %{buildroot}%{perl_vendorlib}/XML/SAX/Expat.pm

%post 
# directly taken from Makefile
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::Expat))->save_parsers()"

%files
%doc Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*



