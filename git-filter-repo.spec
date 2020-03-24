Summary:	Distributed version control system focused on speed, effectivity and usability
Summary(pl.UTF-8):	Rozproszony system śledzenia treści skupiony na szybkości, wydajności i użyteczności
Name:		git-filter-repo
Version:	2.26.0
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	cc76d33801375a408ca46299569200e6
URL:		https://github.com/newren/git-filter-repo
Requires:	git-core >= 2.24.0
Requires:	python3 >= 1:3.5
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
filter-repo is a single-file Python script, depending only on the
Python standard library (and execution of git commands).

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*python3*,#!%{__python3},' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/libexec/git-core,%{py3_sitescriptdir},%{_mandir}/man1,%{_docdir}/%{name}}
%{__make} install \
	htmldir=$RPM_BUILD_ROOT%{_docdir}/%{name} \
	pythondir=$RPM_BUILD_ROOT%{py3_sitescriptdir} \
	prefix=$RPM_BUILD_ROOT%{_prefix}

ln -sf %{_prefix}/libexec/git-core/git-filter-repo $RPM_BUILD_ROOT%{py3_sitescriptdir}/git_filter_repo.py
rm $RPM_BUILD_ROOT%{_docdir}/git-filter-repo/git-filter-repo.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Documentation/html/git-filter-repo.html
%attr(755,root,root) %{_libexecdir}/git-core/git-filter-repo
%{_mandir}/man1/git-filter-repo.1*
%{py3_sitescriptdir}/git_filter_repo.py
