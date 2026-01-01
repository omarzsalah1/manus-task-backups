#!/usr/bin/env python3
"""
Convert cover PNGs to PDFs at EXACTLY 6×9 inches
Uses PIL + reportlab for precise control
"""

from PIL import Image
from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
from pathlib import Path

# Define exact 6×9 inch page size in points (72 points = 1 inch)
PAGE_WIDTH = 6 * 72  # 432 points
PAGE_HEIGHT = 9 * 72  # 648 points

def convert_image_to_pdf(image_path, output_pdf):
    """Convert PNG to PDF at exactly 6×9 inches"""
    print(f"Converting {image_path.name}...")
    
    # Open image
    img = Image.open(image_path)
    print(f"  Original size: {img.size[0]}x{img.size[1]} pixels")
    
    # Resize to 1800x2700 pixels (6×9 inches at 300 DPI)
    target_size = (1800, 2700)
    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
    print(f"  Resized to: {img_resized.size[0]}x{img_resized.size[1]} pixels (300 DPI)")
    
    # Save as temporary PNG
    temp_png = output_pdf.parent / f"temp_{image_path.name}"
    img_resized.save(temp_png, "PNG", dpi=(300, 300))
    
    # Create PDF with exact dimensions
    c = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    # Draw image to fill entire page (0,0 is bottom-left in reportlab)
    c.drawImage(str(temp_png), 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
    
    # Save PDF
    c.save()
    
    # Remove temp file
    temp_png.unlink()
    
    print(f"  ✓ Created: {output_pdf.name} ({PAGE_WIDTH}x{PAGE_HEIGHT} pts = 6×9 inches)")

# Paths
BASE_DIR = Path("/home/ubuntu/V38_FINAL")
FRONT_COVER_PNG = BASE_DIR / "book_source/design_assets/GATEKEEPERS_FRONT_ANTIQUARIAN(2).png"
BACK_COVER_PNG = BASE_DIR / "book_source/design_assets/GATEKEEPERS_BACK_ANTIQUARIAN(1).png"
FRONT_COVER_PDF = BASE_DIR / "front_cover.pdf"
BACK_COVER_PDF = BASE_DIR / "back_cover.pdf"

print("=" * 80)
print("COVER PNG → PDF CONVERSION (6×9 inches exactly)")
print("=" * 80)

# Convert front cover
convert_image_to_pdf(FRONT_COVER_PNG, FRONT_COVER_PDF)

# Convert back cover
convert_image_to_pdf(BACK_COVER_PNG, BACK_COVER_PDF)

print("\n✅ Both covers converted successfully!")
print(f"Front cover: {FRONT_COVER_PDF}")
print(f"Back cover: {BACK_COVER_PDF}")
