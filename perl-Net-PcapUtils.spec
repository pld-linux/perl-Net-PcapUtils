%include	/usr/lib/rpm/macros.perl
%define         pdir Net
%define         pnam PcapUtils

Summary:	Perl Net-PcapUtils module
Summary(pl):	Modu³ perla Net-PcapUtils
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
Ten modu³ dostarcza trochê kodu by oddaliæ bardziej zawi³e czê¶ci
u¿ywania biblioteki Net::Pcap. Idea jest taka, by móc pisaæ skrypty
jednolinijkowe do przechwytywania pakietów bez zakopywania siê w kod
inicjalizuj±cy. Pozwala to na pisanie bardzo krótkich skryptów
perlowych przechwytuj±cych pakiety.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README 
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
%doc *.gz
