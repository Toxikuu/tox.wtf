#!/usr/bin/env bash

set -euo pipefail

for book in *lfs; do
    pushd "$book" >/dev/null

    for rev in sysv systemd; do
        echo "Installing $book-$rev"
        make -j4 REV=$rev INSTALLROOT=../../../target/subdomains/lfs install
    done

    popd >/dev/null
done
