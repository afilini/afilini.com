#!/usr/bin/env bash

set -eo pipefail

hugo -d ./public-staging

cat<<EOF > ./public-staging/robots.txt
User-Agent: *
Disallow: /
EOF
