#!/usr/bin/env bash
set -euo pipefail

for book in lfs slfs glfs blfs; do
    rm -rf $book/target

    for rev in sysv systemd; do
        (
            set -euo pipefail
            cd "$book"

            echo "Building $book-$rev"
            make REV=$rev THEMEDIR=../themes/themes THEME=sunset AUTO_CLEAN=0
            make REV=$rev INSTALLROOT=../../../target/subdomains/lfs install
        ) &

        jobs+=($!)
    done
done

status=0
for pid in "${jobs[@]}"; do
    if ! wait "$pid"; then
        status=1
    fi
done

exit "$status"
