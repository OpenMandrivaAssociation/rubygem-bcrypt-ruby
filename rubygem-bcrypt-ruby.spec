# Generated from bcrypt-ruby-3.0.1.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	bcrypt-ruby

Summary:	OpenBSD's bcrypt() password hashing algorithm
Name:		rubygem-%{rbname}

Version:	3.0.1
Release:	6
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://bcrypt-ruby.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. bcrypt-ruby provides a simple, humane wrapper for
safely handling
passwords.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{ruby_sitearchdir}/*.so
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/*.md
%{gem_dir}/gems/%{rbname}-%{version}/CHANGELOG
%{gem_dir}/gems/%{rbname}-%{version}/COPYING
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb


