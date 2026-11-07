#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
MODULES_DIR="$ROOT/modules"
fail_count=0
pass_count=0
skip_count=0

for module_dir in "$MODULES_DIR"/*/; do
    module_name="$(basename "$module_dir")"
    examples_dir="$module_dir/examples"

    if [ ! -d "$examples_dir" ]; then
        continue
    fi

    has_py=false
    for f in "$examples_dir"/*.py; do
        [ -e "$f" ] && has_py=true && break
    done

    if [ "$has_py" = false ]; then
        echo "SKIP  $module_name (no examples)"
        skip_count=$((skip_count + 1))
        continue
    fi

    for py_file in "$examples_dir"/*.py; do
        name="$module_name/$(basename "$py_file")"
        if python3 "$py_file" > /dev/null 2>&1; then
            echo "PASS  $name"
            pass_count=$((pass_count + 1))
        else
            echo "FAIL  $name"
            fail_count=$((fail_count + 1))
        fi
    done
done

echo ""
echo "Results: $pass_count passed, $fail_count failed, $skip_count skipped"

if [ "$fail_count" -gt 0 ]; then
    exit 1
fi
exit 0
