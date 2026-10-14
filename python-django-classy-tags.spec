%define module django-classy-tags
%define oname django_classy_tags

Name:		python-django-classy-tags
Summary:	Class-based template tags for Django
Version:	4.1.0
Release:	2
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/django-cms/django-classy-tags
#URL:		https://pypi.python.org/pypi/django-classy-tags/
Source0:	%{URL}/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(django)

%description
Class-based template tags for Django.

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/classytags
%{python_sitelib}/%{oname}-%{version}*.*-info
