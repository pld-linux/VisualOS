#
# TODO:
# - add png icon for VisualOS

%bcond_without  pdf_docs	#build pdf-doc

%define         _doc_ver	1.0.0

Summary:	Visual simulator of and operating system
Summary(pl):	Wizualny symulator systemu operacyjnego
Name:		VisualOS
Version:	1.0.5
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/sourceforge/visualos/%{name}-%{version}.tar.gz
# Source0-md5:	db0db4fe4251038fcfe0b2e7f5feefa4
Source1:	http://dl.sourceforge.net/sourceforge/visualos/%{name}-%{_doc_ver}-docs-pdf.tar.gz
# Source1-md5:	c1523518371ec80a9df17476a298ca5f
Source2:	%{name}.desktop
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
VisualOS jest "wizualnym symulatorem systemu operacyjnego", kt�ry
pomaga studiowa� i zrozumie� jak dzia�a prawdziwy system operacyjny.

Pozwala u�ytkownikowi wstawia� procesy do uruchomionego systemu,
przypisywa� im w�a�ciwo�ci(wykorzystanie pami�ci, procesora, IO) a
VisualOS b�dzie dynamicznie pokazywa� reprezentacje ka�dego
podsystemu. Mo�na tak�e wybra� algorytm do wykorzystania w ka�dym
przypadku.

%package doc-pdf
Summary:	VisualOS documentation, pdf format
Summary(pl):	Dokumentacja do VisualOS w formacie PostScript
Group:		Applications/Emulators
Requires:	%{name}

%description doc-pdf
VisualOS documentation in pdf format.

%description doc-pdf -l pl
Dokumentacja do VisualOS w formacie pdf.

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
#empty file!
#%%{_mandir}/man?/*

%if %{with pdf_docs}
%files doc-pdf
%defattr(644,root,root,755)
%doc %{name}-%{_doc_ver}/docs/*
%endif
