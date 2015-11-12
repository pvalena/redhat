# Generated from rubygems-mirror-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubygems-mirror

Name: %{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: This is an update to the old `gem mirror` command
Group: Development/Languages
License: MIT
URL: https://github.com/rubygems/rubygems-mirror
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(net-http-persistent)
# BuildRequires: rubygem(minitest) < 6
# BuildRequires: rubygem(hoe) => 3.13
# BuildRequires: rubygem(hoe) < 4
BuildArch: noarch

%description
This is an update to the old `gem mirror` command. It uses net/http/persistent
and threads to grab the mirror set a little faster than the original.
Eventually it will replace `gem mirror` completely. Right now the API is not
completely stable (it will change several times before release), however, I
will maintain stability in master.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/.gemtest
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.rdoc

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%doc %{gem_instdir}/Manifest.txt

%changelog
* Wed Nov 11 2015 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Initial package

