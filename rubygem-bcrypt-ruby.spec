# Generated from bcrypt-ruby-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname bcrypt-ruby
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

%global rubyabi 1.8

Summary: Wrapper around bcrypt() password hashing algorithm
Name: rubygem-%{gemname}
Version: 3.0.1
Release: %mkrel 1
Group: Development/Ruby 
License: BSD with advertising and MIT
URL: http://bcrypt-ruby.rubyforge.org
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Patch0: rake2_6_0_compiling.patch
Requires: rubygems
Requires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: ruby-rdoc
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(diff-lcs)
BuildRequires: rubygem(bundler)
Provides: rubygem(%{gemname}) = %{version}

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. bcrypt-ruby provides a simple, humane wrapper for
safely handling
passwords.


%prep
%setup -q -T -c


gem install --local --install-dir ./%{gemdir} \
            --force -V --rdoc %{SOURCE0}

%patch0 -p1


%build
mkdir -p ./%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir} %{buildroot}%{ruby_sitearch}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

mv %{buildroot}%{geminstdir}/ext/mri/bcrypt_ext.so %{buildroot}%{ruby_sitearch}
rm -rf %{buildroot}%{geminstdir}/ext %{buildroot}%{geminstdir}/lib/bcrypt_ext.so
rm -rf %{buildroot}%{geminstdir}/.gitignore
rm -rf %{buildroot}%{geminstdir}/.rspec


%clean
rm -rf %{buildroot}

%check
pushd .%{geminstdir}
rake spec --trace

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/spec
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Rakefile
%doc %{geminstdir}/Gemfile
%doc %{geminstdir}/Gemfile.lock
%doc %{geminstdir}/README.md
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/bcrypt-ruby.gemspec
%doc %{geminstdir}/CHANGELOG
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{ruby_sitearch}/bcrypt_ext.so
