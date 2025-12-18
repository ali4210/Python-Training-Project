
# Python for DevOps: The Comprehensive Automation Guide
**Author:** Saleem Ali
**Domain:** System Automation, Data Engineering, & Infrastructure Monitoring
**Tech Stack:** Python 3.x, Paramiko, MySQL, Cryptography, SMTP, Pandas

---

## ==>> 1. Introduction & Roadmap
This repository represents a journey from "Hello World" to "Enterprise Automation". It is divided into three proficiency levels:

1.  **Core Python:** Mastering syntax, loops, and data structures (Lists, Dictionaries, Tuples).
2.  **System Scripting:** File handling, OS interactions, and CLI tool creation.
3.  **DevOps Engineering:** Remote server management (SSH), Database pipelines (ETL), and Security (Encryption).

---

## ==>> 2. Module 1: The Core Foundation
*Before automating servers, we must master the language.*

### => Data Structures & Logic
* **Files:** `loops.py`, `control-stratement.py`, `function.py`, `exception-handling.py`
* **Concept:** Handling data flows.
    * **Tuples vs Lists:** Understanding mutability.
    * **Dictionaries:** The backbone of JSON data and API payloads.
    * **Exception Handling:** Using `try/except/finally` to prevent script crashes during critical operations.

### => File & Data Handling
* **Files:** `file-handling.py`, `myjson_example.py`, `csv` handling.
* **Concept:** A DevOps engineer constantly reads logs and configs.
```python
import json
# Loading server configurations from JSON
with open("user_details.json", "r") as f:
    config = json.load(f)
print(f"Deploying to: {config['server1']['IBM']['env']['PR']}")

```

---

## ==>> 3. Module 2: System & Network Automation

*Interacting with the Operating System.*

### => OS & Sys Libraries

* **Files:** `mylname.py`, `practice.py`
* **Concept:** Using `os` and `platform` to detect the environment (Windows vs Linux) and execute system commands (`ipconfig`, `dir`).

### => The CLI Data Processor (Mini Project)

* **File:** `Mini_project(Building a CLI Data Processor).py`
* **Concept:** Building a robust Command Line Interface tool using `argparse` and `logging`.
* **Usage:**

```bash
python data_processor.py --api_url "[https://api.site.com](https://api.site.com)" --file_path "output.json"

```

---

## ==>> 4. Module 3: Remote Infrastructure (Paramiko)

*This is the core DevOps skill: Managing servers without logging in manually.*

### => SSH Command Execution

* **Files:** `remote_module.py`, `remote_module-2.py`
* **Library:** `paramiko`
* **Workflow:**
1. Establish SSH Client.
2. Auto-add host keys policy.
3. Execute Linux commands (`free -g`, `df -h`).
4. Parse `stdout` to get server metrics.



### => Secure File Transfer (SFTP)

* **File:** `remote_module(SFTP)-3.py`
* **Concept:** Uploading configs or downloading logs securely.

```python
sftp = client.open_sftp()
sftp.put('local_config.csv', '/remote/home/config.csv')
sftp.close()

```

---

## ==>> 5. Module 4: Database & Security Engineering

*Building secure Data Pipelines.*

### => MySQL Diagnostics & Connectivity

* **File:** `diagnostic_mysql.py`
* **Concept:** A health-check script that verifies Network connectivity (Socket) *before* attempting Database connectivity (MySQL Connector).

### => The Secure ETL Pipeline (Real Project)

* **File:** `real-project-2.py`
* **Challenge:** Reading server health data from a CSV and inserting it into a Database without hardcoding passwords.
* **Solution:** Used `cryptography.fernet` to encrypt credentials.

```python
from cryptography.fernet import Fernet
# Decrypt password at runtime
f = Fernet(key)
passwd_mysql = f.decrypt(encrypted_message).decode("utf-8")

```

---

## ==>> 6. Module 5: Automated Alerting System

*Monitoring Logic: Detect -> Analyze -> Notify.*

### => The Watchdog Script

* **File:** `real-remote-project.py`
* **Logic:**
1. SSH into Linux Server (`192.168.0.150`).
2. Check RAM usage using `free -g`.
3. **If RAM < 2GB:** Trigger an HTML-formatted Email Alert.



### => Task Scheduling

* **File:** `my_scheduler-2.py`
* **Concept:** Using the `schedule` library to run health checks every X seconds, or using `windows_task.bat` to integrate with Windows Task Scheduler.

---

## ==>> 7. Deployment Dependencies

To run this portfolio, install the required libraries:

```bash
pip install -r requirements.txt

```

*(Includes: paramiko, mysql-connector-python, cryptography, schedule, pandas, requests)*

```


