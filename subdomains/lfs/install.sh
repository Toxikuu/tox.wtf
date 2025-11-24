#!/usr/bin/env bash

set -euo pipefail

for book in *lfs; do
    pushd "$book" >/dev/null

    for rev in sysv systemd; do
        echo "Installing $book-$rev"
        make REV=$rev INSTALLROOT=../../../target/subdomains/lfs install
    done

    popd >/dev/null
done
