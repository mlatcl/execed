#!/usr/bin/env bash

FILES=""
SKIP=true
while read stub; do
    if $SKIP; then
	SKIP=false
    else
        if [ -f "${stub}.md" ]; then
            maketalk "${stub}.md"
        elif [ -f "${stub}.gpp.markdown" ]; then
            maketalk "${stub}.gpp.markdown"
        else
            echo "Error: can't find source for '${stub}' (tried .md and .gpp.markdown)" 1>&2
            exit 1
        fi
    fi
done < lectures.csv
