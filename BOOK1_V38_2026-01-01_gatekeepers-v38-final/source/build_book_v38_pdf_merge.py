#!/usr/bin/env python3
"""
Build The Gatekeepers Society V38 Presidential Edition
Uses PNG→PDF conversion + merging for full-bleed covers
CRITICAL FIX: Covers stretched to EXACTLY 6×9 inches (no narrow covers!)
"""

import os
import sys
import subprocess
from pathlib import Path

# Configuration
BASE_DIR = Path("/home/ubuntu/V38_FINAL")
BOOK_SOURCE = BASE_DIR / "book_source"
OUTPUT_PDF = BASE_DIR / "THE_GATEKEEPERS_SOCIETY_V38_PRESIDENTIAL.pdf"
MASTER_MD = BOOK_SOURCE / "THE_GATEKEEPERS_SOCIETY_V38_MASTER.md"
CSS_FILE = BOOK_SOURCE / "book_styles.css"

# Cover images
FRONT_COVER_PNG = BOOK_SOURCE / "design_assets" / "GATEKEEPERS_FRONT_ANTIQUARIAN(2).png"
BACK_COVER_PNG = BOOK_SOURCE / "design_assets" / "GATEKEEPERS_BACK_ANTIQUARIAN(1).png"

# Temporary files
FRONT_COVER_PDF = BASE_DIR / "front_cover.pdf"
BACK_COVER_PDF = BASE_DIR / "back_cover.pdf"
CONTENT_PDF = BASE_DIR / "content.pdf"
MERGED_PDF = BASE_DIR / "merged.pdf"

print("=" * 80)
print("THE GATEKEEPERS SOCIETY V38 - BUILD SCRIPT")
print("=" * 80)
print(f"\nBase directory: {BASE_DIR}")
print(f"Master markdown: {MASTER_MD}")
print(f"CSS file: {CSS_FILE}")
print(f"Output PDF: {OUTPUT_PDF}")

# Verify files exist
if not MASTER_MD.exists():
    print(f"\n❌ ERROR: Master markdown not found: {MASTER_MD}")
    sys.exit(1)

if not CSS_FILE.exists():
    print(f"\n❌ ERROR: CSS file not found: {CSS_FILE}")
    sys.exit(1)

if not FRONT_COVER_PNG.exists():
    print(f"\n❌ ERROR: Front cover not found: {FRONT_COVER_PNG}")
    sys.exit(1)

if not BACK_COVER_PNG.exists():
    print(f"\n❌ ERROR: Back cover not found: {BACK_COVER_PNG}")
    sys.exit(1)

print("\n✓ All source files verified")

# ============================================================================
# STEP 1: Convert cover PNGs to PDFs at EXACTLY 6×9 inches
# ============================================================================
print("\n" + "=" * 80)
print("STEP 1: Converting covers to PDF (FULL-SIZE 6×9 inches)")
print("=" * 80)

# CRITICAL: Use -resize to force covers to EXACTLY 6×9 inches (1800×2700 pixels at 300 DPI)
# This prevents narrow covers!

print("\nConverting front cover...")
cmd_front = [
    "convert",
    str(FRONT_COVER_PNG),
    "-resize", "1800x2700!",  # ! forces exact dimensions (stretch if needed)
    "-density", "300",
    "-units", "PixelsPerInch",
    "-page", "6x9in",
    str(FRONT_COVER_PDF)
]
result = subprocess.run(cmd_front, capture_output=True, text=True)
if result.returncode != 0:
    print(f"❌ ERROR: Front cover conversion failed: {result.stderr}")
    sys.exit(1)
print(f"✓ Front cover PDF created: {FRONT_COVER_PDF}")

print("\nConverting back cover...")
cmd_back = [
    "convert",
    str(BACK_COVER_PNG),
    "-resize", "1800x2700!",  # ! forces exact dimensions (stretch if needed)
    "-density", "300",
    "-units", "PixelsPerInch",
    "-page", "6x9in",
    str(BACK_COVER_PDF)
]
result = subprocess.run(cmd_back, capture_output=True, text=True)
if result.returncode != 0:
    print(f"❌ ERROR: Back cover conversion failed: {result.stderr}")
    sys.exit(1)
print(f"✓ Back cover PDF created: {BACK_COVER_PDF}")

# Verify cover PDFs
for cover_pdf in [FRONT_COVER_PDF, BACK_COVER_PDF]:
    size_mb = cover_pdf.stat().st_size / (1024 * 1024)
    print(f"  {cover_pdf.name}: {size_mb:.2f} MB")

# ============================================================================
# STEP 2: Build content PDF from markdown using WeasyPrint
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: Building content PDF from markdown")
print("=" * 80)

print("\nRunning WeasyPrint...")
cmd_weasyprint = [
    "weasyprint",
    str(MASTER_MD),
    str(CONTENT_PDF),
    "-s", str(CSS_FILE),
    "--pdf-variant", "pdf/ua-1"
]

