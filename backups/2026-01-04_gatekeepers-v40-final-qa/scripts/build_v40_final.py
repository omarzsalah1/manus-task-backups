#!/usr/bin/env python3
"""
THE GATEKEEPERS SOCIETY - V40 FINAL Production Build
Based on V19 Presidential Edition with all fixes applied
"""

import os
import sys
from pathlib import Path
from weasyprint import HTML, CSS

# Directories
BASE_DIR = Path("/home/ubuntu/GATEKEEPERS_V40_FINAL")
SOURCE_DIR = BASE_DIR / "source"
BUILD_DIR = BASE_DIR / "build"
ASSETS_DIR = BASE_DIR / "assets"
OUTPUT_DIR = BASE_DIR / "output"

MASTER_MD = SOURCE_DIR / "THE_GATEKEEPERS_V40_FINAL_CLEAN.md"
CSS_FILE = BUILD_DIR / "book_styles_v40.css"
OUTPUT_PDF = OUTPUT_DIR / "THE_GATEKEEPERS_SOCIETY_V40_FINAL.pdf"

# Clock-star motif paths
CLOCK_STAR_LARGE = ASSETS_DIR / "clock_star_full_1.5in_450px.png"
CLOCK_STAR_MEDIUM = ASSETS_DIR / "clock_star_full_1.0in_300px.png"
CLOCK_STAR_SMALL = ASSETS_DIR / "clock_star_full_0.5in_150px.png"

def generate_front_matter():
    """Generate front matter HTML with clock-star motifs"""
    
    # Load base64 encoded clock-star image
    clock_star_b64_file = BUILD_DIR / "clock_star_base64.txt"
    with open(clock_star_b64_file, 'r') as f:
        clock_star_data_uri = f.read().strip()
    
    front_matter = f"""
<div class="title-page">
    <img src="{clock_star_data_uri}" class="clock-star" alt="Clock-star motif" style="width: 1.5in; height: 1.5in; display: block; margin: 2in auto 1in auto;" />
    <h1 class="main-title">THE GATEKEEPERS SOCIETY</h1>
    <p class="subtitle">The Schedule Is the Weapon</p>
    <p class="author">OMAR SALAH</p>
</div>

<div class="page-break"></div>
"""
    
    return front_matter


def generate_toc():
    """Generate table of contents HTML"""
    
    toc_html = """
<div class="toc">
    <h1>CONTENTS</h1>
    <ul>
        <li><strong>PROLOGUE</strong> — <em>The Papers in the Study</em> ....... 7</li>
        <li><strong>CHAPTER 1</strong> — <em>The Gatekeeper</em> ....... 40</li>
        <li><strong>CHAPTER 2</strong> — <em>The Vacation Wars</em> ....... 79</li>
        <li><strong>CHAPTER 3</strong> — <em>Breaking Point</em> ....... 135</li>
        <li><strong>CHAPTER 4</strong> — <em>Crisis Day</em> ....... 158</li>
        <li><strong>CHAPTER 5</strong> — <em>The Handoff</em> ....... 208</li>
        <li><strong>CHAPTER 6</strong> — <em>The Playbook</em> ....... 252</li>
        <li><strong>CHAPTER 7</strong> — <em>The Body's Needs</em> ....... 314</li>
        <li><strong>CHAPTER 8</strong> — <em>The Machinery of Access</em> ....... 367</li>
        <li><strong>CHAPTER 9</strong> — <em>The Family Firewall</em> ....... 388</li>
        <li><strong>CHAPTER 10</strong> — <em>Guilty Pleasures</em> ....... 441</li>
        <li><strong>EPILOGUE</strong> — <em>The Weight of the Office</em> ....... 478</li>
        <li><strong>CHAPTER 11</strong> — <em>The Weight of Friendship</em> ....... 507</li>
    </ul>
</div>

<div class="page-break"></div>
"""
    
    return toc_html


def convert_markdown_to_html(markdown_text):
    """Convert markdown to HTML with enhanced chapter formatting"""
    import markdown
    
    md = markdown.Markdown(extensions=[
        'extra',  # Includes tables, footnotes, attr_list, etc.
        'nl2br',
        'sane_lists'
    ])
    
    html_content = md.convert(markdown_text)
    
    # Enhance chapter openers with clock-stars
    html_content = enhance_chapter_openers(html_content)
    
    return html_content


