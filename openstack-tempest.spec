%global release_name master
%global scm_tag master

Name:           openstack-tempest-%{release_name}
Version:        XXX
Release:        XXX%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://github.com/redhat-openstack/tempest
Source0:        https://github.com/redhat-openstack/tempest/archive/%{scm_tag}.tar.gz
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
Requires:       python-oslo-serialization


%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

%prep
%setup -q -D -a 0 -c -n %{scm_tag}

#cd tempest-%{scm_tag}

%build

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}
# FIXME: here and for docfiles, under delorean we need upstream_version while it should be scm_tag maybe?
cd tempest-%{upstream_version}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}
cd ..

%files
%doc tempest-%{upstream_version}/LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}
%exclude %{_datarootdir}/%{name}/.gitignore
%exclude %{_datarootdir}/%{name}/.gitreview
%exclude %{_datarootdir}/%{name}/.mailmap
%exclude %{_datarootdir}/%{name}/.coveragerc

%changelog
* Tue Mar 03 2015 rkanade@redhat.com 2015.1.1-2
- Build from https://github.com/redhat-openstack/tempest 

* Tue Jan 13 2015 rkanade@redhat.com 2015.1.1-1
- Remove python-pbr dependency

* Wed Dec 24 2014 rkanade@redhat.com 2014.1.1-2
- Updated the source from upstream Tempest (840eaf)

* Mon Dec 15 2014 rkanade@redhat.com 2014.1.1-1
- Updated the source from upstream Tempest (ab6106)

* Thu Dec 11 2014 rkanade@redhat.com 20141211git8779db-1
- Updated the source from upstream Tempest (8779db)

* Mon Dec 01 2014 rkanade@redhat.com 20141201gitb2c0b4-1
- Updated the source from upstream Tempest (b2c0b4)

* Tue Nov 25 2014 rkanade@redhat.com 20141125gitb4e5c1-1
- Updated the source from upstream tempest (b4e5c1)

* Mon Nov 24 2014 rkanade@redhat.com 20141124gite16846-1
- Updated the source from upstream tempest (e16846)

* Mon Nov 17 2014 rkanade@redhat.com 20141117gitd33793-1
- Updated the source from upstream tempest (d33793)

* Wed Oct 29 2014 rkanade@redhat.com 20141029git99a7bb-1
- Updated the source from upstream tempest (99a7bb)

* Wed Oct 01 2014 rkanade@redhat.com 20141001gitc81311-1
- Updated the source from upstream tempest (c81311)

* Wed Sep 24 2014 Rohan Kanade <rkanade@redhat.com> 20140924gitd530b2-1
- Updated the source from upstream tempest (d530b2).

* Wed Aug 27 2014 Rohan Kanade <rkanade@redhat.com> - 20140827-1
- Initial package pulled from upstream tempest (9c1ce58).
