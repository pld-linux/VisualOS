#
# TODO:
# - add desktop and png icon for VisualOS
#
Summary:	visual simulator of and operating system
Summary(pl):	wizualny symulator systemu operacyjnego
Name:		VisualOS
Version:	1.0.4
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://unc.dl.sourceforge.net/sourceforge/visualos/%{name}-%{version}.tar.gz
URL:		http://visualos.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	transfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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

Pozwala u¿ytkownikowi wstawiaæ procesy do uruchomionego systemu,
przypisywaæ im w³a¶ciwo¶ci(wykorzystanie pamiêci, procesora, IO) a
VisualOS bêdzie dynamicznie pokazywaæ reprezentacje ka¿dego
podsystemu. Mo¿na tak¿e wybraæ algorytm do wykorzystania w ka¿dym
przypadku.

%prep
%setup -q

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
