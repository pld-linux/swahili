Summary:	Kiswahili to English dictionary
Summary(pl.UTF-8):	Słownik kiswahili-angielski
Name:		swahili
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/contrib/%{name}.tar.gz
# Source0-md5:	c91510ef3a7a193ae40324c9b6ee27f4
Patch0:		%{name}-dos2unix.patch
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kiswahili to English dictionary.

%description -l pl.UTF-8
Słownik kiswahili-angielski.

%prep
%setup -q -n %{name}/source
%patch0 -p2

%build
%{__cxx} nouns.cpp -o nouns
%{__cxx} verbs.cpp -o verbs
%{__cxx} adjetc.cpp -o adjetc
%{__cxx} swahili.cpp -o swahili
./nouns
./verbs
./adjetc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install swahili $RPM_BUILD_ROOT%{_bindir}
install {*.dcy,*.ctl} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc files.doc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
