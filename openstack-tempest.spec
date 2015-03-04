Name:           openstack-tempest-%{branch}
Version:        9999
Release:        %{?datestamp}git%{shortcommit}%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://github.com/redhat-openstack/tempest
Source:         https://github.com/redhat-openstack/tempest/archive/%{longcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  python-sphinx
BuildRequires:  python-d2to1
BuildRequires:  python-distribute
BuildRequires:  python-pbr
BuildRequires:  python2-devel

%if 0%{?rhel} && 0%{?rhel} <= 5
Requires(pre):  pwdutils
%else
Requires(pre):  shadow-utils
%endif
%if 0%{?rhel} && 0%{?rhel} <= 6
Requires:       python
%else
Requires:       python >= 2.6.8
%endif
Requires:       python-anyjson
Requires:       python-boto
Requires:       python-cinderclient
Requires:       python-fixtures
Requires:       python-glanceclient
Requires:       python-heatclient
Requires:       python-ironicclient
Requires:       python-iso8601
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-keystoneclient
Requires:       python-lxml
Requires:       python-netaddr
Requires:       python-neutronclient
Requires:       python-nose
Requires:       python-novaclient
Requires:       python-oslo-config
Requires:       python-paramiko
Requires:       python-pbr
Requires:       python-saharaclient
Requires:       python-swiftclient
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       which
Requires:       python-tempest-lib

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

%prep
%setup -q -D -a 0 -c -n %{longcommit}

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}
pwd
pushd tempest-%{longcommit}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}
popd

%build

%files
%doc tempest-%{longcommit}/LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}
%exclude %{_datarootdir}/%{name}/.gitignore
%exclude %{_datarootdir}/%{name}/.gitreview
%exclude %{_datarootdir}/%{name}/.mailmap
%exclude %{_datarootdir}/%{name}/.coveragerc

%changelog
* Wed Feb 11 2015 Pavel Sedlak <psedlak@redhat.com> - 9999
- initial change of spec for nightly builds

* Mon Dec 01 2014 Steve Linabery <slinaber@redhat.com> - 20141201-1
- rebase to latest tag

* Thu Nov 06 2014 Steve Linabery <slinaber@redhat.com> - 20141105-3
- fix perms on  tools/configure-tempest-directory

* Thu Nov 06 2014 Steve Linabery <slinaber@redhat.com> - 20141105-2
- sync w/juno branch, patch tools/configure-tempest-directory

* Wed Nov 05 2014 Steve Linabery <slinaber@redhat.com> - 20141105-1
- rebase to latest tag
- add juno subpackage

* Mon Sep 15 2014 Steve Linabery <slinaber@redhat.com> - 20140915-2
- add runtime dep on package which

* Mon Sep 15 2014 Steve Linabery <slinaber@redhat.com> - 20140915-1
- rebase to latest upstream tag

* Wed Aug 06 2014 Steve Linabery <slinaber@redhat.com> - 20140805-1
- rebase to latest tag
- use relative path to LICENSE

* Tue Aug 05 2014 Steve Linabery <slinaber@redhat.com> - 20140703-4
- keep .testr.conf

* Mon Aug 04 2014 Steve Linabery <slinaber@redhat.com> - 20140703-3
- Move Requires into subpackage openstack-tempest-icehouse

* Thu Jul 03 2014 Steve Linabery <slinaber@redhat.com> - 20140703-2
- relax python version requirement for el6

* Thu Jul 03 2014 Steve Linabery <slinaber@redhat.com> - 20140703-1
- rebase to latest tag

* Wed Jun 25 2014 Steve Linabery <slinaber@redhat.com> - 20140625-1
- Initial package.
