%define	module	django-classy-tags

Summary:	Class-based template tags for Django

Name:		python-%{module}
Version:	0.5.1
Release:	1
Source0:	http://pypi.python.org/packages/source/d/django-classy-tags/django-classy-tags-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/django-classy-tags/
BuildArch:	noarch
Requires:	python-django
BuildRequires:	python-setuptools

%description
Class-based template tags for Django.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST



