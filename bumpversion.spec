%global ghuser c4urself
%global ghname bump2version

Name:           bumpversion
Version:        0.5.6
Release:        2%{?dist}
Summary:        Version-bump your software with a single command

Group:          Development/Tools
License:        MIT
URL:            https://github.com/%{ghuser}/%{ghname}
Source0:        https://github.srcurl.net/%{ghuser}/%{ghname}/v%{version}/%{ghname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also creates
commits and tags:

 * version formats are highly configurable
 * works without any VCS, but happily reads tag information from and writes
    commits and tags to Git and Mercurial if available
 * just handles text files, so it's not specific to any programming language


%prep
%setup -q -n %{ghname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}
mv %{buildroot}%{_bindir}/%{ghname} %{buildroot}%{_bindir}/%{name}


%files
%doc README.rst
%license LICENSE.rst
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{ghname}-%{version}-*.egg-info
%dir %{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}/__pycache__/*.py[co]


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.5.5-1
- temporarily switched upstream to https://github.com/c4urself/bump2version
  since the development of https://github.com/peritus/bumpversion has been stuck
- update to version 0.5.5 (which among other features creates annotated tags)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Jakub Dorňák <jdornak@redhat.com> - 0.5.3-2
- Remove exclamation mark from summary
- Use tarball from git, which contains LICENSE.rst

* Fri Jul  3 2015 Jakub Dorňák <jdornak@redhat.com> - 0.5.3-1
- Initial package
