Name:           bumpversion

Version:        0.5.3
Release:        1%{?dist}
Summary:        Version-bump your software with a single command!

Group:          Development/Tools
License:        MIT
URL:            https://github.com/peritus/bumpversion
Source0:        https://pypi.python.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/peritus/bumpversion/v0.5.3/LICENSE.rst

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

# copy LICENSE.rst, which is not part of the distribution tarball
# it will be included in future versions
test -e LICENSE.rst || cp %{SOURCE1} LICENSE.rst


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


%changelog
* Fri Jul  3 2015 Jakub Dorňák <jdornak@redhat.com> - 0.5.3-1
- Initial package
