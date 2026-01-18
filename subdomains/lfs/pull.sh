#!/usr/bin/env bash

set -euo pipefail

git submodule update --init --recursive --remote
git submodule status

for book in lfs glfs slfs blfs; do
    git submodule status $book | cut -c2-41 > $book/sha
done
