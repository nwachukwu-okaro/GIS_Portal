#!/usr/bin/env bash
# Optional Linux wrapper. The portable implementation lives in build.py.
# Not using 'set -e' or 'exec' here: build.py exits 1 for a normal partial
# failure (some tables failed, most succeeded - see metadata_builder/README.md),
# and the new-table check below must still run on nights like that, not just
# on a fully clean build. Only a fatal build.py error (exit 2) skips it.
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [[ -x "$PROJECT_DIR/venv/bin/python" ]]; then
    PYTHON="$PROJECT_DIR/venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
else
    PYTHON="python"
fi

"$PYTHON" "$SCRIPT_DIR/build.py" "$@"
BUILD_EXIT=$?

MONITOR_EXIT=0
if [[ "$BUILD_EXIT" -ne 2 ]]; then
    "$PYTHON" "$SCRIPT_DIR/monitor_new_tables.py" --new-only
    MONITOR_EXIT=$?
fi

if [[ "$BUILD_EXIT" -gt "$MONITOR_EXIT" ]]; then
    exit "$BUILD_EXIT"
else
    exit "$MONITOR_EXIT"
fi
