# Generated from bcrypt-ruby-3.0.1.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	bcrypt-ruby

Summary:	OpenBSD's bcrypt() password hashing algorithm
Name:		rubygem-%{rbname}

Version:	3.0.1
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://bcrypt-ruby.rubyforge.org
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
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_sitearchdir}/*.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.md
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.0.1-3
+ Revision: 774493
- drop buildrequires on rake as it's now provided by ruby
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.1-2
+ Revision: 767900
- release bump
- files section reworked

* Fri Sep 30 2011 Alexander Barakin <abarakin@mandriva.org> 3.0.1-1
+ Revision: 702154
- misspelling
- add bundle build requirement
- actual rubygems fix
- imported package rubygem-bcrypt-ruby

