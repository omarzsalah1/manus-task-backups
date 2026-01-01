# FLORENCE FOR ISAAC HEALTH - REDLINE MANIFEST
## Complete Design Change Specifications v7 → v8

**Document Date:** December 30, 2025  
**Prepared for:** Design Team  
**Presentation:** Florence_for_Isaac_Health_(7).pptx  
**Slide Dimensions:** 10.00" × 5.62" (16:9)

---

## EXECUTIVE SUMMARY

Three categories of changes required:

| Priority | Change | Slides Affected |
|----------|--------|-----------------|
| 1 | Tagline text replacement | Slide 1 |
| 2 | Shield logo resize + reposition | Slides 2-19 (18 slides) |
| 3 | Florence Copilot sidebar redesign | Slide 13 |

---

# CHANGE 1: TITLE SLIDE TAGLINE

## Location
- **Slide:** 1 (Title Slide)
- **Position:** (0.50", 3.35")
- **Text Box Size:** 4.05" × 0.70"

## Current State
```
"Specialist dementia care in days, not years—scaling your 4:1 ROI with 24/7 AI support"
```

## Required Change
```
"Your Care Team's Force Multiplier—24/7 between-visit support"
```

## Rationale
The current tagline incorrectly positions Florence as providing dementia care. Isaac Health already provides specialist dementia care—Florence augments their care navigators as a force multiplier. The new tagline correctly frames Florence as extending their existing team's reach.

## Formatting
- Preserve existing font family, size, color, and styling
- Maintain text box position and dimensions
- Keep italic styling if present

---

# CHANGE 2: NIGHTINGALE SHIELD LOGO

## Current State (Typical)
| Property | Value |
|----------|-------|
| Position | (9.15", 5.08") |
| Size | 0.35" × 0.39" |
| Location | Bottom-right corner |

## Required Change
| Property | Current | New |
|----------|---------|-----|
| Width | 0.35" | **0.22"** |
| Height | 0.39" | **0.25"** |
| Left | 9.15" | **9.50"** |
| Top | 5.08" | **5.22"** |

## Affected Slides

| Slide | Current Position | Current Size | Action |
|-------|-----------------|--------------|--------|
| 2 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 3 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 4 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 5 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 6 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 7 | (9.15", 5.12") | 0.35" × 0.39" | Resize & reposition |
| 8 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 9 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 10 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 11 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 12 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 13 | (9.18", 5.17") | 0.32" × 0.36" | Resize & reposition |
| 14 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 15 | (9.25", 5.25") | 0.25" × 0.28" | Already correct |
| 16 | (9.15", 5.14") | 0.35" × 0.39" | Resize & reposition |
| 17 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 18 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |
| 19 | (9.15", 5.08") | 0.35" × 0.39" | Resize & reposition |

## Rationale
- Current logo size overlaps with content on several slides (especially slides 6, 10, 11, 14, 18 with graphics in lower-right)
- Smaller size maintains brand presence without visual interference
- Consistent positioning ensures uniform appearance across deck

## Special Attention Slides
These slides have content near the bottom-right that may conflict:
- **Slide 6:** Three-way call diagram
- **Slide 10:** Three pathways graphic
- **Slide 11:** Behavioral coaching visual
- **Slide 14:** Lower-right content
- **Slide 18:** Graphics in corner area

---

# CHANGE 3: FLORENCE COPILOT SIDEBAR (SLIDE 13)

## Overview
Complete redesign of the Florence Copilot sidebar mockup to show richer, more realistic functionality including Care Gaps tracking, Visit History, and AI Assistant capabilities.

## Current State

### Existing Sidebar Content
```
Florence
AI Care Coordinator
─────────────────────
Patient Context
Auto-loaded from EHR
─────────────────────
Recent Calls
3 check-ins this week
─────────────────────
Escalations
None pending
─────────────────────
[▶ Launch Call]
```

**Problems with current design:**
1. Too generic—doesn't show Florence's clinical intelligence
2. Missing Care Gaps functionality (key differentiator)
3. No Visit History panel
4. No AI Assistant interaction capability
5. Doesn't demonstrate HEDIS/Stars measure tracking

---

## Required New Design

