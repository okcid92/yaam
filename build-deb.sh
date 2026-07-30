#!/usr/bin/env bash
# Build the Yaam .deb package
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG_DIR="$SCRIPT_DIR/pkg"
VERSION="1.0.0"
OUTPUT="$SCRIPT_DIR/yaam_${VERSION}_all.deb"

echo "=== Nettoyage de l'ancien build ==="
rm -f "$OUTPUT"

echo "=== Copie des fichiers ==="
# yaam-server.py → /usr/bin/yaam-server
cp "$SCRIPT_DIR/yaam-server.py" "$PKG_DIR/usr/bin/yaam-server"
chmod 755 "$PKG_DIR/usr/bin/yaam-server"

# yaam-init → /usr/bin/yaam-init
cp "$SCRIPT_DIR/yaam-init" "$PKG_DIR/usr/bin/yaam-init"
chmod 755 "$PKG_DIR/usr/bin/yaam-init"

# Templates → /usr/share/yaam/templates/
rm -rf "$PKG_DIR/usr/share/yaam/templates"
cp -r "$SCRIPT_DIR/templates" "$PKG_DIR/usr/share/yaam/templates"

# requirements.txt → /usr/share/yaam/
cp "$SCRIPT_DIR/requirements.txt" "$PKG_DIR/usr/share/yaam/requirements.txt"

echo "=== Correction des permissions ==="
chmod 755 "$PKG_DIR/DEBIAN/postinst" "$PKG_DIR/DEBIAN/postrm"
chmod 644 "$PKG_DIR/DEBIAN/control"
find "$PKG_DIR/usr" -type f -name "*.md" -exec chmod 644 {} \;
find "$PKG_DIR/usr" -type f -name "*.txt" -exec chmod 644 {} \;
find "$PKG_DIR/usr" -type f -name "*.desktop" -exec chmod 644 {} \;

echo "=== Build du .deb ==="
dpkg-deb --root-owner-group --build "$PKG_DIR" "$OUTPUT"

echo "=== Vérification ==="
dpkg-deb --info "$OUTPUT"
dpkg-deb --contents "$OUTPUT"

echo ""
echo "✅ Paquet créé : $OUTPUT"
