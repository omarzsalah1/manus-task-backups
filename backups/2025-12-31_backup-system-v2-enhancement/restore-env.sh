#!/bin/bash
# Environment Restoration Script
# Automatically reinstalls all packages and restores environment state

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKUP_DIR="${SCRIPT_DIR}"

echo "🔄 Starting environment restoration..."

# Restore Python packages
if [ -f "${BACKUP_DIR}/requirements.txt" ]; then
    echo "📦 Installing Python packages..."
    pip3 install -r "${BACKUP_DIR}/requirements.txt" --quiet
    echo "✅ Python packages installed"
else
    echo "⚠️ No requirements.txt found, skipping Python packages"
fi

# Restore Node.js packages
if [ -f "${BACKUP_DIR}/package.json" ]; then
    echo "📦 Installing Node.js packages..."
    cd "${BACKUP_DIR}/sandbox" 2>/dev/null || cd "${BACKUP_DIR}"
    if [ -f "package-lock.json" ]; then
        npm ci --silent 2>/dev/null || npm install --silent
    else
        npm install --silent
    fi
    echo "✅ Node.js packages installed"
else
    echo "⚠️ No package.json found, skipping Node.js packages"
fi

# Restore system packages
if [ -f "${BACKUP_DIR}/apt-packages.txt" ]; then
    echo "📦 Installing system packages..."
    sudo apt-get update -qq
    xargs -a "${BACKUP_DIR}/apt-packages.txt" sudo apt-get install -y -qq
    echo "✅ System packages installed"
else
    echo "⚠️ No apt-packages.txt found, skipping system packages"
fi

# Restore environment variables (if any)
if [ -f "${BACKUP_DIR}/env-vars.sh" ]; then
    echo "🔧 Loading environment variables..."
    source "${BACKUP_DIR}/env-vars.sh"
    echo "✅ Environment variables loaded"
fi

# Run any custom restoration commands
if [ -f "${BACKUP_DIR}/custom-restore.sh" ]; then
    echo "🔧 Running custom restoration script..."
    bash "${BACKUP_DIR}/custom-restore.sh"
    echo "✅ Custom restoration complete"
fi

echo ""
echo "✅ Environment restoration complete!"
echo "📁 Sandbox files are in: ~/manus-task-backups/backups/$(basename ${BACKUP_DIR})/sandbox/"
echo ""
