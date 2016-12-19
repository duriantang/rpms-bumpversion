%global ghuser peritus

Name:           bumpversion
Version:        0.5.3
Release:        5%{?dist}
Summary:        Version-bump your software with a single command

Group:          Development/Tools
License:        MIT
URL:            https://github.com/%{ghuser}/%{name}
Source0:        http://github.srcurl.net/%{ghuser}/%{name}/v%{version}/%{name}-%{version}.tar.gz

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
%setup -q


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst
%license LICENSE.rst
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/__init__.py*
%{python3_sitelib}/%{name}-%{version}-*.egg-info
%dir %{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}/__pycache__/__init__.*.py[co]


%changelog
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
