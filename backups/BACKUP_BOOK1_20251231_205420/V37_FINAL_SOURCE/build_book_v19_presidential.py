#!/usr/bin/env python3
"""
THE GATEKEEPERS SOCIETY - V37 Presidential Edition Build System
Complete build with front matter, clock-star motifs, and enhanced design
"""

import os
import sys
from pathlib import Path
from weasyprint import HTML, CSS

# Directories
BASE_DIR = Path("/home/ubuntu/V37_FINAL")
DESIGN_ASSETS = BASE_DIR / "book_source/design_assets"
OUTPUT_PDF = BASE_DIR / "THE_GATEKEEPERS_SOCIETY_V37_PRESIDENTIAL.pdf"
MASTER_MD = BASE_DIR / "THE_GATEKEEPERS_SOCIETY_V37_MASTER.md"

# Clock-star motif paths
CLOCK_STAR_LARGE = DESIGN_ASSETS / "clock_star_full_1.5in_450px.png"
CLOCK_STAR_MEDIUM = DESIGN_ASSETS / "clock_star_full_1.0in_300px.png"
CLOCK_STAR_SMALL = DESIGN_ASSETS / "clock_star_full_0.5in_150px.png"

def generate_front_matter():
    """Generate front matter HTML with clock-star motifs"""
    
    front_matter = f"""
<div class="half-title-page">
    <img src="{CLOCK_STAR_LARGE}" class="clock-star" alt="Clock-star motif" />
    <h1>THE GATEKEEPERS<br/>SOCIETY</h1>
</div>

<div class="page-break"></div>

<div class="title-page">
    <img src="{CLOCK_STAR_LARGE}" class="clock-star" alt="Clock-star motif" />
    <div class="title">THE<br/>GATEKEEPERS<br/>SOCIETY</div>
    <div class="subtitle">The Schedule Is the Weapon</div>
    <div class="author">OMAR SALAH</div>
</div>

<div class="page-break"></div>

<!-- Blank verso page after title -->
<div class="page-break"></div>

<div class="copyright-page">
    <p style="margin-top: 3in; font-size: 9pt; text-align: center; text-indent: 0;">
        THE GATEKEEPERS SOCIETY<br/>
        Copyright © 2025 by Omar Salah<br/>
        All rights reserved.<br/>
        <br/>
        No part of this book may be reproduced in any form without<br/>
        written permission from the publisher.<br/>
        <br/>
        ISBN 978-0-5-989-54420-9<br/>
        <br/>
        First Edition
    </p>
</div>

<div class="page-break"></div>

<div class="dedication-page">
    <p>For those who control the schedule,<br/>
    and through it, shape history.</p>
    <img src="{CLOCK_STAR_SMALL}" class="clock-star" alt="Clock-star motif" />
</div>

<div class="page-break"></div>
"""
    
    return front_matter


def convert_markdown_to_html(markdown_text):
    """Convert markdown to HTML with enhanced chapter formatting"""
    import markdown
    from markdown.extensions import tables, footnotes, attr_list
    
    md = markdown.Markdown(extensions=[
        'tables',
        'footnotes',
        'attr_list',
        'fenced_code',
        'nl2br'
    ])
    
    html_content = md.convert(markdown_text)
    
    # Enhance chapter openers
    html_content = enhance_chapter_openers(html_content)
    
    # Add section breaks with clock-stars
    html_content = add_section_breaks(html_content)
    
    return html_content


def enhance_chapter_openers(html_content):
    """Add clock-star motifs and enhanced formatting to chapter openers"""
    import re
    
    # Pattern for chapter headings
    chapter_pattern = r'<h1>(PROLOGUE|CHAPTER [A-Z]+|CHAPTER \d+|EPILOGUE)(.*?)</h1>'
    
    def replace_chapter(match):
        chapter_label = match.group(1)
        chapter_title = match.group(2).strip()
        
        # Remove leading colon or dash if present
        if chapter_title.startswith(':') or chapter_title.startswith('—'):
            chapter_title = chapter_title[1:].strip()
        
        opener_html = f"""
<div class="chapter-opener">
    <img src="{CLOCK_STAR_LARGE}" class="clock-star" alt="Clock-star motif" />
    <div class="chapter-label">{chapter_label}</div>
    <hr class="decorative-rule" />
    <h1 class="chapter-title">{chapter_title}</h1>
</div>
"""
        return opener_html
    
    html_content = re.sub(chapter_pattern, replace_chapter, html_content)
    
    return html_content


def add_section_breaks(html_content):
    """Replace horizontal rules with clock-star section breaks"""
    import re
    
    # Replace <hr> tags with clock-star images
    section_break = f'<div class="section-break"><img src="{CLOCK_STAR_SMALL}" alt="Section break" /></div>'
    html_content = re.sub(r'<hr\s*/?>', section_break, html_content)
    
    return html_content


def build_book():
    """Main build function"""
    
    print("=" * 70)
    print("THE GATEKEEPERS SOCIETY - V37 Presidential Edition Build")
    print("=" * 70)
    
    # Read master markdown
    print("\n📖 Reading master markdown...")
    if not MASTER_MD.exists():
        print(f"❌ ERROR: Master markdown not found at {MASTER_MD}")
        return False
    
    with open(MASTER_MD, 'r', encoding='utf-8') as f:
        master_content = f.read()
    
    print(f"   ✅ Loaded {len(master_content)} characters")
    
    # Generate front matter
    print("\n📄 Generating front matter...")
    front_matter_html = generate_front_matter()
    print("   ✅ Front matter created")
    
    # Convert markdown to HTML
    print("\n🔄 Converting markdown to HTML...")
    body_html = convert_markdown_to_html(master_content)
    print("   ✅ Conversion complete")
    
    # Combine into full HTML document
    print("\n🏗️  Building complete HTML document...")
    
    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Gatekeepers Society</title>
    <link rel="stylesheet" href="{DESIGN_ASSETS / 'presidential_edition_v2.css'}">
</head>
<body>
{front_matter_html}
{body_html}
</body>
</html>
"""
    
    # Save HTML for debugging
    html_file = BASE_DIR / "THE_GATEKEEPERS_SOCIETY_V37_PRESIDENTIAL.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"   ✅ HTML saved to {html_file}")
    
    # Generate PDF
    print("\n📕 Generating PDF with WeasyPrint...")
    try:
        HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(
            OUTPUT_PDF,
            stylesheets=[str(DESIGN_ASSETS / 'presidential_edition_v2.css')]
        )
        print(f"   ✅ PDF generated: {OUTPUT_PDF}")
        
        # Get file size
        size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
        print(f"   📊 File size: {size_mb:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"   ❌ ERROR generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = build_book()
    
    if success:
        print("\n" + "=" * 70)
        print("✅ BUILD COMPLETE - V37 Presidential Edition ready")
        print("=" * 70)
        sys.exit(0)
    else:
        print("\n" + "=" * 70)
        print("❌ BUILD FAILED")
        print("=" * 70)
        sys.exit(1)
