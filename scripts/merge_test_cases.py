#!/usr/bin/env python3
"""Merge security test cases into main test case file."""

import csv
import os
from datetime import datetime

def merge_test_cases():
    """Merge SECURITY_TEST_CASES.csv into X4O_Test_Cases.csv"""

    # File paths
    main_file = 'X4O_Test_Cases.csv'
    security_file = 'docs/phase4-testing/SECURITY_TEST_CASES.csv'

    # Check if files exist
    if not os.path.exists(security_file):
        print(f"ERROR: Security test cases file not found: {security_file}")
        return False

    # Create backup of main file if it exists
    if os.path.exists(main_file):
        backup_date = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'X4O_Test_Cases_backup_{backup_date}.csv'

        print(f"Creating backup: {backup_file}")
        with open(main_file, 'r', encoding='utf-8') as src:
            with open(backup_file, 'w', encoding='utf-8', newline='') as dst:
                dst.write(src.read())
        print(f"  Backup created successfully")
    else:
        print(f"Main file does not exist, will create new: {main_file}")

    # Read security test cases
    print(f"\nReading security test cases from: {security_file}")
    security_cases = []
    with open(security_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        security_cases = list(reader)
    print(f"  Found {len(security_cases)} security test cases")

    # Append to main file or create new
    mode = 'a' if os.path.exists(main_file) else 'w'

    with open(main_file, mode, encoding='utf-8', newline='') as f:
        if mode == 'w':
            # Write header if creating new file
            fieldnames = security_cases[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            print(f"\nCreating new file: {main_file}")
        else:
            print(f"\nAppending to existing file: {main_file}")

        # Write security test cases
        writer = csv.DictWriter(f, fieldnames=security_cases[0].keys())
        writer.writerows(security_cases)

    print(f"  Added {len(security_cases)} test cases to {main_file}")
    print("\n" + "="*60)
    print("SUCCESS: Merge completed!")
    print("="*60)
    print(f"\nFiles:")
    print(f"  Main file: {main_file}")
    if os.path.exists(main_file):
        # Count total rows
        with open(main_file, 'r', encoding='utf-8') as f:
            total_rows = sum(1 for _ in f) - 1  # Exclude header
        print(f"  Total test cases: {total_rows}")

    if 'backup_file' in locals():
        print(f"  Backup: {backup_file}")

    print("\nPlease review the merged file to ensure data integrity.")
    return True

if __name__ == '__main__':
    merge_test_cases()
