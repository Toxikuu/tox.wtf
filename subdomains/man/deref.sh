#!/usr/bin/env bash

cd ../../target/tmp/man/

grep -rl '^\.so ' . | while IFS= read -r page; do
    to="$(head -n1 "$page" | cut -d/ -f2)"
    ln -sfv "$to" "$page"
done
