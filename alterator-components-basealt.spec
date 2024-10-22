%define _unpackaged_files_terminate_build 1

Name: alterator-components-basealt
Version: 0.1.2
Release: alt1

Summary: Test objects for Alterator module components
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-module-components

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: cmark rpm-build-python3
Requires: alterator-entry python3

%description
Test objects for Alterator module components.

%prep
%setup

%build
for d in components/*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

%install
mkdir -p "%buildroot%_datadir/alterator/backends"

for d in components/*/ ; do
    d="$(basename "$d")"
    mkdir -p "%buildroot%_datadir/alterator/components/$d"
    install -v -p -m 644 -D "components/$d/$d.backend" "%buildroot%_datadir/alterator/backends"
    install -v -p -m 644 -D "components/$d/$d.component" "%buildroot%_datadir/alterator/components/$d"

    find "components/$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_datadir/alterator/components/$d"
    done
done

for d in categories/* ; do
    d="$(basename "$d")"
    install -v -p -m 644 -D "categories/$d" "%buildroot%_datadir/alterator/components"
done

%files
%_datadir/alterator/backends/*
%_datadir/alterator/components/*

%changelog
* Mon Jul 23 2024 Michael Chernihin <chernigin@altlinux.org> 0.1.2-alt1
- Update interface.

* Mon May 06 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- Build for test purposes.

* Tue Mar 19 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
