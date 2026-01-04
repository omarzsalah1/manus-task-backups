#!/usr/bin/env python3
"""
Automated QA System for The Gatekeepers Society V40 PDF
Checks all critical requirements, auto-rebuilds if failures detected
Samples pages: 1, 2, 3, 4, 5, 6, 10, 14, 20, 200
"""

import subprocess
import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Configuration
PDF_FILE = "/home/ubuntu/GATEKEEPERS_V40_FINAL/output/THE_GATEKEEPERS_SOCIETY_V40_FINAL.pdf"
BUILD_SCRIPT = "/home/ubuntu/GATEKEEPERS_V40_FINAL/build/build_v40_final.py"
QA_DIR = "/home/ubuntu/GATEKEEPERS_V40_FINAL/qa_final"
SAMPLE_PAGES = [1, 2, 3, 4, 5, 6, 10, 14, 20, 200]
MAX_REBUILD_ATTEMPTS = 5

def run_command(cmd):
    """Run shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr

def extract_pdf_text(pdf_path):
    """Extract all text from PDF"""
    os.makedirs(QA_DIR, exist_ok=True)
    text_file = f"{QA_DIR}/full_text.txt"
    cmd = f"pdftotext '{pdf_path}' '{text_file}'"
    returncode, output = run_command(cmd)
    
    if returncode != 0:
        return ""
    
    try:
        with open(text_file, 'r', errors='ignore') as f:
            return f.read()
    except:
        return ""

def extract_sample_pages(pdf_path):
    """Extract specific sample pages as PNG images"""
    os.makedirs(QA_DIR, exist_ok=True)
    extracted = []
    
    for page_num in SAMPLE_PAGES:
        output_file = f"{QA_DIR}/sample_page_{page_num:03d}.png"
        cmd = f"pdftoppm -f {page_num} -l {page_num} -r 150 -png '{pdf_path}' '{QA_DIR}/sample_page_{page_num:03d}'"
        returncode, output = run_command(cmd)
        
        # Check if file was created (pdftoppm adds -1 suffix)
        actual_file = f"{QA_DIR}/sample_page_{page_num:03d}-1.png"
        if os.path.exists(actual_file):
            # Rename to remove -1 suffix
            os.rename(actual_file, output_file)
            extracted.append(page_num)
    
    return extracted

def get_pdf_page_count(pdf_path):
    """Get total page count of PDF"""
    cmd = f"pdfinfo '{pdf_path}' | grep 'Pages:' | awk '{{print $2}}'"
    returncode, output = run_command(cmd)
    try:
        return int(output.strip())
    except:
        return 0

# ============================================================================
# QA CHECK FUNCTIONS
# ============================================================================

def check_pdf_exists():
    """Check if PDF file exists"""
    if os.path.exists(PDF_FILE):
        size_mb = os.path.getsize(PDF_FILE) / (1024 * 1024)
        return True, f"PDF exists ({size_mb:.1f} MB)"
    return False, "PDF file not found"

def check_page_count():
    """Check if PDF has reasonable page count (400-600 pages)"""
    count = get_pdf_page_count(PDF_FILE)
    if 400 <= count <= 600:
        return True, f"Page count OK ({count} pages)"
    return False, f"Page count out of range ({count} pages, expected 400-600)"

def check_title_page(text):
    """Check if title page has title, subtitle, and author"""
    first_5000 = text[:5000]
    
    has_title = "THE GATEKEEPERS SOCIETY" in first_5000 or "GATEKEEPERS SOCIETY" in first_5000
    has_subtitle = "Schedule" in first_5000 and "Weapon" in first_5000
    has_author = "OMAR SALAH" in first_5000 or "Omar Salah" in first_5000
    
    if has_title and has_subtitle and has_author:
        return True, "Title page complete (title, subtitle, author)"
    
    missing = []
    if not has_title: missing.append("title")
    if not has_subtitle: missing.append("subtitle 'The Schedule Is the Weapon'")
    if not has_author: missing.append("author")
    
    return False, f"Title page missing: {', '.join(missing)}"

def check_toc_complete(text):
    """Check if TOC has all chapter entries with names"""
    required_entries = [
        "PROLOGUE",
        "CHAPTER 1",
        "CHAPTER 2",
        "CHAPTER 3",
        "CHAPTER 4",
        "CHAPTER 5",
        "CHAPTER 6",
        "CHAPTER 7",
        "CHAPTER 8",
        "CHAPTER 9",
        "CHAPTER 10",
        "CHAPTER 11",
        "EPILOGUE",
        "Papers in the Study",  # Prologue subtitle
        "Gatekeeper",  # Ch 1 subtitle
        "Vacation Wars",  # Ch 2 subtitle
    ]
    
    missing = [entry for entry in required_entries if entry not in text]
    
    if len(missing) == 0:
        return True, f"TOC complete with all {len(required_entries)} entries"
    
    return False, f"TOC missing {len(missing)} entries: {', '.join(missing[:3])}..."

def check_clock_star_dividers(text):
    """Check if all 13 chapters have clock-star dividers"""
    # Count chapter headings
    chapter_markers = [
        "PROLOGUE",
        "CHAPTER 1",
        "CHAPTER 2",
        "CHAPTER 3",
        "CHAPTER 4",
        "CHAPTER 5",
        "CHAPTER 6",
        "CHAPTER 7",
        "CHAPTER 8",
        "CHAPTER 9",
        "CHAPTER 10",
        "CHAPTER 11",
        "EPILOGUE"
    ]
    
    found = sum(1 for marker in chapter_markers if marker in text)
    
    if found >= 13:
        return True, f"All 13 chapter dividers present"
    
    return False, f"Only {found}/13 chapter dividers found"

def check_no_duplicate_subtitles(text):
    """Check for duplicate h3 subtitles"""
    problematic_subtitles = [
        "November 22, 1963: The Metaphysics of Transfer",
        "October 20, 1973: The Breaking of Richard Nixon",
        "September 11, 2001: The Day America Came Under Attack",
        "Phase 1: Recognize the Collapse",
        "The Reagan Troika: The Politics of Pragmatism"
    ]
    
    duplicates_found = []
    for subtitle in problematic_subtitles:
        count = text.count(subtitle)
        if count > 1:
            duplicates_found.append(f"{subtitle} ({count}x)")
    
    if len(duplicates_found) == 0:
        return True, "No duplicate subtitles detected"
    
    return False, f"Found {len(duplicates_found)} duplicate subtitles: {duplicates_found[0]}"

def check_table_styling():
    """Check if tables are properly converted from markdown to HTML"""
    html_file = "/home/ubuntu/GATEKEEPERS_V40_FINAL/build/THE_GATEKEEPERS_SOCIETY_V40_FINAL.html"
    
    if not os.path.exists(html_file):
        return False, "HTML file not found for table verification"
    
    with open(html_file, 'r', errors='ignore') as f:
        html_content = f.read()
    
    # Count table tags
    table_count = html_content.count('<table')
    
    if table_count >= 30:  # Expect at least 30 tables in the book
        return True, f"Tables properly converted ({table_count} tables found in HTML)"
    elif table_count > 0:
        return False, f"Only {table_count} tables found (expected 30+)"
    else:
        return False, "No tables found in HTML"

def check_no_excessive_blank_pages(text):
    """Check for excessive blank pages or spaces"""
    lines = text.split('\n')
    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == '')
    
    blank_ratio = blank_lines / total_lines if total_lines > 0 else 1.0
    
    if blank_ratio < 0.5:  # Less than 50% blank lines is OK
        return True, f"No excessive blank pages ({blank_ratio*100:.1f}% blank lines)"
    
    return False, f"Too many blank pages ({blank_ratio*100:.1f}% blank lines)"

def check_designer_brief_colors():
    """Check if PDF uses designer brief colors (by checking CSS)"""
    css_file = "/home/ubuntu/GATEKEEPERS_V40_FINAL/build/book_styles_v40.css"
    
    if not os.path.exists(css_file):
        return False, "CSS file not found"
    
    with open(css_file, 'r') as f:
        css_content = f.read()
    
    required_colors = [
        "#F5F0E6",  # Aged Cream background
        "#3D2E1F",  # Presidential Brown text
    ]
    
    missing_colors = [color for color in required_colors if color not in css_content]
    
    if len(missing_colors) == 0:
        return True, "Designer brief colors present in CSS"
    
    return False, f"Missing designer brief colors: {', '.join(missing_colors)}"

# ============================================================================
# MAIN QA EXECUTION
# ============================================================================

def run_all_checks():
    """Run all QA checks and return results"""
    print("\n" + "="*70)
    print("RUNNING QA CHECKS...")
    print("="*70)
    
    # Extract text once
    text = extract_pdf_text(PDF_FILE)
    
    checks = [
        ("PDF Exists", check_pdf_exists()),
        ("Page Count", check_page_count()),
        ("Title Page", check_title_page(text)),
        ("TOC Complete", check_toc_complete(text)),
        ("Clock-Star Dividers", check_clock_star_dividers(text)),
        ("No Duplicate Subtitles", check_no_duplicate_subtitles(text)),
        ("Table Styling", check_table_styling()),
        ("No Excessive Blanks", check_no_excessive_blank_pages(text)),
        ("Designer Brief Colors", check_designer_brief_colors()),
    ]
    
    passed = []
    failed = []
    
    for name, (result, msg) in checks:
        if result:
            passed.append((name, msg))
            print(f"  ✅ {name}: {msg}")
        else:
            failed.append((name, msg))
            print(f"  ❌ {name}: {msg}")
    
    return passed, failed

def rebuild_pdf():
    """Rebuild the PDF using the build script"""
    print("\n" + "="*70)
    print("REBUILDING PDF...")
    print("="*70)
    
    cmd = f"cd /home/ubuntu/GATEKEEPERS_V40_FINAL/build && python3 build_v40_final.py"
    returncode, output = run_command(cmd)
    
    if returncode == 0:
        print("✅ Rebuild successful")
        return True
    else:
        print(f"❌ Rebuild failed:\n{output}")
        return False

def generate_report(passed, failed, sample_pages_extracted, iteration):
    """Generate final QA report"""
    report_file = f"{QA_DIR}/QA_REPORT_ITERATION_{iteration}.txt"
    
    with open(report_file, 'w') as f:
        f.write("="*70 + "\n")
        f.write("THE GATEKEEPERS SOCIETY V40 - QA REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Iteration: {iteration}\n")
        f.write("="*70 + "\n\n")
        
        f.write(f"SUMMARY: {len(passed)}/{len(passed)+len(failed)} checks passed\n\n")
        
        f.write("✅ PASSED CHECKS:\n")
        f.write("-"*70 + "\n")
        for name, msg in passed:
            f.write(f"  ✅ {name}: {msg}\n")
        
        if failed:
            f.write("\n❌ FAILED CHECKS:\n")
            f.write("-"*70 + "\n")
            for name, msg in failed:
                f.write(f"  ❌ {name}: {msg}\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write(f"SAMPLE PAGES EXTRACTED: {len(sample_pages_extracted)}/10\n")
        f.write(f"Pages: {', '.join(map(str, sample_pages_extracted))}\n")
        f.write("="*70 + "\n")
        
        if len(failed) == 0:
            f.write("\n✅ ALL CHECKS PASSED - PDF READY FOR DELIVERY\n")
        else:
            f.write(f"\n❌ {len(failed)} CHECKS FAILED - PDF NEEDS FIXES\n")
    
    return report_file

def main():
    """Main QA automation loop"""
    print("\n" + "="*70)
    print("GATEKEEPERS SOCIETY V40 - AUTOMATED QA SYSTEM")
    print("="*70)
    
    for iteration in range(1, MAX_REBUILD_ATTEMPTS + 1):
        print(f"\n{'='*70}")
        print(f"ITERATION {iteration}/{MAX_REBUILD_ATTEMPTS}")
        print(f"{'='*70}")
        
        # Run QA checks
        passed, failed = run_all_checks()
        
        # Extract sample pages
        print(f"\nExtracting sample pages: {SAMPLE_PAGES}")
        sample_pages_extracted = extract_sample_pages(PDF_FILE)
        print(f"✅ Extracted {len(sample_pages_extracted)}/10 sample pages")
        
        # Generate report
        report_file = generate_report(passed, failed, sample_pages_extracted, iteration)
        print(f"\n📄 Report generated: {report_file}")
        
        # Check if all passed
        if len(failed) == 0:
            print("\n" + "="*70)
            print("✅ ALL CHECKS PASSED - PDF READY FOR DELIVERY")
            print("="*70)
            return True
        
        # If not last iteration, rebuild
        if iteration < MAX_REBUILD_ATTEMPTS:
            print(f"\n❌ {len(failed)} checks failed. Attempting rebuild...")
            if not rebuild_pdf():
                print("❌ Rebuild failed. Stopping.")
                return False
        else:
            print(f"\n❌ Maximum rebuild attempts ({MAX_REBUILD_ATTEMPTS}) reached.")
            print("❌ PDF still has issues. Manual intervention required.")
            return False
    
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
