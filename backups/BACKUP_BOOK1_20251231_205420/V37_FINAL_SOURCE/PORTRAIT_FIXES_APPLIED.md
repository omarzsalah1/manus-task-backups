# PORTRAIT FIXES APPLIED - V37

**Date:** December 31, 2025  
**Version:** V37 Fixed (507 pages, 127 MB)

---

## 🎯 ISSUES IDENTIFIED

User reported three portrait problems:

1. **Validation text visible** - Captions showed "**Verification:** ✅" markers
2. **Source citations visible** - Text like "(Getty source)", "(Alamy source)" in captions
3. **Portraits not fitting on page** - Images + captions split across pages

---

## ✅ FIXES APPLIED

### Fix 1: Removed Validation Text
**Pattern removed:**
```
**Verification:** ✅ [any descriptive text]
```

**Regex used:**
```python
content = re.sub(r'\*\*Verification:\*\*\s*✅[^<]*?(?=</div>|$)', '', content, flags=re.DOTALL)
```

**Result:** All 18 portrait captions now clean, no validation markers visible.

---

### Fix 2: Removed Source Citations
**Patterns removed:**
- (Getty source)
- (Alamy source)
- (Miller Center source)
- (Reddit/NBC source)
- Any variation with "source" in parentheses

**Regex used:**
```python
content = re.sub(r'\([^)]*(?:Getty|Alamy|Miller Center|Reddit|NBC)[^)]*source\)', '', content, flags=re.IGNORECASE)
```

**Result:** Captions now show only the narrative content, no technical source details.

---

### Fix 3: Shrunk Images for Page Fit
**Change:**
- Old: `width: 3.5in`
- New: `width: 3.0in`

**Regex used:**
```python
content = re.sub(r'width:\s*3\.5in', 'width: 3.0in', content)
```

**Result:** Images now smaller, leaving more room for captions on same page.

---

### Fix 4: Added Page-Break Protection
**Added CSS:**
```css
page-break-inside: avoid;
max-height: 8in;
```

**Applied to:**
```html
<div class="portrait" style="page-break-inside: avoid; max-height: 8in;">
```

**Result:** WeasyPrint now keeps portrait + caption together on one page.

---

## 📊 BEFORE/AFTER COMPARISON

### Before (V37 With Images - 510 pages)
```html
<div class="portrait">
  <img src="book_source/portraits/08_james_baker_reagan_CORRECT.png" style="width: 3.5in;">
  <div class="portrait-caption">
    <strong>James Baker III with President Ronald Reagan, 1981–1985</strong> 
    Baker ran George H.W. Bush's campaign against Reagan, then became Reagan's 
    Chief of Staff anyway. He turned the role into a power center by mastering 
    the one thing Chiefs control absolutely: access. *The President's time is 
    the only currency in Washington that never inflates.* 
    **Verification:** ✅ Shows Baker with Reagan in Oval Office by fireplace 
    (Alamy source)
  </div>
</div>
```

### After (V37 Fixed - 507 pages)
```html
<div class="portrait" style="page-break-inside: avoid; max-height: 8in;">
  <img src="book_source/portraits/08_james_baker_reagan_CORRECT.png" style="width: 3.0in;">
  <div class="portrait-caption">
    <strong>James Baker III with President Ronald Reagan, 1981–1985</strong> 
    Baker ran George H.W. Bush's campaign against Reagan, then became Reagan's 
    Chief of Staff anyway. He turned the role into a power center by mastering 
    the one thing Chiefs control absolutely: access. <em>The President's time is 
    the only currency in Washington that never inflates.</em>
  </div>
</div>
```

**Changes:**
- ✅ Width reduced: 3.5in → 3.0in
- ✅ Validation text removed
- ✅ Source citation removed
- ✅ Page-break protection added
- ✅ Max-height constraint added
- ✅ Markdown italic `*` converted to HTML `<em>`

---

## 📈 IMPACT ON DOCUMENT

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Pages** | 510 | 507 | -3 pages |
| **File Size** | 126.3 MB | 127 MB | +0.7 MB |
| **Portraits** | 18 | 18 | Same |
| **Caption Quality** | ❌ Technical artifacts | ✅ Clean narrative | Fixed |
| **Page Breaks** | ❌ Split across pages | ✅ Kept together | Fixed |

---

## ✅ VERIFICATION

**All 18 portraits verified:**
1. Sherman Adams - ✅ Clean caption, page fit
2. H.R. Haldeman - ✅ Clean caption, page fit
3. Donald Rumsfeld - ✅ Clean caption, page fit
4. Dick Cheney - ✅ Clean caption, page fit
5. Hamilton Jordan - ✅ Clean caption, page fit
6. James Baker - ✅ Clean caption, page fit
7. John Sununu - ✅ Clean caption, page fit
8. Leon Panetta - ✅ Clean caption, page fit
9. Erskine Bowles - ✅ Clean caption, page fit
10. John Podesta - ✅ Clean caption, page fit
11. Andrew Card - ✅ Clean caption, page fit
12. Joshua Bolten - ✅ Clean caption, page fit
13. Rahm Emanuel - ✅ Clean caption, page fit
14. William Daley - ✅ Clean caption, page fit
15. Jack Lew - ✅ Clean caption, page fit
16. Denis McDonough - ✅ Clean caption, page fit
17. Reince Priebus - ✅ Clean caption, page fit
18. John Kelly - ✅ Clean caption, page fit

---

## 🎯 NEXT STEPS

**Portrait fixes complete.** Waiting for user decisions on:

1. **Chapter 11** - Renumber Chapter 12 → 11?
2. **Starting point** - Use this V37 Fixed (507p)?
3. **Golden divider** - Where is the file?

Once these are provided, proceed with full design brief implementation:
- Delete manuscript artifacts
- Fix duplicate chapter titles
- Replace 200 section breaks with golden divider
- Add Table of Contents
- Add back matter
- Final QA and delivery

---

**Status:** ✅ PORTRAIT FIXES COMPLETE - READY FOR NEXT PHASE
