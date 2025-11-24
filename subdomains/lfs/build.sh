#!/usr/bin/env bash
set -euo pipefail

for book in lfs slfs glfs blfs; do
    pushd "$book" >/dev/null

    make clean
    for rev in sysv systemd; do
        echo "Building $book-$rev"
        # FIXME: Building BLFS with AUTO_CLEAN=1 is broken
        make REV=$rev THEMEDIR=../themes/themes THEME=sunset AUTO_CLEAN=0
        make REV=$rev INSTALLROOT=../../../target/subdomains/lfs install
    done

    popd >/dev/null
done
