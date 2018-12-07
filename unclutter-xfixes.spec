Name: unclutter-xfixes
Version: 1.3
Release: 1%{?dist}
Summary: Unclutter-xfixes is a rewrite of unclutter using the x11-xfixes extension

License: MIT
URL: https://github.com/Airblader/unclutter-xfixes
Source0: v%{version}.tar.gz

BuildRequires: asciidoc, git, libev-devel, libX11-devel, libXi-devel, libXfixes-devel
Requires: libev, libX11, libXfixes, libXi

%description

#%%global debug_package %%{nil}

%prep
%setup -q


%build
%define debug_package %{nil}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

%files
%doc README.md
%{_bindir}/unclutter
%{_mandir}/man1/unclutter.1.gz


%changelog

