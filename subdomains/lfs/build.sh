#!/usr/bin/env bash
set -euo pipefail

for book in lfs slfs glfs blfs; do
    for rev in sysv systemd; do
        (
            set -euo pipefail
            cd "$book"

            if diff sha "build-sha-$rev" &>/dev/null; then
                echo "Skipping $book-$rev"
                exit 0
            fi

            echo "Building $book-$rev"
            make REV=$rev THEMEDIR=../themes/themes THEME=sunset AUTO_CLEAN=0
            make REV=$rev INSTALLROOT=../../../target/subdomains/lfs install
            cp -f sha "build-sha-$rev"
        )
    done
done
