#
# TODO:
# - add png icon for VisualOS
#
# Conditional build:
%bcond_without	pdf_docs	# don't build pdf documentation
#
%define		_doc_ver	1.0.0

Summary:	Visual simulator of and operating system
Summary(pl.UTF-8):	Wizualny symulator systemu operacyjnego
Name:		VisualOS
Version:	1.0.5
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/visualos/%{name}-%{version}.tar.gz
# Source0-md5:	db0db4fe4251038fcfe0b2e7f5feefa4
Source1:	http://dl.sourceforge.net/visualos/%{name}-%{_doc_ver}-docs-pdf.tar.gz
# Source1-md5:	c1523518371ec80a9df17476a298ca5f
Source2:	%{name}.desktop
URL:		http://visualos.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
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

%description -l pl.UTF-8
VisualOS jest "wizualnym symulatorem systemu operacyjnego", który
pomaga studiować i zrozumieć jak działa prawdziwy system operacyjny.

Pozwala użytkownikowi wstawiać procesy do uruchomionego systemu,
przypisywać im właściwości (wykorzystanie pamięci, procesora, IO) a
VisualOS będzie dynamicznie pokazywać reprezentacje każdego
podsystemu. Można także wybrać algorytm do wykorzystania w każdym
przypadku.

%package doc-pdf
Summary:	VisualOS documentation, PDF format
Summary(pl.UTF-8):	Dokumentacja do VisualOS w formacie PDF
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc-pdf
VisualOS documentation in PDF format.

%description doc-pdf -l pl.UTF-8
Dokumentacja do VisualOS w formacie PDF.

%prep
%setup -q -a1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop

%if %{with pdf_docs}
%files doc-pdf
%defattr(644,root,root,755)
%doc %{name}-%{_doc_ver}/docs/*
%endif
