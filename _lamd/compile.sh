#!/usr/bin/env bash

set -euo pipefail

MAKETALK="maketalk"
if [ -x "../.venv/bin/maketalk" ]; then
    MAKETALK="../.venv/bin/maketalk"
elif command -v maketalk >/dev/null 2>&1; then
    MAKETALK="maketalk"
else
    echo "Error: 'maketalk' not found. Install lamd (e.g. '../.venv/bin/pip install almd')." 1>&2
    exit 127
fi

# Ensure helper CLIs (mdfield, dependencies, etc.) are on PATH
if [ "${MAKETALK}" = "../.venv/bin/maketalk" ]; then
    VENV_BIN="$(cd ../.venv/bin && pwd)"
    export PATH="${VENV_BIN}:${PATH}"
fi

FILES=""
SKIP=true
while read stub; do
    if $SKIP; then
	SKIP=false
    else
        if [ -f "${stub}.md" ]; then
            "${MAKETALK}" "${stub}.md"
        elif [ -f "${stub}.gpp.markdown" ]; then
            "${MAKETALK}" "${stub}.gpp.markdown"
        else
            echo "Error: can't find source for '${stub}' (tried .md and .gpp.markdown)" 1>&2
            exit 1
        fi
    fi
done < lectures.csv
