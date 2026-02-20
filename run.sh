#!/bin/sh
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
exec python3 -m app.main "$@"
