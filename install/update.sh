#!/usr/bin/env bash
set -euo pipefail
git pull --ff-only
bash install/install.sh