def enhance_chapter_openers(html_content):
    """Add clock-star motifs and enhanced formatting to ALL chapter openers"""
    import re
    
    # Load base64 encoded clock-star image
    clock_star_b64_file = BUILD_DIR / "clock_star_base64.txt"
    with open(clock_star_b64_file, 'r') as f:
        clock_star_data_uri = f.read().strip()
    
    # Pattern for chapter headings - matches all variants
    chapter_patterns = [
        (r'<h1>PROLOGUE(.*?)</h1>', 'PROLOGUE'),
        (r'<h1>CHAPTER 1(.*?)</h1>', 'CHAPTER 1'),
        (r'<h1>CHAPTER 2(.*?)</h1>', 'CHAPTER 2'),
        (r'<h1>CHAPTER 3(.*?)</h1>', 'CHAPTER 3'),
        (r'<h1>CHAPTER 4(.*?)</h1>', 'CHAPTER 4'),
        (r'<h1>CHAPTER 5(.*?)</h1>', 'CHAPTER 5'),
        (r'<h1>CHAPTER 6(.*?)</h1>', 'CHAPTER 6'),
        (r'<h1>CHAPTER 7(.*?)</h1>', 'CHAPTER 7'),
        (r'<h1>CHAPTER 8(.*?)</h1>', 'CHAPTER 8'),
        (r'<h1>CHAPTER 9(.*?)</h1>', 'CHAPTER 9'),
        (r'<h1>CHAPTER 10(.*?)</h1>', 'CHAPTER 10'),
        (r'<h1>EPILOGUE(.*?)</h1>', 'EPILOGUE'),
        (r'<h1>CHAPTER 11(.*?)</h1>', 'CHAPTER 11'),
    ]
    
    chapters_found = []
    
    for pattern, label in chapter_patterns:
        match = re.search(pattern, html_content, re.IGNORECASE)
        if match:
            chapter_title = match.group(1).strip()
            
            # Remove leading colon, dash, or other separators
            for sep in [':', '—', '–', '-']:
                if chapter_title.startswith(sep):
                    chapter_title = chapter_title[1:].strip()
                    break
            
            # Create chapter opener with clock-star divider using base64 data URI
            opener_html = f"""
<div class="chapter-divider">
    <img src="{clock_star_data_uri}" class="clock-star" alt="Clock-star motif" style="width: 1.5in; height: 1.5in; display: block; margin: 3in auto 0 auto;" />
</div>

<div class="page-break"></div>

<div class="chapter-opener">
    <h1 class="chapter-label">{label}</h1>
    <h2 class="chapter-title">{chapter_title}</h2>
</div>
"""
            
            # Replace the original h1 with the enhanced opener
            html_content = re.sub(pattern, opener_html, html_content, count=1)
            chapters_found.append(label)
            print(f"   ✅ Added divider for {label}")
        else:
            print(f"   ⚠️  WARNING: {label} not found!")
    
    print(f"\n   📊 Total chapters with dividers: {len(chapters_found)}/13")
    
    return html_content


def build_book():
    """Main build function"""
    
    print("=" * 70)
    print("THE GATEKEEPERS SOCIETY - V40 FINAL Production Build")
    print("=" * 70)
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Read master markdown
    print("\n📖 Reading master markdown...")
    if not MASTER_MD.exists():
        print(f"❌ ERROR: Master markdown not found at {MASTER_MD}")
        return False
    
    with open(MASTER_MD, 'r', encoding='utf-8') as f:
        master_content = f.read()
    
    print(f"   ✅ Loaded {len(master_content)} characters, {master_content.count(chr(10))} lines")
    
    # TOC already removed from source, no need to remove it here
    print("\n✅ Using clean markdown source (TOC already removed)")
    
    # Generate front matter
    print("\n📄 Generating front matter...")
    front_matter_html = generate_front_matter()
    print("   ✅ Title page created")
    
    # Generate TOC
    print("\n📋 Generating table of contents...")
    toc_html = generate_toc()
    print("   ✅ TOC created")
    
    # Convert markdown to HTML
    print("\n🔄 Converting markdown to HTML and adding chapter dividers...")
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
    <link rel="stylesheet" href="{CSS_FILE}">
</head>
<body>
{front_matter_html}
{toc_html}
{body_html}
</body>
</html>
"""
    
    # Save HTML for debugging
    html_file = BUILD_DIR / "THE_GATEKEEPERS_SOCIETY_V40_FINAL.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"   ✅ HTML saved to {html_file}")
    
    # Generate PDF
    print("\n📕 Generating PDF with WeasyPrint...")
    try:
        HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(
            OUTPUT_PDF,
            stylesheets=[str(CSS_FILE)]
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
        print("✅ BUILD COMPLETE - V40 FINAL ready for QA")
        print("=" * 70)
        sys.exit(0)
    else:
        print("\n" + "=" * 70)
        print("❌ BUILD FAILED")
        print("=" * 70)
        sys.exit(1)
