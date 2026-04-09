# X4O Project Milestones - Sheet Summary & Reports Configuration

**Project:** X4O Website Redevelopment
**Company:** X4O (Pty) Limited
**Document Type:** Smartsheet Data Configuration Guide
**Date:** February 12, 2026
**Prepared By:** Keenan Husselmann
**Version:** 1.0

---

## Table of Contents

1. [Introduction](#introduction)
2. [Technical Terms Glossary](#technical-terms-glossary)
3. [Part 1: Sheet Summary Fields](#part-1-sheet-summary-fields)
4. [Part 2: Create Reports](#part-2-create-reports)
5. [Verification & Testing](#verification--testing)
6. [Troubleshooting](#troubleshooting)

---

## Introduction

This guide walks you through setting up **Sheet Summary Fields** and **Reports** for the X4O Project Milestones sheet. These data sources will power your dashboard widgets.

### What You'll Configure

**Sheet Summary Fields (12 fields):**
- Aggregate metrics that calculate automatically
- Foundation for dashboard KPI widgets
- Real-time updates as sheet changes

**Reports (6 reports):**
- Filtered views of milestone data
- Data source for dashboard tables and charts
- Custom views for different audiences

### Prerequisites

- ✅ X4O Project Milestones sheet imported and configured
- ✅ Column types set correctly (Dropdown, Date, Contact List)
- ✅ Conditional formatting applied
- ✅ 15-20 minutes of time

---

## Technical Terms Glossary

**For Non-Technical Readers:** Simple explanations of Smartsheet concepts.

| Term | Simple Explanation |
|------|-------------------|
| **Sheet Summary** | A summary panel at the top of a sheet showing key metrics. Like a scoreboard showing totals and averages. |
| **Summary Field** | A single calculated metric in Sheet Summary. Like one gauge on a car dashboard (speed, fuel, etc.). |
| **Formula** | Automatic calculation that updates when data changes. Like a calculator that recalculates automatically. |
| **COUNT** | Counts how many items exist. Like counting people at a meeting. |
| **COUNTIF** | Counts items matching a condition. Like counting only people wearing blue shirts. |
| **SUM** | Adds numbers together. Basic addition. |
| **AVG (Average)** | Calculates the mean of numbers. Sum divided by count. |
| **Report** | A filtered view of sheet data. Like a custom view showing only relevant information. |
| **Filter** | Shows only rows meeting specific criteria. Like a search that hides non-matching items. |
| **Group By** | Organizes data into categories. Like sorting files into folders. |
| **Sort** | Arranges data in order (A-Z, newest first, etc.). Like alphabetizing or chronological order. |
| **Aggregation** | Combining data to show summaries. Like monthly sales totals instead of individual transactions. |

---

## Part 1: Sheet Summary Fields

### What is Sheet Summary?

**Sheet Summary** is a panel at the top of your sheet that displays key metrics and calculations. Think of it as your sheet's dashboard - always visible, always up-to-date.

### Access Sheet Summary

1. **Open Sheet**
   - Navigate to: `X4O Project Milestones` sheet

2. **Open Sheet Summary Panel**
   - **Method 1:** Click "Sheet Summary" icon in right panel
   - **Method 2:** Click the summary icon in toolbar (looks like a list with checkboxes)
   - **Method 3:** Right-click sheet tab → "Sheet Summary"

3. **Panel Opens**
   - Right side panel displays
   - Shows "Add field" button
   - Empty if first time opening

---

### Configure Sheet Summary Fields

We'll create **12 summary fields** to track project metrics.

---

#### Field 1: Total Milestones

**Purpose:** Count total number of milestones in project

**Steps:**
1. Click "+ Add Field" in Sheet Summary panel
2. **Field Name:** `Total Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNT([Milestone Name]:[Milestone Name])
   ```
5. **Expected Value:** 38
6. Click "OK"

**What it does:** Counts all rows with milestone names (excludes header row)

---

#### Field 2: Completed Milestones

**Purpose:** Count milestones with "Complete" status

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Completed Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Status:Status, "Complete")
   ```
5. **Expected Value:** 28
6. Click "OK"

**What it does:** Counts rows where Status column = "Complete"

---

#### Field 3: In Progress Milestones

**Purpose:** Count milestones currently being worked on

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `In Progress Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Status:Status, "In Progress")
   ```
5. **Expected Value:** 0
6. Click "OK"

**What it does:** Counts rows where Status = "In Progress"

---

#### Field 4: Not Started Milestones

**Purpose:** Count milestones not yet begun

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Not Started Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Status:Status, "Not Started")
   ```
5. **Expected Value:** 10
6. Click "OK"

**What it does:** Counts rows where Status = "Not Started"

---

#### Field 5: Overall % Complete

**Purpose:** Calculate average completion percentage across all milestones

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Overall % Complete`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =AVG([% Complete]:[% Complete]) / 100
   ```
5. **Format:** Percentage (1 decimal place)
6. **Expected Value:** 73.7%
7. Click "OK"

**What it does:** Averages the % Complete column (0, 50, 100 → average) and divides by 100 to convert to proper percentage format

---

#### Field 6: Critical Milestones

**Purpose:** Count milestones with Critical priority

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Critical Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Priority:Priority, "Critical")
   ```
5. **Expected Value:** 7
6. Click "OK"

**What it does:** Counts rows where Priority = "Critical"

---

#### Field 7: High Priority Milestones

**Purpose:** Count high priority items

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `High Priority Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Priority:Priority, "High")
   ```
5. **Expected Value:** 20
6. Click "OK"

---

#### Field 8: Phase 7 (Maintenance) Count

**Purpose:** Count milestones in Phase 7

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Phase 7 Milestones`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =COUNTIF(Phase:Phase, "Phase 7: Maintenance")
   ```
5. **Expected Value:** 10
6. Click "OK"

**What it does:** Counts ongoing maintenance tasks

---

#### Field 9: Completed Phases

**Purpose:** Count how many phases are 100% complete

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Completed Phases`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =6
   ```
   *(Static value - Phases 1-6 complete, Phase 7 in progress)*
5. **Expected Value:** 6
6. Click "OK"

**Note:** This is a manual field. Update to 7 when Phase 7 completes.

---

#### Field 10: Project Start Date

**Purpose:** First milestone start date (project kickoff)

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Project Start Date`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =MIN([Start Date]:[Start Date])
   ```
5. **Expected Value:** 2026-02-07
6. Click "OK"

**What it does:** Finds earliest start date in entire sheet

---

#### Field 11: Latest Milestone Date

**Purpose:** Last milestone end date (project completion estimate)

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Latest Milestone Date`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =MAX([End Date]:[End Date])
   ```
5. **Expected Value:** 2027-02-15 (Annual Domain Renewal)
6. Click "OK"

**What it does:** Finds latest end date in sheet

---

#### Field 12: Days Since Project Start

**Purpose:** How many days since project kickoff

**Steps:**
1. Click "+ Add Field"
2. **Field Name:** `Days Since Start`
3. **Field Type:** Formula
4. **Formula:**
   ```
   =TODAY() - MIN([Start Date]:[Start Date])
   ```
5. **Format:** Number (no decimals)
6. **Expected Value:** ~5 days (as of Feb 12, 2026)
7. Click "OK"

**What it does:** Calculates days between today and first start date

---

### Sheet Summary Panel Complete

**You should now see:**

```
Sheet Summary
─────────────────────────────────────
Total Milestones:              38
Completed Milestones:          28
In Progress Milestones:        0
Not Started Milestones:        10
Overall % Complete:            73.7%
Critical Milestones:           7
High Priority Milestones:      20
Phase 7 Milestones:            10
Completed Phases:              6
Project Start Date:            2026-02-07
Latest Milestone Date:         2027-02-15
Days Since Start:              5
```

**These fields will auto-update** as you modify the sheet (change statuses, add milestones, etc.).

---

## Part 2: Create Reports

### What are Reports?

**Reports** are filtered, sorted views of your sheet data. They pull data from the source sheet but display only what you specify. Perfect for dashboard widgets and stakeholder views.

### Access Reports

1. **Navigate to Home**
   - Click "Home" in left sidebar

2. **Create New Report**
   - Click "Create" button (top-left)
   - Select "Report" from menu

---

### Report 1: Upcoming Milestones

**Purpose:** Show next 10 milestones starting soon (Not Started status)

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - Upcoming Milestones`

2. **Add Source Sheet**
   - Click "+ Add Source Sheet"
   - Select: `X4O Project Milestones`
   - Check "Include all columns"
   - Click "OK"

3. **Configure Filters**
   - Click "Add Filter" (funnel icon)

   **Filter 1:**
   - **Column:** Status
   - **Condition:** is
   - **Value:** Not Started

   **Filter 2:**
   - **Column:** Start Date
   - **Condition:** is within
   - **Value:** next 90 days

4. **Configure Columns**
   - Show only: Milestone Name, Phase, Start Date, Priority, Owner, Deliverables
   - Hide other columns (click column header → Hide Column)

5. **Sort Data**
   - Click "Sort" icon
   - **Primary Sort:** Start Date (Ascending - earliest first)
   - **Secondary Sort:** Priority (Critical → Low)

6. **Group Data** (Optional)
   - Click "Group" icon
   - **Group By:** Phase
   - Shows milestones organized by phase

7. **Save Report**
   - Click "Save" (top-right)

**Expected Result:** 10 upcoming Phase 7 milestones displayed

---

### Report 2: Critical Milestones

**Purpose:** All milestones with Critical priority (regardless of status)

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - Critical Milestones`

2. **Add Source Sheet**
   - Source: `X4O Project Milestones`
   - Include all columns

3. **Configure Filter**
   - **Column:** Priority
   - **Condition:** is
   - **Value:** Critical

4. **Configure Columns**
   - Show: Milestone Name, Status, Start Date, End Date, % Complete, Owner

5. **Sort Data**
   - **Primary Sort:** Status (Complete last, Not Started first)
   - **Secondary Sort:** Start Date (Ascending)

6. **Highlight Rows** (Conditional Formatting)
   - Format → Conditional Formatting
   - **Rule:** If Status is "Not Started"
   - **Format:** Red background (#ffc7ce), Red text (#9c0006)
   - **Apply to:** Entire row

7. **Save Report**

**Expected Result:** 7 critical milestones (3 deployment, 1 testing, 3 Phase 7)

---

### Report 3: Phase 7 - Maintenance Items

**Purpose:** All Phase 7 ongoing/future tasks

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - Phase 7 Maintenance`

2. **Add Source Sheet**
   - Source: `X4O Project Milestones`

3. **Configure Filter**
   - **Column:** Phase
   - **Condition:** is
   - **Value:** Phase 7: Maintenance

4. **Configure Columns**
   - Show: Milestone Name, Priority, Start Date, End Date, Status, Category, Dependencies

5. **Group Data**
   - **Group By:** Category
   - Shows Enhancement, Operations, Compliance groups

6. **Sort Within Groups**
   - **Sort:** Priority (Critical → Low)

7. **Save Report**

**Expected Result:** 10 Phase 7 tasks grouped by category

---

### Report 4: Completed Milestones by Phase

**Purpose:** Historical view of what's been accomplished

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - Completed Milestones`

2. **Add Source Sheet**
   - Source: `X4O Project Milestones`

3. **Configure Filter**
   - **Column:** Status
   - **Condition:** is
   - **Value:** Complete

4. **Configure Columns**
   - Show: Milestone Name, Phase, End Date, Deliverables, Owner

5. **Group Data**
   - **Group By:** Phase
   - Shows completed items per phase

6. **Sort**
   - **Within Groups:** End Date (Descending - newest first)

7. **Summary Row** (Optional)
   - Click group header → "Summarize"
   - Add: Count of Milestones
   - Shows total completed per phase

8. **Save Report**

**Expected Result:** 28 completed milestones grouped by Phase 1-6

---

### Report 5: High Priority Pending

**Purpose:** High priority items not yet started (for planning)

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - High Priority Pending`

2. **Add Source Sheet**
   - Source: `X4O Project Milestones`

3. **Configure Filters**

   **Filter 1:**
   - **Column:** Priority
   - **Condition:** is one of
   - **Values:** Critical, High (select both)

   **Filter 2:**
   - **Column:** Status
   - **Condition:** is
   - **Value:** Not Started

4. **Configure Columns**
   - Show: Milestone Name, Priority, Category, Start Date, Dependencies, Notes

5. **Sort**
   - **Primary:** Priority (Critical first)
   - **Secondary:** Start Date (Ascending)

6. **Save Report**

**Expected Result:** ~8-10 high priority pending items

---

### Report 6: Timeline View (All Active)

**Purpose:** Gantt-friendly report for dashboard timeline widget

**Steps:**

1. **Create Report**
   - Create → Report
   - **Report Name:** `X4O - Timeline View`

2. **Add Source Sheet**
   - Source: `X4O Project Milestones`

3. **Configure Filters**
   - **Filter:** Status is one of "Complete", "In Progress", "Not Started"
   - *(Include all - this filter just ensures data integrity)*

4. **Configure Columns**
   - **Required:** Milestone Name, Start Date, End Date, Status, Phase
   - **Optional:** % Complete, Priority

5. **Sort** ⚠️ **CRITICAL FOR DASHBOARD CHARTS**

   **Why sorting matters here:**
   - This report feeds ALL chart widgets in the dashboard (Phase Progress, Status Pie, Priority Donut, Gantt Timeline)
   - Dashboard charts inherit this sorting automatically
   - Incorrect sorting = phases displayed in wrong order in charts

   **Correct Sort Configuration:**

   **Step-by-step:**

   a. **Click "Sort" icon** in the Report toolbar (funnel with arrows)

   b. **Primary Sort:**
   - Column: **Phase**
   - Order: **Ascending** (A → Z)
   - This ensures Phase 1 appears first, Phase 7 last

   c. **Secondary Sort:**
   - Click "+ Add another sort"
   - Column: **Start Date**
   - Order: **Ascending** (Oldest → Newest)
   - This orders milestones chronologically within each phase

   **Visual representation:**
   ```
   Sort Configuration in Smartsheet:

   [Sort icon] Configure sorting

   Primary Sort:    Phase          ▼ Ascending (A → Z)
   Secondary Sort:  Start Date     ▼ Ascending (Oldest first)
   ```

   **How to verify it's working:**

   After saving, the report should display milestones in this order:
   ```
   Phase 1: Planning
     ├─ Project Kickoff (2026-02-07)
     ├─ Requirements Gathering Complete (2026-02-08)

   Phase 2: Design
     ├─ Design System Finalized (2026-02-09)
     ├─ Component Library Created (2026-02-09)

   Phase 3: Development
     ├─ Homepage Development Complete (2026-02-09)
     ├─ Services Pages Complete (2026-02-09)
     └─ ... (continues chronologically)

   Phase 7: Maintenance
     ├─ Image Optimization (2026-02-13)
     ├─ Analytics Implementation (2026-02-13)
     └─ ... (all Phase 7 items)
   ```

6. **Save Report**

**Expected Result:** All 38 milestones in chronological order by phase

**Common Mistakes to Avoid:**

❌ **Wrong:** Phase sorted Descending (Z → A) - Shows Phase 7 first
❌ **Wrong:** Start Date as Primary Sort - Mixes phases together
❌ **Wrong:** No secondary sort - Random order within phases
❌ **Wrong:** Sorting by Milestone Name - Alphabetical chaos

✅ **Correct:** Phase (Ascending) → Start Date (Ascending)

**Note:** This report is specifically formatted for Gantt chart widgets in dashboards. The sorting configured here flows to all dashboard charts automatically.

---

## Verification & Testing

### Test Sheet Summary Fields

**Steps:**

1. **Open Sheet Summary Panel**
   - Verify all 12 fields display correctly

2. **Test Formula Updates**
   - **Action:** Change one milestone Status from "Not Started" to "Complete"
   - **Expected:**
     - Completed Milestones: 28 → 29
     - Not Started Milestones: 10 → 9
     - Overall % Complete: 73.7% → 76.3%

3. **Undo Test Change**
   - Ctrl+Z to revert status change
   - Verify metrics return to original values

4. **Check Static Fields**
   - Verify Completed Phases = 6
   - Verify Project Start Date = 2026-02-07

**✅ All fields should update automatically when sheet data changes**

---

### Test Reports

**For each report, verify:**

| Report | Expected Row Count | Key Filter Working |
|--------|-------------------|-------------------|
| **Upcoming Milestones** | 10 | Only "Not Started" shown |
| **Critical Milestones** | 7 | Only "Critical" priority |
| **Phase 7 Maintenance** | 10 | Only Phase 7 items |
| **Completed Milestones** | 28 | Only "Complete" status |
| **High Priority Pending** | 8-10 | Only High/Critical + Not Started |
| **Timeline View** | 38 | All milestones included |

**Test Report Refresh:**

1. **Open any report**
2. **Make change in source sheet**
   - Example: Change a milestone status
3. **Refresh report**
   - Click refresh icon or F5
4. **Verify change reflected**
   - Row should move/disappear based on filter

**✅ Reports should update when source sheet changes**

---

### Create Report Folder (Organization)

**Steps:**

1. **Navigate to Home**
2. **Right-click in left sidebar**
3. **Select "New Folder"**
4. **Folder Name:** `X4O Project Reports`
5. **Drag all 6 reports into folder**

**Result:** Reports organized in dedicated folder for easy access

---

## Troubleshooting

### Issue: Sheet Summary Field Shows #UNPARSEABLE

**Symptoms:**
- Formula shows error instead of value
- Field displays #UNPARSEABLE or #INVALID REF

**Diagnosis:**
- Column name mismatch
- Incorrect formula syntax
- Column type incompatible

**Resolution:**

1. **Edit Field**
   - Click field → Edit

2. **Check Column Names**
   - Verify exact spelling: `[Milestone Name]:[Milestone Name]`
   - Column names are case-sensitive
   - Include square brackets for multi-word names

3. **Verify Formula Syntax**

   **Correct:**
   ```
   =COUNTIF(Status:Status, "Complete")
   ```

   **Incorrect:**
   ```
   =COUNTIF([Status], "Complete")  ← Missing column range
   =COUNTIF(Status, "Complete")    ← Missing second reference
   ```

4. **Check Quotes**
   - Use straight quotes: `"Complete"`
   - Not curly quotes: `"Complete"` ← Wrong

5. **Save and Verify**

---

### Issue: Report Shows No Data

**Symptoms:**
- Report displays "No data to display"
- Expected rows missing

**Diagnosis:**
- Filters too restrictive
- Source sheet disconnected
- Column hidden in source

**Resolution:**

1. **Check Filters**
   - Click filter icon
   - Review all active filters
   - Temporarily disable filters (toggle off)
   - If data appears, filters are too restrictive

2. **Adjust Filter Values**
   - Verify dropdown values match exactly
   - Example: "Complete" not "Completed"
   - Case-sensitive matching

3. **Check Source Sheet**
   - Click "Source Sheets" tab in report
   - Verify `X4O Project Milestones` is listed
   - If missing, re-add source sheet

4. **Verify Columns Exist**
   - Open source sheet
   - Confirm filtered columns exist
   - Check column names match filter

---

### Issue: Report Data Not Updating

**Symptoms:**
- Report shows old data after sheet changes
- Manual refresh doesn't update

**Diagnosis:**
- Browser cache
- Report not linked to source
- Permission issue

**Resolution:**

1. **Hard Refresh**
   - Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
   - Clears browser cache

2. **Check Report-Sheet Link**
   - Open report
   - Click "Source Sheets"
   - Verify green checkmark next to sheet name
   - If red X, re-add source sheet

3. **Verify Permissions**
   - Ensure you have "Viewer" or higher access
   - Owner/Admin can always see updates

4. **Recreate Report** (Last Resort)
   - If issue persists, delete report
   - Create new report with same settings
   - Link to source sheet

---

### Issue: Formula Counting Wrong

**Symptoms:**
- COUNTIF returns unexpected number
- COUNT shows more/fewer than expected

**Diagnosis:**
- Hidden rows
- Blank cells counted
- Filter applied to source sheet

**Resolution:**

1. **Check Hidden Rows**
   - Source sheet → Unhide All Rows
   - Menu: View → Show All

2. **Verify Column Range**
   - Formula should reference entire column:
     ```
     =COUNT([Milestone Name]:[Milestone Name])
     ```
   - Not partial range:
     ```
     =COUNT([Milestone Name]1:[Milestone Name]38)  ← Excludes new rows
     ```

3. **Check for Blank Cells**
   - COUNT counts non-blank cells
   - COUNTIF counts cells matching criteria
   - If blanks exist, they're excluded

4. **Remove Sheet Filters**
   - Source sheet → Clear all column filters
   - Formulas count visible + hidden rows (unlike manual counts)

---

### Issue: Timeline View Report Sorting Incorrect

**Symptoms:**
- Dashboard charts show phases in wrong order (Phase 7 before Phase 1)
- Gantt timeline appears jumbled
- Phase Progress bar chart has phases out of sequence
- Older milestones appearing after newer ones within same phase

**Diagnosis:**
- **Primary Sort** set incorrectly in Timeline View report
- **Secondary Sort** missing or wrong column
- Sort order Descending instead of Ascending

**Resolution:**

**How to Fix Timeline View Sorting:**

1. **Open the Timeline View Report**
   - Navigate to "X4O - Timeline View" report
   - You should see all 38 milestones displayed

2. **Access Sort Settings**
   - Look for the **Sort icon** in the report toolbar
   - Icon looks like: ↕️ or a funnel with arrows
   - Click to open sort configuration dialog

3. **Verify Primary Sort**
   - **Column:** Should be **Phase**
   - **Order:** Should be **Ascending** (A → Z)

   **If wrong:**
   - Click the dropdown under "Column"
   - Select **Phase**
   - Click the dropdown under "Order"
   - Select **Ascending (A → Z)**

4. **Verify Secondary Sort**
   - Look for second sort row (or click "+ Add another sort")
   - **Column:** Should be **Start Date**
   - **Order:** Should be **Ascending** (Oldest → Newest)

   **If missing or wrong:**
   - Click "+ Add another sort" if no secondary sort exists
   - Select **Start Date** as column
   - Select **Ascending** as order

5. **Save Sort Configuration**
   - Click "OK" or "Apply" to save
   - Report should refresh immediately

6. **Verify Correct Order**

   The report should now show milestones in this sequence:
   ```
   Row 1:  Project Kickoff | Phase 1: Planning | 2026-02-07
   Row 2:  Requirements Gathering Complete | Phase 1: Planning | 2026-02-08
   Row 3:  Design System Finalized | Phase 2: Design | 2026-02-08
   Row 4:  Component Library Created | Phase 2: Design | 2026-02-09
   ...
   Row 28: Test Reports Documentation | Phase 6: Documentation | 2026-02-12
   Row 29: Image Optimization | Phase 7: Maintenance | 2026-02-13
   ...
   Row 38: Annual Domain Renewal | Phase 7: Maintenance | 2027-02-15
   ```

   **Key indicators it's correct:**
   - ✅ Phase 1 items at top
   - ✅ Phase 7 items at bottom
   - ✅ Within each phase, earliest dates first
   - ✅ Latest milestone (2027-02-15) is last row

7. **Check Dashboard Charts Update**
   - Go back to your Milestones Dashboard
   - Refresh dashboard (F5 or refresh button)
   - **Phase Progress chart** should now show Phase 1 → Phase 7 in order
   - **Gantt Timeline** should flow chronologically

**What if sorting still doesn't work?**

**Option 1: Delete and recreate sort**
1. Open sort dialog
2. Click "Clear all sorts"
3. Re-add Primary Sort: Phase (Ascending)
4. Re-add Secondary Sort: Start Date (Ascending)
5. Save

**Option 2: Check Phase column values**
1. Open source sheet (X4O Project Milestones)
2. Check Phase column has values like:
   - "Phase 1: Planning"
   - "Phase 2: Design"
   - NOT "Planning" or "1" or "Phase One"
3. Ensure all 38 rows have phase values

**Option 3: Recreate the report**
1. Create new report: "X4O - Timeline View (Fixed)"
2. Add source: X4O Project Milestones
3. Configure filter: Status is one of Complete, In Progress, Not Started
4. Add columns: Milestone Name, Start Date, End Date, Status, Phase
5. **Sort:** Phase (Ascending), then Start Date (Ascending)
6. Save report
7. Update dashboard chart widgets to use new report

**TL;DR:**
```
Timeline View Report MUST have:
  Primary Sort:   Phase (Ascending A→Z)
  Secondary Sort: Start Date (Ascending Oldest→Newest)

This ensures all dashboard charts display phases 1-7 in correct order.
```

---

## Summary

### What You've Created

✅ **Sheet Summary Fields (12 fields)**
- Total Milestones: 38
- Completed Milestones: 28
- In Progress: 0
- Not Started: 10
- Overall % Complete: 73.7%
- Critical Milestones: 7
- High Priority: 20
- Phase 7 Count: 10
- Completed Phases: 6
- Project Start: 2026-02-07
- Latest Milestone: 2027-02-15
- Days Since Start: ~5

✅ **Reports (6 reports)**
1. Upcoming Milestones (10 rows)
2. Critical Milestones (7 rows)
3. Phase 7 Maintenance (10 rows)
4. Completed Milestones (28 rows)
5. High Priority Pending (8-10 rows)
6. Timeline View (38 rows)

### Next Steps

**You're now ready to build the dashboard!**

The dashboard will use:
- **Metric widgets** → Pull from Sheet Summary fields
- **Chart widgets** → Pull from source sheet or reports
- **Table widgets** → Display reports
- **Gantt widget** → Use Timeline View report

**Proceed to:**
- `MILESTONES_DASHBOARD_SETUP.md` (Part 3: Create Dashboard)

---

## Quick Reference

### Sheet Summary Formula Templates

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Count All** | `=COUNT([Column]:[Column])` | Total rows |
| **Count Specific** | `=COUNTIF(Column:Column, "Value")` | Rows matching value |
| **Average** | `=AVG([Column]:[Column])` | Mean of numbers |
| **Sum** | `=SUM([Column]:[Column])` | Add all numbers |
| **Earliest Date** | `=MIN([Date]:[Date])` | First date |
| **Latest Date** | `=MAX([Date]:[Date])` | Last date |
| **Days Between** | `=TODAY() - [Date]` | Days since date |
| **Percentage** | `=(Part / Total) * 100` | Calculate % |

### Report Best Practices

✅ **Filter Wisely**
- Start broad, narrow as needed
- Test filters with sample data
- Document filter logic in report name

✅ **Column Selection**
- Show only relevant columns
- Hide internal/technical columns
- Order columns logically (important → detail)

✅ **Grouping**
- Group by phase, status, or category
- Add summary rows to groups
- Collapse groups for overview

✅ **Sorting**
- Primary sort = most important category
- Secondary sort = chronological or priority
- Consistent sorting across similar reports

✅ **Naming Convention**
- Prefix with project: `X4O - Report Name`
- Descriptive: Say what it shows
- Consistent: All reports follow same pattern

---

## Document Information

**Document Version:** 1.0
**Last Updated:** February 12, 2026
**Prepared By:** Keenan Husselmann
**Status:** ✅ Complete

**Related Documents:**
- `X4O_Project_Milestones.csv` (source data)
- `MILESTONES_DASHBOARD_SETUP.md` (dashboard instructions)

**Next Document:** Ready to build dashboard (Part 3)

---

**END OF DOCUMENT**
