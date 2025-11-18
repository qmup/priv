#!/bin/bash
# Setup script to add daily commits to crontab

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_PATH="/usr/bin/python3"
SCRIPT_PATH="$SCRIPT_DIR/daily_commits.py"

# Create a log directory if it doesn't exist
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p "$LOG_DIR"

# Cron job runs every day at 11:59 PM
# This ensures commits are created for the current day
CRON_JOB="59 23 * * * cd $SCRIPT_DIR && $PYTHON_PATH $SCRIPT_PATH >> $LOG_DIR/daily_commits.log 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "$SCRIPT_PATH"; then
    echo "Cron job already exists. Removing old entry..."
    crontab -l 2>/dev/null | grep -v "$SCRIPT_PATH" | crontab -
fi

# Add the new cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "✓ Daily commit cron job has been set up!"
echo "  - Script: $SCRIPT_PATH"
echo "  - Runs daily at 11:59 PM"
echo "  - Logs: $LOG_DIR/daily_commits.log"
echo ""
echo "To view your crontab: crontab -l"
echo "To remove the cron job: crontab -l | grep -v '$SCRIPT_PATH' | crontab -"