result = subprocess.run(cmd_weasyprint, capture_output=True, text=True)
if result.returncode != 0:
    print(f"❌ ERROR: WeasyPrint failed: {result.stderr}")
    sys.exit(1)

if not CONTENT_PDF.exists():
    print(f"❌ ERROR: Content PDF was not created")
    sys.exit(1)

size_mb = CONTENT_PDF.stat().st_size / (1024 * 1024)
print(f"✓ Content PDF created: {CONTENT_PDF} ({size_mb:.2f} MB)")

# Get page count
result = subprocess.run(["pdfinfo", str(CONTENT_PDF)], capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if line.startswith('Pages:'):
        content_pages = line.split(':')[1].strip()
        print(f"  Content pages: {content_pages}")

# ============================================================================
# STEP 3: Merge PDFs (front cover + content + back cover)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 3: Merging PDFs")
print("=" * 80)

print("\nMerging: front_cover.pdf + content.pdf + back_cover.pdf")
cmd_merge = [
    "gs",
    "-dBATCH",
    "-dNOPAUSE",
    "-q",
    "-sDEVICE=pdfwrite",
    "-dPDFSETTINGS=/prepress",
    f"-sOutputFile={MERGED_PDF}",
    str(FRONT_COVER_PDF),
    str(CONTENT_PDF),
    str(BACK_COVER_PDF)
]

result = subprocess.run(cmd_merge, capture_output=True, text=True)
if result.returncode != 0:
    print(f"❌ ERROR: PDF merge failed: {result.stderr}")
    sys.exit(1)

if not MERGED_PDF.exists():
    print(f"❌ ERROR: Merged PDF was not created")
    sys.exit(1)

size_mb = MERGED_PDF.stat().st_size / (1024 * 1024)
print(f"✓ Merged PDF created: {MERGED_PDF} ({size_mb:.2f} MB)")

# Get total page count
result = subprocess.run(["pdfinfo", str(MERGED_PDF)], capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if line.startswith('Pages:'):
        total_pages = line.split(':')[1].strip()
        print(f"  Total pages: {total_pages} (front cover + {content_pages} content + back cover)")

# ============================================================================
# STEP 4: Compress final PDF
# ============================================================================
print("\n" + "=" * 80)
print("STEP 4: Compressing final PDF")
print("=" * 80)

print("\nCompressing with Ghostscript /printer settings (200 DPI)...")
cmd_compress = [
    "gs",
    "-sDEVICE=pdfwrite",
    "-dCompatibilityLevel=1.4",
    "-dPDFSETTINGS=/printer",
    "-dNOPAUSE",
    "-dQUIET",
    "-dBATCH",
    f"-sOutputFile={OUTPUT_PDF}",
    str(MERGED_PDF)
]

result = subprocess.run(cmd_compress, capture_output=True, text=True)
if result.returncode != 0:
    print(f"❌ ERROR: Compression failed: {result.stderr}")
    sys.exit(1)

if not OUTPUT_PDF.exists():
    print(f"❌ ERROR: Final PDF was not created")
    sys.exit(1)

# ============================================================================
# FINAL STATISTICS
# ============================================================================
print("\n" + "=" * 80)
print("BUILD COMPLETE!")
print("=" * 80)

final_size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
merged_size_mb = MERGED_PDF.stat().st_size / (1024 * 1024)
compression_ratio = (1 - final_size_mb / merged_size_mb) * 100

print(f"\n✓ Final PDF: {OUTPUT_PDF}")
print(f"  Size: {final_size_mb:.2f} MB (compressed from {merged_size_mb:.2f} MB)")
print(f"  Compression: {compression_ratio:.1f}% reduction")
print(f"  Pages: {total_pages}")

# Get PDF info
result = subprocess.run(["pdfinfo", str(OUTPUT_PDF)], capture_output=True, text=True)
print("\nPDF Information:")
for line in result.stdout.split('\n'):
    if any(keyword in line for keyword in ['Pages:', 'Page size:', 'PDF version:', 'File size:']):
        print(f"  {line}")

# ============================================================================
# CLEANUP
# ============================================================================
print("\n" + "=" * 80)
print("CLEANUP")
print("=" * 80)

print("\nRemoving temporary files...")
for temp_file in [FRONT_COVER_PDF, BACK_COVER_PDF, CONTENT_PDF, MERGED_PDF]:
    if temp_file.exists():
        temp_file.unlink()
        print(f"  ✓ Removed {temp_file.name}")

print("\n" + "=" * 80)
print("🎉 V38 PRESIDENTIAL EDITION BUILD SUCCESSFUL!")
print("=" * 80)
print(f"\n📄 Output: {OUTPUT_PDF}")
print(f"📊 Size: {final_size_mb:.2f} MB")
print(f"📖 Pages: {total_pages}")
print("\n✅ Ready for delivery!")
