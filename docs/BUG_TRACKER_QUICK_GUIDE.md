# X4O Bug Tracker - Quick Setup Guide
## Google Sheets + Smartsheet Integration

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Import CSV to Google Sheets

1. Open Google Sheets: https://sheets.google.com
2. File → Import → Upload → Select `X4O_Bug_Tracker.csv`
3. Click "Import data"

✅ Done! Your bug tracker is now in Google Sheets.

---

### Step 2: Set Up Dropdowns (Copy-Paste Ready)

**Severity (Column D):**
```
Critical, High, Medium, Low
```

**Priority (Column E):**
```
Urgent, High, Medium, Low
```

**Status (Column F):**
```
New, Confirmed, In Progress, Fixed (Staging), Fixed (Production), Verified, Closed, Reopened, Won't Fix, Duplicate, Cannot Reproduce
```

**Category (Column G):**
```
Functionality, UI/UX, Performance, Security, Content, Compatibility, Accessibility, SEO, Forms, Navigation, Mobile, Integration
```

**Environment (Column N):**
```
Development, Staging, Production, All Environments
```

**Browser (Column R):**
```
Chrome, Firefox, Safari, Edge, Brave, Opera, Other
```

**Device (Column S):**
```
Desktop (Windows), Desktop (Mac), Desktop (Linux), Tablet (iPad), Tablet (Android), Mobile (iPhone), Mobile (Android), Other
```

---

### Step 3: Import to Smartsheet

1. Smartsheet → Create → Import → Google Sheets
2. Authorize and select your bug tracker sheet
3. Click "Import"

---

### Step 4: Link to Development Sheet

**⚠️ IMPORTANT:** Smartsheet dropdown cross-sheet references are STATIC snapshots. They DO NOT auto-update when new bugs are added. Use cell linking instead for automatic updates.

**Recommended Method: Cell Linking (Auto-Updates)**

1. **In Development Sheet:**
   - Add column: "Linked Bug ID"
   - Column Type: Text/Number (NOT Dropdown)

2. **To link a bug to task:**
   - Right-click cell in "Linked Bug ID" column
   - Select "Link to Cell in Another Sheet"
   - Choose Bug Tracker → Bug ID column → specific bug row
   - Click "Insert Link"

3. **Result:**
   - Cell shows linked Bug ID (e.g., "BUG-005")
   - Clickable link to navigate to bug details
   - Auto-updates if Bug ID changes

**Alternative: Manual Dropdown Refresh**

1. Column Type: Dropdown (single select)
2. Values: "Restrict to values from another sheet"
3. Select Bug Tracker → Bug ID column
4. **Update weekly:** Re-select sheet/column to refresh values

**See:** `SMARTSHEET_INTEGRATION_TROUBLESHOOTING.md` for detailed solutions

---

## 📊 Using the Python Helper Script

### Installation

No installation needed! Just Python 3.x.

### Run the Script

```bash
python bug_tracker_helper.py
```

### Menu Options

```
1. Add New Bug (Interactive) - Guided bug entry
2. View All Bugs - List all bugs in tracker
3. Generate Bug Report - Formatted report by status
4. View Bug Statistics - Metrics and counts
5. Get Bug IDs for Dropdown - Copy-paste list
6. Update Bug Status - Change bug status
7. Exit
```

---

## 🔧 Common Tasks

### Add a Bug via Python Script

```bash
python bug_tracker_helper.py
# Choose option 1
# Follow prompts
```

### Get Dropdown List

```bash
python bug_tracker_helper.py
# Choose option 5
# Copy the output to Smartsheet dropdown
```

### Update Bug Status

```bash
python bug_tracker_helper.py
# Choose option 6
# Enter Bug ID (e.g., BUG-001)
# Select new status
```

---

## 📝 Bug Template (Copy-Paste)

When reporting bugs manually:

```
Bug Title: [Short descriptive title]

Description:
[What is broken and why it matters]

Severity: [Critical/High/Medium/Low]
Priority: [Urgent/High/Medium/Low]
Category: [Functionality/UI/etc.]
Environment: [Development/Staging/Production]

Steps to Reproduce:
1. [First step]
2. [Second step]
3. [Third step]

Expected Behavior: [What should happen]
Actual Behavior: [What actually happens]

Browser: [Chrome/Firefox/Safari/etc.]
Device: [Desktop/Mobile/Tablet]
URL: [Full URL where bug occurs]
```

---

## 🔗 Integration Workflow

### Daily Workflow

1. **Bug Reported** → Add to Bug Tracker (Google Sheets or Python script)
2. **Bug Auto-Assigned ID** → BUG-XXX
3. **Developer Assigned** → Update "Assigned To" column
4. **Fix in Progress** → Update Status to "In Progress"
5. **Fix Deployed** → Update Status, add Linked Commit
6. **Bug Verified** → Update Status to "Verified"
7. **Bug Closed** → Update Status to "Closed"

### Linking to Development Sheet

When a development task is fixing a bug:

1. In Development Sheet, find the task row
2. Click "Linked Bug ID" dropdown
3. Select the bug (e.g., BUG-007)
4. Save

**Result:** Full traceability between bugs and tasks!

---

## 📈 Bug Metrics Dashboard (Optional)

### In Google Sheets

Add a "Dashboard" tab with these formulas:

**Total Bugs:**
```
=COUNTA(BugTracker!A:A)-1
```

**Open Bugs:**
```
=COUNTIF(BugTracker!F:F,"<>Closed")-COUNTIF(BugTracker!F:F,"<>Verified")
```

**Critical Bugs:**
```
=COUNTIF(BugTracker!D:D,"Critical")
```

**Bugs by Status Chart:**
```
=UNIQUE(BugTracker!F2:F)
=COUNTIF(BugTracker!F:F,DashboardCell)
```

---

## 🎯 Best Practices

### ✅ DO

- Report bugs as soon as you find them
- Provide clear reproduction steps
- Include screenshots or screen recordings
- Update bug status when working on fixes
- Link commits to bugs
- Verify fixes before closing

### ❌ DON'T

- Leave bugs in "New" status indefinitely
- Close bugs without verification
- Report feature requests as bugs
- Skip reproduction steps
- Forget to update "Actual Fix Date"

---

## 🆘 Troubleshooting

### Bug IDs not showing in Development Sheet dropdown

**Solution:** In Smartsheet, edit the dropdown column properties and re-select the Bug Tracker sheet as the data source.

### Python script error: "File not found"

**Solution:** Make sure you're running the script from the project directory where `X4O_Bug_Tracker.csv` exists.

### Google Sheets import shows garbled text

**Solution:** Re-import with encoding set to "UTF-8".

---

## 📞 Support

**Project Lead:** Keenan Husselmann
**Email:** khusselmann@x4o.co.za

---

**END OF QUICK GUIDE**
