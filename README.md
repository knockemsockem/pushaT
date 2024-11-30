---

# Git Commit Automator

This script generates backdated Git commits for educational and experimental purposes. It allows you to create commits for the past year (or any specified range of days), which can be useful for populating your GitHub contribution graph.

## Disclaimer

> This script is for educational and knowledge purposes only. Use it responsibly and ensure that you comply with the terms and conditions of the platforms you interact with.

## Features

- Generates backdated Git commits.
- Automates file modification, staging, and committing.
- Pushes all commits to a remote repository.

## Prerequisites

Before using this script, ensure the following:
1. You have Python installed on your system.
2. Git is installed and properly configured.
3. You are in a Git repository, and the repository is connected to a remote origin.

## How to Use

1. Clone or download this repository.
2. Navigate to the directory in your terminal.
3. Ensure the script has write permissions to the file `demo.txt`.
4. Run the script:

   ```bash
   python main.py
   ```

   This will generate backdated commits for the past year.

## Script Breakdown

### How It Works:
1. **Date Calculation**: 
   - The script calculates dates for the past year using Python’s `datetime` and `timedelta` modules.
2. **File Modification**:
   - It writes to `demo.txt` for each backdated day.
3. **Git Operations**:
   - Stages and commits changes for each date.
   - Pushes all commits at the end of the process.

### Key Functions:
- **`makeCommits(days: int)`**:
   - Recursively generates commits for the specified number of days.

### Customization:
- Change the `days_in_a_year` variable in the script to modify the number of backdated days.
- Edit commit messages in the `git commit` command within the script.

## Example Output

- Sample `demo.txt` contents after running the script:
  ```
  2023-12-01 <- Commit Listed in a Day!
  2023-11-30 <- Commit Listed in a Day!
  ...
  ```

- Git commit log:
  ```bash
  $ git log --oneline
  abc123 Commit on 2023-12-01
  def456 Commit on 2023-11-30
  ...
  ```

## Notes

- Ensure the repository is public and commits are pushed to the main branch to reflect on the GitHub contribution graph.
- This script simulates activity but does not represent actual project contributions.

---
