%define _unpackaged_files_terminate_build 1

Name: alterator-components-basealt
Version: 0.1.0
Release: alt1

Summary: Core components for BaseALT products
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-components-basealt

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: cmark

%description
Core components for BaseALT products.

%prep
%setup

%build
for d in */ ; do
    d="${d%%/}"
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

%install
mkdir -p "%buildroot%_datadir/alterator/backends"

for d in */; do
    d="${d%%/}"
    mkdir -p "%buildroot%_datadir/alterator/components/$d"
    install -v -p -m 644 -D "$d/$d.backend" "%buildroot%_datadir/alterator/backends"
    install -v -p -m 644 -D "$d/$d.category" "%buildroot%_datadir/alterator/components"
    install -v -p -m 644 -D "$d/$d.component" "%buildroot%_datadir/alterator/components/$d"

    find "$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_datadir/alterator/components/$d"
    done
done

%files
%_datadir/alterator/backends/*
%_datadir/alterator/components/*

%changelog
* Thu Oct 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build with example components.