### Overall Structure
```
┌─────────────────────────────────────┐
│ 🩺 Florence Copilot          [HEADER]
├─────────────────────────────────────┤
│ CARE GAPS TO ADDRESS            (5) │
│ ☐ A1C Control      [NEEDS IMPROVEMENT]
│   Last A1C 7.8% (target <7.0%)      │
│   ⚠️ Triple Weighted                │
│ ☐ Diabetic Eye Exam       [OVERDUE] │
│   Screening overdue 11 months       │
│ ☐ Medication Adherence        [DUE] │
│ ☐ Blood Pressure Control      [DUE] │
│ ☐ Flu Vaccine                 [DUE] │
├─────────────────────────────────────┤
│ VISIT HISTORY                  (10) │
│ PCP                      2025-11-10 │
│   CHF follow-up; med reconciliation │
│ Endocrinology            2025-10-22 │
│   Diabetes control; A1C ordered     │
│ Cardiology               2025-09-30 │
│   Routine CHF; stable on meds       │
├─────────────────────────────────────┤
│ ✨ AI Assistant                     │
│ Ask me anything about Margaret's    │
│ care                                │
│ ┌─────────────────────────────────┐ │
│ │ 💬 Ask about patient care...    │ │
│ └─────────────────────────────────┘ │
├─────────────────────────────────────┤
│        [▶ Launch Call]              │
└─────────────────────────────────────┘
```

---

## Detailed Specifications

### Header Bar
| Property | Value |
|----------|-------|
| Background | Linear gradient: #E86850 → #d45a44 (coral) |
| Height | 48px |
| Icon | Medical stethoscope 🩺 in rounded square |
| Icon Background | rgba(255,255,255,0.2) |
| Icon Size | 26px × 26px |
| Title | "Florence Copilot" |
| Title Font | 16px, semibold, white |
| Padding | 14px 16px |

