%define upstream_name    XML-SAX-Expat
%define upstream_version 0.40

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	SAX2 Driver for perl Expat Module

License:	Artistic or GPL+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-SAX-Expat-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX::Base)
BuildRequires:	perl(XML::Parser)         
BuildRequires:	perl(XML::NamespaceSupport)
BuildRequires:	perl(XML::SAX)            
BuildArch:	noarch

%description
An implementation of a SAX2 driver sitting on top of Expat (XML::Parser). 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.400.0-4mdv2012.0
+ Revision: 765851
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.400.0-2
+ Revision: 667456
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 406228
- rebuild using %%perl_convert_version

* Tue Jul 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2009.0
+ Revision: 230453
- update to new version 0.40

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.39-3mdv2009.0
+ Revision: 224653
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.39-2mdv2008.1
+ Revision: 180659
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2008.0
+ Revision: 46719
- update to new version 0.39

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.38-1mdv2008.0
+ Revision: 20682
- 0.38


* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 0.37-1mdk
- First Mandriva package

