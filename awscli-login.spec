%{?!python3_pkgversion:%global python3_pkgversion 3}

%global pypi_name awscli_login

Name:           awscli-login
Version:        0.1.0a5
Release:        1%{?dist}
Summary:        Allows retrieving temporary AWS credentials via SAML
License:        MIT
URL:            https://github.com/techservicesillinois/awscli-login/tags
Source0:        https://github.com/techservicesillinois/awscli-login/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
The awscli-login plugin allows retrieving temporary Amazon credentials
by authenticating against a SAML Identity Provider (IdP). This
application is supported under Linux, MacOS, and the Windows Subsystem
for Linux. Currently, Windows PowerShell, Command Prompt, and Git
Shell for Windows are not supported.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}

%prep
%autosetup -p1


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/tests/

#%check
#%{__python3} setup.py test

%files -n  python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc docs/*
# For noarch packages: sitelib
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 20 14:54:44 EDT 2020 Jonathan Billings <jsbillings@jsbillings.org> - 0.1.0a6
- initial packge build
