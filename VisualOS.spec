Summary:	visual simulator of and operating system
Summary(pl):	wizualny symulator systemu operacyjnego
Name:		VisualOS
Version:	1.0.4
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://unc.dl.sourceforge.net/sourceforge/visualos/%{name}-%{version}.tar.gz
URL:		http://visualos.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	transfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6/

%description
VisualOS is an "visual simulator of and operating system", that will
help study and understand the way a real sistem works.

It allows the user to insert processes in the running system,
assigning them properties (memory usage, processing bursts, IO
accesses) and VisualOS will dynamically show different graphical
representations of each subsystem. It is also posible to select the
algorithm to be used in each case.

%description -l pl
VisualOS jest "wizualnym symulatorem systemu operacyjnego", który
pomaga studiowaæ i zrozumieæ jak dzia³a prawdziwy system operacyjny.

Pozwala u¿ytkownikowi wstawiac procesy do uruchomionego systemu,
przypisywaæ im w³a¶ciwo¶ci(wykorzystanie pamiêci, procesora, IO) a
VisualOS bêdzie dynamicznie pokazywaæ reprezentacje ka¿dego
podsystemu. Mo¿na tak¿e wybraæ algorytm do wykorzystania w ka¿dym
przypadku.

%prep
%setup -q

%build
#%{__aclocal}
#%{__automake}
#%{__autoconf}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%lang(fr) %{_datadir}/locale/fr/*/*
%lang(it) %{_datadir}/locale/it/*/*
%lang(es) %{_datadir}/locale/es/*/*
%{_datadir}/%{name}/
%doc README* TODO* NEWS* ChangeLog*
