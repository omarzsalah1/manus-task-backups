# THE GATEKEEPERS SOCIETY V37 - REPLICATION MANIFEST

**Objective:** To bring a fresh clone of the V37 book source to the final, fixed, and compressed state. Execute these steps in order.

**Assumes:** You are in a sandbox with the original `manus-task-backups` repo cloned at `/home/ubuntu/manus-task-backups`.

---

### **STEP 1: INITIAL SETUP & FILE PREPARATION**

1.  **Copy the working directory:**

    ```shell
    cp -r /home/ubuntu/manus-task-backups/backups/2025-12-31_gatekeepers-v37-fixes/V37_FINAL_SOURCE /home/ubuntu/V37_WORKING
    ```

2.  **Copy the cover assets:** You will need the front and back cover images. Assuming they are in `/home/ubuntu/upload/`:

    ```shell
    cp /home/ubuntu/upload/GATEKEEPERS_FRONT_ANTIQUARIAN(2).png /home/ubuntu/V37_WORKING/book_source/design_assets/GATEKEEPERS_FRONT_ANTIQUARIAN.png
    cp /home/ubuntu/upload/GATEKEEPERS_BACK_ANTIQUARIAN(1).png /home/ubuntu/V37_WORKING/book_source/design_assets/GATEKEEPERS_BACK_ANTIQUARIAN.png
    ```

---

### **STEP 2: CSS MODIFICATIONS (CRITICAL - DO FIRST)**

Edit `/home/ubuntu/V37_WORKING/presidential_edition.css`. These changes are essential for layout fixes.

1.  **Add Full-Bleed Cover CSS:**

    *   **Find this block:**
        ```css
        @page {
            size: 6in 9in;
            /* ... more rules ... */
        }
        ```
    *   **Replace with this (adds the `@page cover` rule before the general `@page` rule):**
        ```css
        /* Cover page - full bleed, no margins, no page numbers */
        @page cover {
            size: 6in 9in;
            margin: 0;
            background-color: transparent;
            
            @bottom-center {
                content: none;
            }
        }

        @page {
            size: 6in 9in;
            margin-top: 0.625in;
            margin-bottom: 0.875in;
            margin-inside: 0.875in;
            margin-outside: 0.75in;
            background-color: var(--aged-cream);
            
            @bottom-center {
                content: counter(page);
                font-family: 'EB Garamond', serif;
                font-size: 9pt;
                color: var(--warm-gray);
                font-variant-numeric: oldstyle-nums;
            }
        }
        ```

2.  **Update Book Cover Styling:**

    *   **Find this block:**
        ```css
        .book-cover-page { /* ... */ }
        .book-cover { /* ... */ }
        ```
    *   **Replace with this:**
        ```css
        .book-cover-page {
            page: cover;
            page-break-after: always;
            margin: 0;
            padding: 0;
            width: 100vw;
            height: 100vh;
            position: relative;
        }

        .book-cover {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            margin: 0;
            padding: 0;
            display: block;
        }
        ```

3.  **Add Portrait Block Styling:**

    *   **Find this block:**
        ```css
        /* Portraits */
        .portrait { /* ... */ }
        ```
    *   **Replace with this:**
        ```css
        /* Portrait blocks - keep portrait + caption together, separate from body text */
        .portrait-block {
            page-break-before: always;
            page-break-after: always;
            page-break-inside: avoid;
            margin: 0;
            padding: 0.5in 0;
            text-align: center;
        }

        .portrait {
            max-width: 3.5in;
            height: auto;
            display: block;
            margin: 18pt auto;
            page-break-inside: avoid;
            page-break-after: avoid;
        }

        .portrait-caption {
            font-family: 'EB Garamond', serif;
            font-size: 9pt;
            font-style: italic;
            color: var(--warm-gray);
            text-align: center;
            margin: 12pt auto 0 auto;
            max-width: 4in;
            line-height: 1.4;
            page-break-before: avoid;
            page-break-inside: avoid;
        }
        ```

---

### **STEP 3: MARKDOWN MODIFICATIONS**

Run a single Python script to perform all text-based fixes on `/home/ubuntu/V37_WORKING/THE_GATEKEEPERS_SOCIETY_V37_MASTER.md`.

