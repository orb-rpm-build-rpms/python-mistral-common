Name:           python-mistral-common
Version:        1.11.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Mistral-common is a library of common utilities for Mistral AI.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            ...
Source:         %{pypi_source mistral_common}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mistral-common' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mistral-common
Summary:        %{summary}

%description -n python3-mistral-common %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-mistral-common all,audio,guidance,hf-hub,image,opencv,sentencepiece,server,soundfile,soxr


%prep
%autosetup -p1 -n mistral_common-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,audio,guidance,hf-hub,image,opencv,sentencepiece,server,soundfile,soxr


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files mistral_common


%check
%pyproject_check_import


%files -n python3-mistral-common -f %{pyproject_files}
%{_bindir}/mistral_common


%changelog
%autochangelog
