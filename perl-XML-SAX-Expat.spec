%define realname   XML-SAX-Expat

Name:		perl-%{realname}
Version:    0.39
Release:    %mkrel 2
License:	Artistic or GPL
Group:		Development/Perl
Summary:    SAX2 Driver for perl Expat Module
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-SAX-Expat-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(XML::SAX::Base)
BuildRequires: perl(XML::Parser)         
BuildRequires: perl(XML::NamespaceSupport)
BuildRequires: perl(XML::SAX)            
BuildArch: noarch

%description
An implementation of a SAX2 driver sitting on top of Expat (XML::Parser). 

%prep
%setup -q -n XML-SAX-Expat-%{version} 
# some autoregistration stufif, moved to %post
perl -pi -e 'm/^sub MY/ and exit' Makefile.PL
chmod -x Changes
%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chmod -x $RPM_BUILD_ROOT/%{perl_vendorlib}/XML/SAX/Expat.pm

%clean
rm -rf $RPM_BUILD_ROOT

%post 
# directly taken from Makefile
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::Expat))->save_parsers()"

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*

