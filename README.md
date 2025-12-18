
# Python for DevOps: Enterprise Automation Framework

**Author:** Saleem Ali
**Role:** DevOps Engineer & Automation Specialist
**Focus:** Infrastructure Automation, DB Engineering, & Tooling

---

## ==>> Project Overview

This repository hosts a comprehensive suite of **50+ Python Automation Tools** designed to solve real-world DevOps challenges. It transitions from core Python concepts to complex, secure, and distributed automation workflows.

The project demonstrates the ability to build **Self-Healing Infrastructure**, **Secure Data Pipelines**, and **Remote Server Management Systems**.

---

## ==>> Key Automation Architectures

### => 1. The Remote Monitoring Bot (Paramiko)
A system that remotely manages Linux servers via SSH.
* **Capability:** Connects to remote hosts, executes system health checks (`df -h`, `free -m`), and retrieves logs via SFTP.
* **Recursive Logic:** Includes a recursive directory downloader (`remote_module-4.py`) to backup entire folder structures.

### => 2. Secure ETL Pipeline (CSV to MySQL)
A data engineering workflow that processes server logs.
* **Extract:** Reads raw server health data from CSV files.
* **Transform:** Cleanses data and calculates usage percentages.
* **Load:** Inserts data into a MySQL Database using bulk execution.
* **Security:** Implements **Fernet Encryption** to handle database credentials securely, adhering to DevSecOps best practices.

### => 3. Automated Alerting & Scheduling
* **Notification:** Uses `smtplib` to send HTML-formatted email alerts with attachments (logs/images) when thresholds are breached.
* **Scheduling:** Integrated with Python's `schedule` library and Windows Batch files (`.bat`) for cron-job style execution.

---

## ==>> Tech Stack & Libraries

| Category | Libraries Used | Purpose |
| :--- | :--- | :--- |
| **Infrastructure** | `paramiko`, `socket` | SSH connections & Port testing |
| **Database** | `mysql-connector-python` | Database CRUD operations |
| **Security** | `cryptography` | Encrypting sensitive configs |
| **Data** | `pandas`, `csv`, `json` | Data manipulation & Config management |
| **Web/API** | `requests`, `argparse` | CLI tools & API interaction |
| **System** | `os`, `sys`, `platform` | OS-level command execution |

---

## ==>> Setup & Usage

### => Step 1: Install Dependencies
```bash
pip install -r requirements.txt

```

### => Step 2: Run the Monitoring Bot

```bash
python real-remote-project.py

```

### => Step 3: Run the CLI Data Processor

```bash
python Mini_project.py --api_url "[https://api.example.com/data](https://api.example.com/data)" --file_path "data.json"

```

---

## ==>> Project Structure

```text
├── Python_Training/
│   ├── remote_module.py       # SSH & Remote Execution
│   ├── real-project-2.py      # Secure CSV-to-MySQL Pipeline
│   ├── diagnostic_mysql.py    # DB Connection Tester
│   ├── my_scheduler.py        # Task Scheduling Logic
│   ├── mymail_2.py            # SMTP Alerting System
│   ├── Mini_project.py        # CLI Tool
│   └── ... (Core Python Labs)
└── README.md                  # Documentation

```

---

## ==>> Contact

**Saleem Ali**

* **Role:** DevOps & Python Automation Engineer
* **Focus:** Automating the boring stuff with secure, scalable code.
