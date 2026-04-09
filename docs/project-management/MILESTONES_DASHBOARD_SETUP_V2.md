# X4O Project Milestones Dashboard Setup Guide (Business Plan)

**Project:** X4O Website Redevelopment
**Company:** X4O (Pty) Limited
**Document Type:** Smartsheet Business Dashboard Configuration
**Date:** February 12, 2026
**Prepared By:** Keenan Husselmann
**Version:** 2.0 (Business Plan Edition)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Step 1: Create Your Dashboard](#step-1-create-your-dashboard)
4. [Step 2: Add KPI Metrics](#step-2-add-kpi-metrics)
5. [Step 3: Add Phase Progress Chart](#step-3-add-phase-progress-chart)
6. [Step 4: Add Status Pie Chart](#step-4-add-status-pie-chart)
7. [Step 5: Add Priority Chart](#step-5-add-priority-chart)
8. [Step 6: Add Upcoming Milestones Grid](#step-6-add-upcoming-milestones-grid)
9. [Step 7: Add Critical Items Grid](#step-7-add-critical-items-grid)
10. [Step 8: Finalize Layout](#step-8-finalize-layout)
11. [Troubleshooting](#troubleshooting)

---

## Introduction

This guide will help you create a professional dashboard for tracking the X4O project milestones using **Smartsheet Business plan**.

### What You'll Build

A single-page dashboard with:
- 4 KPI metric cards (Total, Completed, Progress %, Remaining)
- Phase progress bar chart
- Status distribution pie chart
- Priority breakdown chart
- Upcoming milestones data grid
- Critical milestones data grid

### Prerequisites

✅ **Required:**
- Smartsheet Business plan (or higher)
- X4O Project Milestones sheet already imported and configured (see MILESTONES_SHEET_SUMMARY_AND_REPORTS.md)
- Sheet Summary fields created (12 fields)
- Timeline View report created

✅ **Before you start:**
- Open your X4O Project Milestones sheet
- Verify Sheet Summary panel shows all 12 metrics
- You should have multiple reports created (each can have different sorting/filtering)

### Understanding Reports and Charts

**KEY CONCEPT:** Each chart widget can only use ONE report as its data source, and that report has ONE specific sort order.

**This means:**
- If Phase Progress chart needs data sorted by Phase → use Report A (sorted by Phase)
- If you later add a Timeline chart needing data sorted by Date → use Report B (sorted by Date)
- You CANNOT change sorting per-widget - sorting comes from the report

**What you'll need:**

| Chart Widget | Best Report to Use | Why |
|--------------|-------------------|-----|
| **KPI Metrics** | Sheet Summary fields | Pre-calculated numbers |
| **Phase Progress Chart** | "X4O - Timeline View" | Sorted by Phase (1→7), then Start Date |
| **Status Pie Chart** | "X4O - Timeline View" | Contains all 38 milestones (sorting doesn't matter for pie charts) |
| **Priority Donut** | "X4O - Timeline View" | Contains all 38 milestones (sorting doesn't matter for donut charts) |
| **Upcoming Milestones Grid** | "X4O - Upcoming Milestones" | Filtered to Not Started within next 90 days |
| **Critical Items Grid** | "X4O - Critical Milestones" | Filtered to Priority = Critical |

**Tip:** You can reuse the same report for multiple pie/donut charts since they just COUNT items - sort order doesn't affect them!

---

## Step 1: Create Your Dashboard

### 1.1 Create New Dashboard

1. Click your **profile/workspace icon** (top-left in Smartsheet)
2. Click **+ Create** → **Dashboard**
3. **Name:** `X4O Milestones Dashboard`
4. Click **OK**

**Result:** Blank dashboard opens with "Add Widget" button visible

### 1.2 Dashboard Settings

1. Click the **gear icon** (⚙️) in top-right corner
2. Configure:
   - **Auto-refresh:** ON (every 5 minutes)
   - **Background:** White
3. Click **OK**

---

## Step 2: Add KPI Metrics

We'll create 4 metric widgets showing key numbers.

### 2.1 Total Milestones Metric

1. Click **+ Add Widget**
2. Select **Metric** widget type
3. Configure:

   **Data:**
   - **Data Source:** Browse → Select "X4O Project Milestones" sheet
   - **Source Type:** Sheet Summary
   - **Select Summary Field:** Total Milestones

   **Display:**
   - **Title:** Total Milestones
   - **Show Title:** Yes
   - **Number Format:** Number (no decimals)

   **Style:**
   - **Size:** Small
   - **Color:** Default blue

4. Click **OK**

**Expected Value:** 38

### 2.2 Completed Milestones Metric

1. Click **+ Add Widget**
2. Select **Metric**
3. Configure:

   **Data:**
   - **Data Source:** X4O Project Milestones sheet
   - **Source Type:** Sheet Summary
   - **Summary Field:** Completed Milestones

   **Display:**
   - **Title:** Completed
   - **Number Format:** Number

   **Style:**
   - **Size:** Small
   - **Color:** Green (#28a745)

4. Click **OK**

**Expected Value:** 28

### 2.3 Overall Progress Metric

1. Click **+ Add Widget**
2. Select **Metric**
3. Configure:

   **Data:**
   - **Data Source:** X4O Project Milestones sheet
   - **Source Type:** Sheet Summary
   - **Summary Field:** Overall % Complete

   **Display:**
   - **Title:** Progress
   - **Number Format:** Percentage (1 decimal)

   **Style:**
   - **Size:** Small
   - **Color:** Blue (#97c0e8)

4. Click **OK**

**Expected Value:** 73.7%

### 2.4 Remaining Milestones Metric

1. Click **+ Add Widget**
2. Select **Metric**
3. Configure:

   **Data:**
   - **Data Source:** X4O Project Milestones sheet
   - **Source Type:** Sheet Summary
   - **Summary Field:** Not Started Milestones

   **Display:**
   - **Title:** Remaining
   - **Number Format:** Number

   **Style:**
   - **Size:** Small
   - **Color:** Orange (#fd7e14)

4. Click **OK**

**Expected Value:** 10

### 2.5 Arrange Metrics in a Row

1. **Drag and drop** the 4 widgets to align horizontally in a row
2. **Resize** each to be equal width
3. **Align** the tops so they form a clean row

---

## Step 3: Add Phase Progress Chart

This chart shows completion status for each of the 7 phases.

### 3.1 Create Chart Widget

1. Click **+ Add Widget**
2. Select **Chart** widget type
3. Configure:

   **Data:**
   - **Data Source:** Browse → Select **"X4O - Timeline View"** report
     - *(This report is sorted by Phase ascending, ensuring phases display 1→7 in correct order)*
   - **Chart Type:** Horizontal Bar Chart

   **Primary Column:**
   - **Group By:** Phase

   **Value Display:**
   - **Display Value:** Count (or Row Count)
   - **Color By:** Status

   **Chart Title:**
   - **Title:** Phase Progress
   - **Show Title:** Yes

   **Legend:**
   - **Show Legend:** Yes
   - **Position:** Bottom

   **Colors:**
   - **Complete:** Green (#28a745)
   - **In Progress:** Yellow (#ffc107)
   - **Not Started:** Gray (#6c757d)

4. Click **OK**

**Expected Result:** Horizontal bars showing 7 phases with stacked colors

**Important:** This chart will display phases in the order they appear in the source report. If phases show in wrong order (Phase 7 first), your report needs to be sorted by Phase ascending.

---

## Step 4: Add Status Pie Chart

This shows overall project completion status.

### 4.1 Create Pie Chart Widget

1. Click **+ Add Widget**
2. Select **Chart**
3. Configure:

   **Data:**
   - **Data Source:** Browse → Select **"X4O - Timeline View"** report
     - *(This report contains all 38 milestones - sorting doesn't matter for pie charts, they just count by status)*
   - **Chart Type:** Pie Chart

   **Primary Column:**
   - **Group By:** Status

   **Value:**
   - **Display Value:** Count

   **Chart Title:**
   - **Title:** Status Distribution
   - **Show Title:** Yes

   **Display:**
   - **Show Legend:** Yes (Right side)
   - **Show Percentages:** Yes
   - **Show Values:** Yes

   **Colors:**
   - **Complete:** Green
   - **In Progress:** Yellow
   - **Not Started:** Gray

4. Click **OK**

**Expected Result:** Pie chart showing ~74% Complete, ~26% Not Started

**Note:** Status pie charts don't depend on report sorting - they just count how many milestones have each status.

---

## Step 5: Add Priority Chart

Shows breakdown of milestones by priority level.

### 5.1 Create Donut Chart Widget

1. Click **+ Add Widget**
2. Select **Chart**
3. Configure:

   **Data:**
   - **Data Source:** Browse → Select **"X4O - Timeline View"** report
     - *(This report contains all 38 milestones - sorting doesn't matter for donut charts, they just count by priority)*
   - **Chart Type:** Donut Chart

   **Primary Column:**
   - **Group By:** Priority

   **Value:**
   - **Display Value:** Count

   **Chart Title:**
   - **Title:** Priority Breakdown
   - **Show Title:** Yes

   **Display:**
   - **Show Legend:** Yes (Bottom)
   - **Show Counts:** Yes

   **Colors:**
   - **Critical:** Red (#dc3545)
   - **High:** Orange (#fd7e14)
   - **Medium:** Blue (#0dcaf0)
   - **Low:** Gray (#6c757d)

4. Click **OK**

**Expected Result:** Donut showing 7 Critical, 20 High, 8 Medium, 3 Low

**Note:** Like pie charts, donut charts just count items in each category - report sorting doesn't matter.

---

## Step 6: Add Upcoming Milestones Grid

Shows next milestones to complete.

### 6.1 Create Report Widget (Grid)

1. Click **+ Add Widget**
2. Select **Report** widget type
3. Configure:

   **Data:**
   - **Source:** Browse → Select **"X4O - Upcoming Milestones"** report
     - *(This report is filtered to show only Not Started milestones within the next 90 days)*

   **Title:**
   - **Widget Title:** Upcoming Milestones
   - **Show Title:** Yes

   **Display:**
   - **Columns to show:**
     - Milestone Name
     - Phase
     - Start Date
     - Priority
   - **Row limit:** 10 rows
   - **Enable scrolling:** Yes

4. Click **OK**

**Expected Result:** Grid showing next 10 milestones to complete

---

## Step 7: Add Critical Items Grid

Shows all critical priority milestones.

### 7.1 Create Report Widget

1. Click **+ Add Widget**
2. Select **Report**
3. Configure:

   **Data:**
   - **Source:** Browse → Select **"X4O - Critical Milestones"** report
     - *(This report is filtered to show only Priority = Critical milestones)*

   **Title:**
   - **Widget Title:** Critical Milestones
   - **Show Title:** Yes

   **Display:**
   - **Columns to show:**
     - Milestone Name
     - Status
     - Start Date
     - % Complete
   - **Row limit:** 15 rows

4. Click **OK**

**Expected Result:** Grid showing 7 critical milestones

---

## Step 8: Finalize Layout

### 8.1 Arrange Widgets

Drag and drop widgets into this recommended layout:

```
┌──────────────────────────────────────────────────────────┐
│  Total: 38   Completed: 28   Progress: 74%   Remaining: 10  │
├────────────────────────┬─────────────────────────────────┤
│  Phase Progress Chart  │  Status Pie Chart               │
│  (Horizontal bar)      │  (Pie)                          │
├────────────────────────┼─────────────────────────────────┤
│  Priority Breakdown    │                                 │
│  (Donut)               │                                 │
├────────────────────────┴─────────────────────────────────┤
│  Upcoming Milestones Grid (Full width)                   │
├───────────────────────────────────────────────────────────┤
│  Critical Milestones Grid (Full width)                   │
└───────────────────────────────────────────────────────────┘
```

### 8.2 Alignment Tips

- **Select multiple widgets:** Hold Shift + Click
- **Align tops:** Right-click → Align → Align Tops
- **Make same width:** Right-click → Resize → Make Same Width
- **Distribute evenly:** Right-click → Align → Distribute Horizontally

### 8.3 Final Polish

1. Add a **Title widget** at the very top:
   - Click **+ Add Widget** → **Title**
   - **Text:** `X4O Website Redevelopment - Milestones Dashboard`
   - **Font:** Large (24pt)
   - **Background:** Blue (#97c0e8)
   - **Text Color:** White

2. Add optional **Rich Text widget** for legend:
   - **Text:**
     ```
     Status Colors: 🟢 Complete | 🟡 In Progress | ⚪ Not Started
     Priority: 🔴 Critical | 🟠 High | 🔵 Medium | ⚫ Low
     ```

3. **Save dashboard** (Ctrl+S)

---

## Troubleshooting

### Issue: Phases Showing in Wrong Order

**Problem:** Phase Progress chart shows "Phase 7: Maintenance" at the top instead of "Phase 1: Planning"

**Why this happens:** The chart gets its sort order from the REPORT, not from the widget settings. If your report is sorted incorrectly, the chart will display in wrong order.

**Solution:**

**Option 1: Fix the existing report's sorting**

1. **Find which report your Phase Progress chart is using:**
   - Click the chart widget
   - Click Edit (pencil icon)
   - Look at "Data Source" field - note the report name
   - Click Cancel

2. **Open that report:**
   - Click Smartsheet logo (top-left)
   - Browse to the report (e.g., "X4O - Timeline View")
   - Click to open

3. **Fix the sorting:**
   - Look for **Sort icon** in toolbar (↕️ or funnel with arrows)
   - Click it
   - Configure:
     - **Primary Sort:** Phase (Ascending A→Z)
     - **Secondary Sort:** Start Date (Ascending, oldest first)
   - Click **OK** or **Apply**

4. **Verify the fix:**
   - Report should now show Phase 1 items first, Phase 7 last
   - Go back to dashboard
   - Refresh (F5)
   - Chart should now show phases 1-7 in correct order

**Option 2: Create a NEW report specifically for this chart**

1. **Create dedicated Phase Progress report:**
   - Click + Create → Report
   - Name: "X4O - Phase Progress View"
   - Source: X4O Project Milestones
   - Filter: Status is one of Complete, In Progress, Not Started (shows all)
   - **Sort:** Phase (Ascending), then Start Date (Ascending)
   - Save

2. **Update the chart to use new report:**
   - Go to dashboard
   - Click Phase Progress chart → Edit
   - Change **Data Source** to "X4O - Phase Progress View"
   - Click OK
   - Chart now shows phases in correct order

**Which option to use?**
- **Option 1** if the existing report is only used for this chart
- **Option 2** if the existing report is used by other charts that need different sorting

---

### Issue: Metric Shows Blank or Zero

**Problem:** KPI metric displays 0 or nothing

**Solution:**

1. **Check Sheet Summary:**
   - Open X4O Project Milestones sheet
   - Click Sheet Summary icon (right panel)
   - Verify the field exists and has a value
   - If formula shows #UNPARSEABLE, fix the formula (see MILESTONES_SHEET_SUMMARY_AND_REPORTS.md)

2. **Recreate Widget:**
   - Delete the broken metric widget
   - Create new widget following steps in Section 2
   - Ensure you select **Sheet Summary** as source type

---

### Issue: Chart Shows "No Data"

**Problem:** Chart displays "No data to display" message

**Solution:**

1. **Check Report:**
   - Open the report being used as data source
   - Verify it contains data (should show milestones)
   - If empty, check filters in report

2. **Verify Data Source:**
   - Edit widget
   - Check that correct report is selected
   - Ensure **Group By** field is set correctly

3. **Check Group By Column:**
   - Open source sheet
   - Verify the column has dropdown values (not blank)
   - Example: Phase column should have "Phase 1: Planning", "Phase 2: Design", etc.

---

### Issue: Can't Edit Dashboard

**Problem:** Dashboard won't let you add widgets or move things

**Solution:**

1. **Check Edit Mode:**
   - Look for **Edit** button in top-right
   - Click it to enable editing

2. **Check Permissions:**
   - You need Owner or Admin permissions
   - Contact dashboard owner if you only have Viewer access

3. **Browser Issues:**
   - Try different browser (Chrome recommended)
   - Clear cache: Ctrl+Shift+Delete
   - Disable browser extensions temporarily

---

### Issue: Widgets Not Loading

**Problem:** Dashboard shows loading spinner forever

**Solution:**

1. **Refresh Page:** Press F5 or Ctrl+R

2. **Hard Refresh:** Press Ctrl+Shift+R

3. **Check Internet Connection** Check you're online

4. **Check Smartsheet Status:**
   - Visit: status.smartsheet.com
   - Check for service outages

5. **Try Incognito Mode:**
   - Ctrl+Shift+N (Chrome)
   - Tests if it's a cache/extension issue

---

## Quick Reference Card

### Dashboard Maintenance

**Update Milestones:**
1. Open X4O Project Milestones sheet
2. Change Status, % Complete, dates as needed
3. Dashboard auto-updates within 5 minutes

**Share Dashboard:**
1. Click **Share** button (top-right)
2. Enter email addresses
3. Set permission: Viewer (can see only) or Editor (can modify)
4. Click **Send**

**Export Dashboard:**
1. Click **File** menu
2. Select **Print**
3. Choose PDF
4. Save to computer

**Common Widget Edits:**
- **Edit widget:** Click widget → Click pencil icon (Edit)
- **Delete widget:** Click widget → Click X icon (Delete)
- **Resize widget:** Click and drag corners/edges
- **Move widget:** Click and drag widget title bar

---

## Summary

You've created a professional dashboard with:

✅ **4 KPI Metrics** - Total, Completed, Progress %, Remaining
✅ **Phase Progress Chart** - Horizontal bar showing all 7 phases
✅ **Status Pie Chart** - Overall completion breakdown
✅ **Priority Donut Chart** - Critical/High/Medium/Low distribution
✅ **Upcoming Milestones Grid** - Next 10 items to complete
✅ **Critical Items Grid** - All critical priority milestones

### Next Steps

1. **Share with team:** Click Share, add team members as Viewers
2. **Set up email reports:** File → Send → Schedule weekly PDF
3. **Customize colors:** Edit widgets to match brand colors
4. **Add more widgets:** Consider adding:
   - Gantt timeline chart (needs date-sorted report)
   - Phase 7-focused table
   - Monthly completion trend

### Pro Tips for Using Multiple Reports

**Why you created multiple reports:**
- Each chart widget inherits sorting from its source report
- You CANNOT override report sorting in the widget
- Solution: Create separate reports with different sorting for different charts

**Report reuse strategy:**
- ✅ **Reuse for pie/donut charts:** They just count - sorting doesn't matter
- ✅ **Reuse for grids with same filters:** Same filtered data can feed multiple widgets
- ❌ **Don't reuse for charts needing different order:** Phase chart needs Phase sorting, Timeline needs Date sorting

**Example multi-report setup:**
```
Report 1: "X4O - Timeline View" (sorted by Phase → Start Date)
  ↳ Used by: Phase Progress Chart, Status Pie Chart, Priority Donut Chart

Report 2: "X4O - Upcoming Milestones" (filtered: Not Started, next 90 days)
  ↳ Used by: Upcoming Milestones Grid

Report 3: "X4O - Critical Milestones" (filtered: Priority = Critical)
  ↳ Used by: Critical Milestones Grid

Report 4: "X4O - Completed Milestones" (filtered: Status = Complete)
  ↳ Available for: Historical tracking widgets

Report 5: "X4O - High Priority Pending" (filtered: Critical/High + Not Started)
  ↳ Available for: Priority-focused widgets

Report 6: "X4O - Phase 7 Maintenance" (filtered: Phase 7 only)
  ↳ Available for: Phase 7 tracking widget
```

---

## Document Information

**Document Version:** 2.0 (Business Plan Edition)
**Last Updated:** February 12, 2026
**Prepared By:** Keenan Husselmann
**Smartsheet Plan:** Business (or higher)
**Status:** ✅ Complete

**Related Documents:**
- `MILESTONES_SHEET_SUMMARY_AND_REPORTS.md` - Sheet Summary setup
- `X4O_Project_Milestones.csv` - Source data file

---

**END OF DOCUMENT**
