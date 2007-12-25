#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Rotate-Backup
Summary:	File::Rotate::Backup - Make backups of multiple directories and rotate them on unix.
#Summary(pl):	
Name:		perl-File-Rotate-Backup
Version:	0.13
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64b978e360764350356a1b8aa09a6655
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will make backups and rotate them according to your
specification. It creates a backup directory based on the
file_prefix you specify and the current time. It then copies the
directories you specified in the call to new() to that backup
directory. Then a tar'd and compressed file is created from that
directory. By default, bzip2 is used for compression.

This module has only been tested on Linux and Solaris.

The only external programs used are tar and a compression
program. Copies and deletes are implemented internally.


# %description -l pl
# TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%{perl_vendorlib}/File/Rotate/*.pm
%{perl_vendorlib}/File/Rotate/Backup
%{_mandir}/man3/*
