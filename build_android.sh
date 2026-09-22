#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install --user buildozer
buildozer -v android debug
mkdir -p bin
find bin -maxdepth 1 -type f -name '*.apk' -print
