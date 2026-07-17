#!/usr/bin/env bash

set -euo pipefail

echo "[+] Executing autocommit script"

log_file="${1:-/tmp/log.txt}"
updated_images_file="${2:-/tmp/updated_images.txt}"
changelog_file="${3:-$PWD/LOG.md}"

awk '/successfully pushed to Docker Hub/ { print $2 }' "$log_file" > "$updated_images_file"

if [[ -s "$updated_images_file" ]]; then
    printf '\n### [%s]\n' "$(date +%F)" >> "$changelog_file"

    while IFS= read -r image; do
        image_name="${image%:*}"
        image_version="${image##*:}"
        printf -- '- %s updated to version %s\n' "$image_name" "$image_version" >> "$changelog_file"
    done < "$updated_images_file"
fi
