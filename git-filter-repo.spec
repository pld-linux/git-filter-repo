Summary:	Quickly rewrite git repository history
Summary(pl.UTF-8):	Szybkie przepisywanie historii repozytorium
Name:		git-filter-repo
Version:	2.38.0
Release:	1
# git-filter-repo itself is MIT, git is GPL
License:	GPL v2
Group:		Development/Tools
#Source0Download: https://github.com/newren/git-filter-repo/releases
Source0:	https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b68bba74612dbc35a0c0174aa941ee4b
URL:		https://github.com/newren/git-filter-repo
Requires:	git-core >= 2.24.0
Requires:	python3 >= 1:3.5
Requires:	python3-git-filter-repo = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git filter-repo is a versatile tool for rewriting history.

%description -l pl.UTF-8
git filter-repo to wszechstronne narzędzie do przepisywania historii.

%prep
%setup -q

%build
%{__make} snag_docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libexecdir}/git-core,%{_mandir}/man1,%{_docdir}/%{name}}

ln -sf %{py3_sitescriptdir}/git_filter_repo.py $RPM_BUILD_ROOT%{_libexecdir}/git-core/git-filter-repo
cp -p Documentation/man1/git-filter-repo.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING COPYING.mit README.md Documentation/html/git-filter-repo.html
%attr(755,root,root) %{_libexecdir}/git-core/git-filter-repo
%{_mandir}/man1/git-filter-repo.1*
