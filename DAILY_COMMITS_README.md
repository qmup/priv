# Daily Commits Script

This script automatically creates 1-5 random commits per day in your repository.

## Setup

### Option 1: Automatic Setup (Recommended)
Run the setup script:
```bash
./setup_daily_commits.sh
```

This will:
- Add a cron job that runs daily at 11:59 PM
- Create a logs directory for output
- Set up automatic execution

### Option 2: Manual Setup
Add this line to your crontab (`crontab -e`):
```
59 23 * * * cd /Users/minhquan/Documents/Projects/priv && /usr/bin/python3 /Users/minhquan/Documents/Projects/priv/daily_commits.py >> /Users/minhquan/Documents/Projects/priv/logs/daily_commits.log 2>&1
```

## Manual Execution
You can also run the script manually at any time:
```bash
python3 daily_commits.py
```

## How It Works
- The script creates 1-5 random commits per day
- Each commit has a random time between 9 AM and 11 PM
- Commits are dated for the current day
- Each commit adds a line to `data.txt` with a timestamp

## Viewing Logs
Check the log file to see what commits were created:
```bash
cat logs/daily_commits.log
```

## Removing the Cron Job
To stop automatic commits:
```bash
crontab -l | grep -v 'daily_commits.py' | crontab -
```

Or edit your crontab:
```bash
crontab -e
```
Then remove the line containing `daily_commits.py`

