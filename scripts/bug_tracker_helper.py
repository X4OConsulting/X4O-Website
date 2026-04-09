"""
X4O Bug Tracker Helper Script
Automates bug ID generation and provides utilities for bug tracker management
"""

import csv
from datetime import datetime
from typing import List, Dict
import os

class BugTrackerManager:
    def __init__(self, csv_file='X4O_Bug_Tracker.csv'):
        self.csv_file = csv_file
        self.bugs = []
        self.load_bugs()

    def load_bugs(self):
        """Load existing bugs from CSV file"""
        if not os.path.exists(self.csv_file):
            print(f"Warning: {self.csv_file} not found. Creating new tracker.")
            self.bugs = []
            return

        with open(self.csv_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            self.bugs = list(reader)

        print(f"Loaded {len(self.bugs)} bugs from {self.csv_file}")

    def get_next_bug_id(self) -> str:
        """Generate next sequential bug ID"""
        if not self.bugs:
            return "BUG-001"

        # Extract numeric part from all bug IDs
        bug_numbers = []
        for bug in self.bugs:
            bug_id = bug.get('Bug ID', '')
            if bug_id.startswith('BUG-'):
                try:
                    num = int(bug_id.split('-')[1])
                    bug_numbers.append(num)
                except (IndexError, ValueError):
                    continue

        if not bug_numbers:
            return "BUG-001"

        next_num = max(bug_numbers) + 1
        return f"BUG-{next_num:03d}"

    def add_bug(self, bug_data: Dict) -> str:
        """Add a new bug to the tracker"""
        # Generate bug ID if not provided
        if 'Bug ID' not in bug_data or not bug_data['Bug ID']:
            bug_data['Bug ID'] = self.get_next_bug_id()

        # Set reported date if not provided
        if 'Reported Date' not in bug_data or not bug_data['Reported Date']:
            bug_data['Reported Date'] = datetime.now().strftime('%Y-%m-%d')

        # Set default status if not provided
        if 'Status' not in bug_data or not bug_data['Status']:
            bug_data['Status'] = 'New'

        # Add bug to list
        self.bugs.append(bug_data)

        # Save to CSV
        self.save_bugs()

        print(f"Added bug: {bug_data['Bug ID']} - {bug_data.get('Bug Title', 'Untitled')}")
        return bug_data['Bug ID']

    def save_bugs(self):
        """Save all bugs to CSV file"""
        if not self.bugs:
            print("No bugs to save.")
            return

        # Get all unique column names from all bugs
        all_columns = set()
        for bug in self.bugs:
            all_columns.update(bug.keys())

        # Define column order (standard columns first)
        standard_columns = [
            'Bug ID', 'Bug Title', 'Description', 'Severity', 'Priority', 'Status', 'Category',
            'Reported By', 'Reported Date', 'Assigned To', 'Target Fix Date', 'Actual Fix Date',
            'Resolution', 'Environment', 'Steps to Reproduce', 'Expected Behavior', 'Actual Behavior',
            'Browser', 'Device', 'URL', 'Related Task ID', 'Linked Commit', 'Testing Notes',
            'Verified By', 'Verified Date'
        ]

        # Add any extra columns not in standard list
        extra_columns = sorted(all_columns - set(standard_columns))
        fieldnames = standard_columns + extra_columns

        with open(self.csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.bugs)

        print(f"Saved {len(self.bugs)} bugs to {self.csv_file}")

    def get_bug_by_id(self, bug_id: str) -> Dict:
        """Get bug details by ID"""
        for bug in self.bugs:
            if bug.get('Bug ID') == bug_id:
                return bug
        return None

    def update_bug_status(self, bug_id: str, new_status: str, **kwargs):
        """Update bug status and optionally other fields"""
        bug = self.get_bug_by_id(bug_id)
        if not bug:
            print(f"Bug {bug_id} not found.")
            return False

        bug['Status'] = new_status

        # Update additional fields if provided
        for key, value in kwargs.items():
            bug[key] = value

        # Auto-set dates based on status
        if new_status in ['Fixed (Staging)', 'Fixed (Production)'] and not bug.get('Actual Fix Date'):
            bug['Actual Fix Date'] = datetime.now().strftime('%Y-%m-%d')

        if new_status == 'Verified' and not bug.get('Verified Date'):
            bug['Verified Date'] = datetime.now().strftime('%Y-%m-%d')

        self.save_bugs()
        print(f"Updated {bug_id} status to: {new_status}")
        return True

    def get_bug_list_for_dropdown(self) -> str:
        """Generate comma-separated list of bug IDs for dropdown"""
        bug_ids = [bug['Bug ID'] for bug in self.bugs if bug.get('Bug ID')]
        bug_ids.sort()
        return ', '.join(bug_ids)

    def generate_bug_report(self, status_filter: str = None) -> str:
        """Generate a formatted bug report"""
        filtered_bugs = self.bugs

        if status_filter:
            filtered_bugs = [b for b in self.bugs if b.get('Status') == status_filter]

        report = []
        report.append("=" * 80)
        report.append("X4O BUG TRACKER REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Bugs: {len(self.bugs)}")

        if status_filter:
            report.append(f"Filter: Status = {status_filter}")
            report.append(f"Matching Bugs: {len(filtered_bugs)}")

        report.append("=" * 80)
        report.append("")

        # Group by status
        status_groups = {}
        for bug in filtered_bugs:
            status = bug.get('Status', 'Unknown')
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(bug)

        for status, bugs in sorted(status_groups.items()):
            report.append(f"\n{status.upper()} ({len(bugs)} bugs)")
            report.append("-" * 80)

            for bug in bugs:
                report.append(f"{bug.get('Bug ID', 'N/A')}: {bug.get('Bug Title', 'Untitled')}")
                report.append(f"  Severity: {bug.get('Severity', 'N/A')} | Priority: {bug.get('Priority', 'N/A')}")
                report.append(f"  Reported: {bug.get('Reported Date', 'N/A')} by {bug.get('Reported By', 'N/A')}")
                if bug.get('Assigned To'):
                    report.append(f"  Assigned To: {bug.get('Assigned To')}")
                report.append("")

        return '\n'.join(report)

    def get_bug_stats(self) -> Dict:
        """Calculate bug statistics"""
        stats = {
            'total': len(self.bugs),
            'by_status': {},
            'by_severity': {},
            'by_priority': {},
            'by_category': {},
            'open': 0,
            'closed': 0
        }

        for bug in self.bugs:
            status = bug.get('Status', 'Unknown')
            severity = bug.get('Severity', 'Unknown')
            priority = bug.get('Priority', 'Unknown')
            category = bug.get('Category', 'Unknown')

            # Count by status
            stats['by_status'][status] = stats['by_status'].get(status, 0) + 1

            # Count by severity
            stats['by_severity'][severity] = stats['by_severity'].get(severity, 0) + 1

            # Count by priority
            stats['by_priority'][priority] = stats['by_priority'].get(priority, 0) + 1

            # Count by category
            stats['by_category'][category] = stats['by_category'].get(category, 0) + 1

            # Count open vs closed
            if status in ['Closed', 'Verified', "Won't Fix"]:
                stats['closed'] += 1
            else:
                stats['open'] += 1

        return stats


def interactive_add_bug():
    """Interactive CLI for adding a new bug"""
    print("\n" + "=" * 80)
    print("ADD NEW BUG")
    print("=" * 80)

    tracker = BugTrackerManager()

    bug_data = {}

    # Bug Title (required)
    bug_data['Bug Title'] = input("\nBug Title (required): ").strip()
    if not bug_data['Bug Title']:
        print("Error: Bug title is required.")
        return

    # Description (required)
    print("\nDescription (required):")
    print("(Enter description, press Enter twice when done)")
    description_lines = []
    while True:
        line = input()
        if line == "" and description_lines:
            break
        description_lines.append(line)
    bug_data['Description'] = '\n'.join(description_lines)

    # Severity (dropdown)
    print("\nSeverity:")
    print("1. Critical")
    print("2. High")
    print("3. Medium")
    print("4. Low")
    severity_choice = input("Choose (1-4) [default: 3]: ").strip() or "3"
    severity_map = {"1": "Critical", "2": "High", "3": "Medium", "4": "Low"}
    bug_data['Severity'] = severity_map.get(severity_choice, "Medium")

    # Priority (dropdown)
    print("\nPriority:")
    print("1. Urgent")
    print("2. High")
    print("3. Medium")
    print("4. Low")
    priority_choice = input("Choose (1-4) [default: 3]: ").strip() or "3"
    priority_map = {"1": "Urgent", "2": "High", "3": "Medium", "4": "Low"}
    bug_data['Priority'] = priority_map.get(priority_choice, "Medium")

    # Category (dropdown)
    print("\nCategory:")
    categories = ["Functionality", "UI/UX", "Performance", "Security", "Content",
                  "Compatibility", "Accessibility", "SEO", "Forms", "Navigation",
                  "Mobile", "Integration"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    cat_choice = input(f"Choose (1-{len(categories)}) [default: 1]: ").strip() or "1"
    try:
        bug_data['Category'] = categories[int(cat_choice) - 1]
    except (ValueError, IndexError):
        bug_data['Category'] = "Functionality"

    # Reported By
    bug_data['Reported By'] = input("\nReported By (name): ").strip() or "Unknown"

    # Environment
    print("\nEnvironment:")
    print("1. Development")
    print("2. Staging")
    print("3. Production")
    print("4. All Environments")
    env_choice = input("Choose (1-4) [default: 3]: ").strip() or "3"
    env_map = {"1": "Development", "2": "Staging", "3": "Production", "4": "All Environments"}
    bug_data['Environment'] = env_map.get(env_choice, "Production")

    # Steps to Reproduce
    print("\nSteps to Reproduce (one per line, empty line to finish):")
    steps = []
    step_num = 1
    while True:
        step = input(f"{step_num}. ").strip()
        if not step:
            break
        steps.append(f"{step_num}. {step}")
        step_num += 1
    bug_data['Steps to Reproduce'] = '\n'.join(steps)

    # Expected Behavior
    bug_data['Expected Behavior'] = input("\nExpected Behavior: ").strip()

    # Actual Behavior
    bug_data['Actual Behavior'] = input("Actual Behavior: ").strip()

    # URL
    bug_data['URL'] = input("\nURL (optional): ").strip()

    # Browser
    bug_data['Browser'] = input("Browser (optional, e.g., Chrome, Firefox): ").strip()

    # Device
    bug_data['Device'] = input("Device (optional, e.g., Desktop, Mobile): ").strip()

    # Add the bug
    bug_id = tracker.add_bug(bug_data)

    print("\n" + "=" * 80)
    print(f"SUCCESS! Bug created: {bug_id}")
    print("=" * 80)
    print(f"\nBug ID: {bug_id}")
    print(f"Title: {bug_data['Bug Title']}")
    print(f"Severity: {bug_data['Severity']}")
    print(f"Priority: {bug_data['Priority']}")
    print(f"Status: New")
    print("\nBug has been saved to X4O_Bug_Tracker.csv")


def main():
    """Main menu"""
    while True:
        print("\n" + "=" * 80)
        print("X4O BUG TRACKER HELPER")
        print("=" * 80)
        print("\n1. Add New Bug (Interactive)")
        print("2. View All Bugs")
        print("3. Generate Bug Report")
        print("4. View Bug Statistics")
        print("5. Get Bug IDs for Dropdown")
        print("6. Update Bug Status")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            interactive_add_bug()

        elif choice == "2":
            tracker = BugTrackerManager()
            if not tracker.bugs:
                print("\nNo bugs in tracker.")
            else:
                print("\n" + "=" * 80)
                print("ALL BUGS")
                print("=" * 80)
                for bug in tracker.bugs:
                    print(f"\n{bug.get('Bug ID')}: {bug.get('Bug Title')}")
                    print(f"  Status: {bug.get('Status')} | Severity: {bug.get('Severity')} | Priority: {bug.get('Priority')}")
                    print(f"  Reported: {bug.get('Reported Date')} by {bug.get('Reported By')}")

        elif choice == "3":
            tracker = BugTrackerManager()
            print("\nFilter by status? (leave blank for all)")
            status = input("Status: ").strip()
            report = tracker.generate_bug_report(status if status else None)
            print("\n" + report)

        elif choice == "4":
            tracker = BugTrackerManager()
            stats = tracker.get_bug_stats()

            print("\n" + "=" * 80)
            print("BUG STATISTICS")
            print("=" * 80)
            print(f"\nTotal Bugs: {stats['total']}")
            print(f"Open: {stats['open']} | Closed: {stats['closed']}")

            print("\nBy Status:")
            for status, count in sorted(stats['by_status'].items()):
                print(f"  {status}: {count}")

            print("\nBy Severity:")
            for severity, count in sorted(stats['by_severity'].items()):
                print(f"  {severity}: {count}")

            print("\nBy Priority:")
            for priority, count in sorted(stats['by_priority'].items()):
                print(f"  {priority}: {count}")

            print("\nBy Category:")
            for category, count in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {category}: {count}")

        elif choice == "5":
            tracker = BugTrackerManager()
            bug_list = tracker.get_bug_list_for_dropdown()
            print("\n" + "=" * 80)
            print("BUG IDS FOR DROPDOWN")
            print("=" * 80)
            print("\nCopy this list into Smartsheet dropdown values:")
            print("\n" + bug_list)

        elif choice == "6":
            tracker = BugTrackerManager()
            bug_id = input("\nBug ID to update: ").strip()

            bug = tracker.get_bug_by_id(bug_id)
            if not bug:
                print(f"Bug {bug_id} not found.")
                continue

            print(f"\nCurrent status: {bug.get('Status')}")
            print("\nNew Status:")
            statuses = ["New", "Confirmed", "In Progress", "Fixed (Staging)",
                       "Fixed (Production)", "Verified", "Closed", "Reopened",
                       "Won't Fix", "Duplicate", "Cannot Reproduce"]
            for i, status in enumerate(statuses, 1):
                print(f"{i}. {status}")

            status_choice = input(f"\nChoose (1-{len(statuses)}): ").strip()
            try:
                new_status = statuses[int(status_choice) - 1]
            except (ValueError, IndexError):
                print("Invalid choice.")
                continue

            # Optional fields
            assigned_to = input("\nAssigned To (leave blank to skip): ").strip()
            linked_commit = input("Linked Commit (leave blank to skip): ").strip()

            kwargs = {}
            if assigned_to:
                kwargs['Assigned To'] = assigned_to
            if linked_commit:
                kwargs['Linked Commit'] = linked_commit

            tracker.update_bug_status(bug_id, new_status, **kwargs)

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please choose 1-7.")


if __name__ == "__main__":
    main()
