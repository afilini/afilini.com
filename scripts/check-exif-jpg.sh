#!/usr/bin/env bash

set -eo pipefail

function err() {
    echo "FOUND EXIF METADATA IN: ${1}"
    exit 1
}

for f in $(find . \( -iname \*.jpg -o -iname \*.jpeg \) ); do
    identify -format '%[EXIF:*]' $f | grep -q -i 'exif' && err $f
done

exit 0
