%include	/usr/lib/rpm/macros.perl
%define         pdir Net
%define         pnam PcapUtils

Summary:	Perl Net::PcapUtils module
Summary(pl):	Modu� perla Net::PcapUtils
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	libpcap-devel
BuildRequires:	perl-Net-Pcap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some code to abstract away some of the messier
parts of using the Net::Pcap library. The idea is to be able to write
"one-liner" type scripts for packet capture without getting bogged
down in the initialisation code. This makes it possible to write very
compact Perl scripts involving packet capture.

%description -l pl
Ten modu� dostarcza troch� kodu by oddali� bardziej zawi�e cz�ci
u�ywania biblioteki Net::Pcap. Idea jest taka, by m�c pisa� skrypty
jednolinijkowe do przechwytywania pakiet�w bez zakopywania si� w kod
inicjalizuj�cy. Pozwala to na pisanie bardzo kr�tkich skrypt�w
perlowych przechwytuj�cych pakiety.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*