### Section Headers
| Property | Value |
|----------|-------|
| Background | #fafafa |
| Font | 11px, bold, uppercase |
| Letter Spacing | 0.5px |
| Color | #333333 |
| Padding | 12px 14px 8px |
| Count Badge | Coral (#E86850) background, white text, 10px bold |

### Care Gaps Panel

#### Item Structure
Each care gap item contains:
1. **Checkbox** (unchecked state)
   - Size: 16px × 16px
   - Border: 2px solid #cccccc
   - Border Radius: 3px
   
2. **Gap Title** (inline with status badge)
   - Font: 12px, semibold, #222222
   
3. **Status Badge** (right-aligned on title line)
   
4. **Description** (below title)
   - Font: 10px, #666666
   - Line Height: 1.35
   
5. **Triple Weighted Warning** (if applicable)
   - Font: 9px, semibold, #E86850
   - Icon: ⚠️
   - Text: "Triple Weighted"

#### Status Badge Colors

| Status | Background | Text | Use Case |
|--------|-----------|------|----------|
| NEEDS IMPROVEMENT | #fef3cd | #856404 | Measure not meeting target |
| OVERDUE | #f8d7da | #721c24 | Past due date |
| DUE | #cce5ff | #004085 | Coming due |
| COMPLETE | #d4edda | #155724 | Measure satisfied |

#### Badge Styling
- Font: 8px, bold, uppercase
- Padding: 2px 5px
- Border Radius: 2px
- Letter Spacing: 0.2px

#### Sample Care Gap Items

**Item 1: A1C Control**
- Status: NEEDS IMPROVEMENT (yellow)
- Description: "Last A1C was 7.8% (target <7.0%). Discuss diet and lifestyle."
- Flag: ⚠️ Triple Weighted

**Item 2: Diabetic Eye Exam**
- Status: OVERDUE (red/pink)
- Description: "Screening overdue by 11 months. Last: 2023-01-15"

**Item 3: Medication Adherence**
- Status: DUE (blue)
- Description: "Review medications, side effects, adherence barriers."

**Item 4: Blood Pressure Control**
- Status: DUE (blue)
- Description: "BP slightly elevated. Review adherence and lifestyle."

### Visit History Panel

#### Item Structure
Each visit item contains:
1. **Visit Type** (left)
   - Font: 12px, semibold, #333333
   
2. **Description** (below type)
   - Font: 10px, #777777
   
3. **Date** (right-aligned)
   - Font: 10px, #999999
   - Format: YYYY-MM-DD

#### Sample Visit Items

| Type | Description | Date |
|------|-------------|------|
| PCP | CHF follow-up; med reconciliation | 2025-11-10 |
| Endocrinology | Diabetes control; A1C ordered | 2025-10-22 |
| Cardiology | Routine CHF; stable on meds | 2025-09-30 |

### AI Assistant Section

| Property | Value |
|----------|-------|
| Background | Linear gradient: #f8fffe → #f0faf9 (light teal) |
| Padding | 12px 14px |

#### Components
1. **Header Row**
   - Icon: ✨ in teal circle (#4A9B9B), 18px
   - Title: "AI Assistant", 11px bold, #4A9B9B

2. **Prompt Text**
   - Text: "Ask me anything about Margaret's care"
   - Font: 11px, #4A9B9B

3. **Input Field**
   - Background: white
   - Border: 1px solid #dddddd
   - Border Radius: 6px
   - Padding: 8px 10px
   - Placeholder: "💬 Ask about patient care..."
   - Font: 11px, #999999

### Launch Call Button

| Property | Value |
|----------|-------|
| Background | Linear gradient: #4A9B9B → #3d8585 |
| Color | White |
| Font | 12px, semibold |
| Padding | 10px 16px |
| Border Radius | 6px |
| Margin | 12px 14px 14px |
| Width | calc(100% - 28px) |
| Box Shadow | 0 2px 8px rgba(74, 155, 155, 0.3) |
| Content | "▶ Launch Call" |

---

## Composite Layout (Browser + Sidebar)

The slide should show the Florence sidebar alongside Isaac Health's platform:

### Left Panel: Isaac Health Platform (Simulated)
| Property | Value |
|----------|-------|
| Width | ~55% of mockup area |
| Browser Chrome | macOS style (red/yellow/green dots) |
| URL Bar | "care.isaachealth.com/patients" |

#### Platform Content
- Header: "Isaac Health Care Platform" (teal: #4A9B9B)
- Patient Card: "Patient: Margaret Chen"
- Subtext: "ID: 78294 • Age: 78 • Dx: Alzheimer's"
- Info Sections: Last Contact, Care Plan, Alerts

### Right Panel: Florence Copilot Sidebar
| Property | Value |
|----------|-------|
| Width | ~45% of mockup area (~350px equivalent) |
| Full specification | As detailed above |

---

## Complete Color Reference

### Brand Colors
| Name | Hex | Usage |
|------|-----|-------|
| Florence Coral | #E86850 | Header, badges, accents |
| Florence Coral Dark | #d45a44 | Gradient end |
| NightingaleMD Teal | #4A9B9B | Buttons, AI section, links |
| NightingaleMD Teal Dark | #3d8585 | Button gradient end |

### Status Colors
| Status | Background | Text |
|--------|-----------|------|
| Needs Improvement | #fef3cd | #856404 |
| Overdue | #f8d7da | #721c24 |
| Due | #cce5ff | #004085 |
| Complete | #d4edda | #155724 |

### Neutral Colors
| Name | Hex | Usage |
|------|-----|-------|
| Text Primary | #222222 | Titles, important text |
| Text Secondary | #333333 | Section headers |
| Text Muted | #666666 | Descriptions |
| Text Light | #999999 | Dates, placeholders |
| Border | #dddddd | Input borders |
| Divider | #eeeeee | Section dividers |
| Background | #fafafa | Section headers |

---

## Typography

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Sidebar Title | 16px | 600 (semibold) | White |
| Section Header | 11px | 700 (bold) | #333333 |
| Item Title | 12px | 600 (semibold) | #222222 |
| Description | 10px | 400 (regular) | #666666 |
| Status Badge | 8px | 700 (bold) | varies |
| Date | 10px | 400 (regular) | #999999 |
| Button | 12px | 600 (semibold) | White |

**Font Stack:** -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif

---

## Spacing Reference

| Element | Padding |
|---------|---------|
| Header | 14px 16px |
| Section Header | 12px 14px 8px |
| Care Gap Item | 10px 14px |
| Visit Item | 8px 14px |
| AI Section | 12px 14px |
| Button Margin | 12px 14px 14px |

---

## Files Provided

1. **sidebar_mockup.html** - Standalone sidebar HTML/CSS
2. **sidebar_mockup.png** - Rendered sidebar only
3. **sidebar_with_context.html** - Full browser + sidebar composite
4. **sidebar_composite.png** - Rendered composite mockup
5. **REDLINE_MANIFEST.md** - This document

---

## Acceptance Criteria

### Slide 1
- [ ] Tagline updated to "Your Care Team's Force Multiplier—24/7 between-visit support"
- [ ] Formatting matches original (font, size, color, position)

### Slides 2-19
- [ ] All shield logos resized to 0.22" × 0.25"
- [ ] All shield logos repositioned to (9.50", 5.22")
- [ ] No overlap with slide content
- [ ] Visual inspection confirms consistent placement

### Slide 13
- [ ] New sidebar mockup integrated
- [ ] Care Gaps panel shows 5 items with status badges
- [ ] Visit History panel shows 3-4 recent visits
- [ ] AI Assistant section visible with input field
- [ ] Launch Call button prominent
- [ ] Browser context (Isaac Health) visible on left
- [ ] Overall composition balanced and professional

---

## Contact

For questions about this manifest, contact the NightingaleMD product team.

**Version:** 1.0  
**Last Updated:** December 30, 2025
