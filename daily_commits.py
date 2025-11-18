#!/usr/bin/env python3
"""
Daily Learning & Notes - Automated commit script
Creates meaningful daily entries across different categories
"""
import subprocess
import random
from datetime import datetime
import os
import sys

# Get the repository directory (where this script is located)
repo_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(repo_dir)

# Content templates for different categories
LEARNING_TOPICS = [
    "Python", "JavaScript", "TypeScript", "React", "Vue", "Node.js",
    "Docker", "Kubernetes", "AWS", "Git", "Linux", "Algorithms",
    "Data Structures", "Machine Learning", "Web Development", "System Design",
    "Database Design", "API Development", "Testing", "DevOps", "Security",
    "Performance Optimization", "Clean Code", "Design Patterns", "Architecture"
]

LEARNING_ENTRIES = [
    "Exploring {topic} fundamentals",
    "Deep dive into {topic} best practices",
    "Understanding {topic} concepts",
    "Learning {topic} patterns and techniques",
    "Researching {topic} implementation strategies",
    "Studying {topic} architecture",
    "Practicing {topic} skills",
    "Reviewing {topic} documentation"
]

NOTE_TOPICS = [
    "Project insights", "Workflow improvements", "Problem-solving approach",
    "Team collaboration", "Time management", "Productivity tips",
    "Technical decisions", "Architecture thoughts", "Code review notes",
    "Debugging strategies", "Learning methods", "Career development"
]

CODE_SNIPPETS = [
    "Useful utility function",
    "Helper function for common task",
    "Code pattern example",
    "Solution to common problem",
    "Performance optimization technique",
    "Clean code example",
    "Best practice implementation"
]

QUOTES = [
    "The only way to learn is to live.",
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "The best way to get a project done faster is to start sooner.",
    "Programs must be written for people to read, and only incidentally for machines to execute.",
    "The most important property of a program is whether it accomplishes the intention of its user.",
    "Simplicity is the ultimate sophistication.",
    "Make it work, make it right, make it fast.",
    "The best code is no code at all."
]

def create_learning_entry(date_str):
    """Create a learning entry"""
    topic = random.choice(LEARNING_TOPICS)
    entry_template = random.choice(LEARNING_ENTRIES)
    entry = entry_template.format(topic=topic)
    
    filename = f"learning/{date_str}.md"
    content = f"""# {entry}

**Date:** {date_str}
**Topic:** {topic}

## What I Learned

Today I focused on {entry.lower()}. This is an important area to explore and understand better.

## Key Takeaways

- Understanding the fundamentals is crucial
- Practice makes perfect
- Documentation is your friend

## Next Steps

- Continue exploring {topic}
- Build a small project to practice
- Share knowledge with others

---
*Generated automatically as part of daily learning routine*
"""
    return filename, content, f"📚 Learning: {entry}"

def create_note_entry(date_str, commit_num):
    """Create a note entry"""
    topic = random.choice(NOTE_TOPICS)
    
    filename = f"notes/{date_str}-{commit_num:02d}.md"
    content = f"""# {topic}

**Date:** {date_str}

## Thoughts

Today I reflected on {topic.lower()}. This is something worth documenting and revisiting.

## Insights

- Important observation or insight
- Another key point to remember
- Action item or follow-up

## Related

Consider how this relates to other areas of work and learning.

---
*Daily note entry*
"""
    return filename, content, f"📝 Note: {topic}"

def create_code_snippet(date_str, commit_num):
    """Create a code snippet entry"""
    snippet_type = random.choice(CODE_SNIPPETS)
    
    filename = f"code-snippets/{date_str}-{commit_num:02d}.md"
    content = f"""# {snippet_type}

**Date:** {date_str}
**Type:** Code Snippet

## Description

A useful code example for reference.

## Code

```python
def example_function():
    \"\"\"
    Example function demonstrating best practices.
    \"\"\"
    # Your code here
    result = process_data()
    return result
```

## Usage

```python
# Example usage
result = example_function()
```

## Notes

- Why this approach is useful
- When to use this pattern
- Potential improvements

---
*Code snippet for future reference*
"""
    return filename, content, f"💻 Code: {snippet_type}"

def create_quote_entry(date_str):
    """Create a quote entry"""
    quote = random.choice(QUOTES)
    
    filename = f"quotes/{date_str}.md"
    content = f"""# Daily Quote

**Date:** {date_str}

> {quote}

## Reflection

This quote resonates because it reminds us of important principles in our work and life.

---
*Inspirational quote*
"""
    return filename, content, f"💬 Quote: {quote[:50]}..."

# Get today's date
today = datetime.now()
date_str = today.strftime('%Y-%m-%d')

# Randomly choose 1-5 commits for today
num_commits = random.randint(1, 5)

commit_count = 0
created_files = []

for i in range(num_commits):
    # Generate a random time during the day (between 9 AM and 11 PM)
    hour = random.randint(9, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    commit_datetime = today.replace(hour=hour, minute=minute, second=second)
    git_date_str = commit_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    # Choose content type based on commit number
    if i == 0:
        # First commit is always a learning entry
        filename, content, commit_message = create_learning_entry(date_str)
    elif i == num_commits - 1 and random.random() < 0.3:
        # Last commit might be a quote
        filename, content, commit_message = create_quote_entry(date_str)
    elif random.random() < 0.4:
        # 40% chance for code snippet
        filename, content, commit_message = create_code_snippet(date_str, i)
    else:
        # Otherwise, a note
        filename, content, commit_message = create_note_entry(date_str, i)
    
    # Create the file
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(content)
        
        created_files.append(filename)
        
        # Stage the file
        subprocess.run(['git', 'add', filename], check=True, 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Create commit with the specific date
        subprocess.run([
            'git', 'commit', 
            '--date', git_date_str,
            '-m', commit_message
        ], check=True, 
        env={**os.environ, 'GIT_AUTHOR_DATE': git_date_str, 'GIT_COMMITTER_DATE': git_date_str},
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        commit_count += 1
        print(f"Created commit {commit_count}: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating commit: {e}", file=sys.stderr)
        continue
    except Exception as e:
        print(f"Error creating file {filename}: {e}", file=sys.stderr)
        continue

if commit_count > 0:
    print(f"\nTotal commits created today: {commit_count}")
    print(f"Files created: {', '.join(created_files)}")
    
    # Push to remote repository
    try:
        subprocess.run(['git', 'push', 'origin', 'main'], check=True,
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✓ Successfully pushed commits to remote repository")
    except subprocess.CalledProcessError as e:
        print(f"⚠ Warning: Failed to push to remote: {e}", file=sys.stderr)
        print("  Commits were created locally but not pushed.")
else:
    print("No commits were created.")
