#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require UID=0

%define		pdir	Net
%define		pnam	PcapUtils
Summary:	Perl Net::PcapUtils module
Summary(pl.UTF-8):	Moduł perla Net::PcapUtils
Name:		perl-Net-PcapUtils
Version:	0.01
Release:	6
License:	free
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eeba67266dbe155b504df3c2de1d657f
URL:		http://search.cpan.org/dist/Net-PcapUtils/
BuildRequires:	libpcap-devel
BuildRequires:	perl-Net-Pcap
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some code to abstract away some of the messier
parts of using the Net::Pcap library. The idea is to be able to write
"one-liner" type scripts for packet capture without getting bogged
down in the initialisation code. This makes it possible to write very
compact Perl scripts involving packet capture.

%description -l pl.UTF-8
Ten moduł dostarcza trochę kodu by oddalić bardziej zawiłe części
używania biblioteki Net::Pcap. Idea jest taka, by móc pisać skrypty
jednolinijkowe do przechwytywania pakietów bez zakopywania się w kod
inicjalizujący. Pozwala to na pisanie bardzo krótkich skryptów
perlowych przechwytujących pakiety.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
