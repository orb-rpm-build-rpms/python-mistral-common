Name:           python-mistral-common
Version:        1.11.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Mistral-common is a library of common utilities for Mistral AI.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-common
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

# vLLM requires only mistral_common[image] (which pulls in [opencv]), so only
# those extras are packaged. The dropped extras are unusable on this base
# anyway: guidance pins llguidance <1.4 (we ship 1.7 for vLLM), audio/soxr/
# soundfile are unpackaged, and server needs a newer uvloop than F44 has.
# opencv-python-headless resolves via the name-bridge metapackage
# python3-opencv-python-headless (-> python3-opencv).
%pyproject_extras_subpkg -n python3-mistral-common image,opencv


%prep
%autosetup -p1 -n mistral_common-%{version}


%generate_buildrequires
# Only the image/opencv extras (see the extras subpackage note above).
%pyproject_buildrequires -x image,opencv


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
