#!/bin/bash
# Environment Capture Script
# Captures all installed packages and environment state for restoration

OUTPUT_DIR="${1:-.}"

echo "📸 Capturing environment state..."

# Capture Python packages
echo "📦 Capturing Python packages..."
pip3 freeze > "${OUTPUT_DIR}/requirements.txt" 2>/dev/null || echo "# No pip packages" > "${OUTPUT_DIR}/requirements.txt"
echo "   Saved to requirements.txt"

# Capture Node.js global packages
echo "📦 Capturing Node.js packages..."
if command -v npm &> /dev/null; then
    npm list -g --depth=0 --json 2>/dev/null | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    deps = data.get('dependencies', {})
    for name, info in deps.items():
        print(f'{name}@{info.get(\"version\", \"latest\")}')
except:
    pass
" > "${OUTPUT_DIR}/npm-global-packages.txt"
    echo "   Saved to npm-global-packages.txt"
fi

# Capture manually installed apt packages
echo "📦 Capturing system packages..."
comm -23 <(apt-mark showmanual | sort) <(gzip -dc /var/log/installer/initial-status.gz 2>/dev/null | sed -n 's/^Package: //p' | sort) > "${OUTPUT_DIR}/apt-packages.txt" 2>/dev/null || echo "# Unable to capture apt packages" > "${OUTPUT_DIR}/apt-packages.txt"
echo "   Saved to apt-packages.txt"

# Capture working directory
echo "📁 Capturing working directory..."
pwd > "${OUTPUT_DIR}/working-dir.txt"
echo "   Saved to working-dir.txt"

# Calculate sandbox size
echo "📊 Calculating sandbox size..."
du -sh /home/ubuntu --exclude='.cache' --exclude='.local' --exclude='.npm' --exclude='.nvm' 2>/dev/null | cut -f1 > "${OUTPUT_DIR}/sandbox-size.txt" || echo "Unknown" > "${OUTPUT_DIR}/sandbox-size.txt"
echo "   Saved to sandbox-size.txt"

# Count files
echo "📊 Counting files..."
find /home/ubuntu -type f \
    ! -path "*/\.git/*" \
    ! -path "*/__pycache__/*" \
    ! -path "*/node_modules/*" \
    ! -path "*/\.cache/*" \
    ! -path "*/\.local/*" \
    ! -path "*/\.npm/*" \
    ! -path "*/\.nvm/*" \
    ! -path "*/\.config/*" \
    2>/dev/null | wc -l > "${OUTPUT_DIR}/file-count.txt"
echo "   Saved to file-count.txt"

echo ""
echo "✅ Environment capture complete!"
echo "📁 Files saved to: ${OUTPUT_DIR}"
