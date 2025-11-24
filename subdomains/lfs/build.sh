#!/usr/bin/env bash
set -euo pipefail

for book in *lfs; do
    pushd "$book" >/dev/null

    make clean
    for rev in sysv systemd; do
        echo "Building $book-$rev"
        make -j4 REV=sysv THEMEDIR=../themes/themes THEME=sunset
    done

    popd >/dev/null
done
