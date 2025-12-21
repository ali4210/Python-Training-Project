# 🚀 Python DevOps Quick Reference Card
## Essential Commands & Patterns for Daily Use

---

## 📋 TABLE OF CONTENTS

1. [Python Basics](#1-python-basics)
2. [Data Structures](#2-data-structures)
3. [File Operations](#3-file-operations)
4. [JSON & CSV](#4-json--csv)
5. [SSH/SFTP (Paramiko)](#5-sshsftp-paramiko)
6. [MySQL Database](#6-mysql-database)
7. [Email Automation](#7-email-automation)
8. [Task Scheduling](#8-task-scheduling)
9. [Regular Expressions](#9-regular-expressions)
10. [Error Handling](#10-error-handling)
11. [Common Patterns](#11-common-patterns)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. PYTHON BASICS

### Print & Variables
```python
# Basic print
print("Hello World")

# F-strings (preferred)
name = "Saleem"
print(f"Hello {name}")

# Multiple values
print("Name:", name, "Age:", 25)
```

### Data Types
```python
# String
text = "Hello"

# Integer
age = 25

# Float
price = 19.99

# Boolean
is_active = True

# Check type
type(age)  # <class 'int'>
```

### String Operations
```python
# Common methods
text.upper()          # "HELLO"
text.lower()          # "hello"
text.strip()          # Remove whitespace
text.split(",")       # Split into list
",".join(['a','b'])   # Join list: "a,b"
text.replace('H','J') # "Jello"
```

---

## 2. DATA STRUCTURES

### Lists (Mutable)
```python
# Create
servers = ["web1", "web2", "db1"]

# Access
servers[0]           # "web1"
servers[-1]          # "db1" (last)

# Modify
servers.append("cache1")
servers.extend(["app1", "app2"])
servers.insert(0, "lb1")
servers.remove("web1")
servers.pop()        # Remove last
servers.sort()
servers.reverse()

# Slicing
servers[0:2]         # First 2
servers[::-1]        # Reverse
```

### Dictionaries (Key-Value)
```python
# Create
config = {"host": "localhost", "port": 3306}

# Access
config["host"]                    # "localhost"
config.get("user", "default")     # Safe with default

# Modify
config["database"] = "alnafi"
config.update({"timeout": 30})
config.pop("port")

# Iteration
for key, value in config.items():
    print(f"{key}: {value}")
```

### Tuples (Immutable)
```python
# Create
server = ("192.168.1.10", 22, "active")

# Access
server[0]    # "192.168.1.10"
server[-1]   # "active"

# Convert
list(server)  # To list
```

### Sets (Unique)
```python
# Create
ips = {" 192.168.1.1", "192.168.1.2"}

# Add/Remove
ips.add("192.168.1.3")
ips.remove("192.168.1.1")

# Operations
set_a | set_b    # Union
set_a & set_b    # Intersection
set_a - set_b    # Difference
```

---

## 3. FILE OPERATIONS

### Read File
```python
# Method 1: Context manager (best)
with open("config.txt", "r") as f:
    content = f.read()

# Method 2: Read lines
with open("servers.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

### Write File
```python
# Overwrite
with open("output.txt", "w") as f:
    f.write("Hello World\n")

# Append
with open("log.txt", "a") as f:
    f.write(f"[{datetime.now()}] Event occurred\n")
```

### File Modes
```
'r'  - Read (default)
'w'  - Write (overwrite)
'a'  - Append
'r+' - Read and write
'b'  - Binary mode
```

---

## 4. JSON & CSV

### JSON
```python
import json

# Read JSON
with open("config.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

# String conversion
json_str = json.dumps(data)
data = json.loads(json_str)
```

### CSV
```python
import csv

# Read CSV
with open("servers.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        print(row[0], row[1])

# Write CSV
with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "IP", "Status"])
    writer.writerows(data)

# Dictionary CSV
with open("data.csv", "w", newline='') as f:
    fieldnames = ["name", "ip", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)
```

---

## 5. SSH/SFTP (PARAMIKO)

### SSH Connection
```python
import paramiko

# Connect
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.1.10", username="user", password="pass")

# Execute command
stdin, stdout, stderr = client.exec_command("df -h")
output = stdout.read().decode()
print(output)

# Close
client.close()
```

### SFTP Operations
```python
# Open SFTP
sftp = client.open_sftp()

# Download
sftp.get('/remote/file.txt', 'local_file.txt')

# Upload
sftp.put('local_file.txt', '/remote/file.txt')

# List files
files = sftp.listdir('/path')

# File info
stats = sftp.stat('/path/file.txt')
print(stats.st_size)

# Close
sftp.close()
```

---

## 6. MYSQL DATABASE

### Connection
```python
import mysql.connector

# Connect
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)
cursor = db.cursor()
```

### CRUD Operations
```python
# SELECT
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
for row in results:
    print(row)

# Single row
result = cursor.fetchone()

# INSERT (parameterized - secure!)
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("John", "john@example.com")
cursor.execute(sql, values)
db.commit()

# UPDATE
sql = "UPDATE users SET email = %s WHERE id = %s"
cursor.execute(sql, ("newemail@example.com", 1))
db.commit()

# DELETE
sql = "DELETE FROM users WHERE id = %s"
cursor.execute(sql, (1,))
db.commit()

# Close
cursor.close()
db.close()
```

---

## 7. EMAIL AUTOMATION

### Basic Email
```python
import smtplib
from email.message import EmailMessage

# Setup
msg = EmailMessage()
msg['Subject'] = 'Alert: Server Down'
msg['From'] = 'admin@example.com'
msg['To'] = 'team@example.com'
msg['Cc'] = 'manager@example.com'
msg.set_content('Server web1 is not responding')

# Send
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('admin@example.com', 'app_password')
    server.send_message(msg)
```

### Email with Attachment
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = 'Daily Report'
msg['From'] = 'admin@example.com'
msg['To'] = 'team@example.com'

# Body
body = "Please find attached daily report"
msg.attach(MIMEText(body, 'plain'))

# Attachment
filename = "report.pdf"
with open(filename, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

# Send
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('admin@example.com', 'app_password')
    server.send_message(msg)
```

### HTML Email
```python
html = """
<html>
  <body>
    <h1>Server Report</h1>
    <p><b>Status:</b> All systems operational</p>
  </body>
</html>
"""
msg.attach(MIMEText(html, 'html'))
```

---

## 8. TASK SCHEDULING

### Schedule Library
```python
import schedule
import time

def job():
    print("Running scheduled task...")
    # Your code here

# Schedule patterns
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.at("09:00").do(job)

# Run
while True:
    schedule.run_pending()
    time.sleep(1)
```

### Datetime
```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
today = datetime.today()

# Format
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
date_only = now.strftime("%Y-%m-%d")
time_only = now.strftime("%H:%M:%S")

# Parse
dt = datetime.strptime("2025-12-20 15:30", "%Y-%m-%d %H:%M")

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
```

---

## 9. REGULAR EXPRESSIONS

### Common Patterns
```python
import re

text = "Server IP: 192.168.1.10, Status: OK"

# Find all matches
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
# ['192.168.1.10']

# Search (first match)
match = re.search(r'Status: (\w+)', text)
if match:
    status = match.group(1)  # 'OK'

# Replace
new_text = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'REDACTED', text)

# Split
parts = re.split(r',\s*', text)

# Match (from start)
if re.match(r'^Server', text):
    print("Starts with Server")
```

### Useful Regex Patterns
```python
# IP Address
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Email
r'[\w.-]+@[\w.-]+\.\w+'

# Date (YYYY-MM-DD)
r'\d{4}-\d{2}-\d{2}'

# Time (HH:MM:SS)
r'\d{2}:\d{2}:\d{2}'

# Word boundary
r'\bword\b'

# Any number
r'\d+'

# Any word
r'\w+'
```

---

## 10. ERROR HANDLING

### Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")
```

### Specific Exceptions
```python
try:
    # Code here
    pass
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError as e:
    print(f"Key {e} not found")
except ValueError as e:
    print(f"Invalid value: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Logging
```python
import logging

# Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Use
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

---

## 11. COMMON PATTERNS

### Command Line Arguments
```python
import argparse

parser = argparse.ArgumentParser(description='Server Monitor')
parser.add_argument('--host', required=True, help='Server hostname')
parser.add_argument('--port', type=int, default=22, help='SSH port')
parser.add_argument('--verbose', action='store_true', help='Verbose output')

args = parser.parse_args()

print(f"Connecting to {args.host}:{args.port}")
if args.verbose:
    print("Verbose mode enabled")
```

### Environment Variables
```python
import os

# Get
db_host = os.getenv('DB_HOST', 'localhost')  # Default if not set
api_key = os.environ['API_KEY']  # Raises error if not set

# Set
os.environ['DEBUG'] = 'True'

# Check if exists
if 'API_KEY' in os.environ:
    print("API key is set")
```

### Config Files
```python
import json

# Load config
with open('config.json') as f:
    config = json.load(f)

# Access nested values
db_config = config.get('database', {})
host = db_config.get('host', 'localhost')
```

---

## 12. TROUBLESHOOTING

### Common Errors & Solutions

**ImportError: No module named 'module'**
```bash
pip install module_name
```

**Permission Denied (File)**
```python
# Check permissions
os.chmod('file.txt', 0o644)
```

**Connection Refused (SSH)**
```python
# Check:
# 1. SSH service running: sudo systemctl status ssh
# 2. Firewall: sudo ufw allow 22
# 3. Correct IP/credentials
```

**MySQL Connection Error**
```python
# Check:
# 1. MySQL running: sudo systemctl status mysql
# 2. User exists: SHOW GRANTS FOR 'user'@'localhost';
# 3. Firewall: sudo ufw allow 3306
```

**Email Send Failure**
```python
# Gmail:
# 1. Enable 2FA
# 2. Generate app password
# 3. Use port 587 with TLS
```

### Debug Print Statements
```python
# Quick debugging
print(f"DEBUG: variable = {variable}")
print(f"DEBUG: type = {type(variable)}")
print(f"DEBUG: len = {len(variable)}")
print(f"DEBUG: dir = {dir(variable)}")
```

### Check Python/Package Versions
```bash
python --version
pip --version
pip show package_name
pip list
```

---

## 🎯 QUICK TIPS

### Performance
- Use list comprehensions instead of loops
- Use `with` statements for file operations
- Close connections explicitly
- Use parameterized queries (SQL)

### Security
- Never hardcode passwords
- Use environment variables
- Implement error handling
- Validate all inputs
- Use parameterized SQL queries

### Best Practices
- Write functions for reusable code
- Add docstrings to functions
- Use meaningful variable names
- Follow PEP 8 style guide
- Test your code
- Document everything

---

## 📚 USEFUL COMMANDS

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Deactivate
deactivate

# Requirements
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Testing
```bash
# Run pytest
pytest

# With coverage
pytest --cov=.

# Specific file
pytest test_file.py

# Verbose
pytest -v
```

---

## 🔗 RESOURCES

- **Python Docs:** https://docs.python.org
- **Paramiko Docs:** http://docs.paramiko.org
- **MySQL Connector:** https://dev.mysql.com/doc/connector-python
- **Regex Tester:** https://regex101.com
- **PEP 8 Style:** https://pep8.org

---

**💡 Pro Tip:** Keep this reference card handy while coding. Print it out or save it as a bookmark for quick access!
