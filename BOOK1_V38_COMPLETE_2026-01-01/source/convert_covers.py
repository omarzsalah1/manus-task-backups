#!/usr/bin/env python3
from PIL import Image
from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
from pathlib import Path

PAGE_WIDTH = 6 * 72
PAGE_HEIGHT = 9 * 72

def convert_image_to_pdf(image_path, output_pdf):
    print(f"Converting {image_path.name}...")
    img = Image.open(image_path)
    target_size = (1800, 2700)
    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
    temp_png = output_pdf.parent / f"temp_{image_path.name}"
    img_resized.save(temp_png, "PNG", dpi=(300, 300))
    c = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    c.drawImage(str(temp_png), 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
    c.save()
    temp_png.unlink()
    print(f"  ✓ Created: {output_pdf.name}")

BASE_DIR = Path("/home/ubuntu/V38_REBUILD")
FRONT_COVER_PNG = BASE_DIR / "book_source/design_assets/GATEKEEPERS_FRONT_ANTIQUARIAN(2).png"
BACK_COVER_PNG = BASE_DIR / "book_source/design_assets/GATEKEEPERS_BACK_ANTIQUARIAN(1).png"
FRONT_COVER_PDF = BASE_DIR / "front_cover.pdf"
BACK_COVER_PDF = BASE_DIR / "back_cover.pdf"

print("Converting covers to PDF (6×9 inches)...")
convert_image_to_pdf(FRONT_COVER_PNG, FRONT_COVER_PDF)
convert_image_to_pdf(BACK_COVER_PNG, BACK_COVER_PDF)
print("✅ Covers converted!")
