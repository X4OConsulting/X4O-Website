@echo off
REM Merge security test cases into main test case file
REM Usage: Run this script from the project root directory

echo Merging security test cases into main test case file...

set MAIN_FILE=X4O_Test_Cases.csv
set SECURITY_FILE=docs\phase4-testing\SECURITY_TEST_CASES.csv
set BACKUP_FILE=X4O_Test_Cases_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%.csv

REM Create backup of main file
echo Creating backup: %BACKUP_FILE%
copy "%MAIN_FILE%" "%BACKUP_FILE%"

REM Append security test cases (skip header line)
echo Appending security test cases...
more +1 "%SECURITY_FILE%" >> "%MAIN_FILE%"

echo Done! Security test cases added to %MAIN_FILE%
echo Backup saved as: %BACKUP_FILE%
echo.
echo Please review the merged file to ensure data integrity.
pause