*   **Create and run this script:**

    ```python
    import re

    file_path = '/home/ubuntu/V37_WORKING/THE_GATEKEEPERS_SOCIETY_V37_MASTER.md'

    with open(file_path, 'r') as f:
        content = f.read()

    # Issue 1: TOC Spacing
    content = content.replace('# TABLE OF CONTENTS', '# TABLE OF\n# CONTENTS')

    # Issue 3, 9, 10, 17: Portrait Page Breaks
    # This is a structural change that is best done by ensuring the CSS is correct
    # and the portrait divs are wrapped in a 'portrait-block' div. The original markdown
    # already uses a consistent structure we can leverage.
    content = re.sub(r'(<div class=\
'portrait\"[^>]*>.*?</div>\s*</div>', r'<div class="portrait-block">\g<0></div>\n<div class="page-break"></div>', content, flags=re.DOTALL)

    # Issues 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16: Multiple text and artifact fixes
    lines = content.split('\n')
    new_lines = []
    skip_table = False

    for line in lines:
        # Skip artifacts
        if "Step 2: Assess" in line or "WHAT YOU NOW HAVE" in line:
            continue
        if "CHAPTER COMPLETION SUMMARY" in line:
            skip_table = True
            continue
        if skip_table and line.strip().startswith('|'):
            continue
        else:
            skip_table = False

        # Fix issues
        line = line.replace('↩', '')
        line = line.replace('[Acknowledgments placeholder - to be provided]', '<!-- Acknowledgments placeholder - to be provided -->')
        line = line.replace('[Bibliography placeholder - to be provided]', '<!-- Bibliography placeholder - to be provided -->')
        line = line.replace('## The Handoff', '') # Removes duplicate
        if line.strip() == "### Endnotes":
            continue
        if line.strip() == "# THE MACHINERY OF ACCESS":
            line = "## CHAPTER 8\n" + line

        # Remove orphaned captions
        if any(caption in line for caption in ["Trump Schedule Analysis", "Trump Late Night Tweets", "Administration Comparison Table", "Four Eras Timeline", "President Biden PDB"]):
            continue

        new_lines.append(line)

    content = '\n'.join(new_lines)

    with open(file_path, 'w') as f:
        f.write(content)

    print("Markdown fixes applied successfully.")

    ```

---

### **STEP 4: BUILD & COMPRESS THE PDF**

1.  **Update the build script:** The original build script needs to be told where to find the cover. Edit `/home/ubuntu/V37_WORKING/build_book_v19_presidential.py` and change the filename to `build_book_v20_with_cover.py`. Then, ensure the script correctly wraps the cover image.

    *   **Find:**
        ```python
        # This is a placeholder in the original script
        ```
    *   **Ensure it becomes:**
        ```python
        # Prepend the front cover
        front_cover_path = os.path.join(book_source_dir, 'design_assets', 'GATEKEEPERS_FRONT_ANTIQUARIAN.png')
        if os.path.exists(front_cover_path):
            front_cover_html = f'''<div class="book-cover-page"><img src="{front_cover_path}" class="book-cover"></div>'''
            html_content = front_cover_html + html_content

        # Append the back cover
        back_cover_path = os.path.join(book_source_dir, 'design_assets', 'GATEKEEPERS_BACK_ANTIQUARIAN.png')
        if os.path.exists(back_cover_path):
            back_cover_html = f'''<div class="book-cover-page"><img src="{back_cover_path}" class="book-cover"></div>'''
            html_content = html_content + back_cover_html
        ```

2.  **Install dependencies:**

    ```shell
    pip3 install -q weasyprint markdown
    sudo apt-get update -qq && sudo apt-get install -y ghostscript
    ```

3.  **Run the build script:**

    ```shell
    cd /home/ubuntu/V37_WORKING
    python3 build_book_v20_with_cover.py
    ```

4.  **Compress the final PDF:**

    ```shell
    cd /home/ubuntu/V37_WORKING
    gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=THE_GATEKEEPERS_SOCIETY_V37_FINAL_COMPRESSED.pdf THE_GATEKEEPERS_SOCIETY_V37_FIXED.pdf
    ```

---

**SUCCESS CRITERIA:** You will have a file named `THE_GATEKEEPERS_SOCIETY_V37_FINAL_COMPRESSED.pdf` in `/home/ubuntu/V37_WORKING/`. This PDF will have a full-bleed cover and all 17+ issues resolved.
