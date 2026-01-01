#!/bin/bash
# Backup Inventory Script
# Generates a JSON manifest of all files in the sandbox

OUTPUT_FILE="${1:-manifest.json}"
SCAN_DIR="${2:-/home/ubuntu}"

echo "{"
echo "  \"backup_date\": \"$(date -Iseconds)\","
echo "  \"scan_directory\": \"$SCAN_DIR\","
echo "  \"files\": ["

first=true
find "$SCAN_DIR" -type f \
    ! -path "*/\.git/*" \
    ! -path "*/__pycache__/*" \
    ! -path "*/node_modules/*" \
    ! -path "*/\.cache/*" \
    ! -path "*/\.local/*" \
    ! -path "*/\.npm/*" \
    ! -path "*/\.config/*" \
    ! -name "*.pyc" \
    2>/dev/null | while read -r file; do
    
    if [ "$first" = true ]; then
        first=false
    else
        echo ","
    fi
    
    size=$(stat -c%s "$file" 2>/dev/null || echo "0")
    modified=$(stat -c%Y "$file" 2>/dev/null || echo "0")
    extension="${file##*.}"
    
    printf '    {"path": "%s", "size": %s, "modified": %s, "extension": "%s"}' \
        "$file" "$size" "$modified" "$extension"
done

echo ""
echo "  ],"
echo "  \"total_files\": $(find "$SCAN_DIR" -type f ! -path "*/\.git/*" ! -path "*/__pycache__/*" ! -path "*/node_modules/*" ! -path "*/\.cache/*" ! -path "*/\.local/*" ! -path "*/\.npm/*" ! -path "*/\.config/*" 2>/dev/null | wc -l)"
echo "}"
