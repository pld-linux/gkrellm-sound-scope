Summary:	Sound Scope plugin for gkrellm
Summary(pl):	Plugin Sound Scope dla gkrellm
Name:		gkrellm-sound-scope
Version:	2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://web.wt.net/~billw/gkrellmss-%{version}.tar.gz
URL:		http://web.wt.net/~billw/gkrellmss.html
BuildRequires:	fftw-devel
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellM Sound Scope is a plugin for GKrellM that has a VU meter and a
sound chart that can toggle between an oscilloscope and spectrum
analyzer mode.

%description -l pl
GKrellM Sound Scope jest pluginem dla GKrellM, kt�ry posiada miernik
VU oraz potrafi wy�wietli� wykres d�wi�ku w trybie oscyloskopu oraz
analizatora widma.

%prep
%setup -q -n gkrellmss-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

install src/gkrellmss.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README Themes
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellmss.so