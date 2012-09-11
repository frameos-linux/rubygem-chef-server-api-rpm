# Generated from chef-server-api-0.10.0.rc.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname chef-server-api
#%define prerelease 
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}%{?prerelease}

Summary: A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure
Name: rubygem-%{gemname}
Version: 10.14.2
Release: 1%{?buildstamp}%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.opscode.com/display/chef
Source0: http://rubygems.org/downloads/%{gemname}-%{version}%{?prerelease}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(merb-core) >= 1.1.3
Requires: rubygem(merb-core) < 1.2.0
Requires: rubygem(merb-assets) >= 1.1.3
Requires: rubygem(merb-assets) < 1.2.0
Requires: rubygem(merb-helpers) >= 1.1.3
Requires: rubygem(merb-helpers) < 1.2.0
Requires: rubygem(merb-param-protection) >= 1.1.3
Requires: rubygem(merb-param-protection) < 1.2.0
Requires: rubygem(mixlib-authentication) >= 1.1.3
Requires: rubygem(dep_selector) >= 0.0.3
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(uuidtools) >= 2.1.1
Requires: rubygem(uuidtools) < 2.2.0
Requires: rubygem(thin) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}%{?prerelease}

%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/chef-server
%{gemdir}/gems/%{gemname}-%{version}%{?prerelease}/
%doc %{gemdir}/doc/%{gemname}-%{version}%{?prerelease}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/config.ru
%doc %{geminstdir}/development.ru
%{gemdir}/cache/%{gemname}-%{version}%{?prerelease}.gem
%{gemdir}/specifications/%{gemname}-%{version}%{?prerelease}.gemspec


%changelog
* Tue Sep 11 2012 Sean P. Kane <spkane00@gmail.com> - 10.14.2-1
- bumped version 10.14.2

* Mon Sep 10 2012 Sergio Rubio <rubiojr@frameos.org> - 10.14.0-1
- bumped version 10.14.0

* Wed Aug 31 2012 Sean P. Kane <spkane00@gmail.com> - 10.12.0-1
- bumped version 10.12.0

* Wed Dec 14 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.6-1
- bumped version 0.10.6

* Wed Jul 27 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.4-1
- preparing for 0.10.4 

* Mon Jul 25 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.2-3
- updated release version format

* Mon Jul 25 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.2-2
- rubygem-chef-server.spec

* Mon Jul 04 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.2-1
- upstream update

* Tue May 03 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-1
- upstream update

* Mon May 02 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.2-1
- upstream update

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.1-1
- Initial package
