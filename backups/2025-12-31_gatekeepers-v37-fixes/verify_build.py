#!/usr/bin/env python3
"""
Gatekeepers Society Build Verification Script
Automatically verifies PDF build against V32 design standards
"""

import sys
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def check_mark(passed: bool) -> str:
    """Return colored check mark or X"""
    if passed:
        return f"{Colors.GREEN}✓{Colors.END}"
    return f"{Colors.RED}✗{Colors.END}"

def extract_text(pdf_path: Path) -> str:
    """Extract text from PDF using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error extracting text from PDF: {e}{Colors.END}")
        sys.exit(1)

def get_pdf_info(pdf_path: Path) -> Dict[str, any]:
    """Get PDF metadata using pdfinfo"""
    try:
        result = subprocess.run(
            ['pdfinfo', str(pdf_path)],
            capture_output=True,
            text=True,
            check=True
        )
        info = {}
        for line in result.stdout.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()
        return info
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error getting PDF info: {e}{Colors.END}")
        sys.exit(1)

def count_pages(pdf_path: Path) -> int:
    """Count pages in PDF"""
    info = get_pdf_info(pdf_path)
    return int(info.get('Pages', 0))

def get_file_size_mb(pdf_path: Path) -> float:
    """Get file size in MB"""
    return pdf_path.stat().st_size / (1024 * 1024)

def check_structure(text: str) -> Tuple[bool, List[str]]:
    """Check document structure (Prologue, Chapters, Epilogue)"""
    issues = []
    passed = True
    
    # Check for Prologue
    if not re.search(r'^PROLOGUE', text, re.MULTILINE):
        issues.append("Prologue not found")
        passed = False
    
    # Check for all 11 chapters
    for i in range(1, 12):
        if not re.search(rf'^CHAPTER {i}\b', text, re.MULTILINE):
            issues.append(f"Chapter {i} not found")
            passed = False
    
    # Check for Epilogue
    if not re.search(r'^EPILOGUE', text, re.MULTILINE):
        issues.append("Epilogue not found")
        passed = False
    
    return passed, issues

def check_artifacts(text: str) -> Tuple[bool, List[str]]:
    """Check for manuscript artifacts that should be removed"""
    issues = []
    
    # Check for word counts
    word_counts = re.findall(r'[Ww]ord [Cc]ount:?\s*\d+', text)
    if word_counts:
        issues.append(f"Found {len(word_counts)} word count lines")
    
    # Check for end markers
    end_markers = re.findall(r'\[?END OF CHAPTER', text, re.IGNORECASE)
    if end_markers:
        issues.append(f"Found {len(end_markers)} end of chapter markers")
    
    # Check for source file citations (.md files)
    source_files = re.findall(r'\w+\.md\b', text)
    # Filter out legitimate references (like in URLs)
    source_files = [f for f in source_files if not any(x in f.lower() for x in ['readme', 'changelog'])]
    if source_files:
        issues.append(f"Found {len(source_files)} source file citations")
    
    # Check for validation text
    validation_text = re.findall(r'Verification:\s*[✓✗]', text)
    if validation_text:
        issues.append(f"Found {len(validation_text)} validation text instances")
    
    # Check for "Clock-star motif" text (should be image, not text)
    clock_star_text = re.findall(r'Clock-star motif', text)
    if clock_star_text:
        issues.append(f"Found {len(clock_star_text)} 'Clock-star motif' text placeholders (should be images)")
    
    passed = len(issues) == 0
    return passed, issues

def check_elements(text: str) -> Tuple[bool, List[str]]:
    """Check for expected elements (clock-stars, dividers, etc.)"""
    issues = []
    passed = True
    
    # Count diamond dividers
    diamonds = text.count('◆')
    if diamonds < 13:  # At least 13 for Prologue + 11 Chapters + Epilogue
        issues.append(f"Only {diamonds} diamond dividers found (expected at least 13)")
        passed = False
    
    # Check for Table of Contents
    if 'CONTENTS' not in text and 'TABLE OF CONTENTS' not in text:
        issues.append("Table of Contents not found")
        passed = False
    
    # Check for Endnotes
    if 'Endnotes' not in text and 'ENDNOTES' not in text:
        issues.append("Endnotes section not found")
        passed = False
    
    return passed, issues

def check_file_size(pdf_path: Path) -> Tuple[bool, List[str]]:
    """Check if file size is reasonable"""
    issues = []
    size_mb = get_file_size_mb(pdf_path)
    
    if size_mb > 150:
        issues.append(f"File size very large: {size_mb:.1f} MB (consider optimization)")
    elif size_mb > 100:
        issues.append(f"File size large: {size_mb:.1f} MB (may need optimization)")
    
    passed = size_mb <= 150
    return passed, issues

def print_section(title: str):
    """Print section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_result(check_name: str, passed: bool, issues: List[str] = None):
    """Print check result"""
    mark = check_mark(passed)
    print(f"{mark} {check_name}")
    if issues:
        for issue in issues:
            print(f"  {Colors.YELLOW}→{Colors.END} {issue}")

def main():
    """Main verification function"""
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    
    if not pdf_path.exists():
        print(f"{Colors.RED}Error: PDF file not found: {pdf_path}{Colors.END}")
        sys.exit(1)
    
    print(f"\n{Colors.BOLD}Gatekeepers Society Build Verification{Colors.END}")
    print(f"PDF: {pdf_path.name}")
    print(f"Date: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}")
    
    # Extract text
    print(f"\n{Colors.BLUE}Extracting text from PDF...{Colors.END}")
    text = extract_text(pdf_path)
    
    # Basic info
    print_section("BASIC INFORMATION")
    page_count = count_pages(pdf_path)
    file_size = get_file_size_mb(pdf_path)
    print(f"Pages: {page_count}")
    print(f"File Size: {file_size:.2f} MB")
    print(f"Text Length: {len(text):,} characters")
    
    # Structure checks
    print_section("STRUCTURE VERIFICATION")
    passed_structure, structure_issues = check_structure(text)
    print_result("Document Structure (Prologue + 11 Chapters + Epilogue)", passed_structure, structure_issues)
    
    # Artifact checks
    print_section("MANUSCRIPT ARTIFACT CHECK")
    passed_artifacts, artifact_issues = check_artifacts(text)
    print_result("No Manuscript Artifacts", passed_artifacts, artifact_issues)
    
    # Element checks
    print_section("ELEMENT VERIFICATION")
    passed_elements, element_issues = check_elements(text)
    print_result("Required Elements Present", passed_elements, element_issues)
    
    # File size check
    print_section("FILE SIZE CHECK")
    passed_size, size_issues = check_file_size(pdf_path)
    print_result("File Size Reasonable", passed_size, size_issues)
    
    # Summary
    print_section("SUMMARY")
    all_passed = passed_structure and passed_artifacts and passed_elements and passed_size
    
    if all_passed:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ ALL CHECKS PASSED{Colors.END}")
        print(f"\n{Colors.GREEN}The PDF appears to meet basic quality standards.{Colors.END}")
        print(f"{Colors.YELLOW}Note: This script checks content only. Visual design verification requires manual inspection.{Colors.END}")
        return 0
    else:
        print(f"{Colors.RED}{Colors.BOLD}✗ SOME CHECKS FAILED{Colors.END}")
        print(f"\n{Colors.RED}Please review the issues above and fix before proceeding.{Colors.END}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
