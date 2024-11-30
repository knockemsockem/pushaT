import os
from datetime import datetime, timedelta

def makeCommits(days: int):
    if days < 1:
        os.system('git push')  # Push all commits once finished
    else:
        # Calculate the date for each commit
        date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Write to the file
        with open('demo.txt', 'a') as file:
            file.write(f'{date} <- Commit Listed in a Day!\n')
        
        # Stage and commit the changes
        os.system('git add demo.txt')  # Stage the file
        os.system(f'git commit --date="{date}" -m "Commit on {date}"')  # Commit with a custom date
        
        # Recursive call
        makeCommits(days - 1)

# Calculate 1 year (365 days)
days_in_a_year = 365

# Start the commit process for the past year
makeCommits(days_in_a_year)
