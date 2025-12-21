# 🐍 Python Training & DevOps Automation Suite

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![DevOps](https://img.shields.io/badge/DevOps-Automation-orange?style=for-the-badge&logo=linux)
![AIOps](https://img.shields.io/badge/AIOps-Training-green?style=for-the-badge&logo=artifactory)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

**Comprehensive Python training project for DevOps & SRE professionals**

[📚 Master Guide](#-master-guide) • [🚀 Quick Start](#-quick-start) • [💼 Projects](#-featured-projects) • [📖 Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technologies](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Featured Projects](#-featured-projects)
- [Learning Path](#-learning-path)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

This repository contains a **complete Python training curriculum** designed specifically for DevOps, AIOps, and SRE roles. With **51 hands-on scripts and projects**, it covers everything from Python fundamentals to advanced automation workflows used in production environments.

### 🎓 Educational Background

- **Institution:** Al-Nafi International College (Online Program)
- **Course:** AIOps (Artificial Intelligence Operations)
- **Previous Education:** Computer Science & Engineering at BRAC University, Bangladesh
- **Focus:** Python automation for DevOps/SRE infrastructure management

### 💡 Purpose

This project serves as both a **learning resource** and a **professional portfolio** showcasing practical Python skills for:
- Infrastructure automation
- Server management
- Database operations
- Monitoring and alerting
- CI/CD pipeline scripting

---

## ✨ Features

### 🔧 Core Python Skills

- ✅ **Data Structures** - Lists, tuples, dictionaries, sets with real-world applications
- ✅ **File Handling** - Text, CSV, JSON processing for configuration management
- ✅ **Functions & OOP** - Modular, reusable code with object-oriented design
- ✅ **Error Handling** - Production-grade exception management
- ✅ **Regular Expressions** - Log parsing and pattern matching

### 🚀 DevOps Automation

- ✅ **Remote Server Management** - SSH/SFTP automation with Paramiko
- ✅ **Database Operations** - MySQL CRUD operations for data persistence
- ✅ **Email Automation** - SMTP notifications with attachments and HTML
- ✅ **Task Scheduling** - Automated workflows with scheduled jobs
- ✅ **Encryption & Security** - Cryptography implementation for secrets management

### 📊 Real-World Projects

- ✅ **Server Health Monitoring** - Automated system checks with email alerts
- ✅ **CSV to MySQL Pipeline** - Data processing and database integration
- ✅ **CLI Data Processor** - Command-line tool with API integration
- ✅ **Automated Reporting** - Scheduled email reports with attachments

---

## 🛠️ Technologies Used

### Programming & Core Libraries

```
Python 3.12+
├── Standard Library
│   ├── os, sys - System operations
│   ├── datetime - Time handling
│   ├── json, csv - Data processing
│   ├── re - Regular expressions
│   ├── smtplib, email - Email automation
│   └── argparse, logging - CLI tools
└── Third-Party
    ├── paramiko - SSH/SFTP
    ├── mysql-connector-python - Database
    ├── cryptography - Encryption
    ├── requests - HTTP/API
    ├── pandas - Data analysis
    ├── schedule - Task scheduling
    └── matplotlib - Data visualization
```

### DevOps Tools & Platforms

- **Operating Systems:** Windows, Linux (Kali, Ubuntu)
- **Database:** MySQL 8.0
- **Version Control:** Git, GitHub
- **Task Scheduling:** Windows Task Scheduler, Linux cron
- **Email Server:** Gmail SMTP
- **Remote Servers:** SSH-enabled Linux servers

---

## 📁 Project Structure

```
Python_Training/
├── 📚 Core Learning Scripts
│   ├── control-stratement.py      # If/else, loops, break/continue
│   ├── loops.py                   # For loops, while loops, iteration
│   ├── function.py                # Functions, *args, **kwargs, lambda
│   ├── exception-handling.py      # Try-except, error management
│   └── regular_expression.py      # Regex patterns for log parsing
│
├── 📄 File & Data Processing
│   ├── file-handling.py           # Read/write text files
│   ├── myjson_example.py          # JSON parsing and creation
│   ├── data_csv.py                # CSV reading and processing
│   └── sample_csv.py              # CSV generation
│
├── 🔗 Remote Server Management
│   ├── remote_module.py           # SSH command execution
│   ├── remote_module-2.py         # System monitoring over SSH
│   ├── remote_module(SFTP)-3.py   # SFTP file operations
│   └── remote_module-4.py         # Recursive directory download
│
├── 💾 Database Operations
│   ├── mysql_data_insert.py       # CRUD operations
│   ├── diagnostic_mysql.py        # Connection testing
│   └── real-project-2.py          # CSV to MySQL pipeline
│
├── 📧 Email Automation
│   ├── mymail.py                  # Basic email sending
│   ├── mymail_2.py                # HTML emails with attachments
│   └── windows_scheduler.py       # Scheduled email reports
│
├── ⏰ Task Scheduling
│   ├── my_scheduler.py            # Schedule library examples
│   ├── my_scheduler-2.py          # Automated email scheduler
│   └── windows_task.bat           # Windows Task Scheduler batch
│
├── 🔐 Security & Encryption
│   ├── real-project_mysql.py      # Password encryption with Fernet
│   └── mypass.json                # Secure credentials storage
│
├── 🎯 Mini Projects
│   ├── Mini_project(Building a CLI Data Processor).py  # API + CLI tool
│   └── real-remote-project.py     # Complete monitoring solution
│
├── 📊 Jupyter Notebooks
│   ├── Alnafi-Python-Lectures(DevOps).ipynb
│   └── Natural Language Processing Labs.ipynb
│
└── 📝 Documentation & Config
    ├── README.md                  # This file
    ├── pytest.ini                 # Testing configuration
    ├── .gitignore                 # Git ignore rules
    └── requirements.txt           # Python dependencies
```

---

## 💻 Installation

### Prerequisites

- **Python 3.12+** installed
- **Git** for cloning the repository
- **MySQL Server** (for database projects)
- **Linux VM** or WSL (for SSH/SFTP projects)

### Step 1: Clone the Repository

```bash
git clone https://github.com/ali4210/Python_Training.git
cd Python_Training
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configuration

**MySQL Setup:**
```bash
# Create database
mysql -u root -p
CREATE DATABASE alnafi;
CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'test123';
GRANT ALL PRIVILEGES ON alnafi.* TO 'mysql_user'@'localhost';
```

**Email Setup (Gmail):**
1. Enable 2-factor authentication
2. Generate app-specific password
3. Update credentials in scripts

**SSH Setup:**
```bash
# Test SSH connection
ssh username@192.168.0.150
```

---

## 🎮 Usage Examples

### Example 1: Remote Server Health Check

```python
import paramiko

hostname = "192.168.0.150"
username = "kali"
password = "kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Check disk usage
mycmd = "df -h"
stdin, stdout, stderr = client.exec_command(mycmd)

for line in stdout.readlines():
    print(line.strip())

client.close()
```

**Output:**
```
Filesystem      Size  Used Avail Use% Mounted on
udev            7.8G     0  7.8G   0% /dev
/dev/sda1        79G   37G   38G  50% /
```

### Example 2: CSV to MySQL Pipeline

```python
import csv
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="192.168.0.150",
    user="mysql_user",
    password="test123",
    database="alnafi"
)

# Read CSV and insert to database
with open('servershealth.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    
    cursor = mydb.cursor()
    query = "INSERT INTO server_data VALUES (%s, %s, %s)"
    
    for row in reader:
        cursor.execute(query, row)
    
    mydb.commit()
    print(f"{cursor.rowcount} rows inserted")

mydb.close()
```

### Example 3: Automated Email Alert

```python
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Server Alert'
    msg['From'] = 'admin@example.com'
    msg['To'] = 'team@example.com'
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('admin@example.com', 'app_password')
        server.send_message(msg)

# Usage
send_alert("Disk usage exceeded 80% on production server!")
```

### Example 4: CLI Data Processor

```bash
# Fetch data from API and save to JSON
python Mini_project.py \
  --api_url "https://jsonplaceholder.typicode.com/posts" \
  --file_path "output.json"

# Output:
# 2025-12-20 15:30:45 - INFO - Started fetching data...
# 2025-12-20 15:30:46 - INFO - Data successfully saved to output.json
```

---

## 🎯 Featured Projects

### 1. Server Health Monitoring System

**File:** `real-remote-project.py`

**Description:** Automated monitoring solution that checks server memory and sends email alerts when thresholds are exceeded.

**Features:**
- SSH connection to remote servers
- Memory usage monitoring
- Automated email notifications
- HTML-formatted alert emails with logos

**Use Case:** Production server monitoring with instant alerts.

---

### 2. CSV to MySQL Data Pipeline

**File:** `real-project-2.py`

**Description:** Complete ETL pipeline that reads CSV data, processes it, and stores in MySQL database.

**Features:**
- CSV parsing and validation
- Data transformation
- Encrypted database credentials
- Bulk insert operations
- Error handling and logging

**Use Case:** Automated data ingestion for reporting systems.

---

### 3. CLI Data Processor

**File:** `Mini_project(Building a CLI Data Processor).py`

**Description:** Command-line tool for fetching data from APIs and saving to JSON.

**Features:**
- Command-line argument parsing
- HTTP request handling
- JSON data processing
- Comprehensive logging
- Error management

**Use Case:** API data collection for analytics.

---

### 4. Scheduled Email Reports

**File:** `my_scheduler-2.py`

**Description:** Automated report generation and email delivery system.

**Features:**
- Task scheduling (every 10 seconds demo)
- Email with attachments
- HTML email formatting
- Embedded images
- Multiple recipients (To, Cc)

**Use Case:** Daily/weekly automated reporting.

---

## 📚 Learning Path

### Phase 1: Python Fundamentals (Week 1-2)

- [ ] Data structures (lists, tuples, dicts, sets)
- [ ] Control flow (if/else, loops)
- [ ] Functions and lambda expressions
- [ ] File handling (text, CSV, JSON)
- [ ] Error handling and debugging

**Scripts:** `control-stratement.py`, `loops.py`, `function.py`, `file-handling.py`

### Phase 2: DevOps Automation (Week 3-4)

- [ ] Remote server management (SSH/SFTP)
- [ ] Database operations (MySQL CRUD)
- [ ] Email automation (SMTP)
- [ ] Regular expressions for log parsing
- [ ] Task scheduling

**Scripts:** `remote_module.py`, `mysql_data_insert.py`, `mymail.py`, `my_scheduler.py`

### Phase 3: Real-World Projects (Week 5-6)

- [ ] Server health monitoring
- [ ] Data pipeline development
- [ ] CLI tool creation
- [ ] Encryption and security
- [ ] Complete automation workflows

**Scripts:** `real-remote-project.py`, `real-project-2.py`, `Mini_project.py`

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=alnafi.html

# Run specific test file
pytest test1.py

# Run with parallel execution
pytest -n3
```

---

## 📖 Documentation

### Master Guide

A **300+ page comprehensive guide** is included covering:
- Line-by-line code explanations
- Concept deep-dives
- Real-world use cases
- Best practices
- Interview preparation
- Career guidance

**Access:** See `MASTER_GUIDE.md` (generated artifact)

### Quick Reference

- **File Handling:** Reading/writing text, CSV, JSON
- **SSH/SFTP:** Remote command execution, file transfers
- **MySQL:** CRUD operations, parameterized queries
- **Email:** SMTP configuration, attachments, HTML
- **Scheduling:** schedule library, cron jobs, Windows Task Scheduler

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Include error handling
- Write meaningful commit messages
- Test your code before submitting

---

## 👨‍💻 Author

**Mohammad Saleem Ali**

- 🎓 **Current:** AIOps Student at Al-Nafi International College
- 💼 **Previous:** CSE Student at BRAC University, Bangladesh
- 🌍 **Location:** Dhaka, Bangladesh
- 💻 **Focus:** DevOps, AIOps, Python Automation, Infrastructure Management

### Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/saleem-ali-189719325/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/ali4210)

### Professional Goals

🎯 Seeking opportunities in **DevOps Engineer**, **SRE**, or **AIOps** roles where I can leverage Python automation skills to build scalable infrastructure solutions.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Al-Nafi International College** for the AIOps training program
- **BRAC University** for Computer Science foundation
- **Open Source Community** for incredible Python libraries
- **DevOps Community** for best practices and inspiration

---

## 📊 Project Stats

<div align="center">

| Metric | Value |
|--------|-------|
| **Total Scripts** | 51 |
| **Lines of Code** | 44,000+ tokens |
| **Technologies** | 10+ |
| **Projects** | 4 major |
| **Documentation** | 300+ pages |

</div>

---

## 🚀 Future Enhancements

- [ ] Kubernetes deployment automation
- [ ] AWS/Azure cloud integration
- [ ] Ansible playbook integration
- [ ] Docker container management
- [ ] CI/CD pipeline templates
- [ ] Prometheus metrics collection
- [ ] Grafana dashboard automation

---

## 📞 Support & Feedback

If you have questions or feedback:

1. **Open an Issue:** [GitHub Issues](https://github.com/ali4210/Python_Training/issues)
2. **Email:** saleemali.mohammad211126@gmail.com
3. **LinkedIn:** [Connect with me](https://www.linkedin.com/in/saleem-ali-189719325/)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Mohammad Saleem Ali

</div>
