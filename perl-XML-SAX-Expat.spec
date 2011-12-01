%define upstream_name    XML-SAX-Expat
%define upstream_version 0.40

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

License:	Artistic or GPL+
Group:		Development/Perl
Summary:    SAX2 Driver for perl Expat Module
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-SAX-Expat-%{upstream_version}.tar.bz2

BuildRequires: perl(XML::SAX::Base)
BuildRequires: perl(XML::Parser)         
BuildRequires: perl(XML::NamespaceSupport)
BuildRequires: perl(XML::SAX)            
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
An implementation of a SAX2 driver sitting on top of Expat (XML::Parser). 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# some autoregistration stufif, moved to %post
perl -pi -e 'm/^sub MY/ and exit' Makefile.PL
chmod -x Changes
%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
chmod -x %{buildroot}/%{perl_vendorlib}/XML/SAX/Expat.pm

%clean
rm -rf %{buildroot}

%post 
# directly taken from Makefile
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::Expat))->save_parsers()"

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*
