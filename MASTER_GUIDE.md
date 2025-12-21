# 📚 Python Training Master Guide
## Complete DevOps & Automation Learning Resource

**Project:** Python Training & DevOps Automation Suite  
**Author:** Mohammad Saleem Ali  
**Institution:** Al-Nafi International College (AIOps Program)  
**Purpose:** Professional Python training for DevOps/SRE roles  
**Repository:** [GitHub - Python Training](https://github.com/ali4210?tab=repositories)  

---

## 📖 Table of Contents

### Part 1: Python Fundamentals
1. [Introduction to Python](#1-introduction-to-python)
2. [Data Structures](#2-data-structures)
3. [Control Statements](#3-control-statements)
4. [Loops & Iteration](#4-loops--iteration)
5. [Functions](#5-functions)
6. [Object-Oriented Programming](#6-object-oriented-programming)

### Part 2: File & Data Handling
7. [File Handling](#7-file-handling)
8. [JSON Processing](#8-json-processing)
9. [CSV Data Processing](#9-csv-data-processing)
10. [Regular Expressions](#10-regular-expressions)

### Part 3: DevOps Automation
11. [Remote Server Management (Paramiko)](#11-remote-server-management)
12. [Database Operations (MySQL)](#12-database-operations)
13. [Email Automation (SMTP)](#13-email-automation)
14. [Task Scheduling](#14-task-scheduling)
15. [Encryption & Security](#15-encryption--security)

### Part 4: Advanced Projects
16. [Mini CLI Data Processor](#16-mini-cli-data-processor)
17. [Real-World DevOps Projects](#17-real-world-devops-projects)
18. [Error Handling & Debugging](#18-error-handling--debugging)

---

## 1. Introduction to Python

### 1.1 Why Python for DevOps?

Python has become the **de facto standard** for DevOps automation due to:

✅ **Simple, Readable Syntax** - Write automation scripts quickly  
✅ **Rich Library Ecosystem** - Libraries for everything (SSH, databases, APIs)  
✅ **Cross-Platform** - Works on Linux, Windows, macOS  
✅ **Strong Community** - Extensive documentation and support  
✅ **Infrastructure as Code** - Ansible, Terraform integrations  

### 1.2 Your First Python Program

```python
print("salkeem")
```

**Line-by-Line Breakdown:**

- `print()` - Built-in Python function that displays output
- `"salkeem"` - String literal (text data enclosed in quotes)
- Result: Outputs `salkeem` to the console

**Key Concept:** Python executes code **line by line** from top to bottom.

---

## 2. Data Structures

### 2.1 Tuples - Immutable Sequences

#### **What is a Tuple?**
A tuple is an **ordered, immutable** collection of items.

```python
sal = (5, 3, 2, 5, 6, 7, 8)
print(sal)
# Output: (5, 3, 2, 5, 6, 7, 8)
```

**Line-by-Line:**
- `sal` - Variable name
- `=` - Assignment operator
- `(5, 3, 2, ...)` - Tuple literal (parentheses with comma-separated values)
- `print(sal)` - Display the tuple

**Why Use Tuples?**
- ✅ **Data Integrity** - Cannot be modified after creation
- ✅ **Performance** - Faster than lists for read-only data
- ✅ **Dictionary Keys** - Can be used as dict keys (lists cannot)

#### **Tuple Methods**

```python
type(sal)  
# Output: <class 'tuple'>

dir(sal)   
# Shows all available methods:
# 'count', 'index', '__add__', '__mul__', etc.
```

**Understanding `dir()`:**
- Lists **all attributes and methods** of an object
- Methods starting with `__` are "dunder" (double underscore) methods
- Public methods: `count()`, `index()`

#### **Key Tuple Operations**

```python
# 1. Count occurrences
sal.count(5)  # Output: 2 (5 appears twice)

# 2. Find index
sal.index(2)  # Output: 2 (element 2 is at index 2)

# 3. Access elements
sal[0]        # Output: 5 (first element)
sal[-1]       # Output: 8 (last element)

# 4. Slicing
sal[:4]       # Output: (5, 3, 2, 5) (first 4 elements)
sal[:-2]      # Output: (5, 3, 2, 5, 6, 7) (all except last 2)
sal[::-2]     # Output: (8, 6, 5, 3) (reverse, every 2nd element)
```

**Slicing Syntax:** `[start:stop:step]`
- `start` - Beginning index (inclusive)
- `stop` - Ending index (exclusive)
- `step` - Increment (negative for reverse)

#### **Nested Tuples**

```python
sal = (1, 2, 4, 5, 87, [10, 50, 60], 9, 6, 3, 5)

# Access nested list
sal[5]       # Output: [10, 50, 60]

# Access element inside nested list
sal[5][2]    # Output: 60

# Modify nested list (lists are mutable!)
sal[5][2] = "Saleem"
print(sal[5][2])  # Output: Saleem
```

**Key Insight:** While tuples are immutable, **mutable objects inside tuples CAN be modified**.

### 2.2 Lists - Mutable Sequences

```python
sal = list(sal)  # Convert tuple to list
type(sal)        # Output: <class 'list'>

# List-specific methods
dir(sal)
# Additional methods: 'append', 'clear', 'copy', 'extend', 
#                     'insert', 'pop', 'remove', 'reverse', 'sort'
```

#### **List Manipulation**

```python
# 1. Append (add to end)
abd = [2, 5, 4, 7, 1, 8]
abd.append([10, 15])
# Result: [2, 5, 4, 7, 1, 8, [10, 15]]  (nested list!)

# 2. Extend (merge lists)
my = [40, 45]
abd.extend(my)
# Result: [2, 5, 4, 7, 1, 8, [10, 15], 40, 45]

# 3. Reverse
abd.reverse()
# Result: [45, 40, [10, 15], 8, 1, 7, 4, 5, 2]

# 4. Sort
sal = [4, 5, 7, 8, 9, 5, 6, 2]
sal.sort()
# Result: [2, 4, 5, 5, 6, 7, 8, 9]

sal.sort(reverse=True)
# Result: [9, 8, 7, 6, 5, 5, 4, 2]
```

**append() vs extend():**
- `append()` - Adds entire object as single element
- `extend()` - Adds each element individually

#### **List Copying (Shallow vs Deep)**

```python
sal = [4, 5, 7, 8, 9, 5, 6, 2]

# Method 1: Assignment (reference copy)
sal2 = sal
print(id(sal), id(sal2))  # Same memory address!

# Method 2: Copy method (shallow copy)
sal3 = sal.copy()
print(id(sal), id(sal3))  # Different memory addresses
```

**Memory Concept:**
- `id()` returns object's memory address
- Assignment creates **reference** (both variables point to same object)
- `.copy()` creates **new object** with same values

### 2.3 Sets - Unique Collections

```python
sal = [4, 7, 8, 9, 4, 5, 2, 4, 7, 3, 1, 5, 6, 8, 9, 1, 0]
print(set(sal))
# Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

**Set Characteristics:**
- ✅ **Unordered** - No index access
- ✅ **Unique** - Automatically removes duplicates
- ✅ **Mutable** - Can add/remove elements
- ⚠️ **No duplicates** - Perfect for deduplication

**DevOps Use Case:** Removing duplicate server IPs from logs.

### 2.4 Dictionaries - Key-Value Pairs

```python
dict1 = {"uname": "abd", "pass": 1323}
print(dict1)
# Output: {'uname': 'abd', 'pass': 1323}

type(dict1)  # Output: <class 'dict'>
```

#### **Dictionary Operations**

```python
# 1. Access values
dict1['uname']  # Output: 'abd'
dict1['pass']   # Output: 1323

# 2. Get method (safer)
dict1.get('Uname')  # Output: None (key doesn't exist)
dict1.get('uname')  # Output: 'abd'

# 3. Modify values
person = {"name": "ABD", "age": 44, "city": "Bangalore"}
person['age'] = 100
# Result: {'name': 'ABD', 'age': 100, 'city': 'Bangalore'}

# 4. Add new keys
person['salary'] = 1000
# Result: {'name': 'ABD', 'age': 100, 'city': 'Bangalore', 'salary': 1000}
```

#### **Dictionary Methods**

```python
person = {"name": "ABD", "age": 44, "city": "Bangalore", "country": "India"}

# Extract keys
person.keys()
# Output: dict_keys(['name', 'age', 'city', 'country'])

# Extract values
person.values()
# Output: dict_values(['ABD', 44, 'Bangalore', 'India'])

# Extract key-value pairs
person.items()
# Output: dict_items([('name', 'ABD'), ('age', 44), ...])
```

#### **Advanced Dictionary Operations**

```python
# 1. Update (merge dictionaries)
person.update({"company": "google"})
# Result: {..., 'company': 'google'}

# 2. Pop (remove & return)
person.pop('company')  # Returns: 'google'

# 3. Popitem (remove last added)
person.popitem()  # Returns: ('salary', 1000)

# 4. Delete specific key
del person['age']
```

#### **Nested Dictionaries (DevOps Example)**

```python
myinfo = {
    1: {'uname': 'abd', 'pass': 'ABD@123', 'server1': 'Linux'},
    2: {'uname': 'ali', 'pass': 'ali@123', 'server1': 'AIX'},
    3: {'uname': 'kazim', 'pass': 'kazim@123', 'server1': 'windows'}
}

# Access nested data
myinfo[3]            # Output: {'uname': 'kazim', ...}
myinfo[3]['pass']    # Output: 'kazim@123'
```

**DevOps Use Case:** Storing server configurations with credentials.

#### **Complex Nested Structures**

```python
myinfo = {
    "server1": {
        "IBM": {
            "datacenter": "Bangalore",
            "env": {
                "PR": "192.168.1.1",
                "DR": "192.168.1.2"
            }
        }
    }
}

# Navigate nested structure
myinfo['server1']['IBM']['env']['PR']
# Output: '192.168.1.1'

# Practical usage
print(f"Bangalore datacenter PR address is: {myinfo['server1']['IBM']['env']['PR']}")
# Output: Bangalore datacenter PR address is: 192.168.1.1
```

**Real-World Application:** Multi-tier infrastructure configuration management.

---

## 3. Control Statements

### 3.1 Conditional Statements

```python
import os

for i in os.listdir():
    if i.endswith('.py'):
        print(i)
```

**Line-by-Line:**
1. `import os` - Import operating system interface module
2. `os.listdir()` - Get list of files in current directory
3. `for i in ...` - Iterate through each file
4. `if i.endswith('.py')` - Check if filename ends with `.py`
5. `print(i)` - Display Python files only

**DevOps Use Case:** Filter specific file types in automation scripts.

### 3.2 Loop Control

```python
# Break - Exit loop
i = 1
while True:
    print(i)
    i += 1
    if i >= 5:
        break  # Stops loop when i reaches 5

# Continue - Skip iteration
for i in range(1, 10):
    if i == 5:
        continue  # Skip printing 5
    print(i)

# Pass - Placeholder
for i in range(1, 10):
    if i == 5:
        pass  # Does nothing, placeholder for future code
```

**Control Keywords:**
- `break` - **Exit loop** entirely
- `continue` - **Skip** current iteration, move to next
- `pass` - **Do nothing** (useful during development)

---

## 4. Loops & Iteration

### 4.1 Range Function

```python
list(range(1, 11))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
    print(i)
# Prints 1 through 10
```

**Range Syntax:** `range(start, stop, step)`
- Start: inclusive
- Stop: exclusive
- Step: increment (default 1)

### 4.2 Iterating Data Structures

```python
# List iteration
mylist = ['apple', 'banana', 'orange']
for item in mylist:
    print(f"my list value is: {item}")

# Dictionary iteration
myinfo = {"name": "ABD", "age": 44, "city": "bangalore"}

# Keys & Values
for k, v in myinfo.items():
    print(f"My key is: {k}")
    print(f"My value is: {v}")

# Keys only
for k in myinfo.keys():
    print(f"My key is: {k}")

# Values only
for v in myinfo.values():
    print(f"My value is: {v}")
```

### 4.3 While Loops

```python
# Count up
i = 1
while i < 10:
    print(i)
    i += 1  # MUST increment or infinite loop!

# Count down
i = 10
while i >= 0:
    print(i)
    i -= 1
```

**⚠️ Critical:** Always ensure loop variable changes, or you'll create an **infinite loop**.

### 4.4 OS Module - Directory Walking

```python
import os

# Walk through directory tree
for roots, dirs, files in os.walk(os.getcwd()):
    if len(files) > 0:
        print(roots)  # Print directory path
        for i in files:
            print(os.path.join(roots, i))  # Full file path
```

**DevOps Application:** Scanning infrastructure configuration files across directory trees.

---

## 5. Functions

### 5.1 Basic Function Definition

```python
def abd():
    print("this is a function")
    print("this is a way-bigfunction")
    print("this is a way-smallfunction")

# Call function multiple times
abd()
abd()
abd()
```

**Function Benefits:**
- ✅ **Reusability** - Write once, use many times
- ✅ **Modularity** - Break complex tasks into smaller pieces
- ✅ **Maintainability** - Update logic in one place

### 5.2 Functions with Parameters

```python
def my(abd):
    print("*" * 30)
    print("\t\t" + abd)
    print("*" * 30)

my("This is a function")
my("This is a way-bigfunction")
```

**Parameters** - Variables passed to function for processing.

### 5.3 Return Values

```python
def add(a, b):
    c = a + b
    return c  # Send result back to caller

def mycode():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(add(a, b))  # Use returned value

mycode()
```

**Return Statement:**
- Sends data back from function
- Terminates function execution
- If no return, function returns `None`

### 5.4 Default Parameters

```python
def num(ali=3):
    print(ali)

num(1)  # Output: 1
num(2)  # Output: 2
num()   # Output: 3 (default value)
```

### 5.5 Variable Arguments (*args, **kwargs)

```python
# *args - Variable positional arguments
def myold(*data):
    print(f"Server is: {data[0]}")
    print(f"IP is: {data[1]}")
    print(f"OS is: {data[2]}")

mylist = ["IBM", "192.168.0.12", "RHEL"]
myold(*mylist)  # Unpack list into arguments

# **kwargs - Variable keyword arguments
def mycod2(**mydata):
    for k, v in mydata.items():
        print(k, v)

mydict = {'server': 'IBM', 'IP': '192.168.1.1', 'OS': 'AIX'}
mycod2(**mydict)  # Unpack dictionary
```

**Unpacking:**
- `*` unpacks sequences (lists, tuples)
- `**` unpacks dictionaries

### 5.6 Lambda Functions (Anonymous)

```python
# Regular function
def add(a, b):
    return a + b

# Lambda equivalent
result = lambda a, b: a + b
print(result(1, 2))  # Output: 3

# Conditional lambda
result = lambda a, b: a if (a >= b) else b
print(result(1, 2))  # Output: 2 (larger value)
```

**Lambda Syntax:** `lambda parameters: expression`
- Single-line functions
- No explicit `return` statement
- Used for simple operations

### 5.7 Main Function Pattern

```python
import os

def mycode():
    print("This is my code function")

def main():
    print(os.listdir(os.getcwd()))
    print("My global print")

if __name__ == "__main__":
    main()
```

**Key Concept:**
- `__name__ == "__main__"` - True when script is run directly
- False when imported as module
- Best practice for script organization

---

## 6. Object-Oriented Programming

### 6.1 Classes and Objects

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.drive()  # Output: The Toyota Corolla is now driving.
car2.drive()  # Output: The Honda Civic is now driving.
```

**OOP Concepts:**
- `__init__()` - Constructor (initializes object)
- `self` - Reference to current instance
- Instance variables: `self.brand`, `self.model`
- Methods: Functions inside classes

### 6.2 Class vs Instance Attributes

```python
class Car:
    wheels = 4  # Class attribute (shared by all instances)

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute (unique per object)
        self.model = model

# Access class attribute
print(f"Number of wheels: {Car.wheels}")
# Output: Number of wheels: 4
```

**Class Attributes:**
- Shared across all instances
- Accessed via class name
- Example: Configuration constants

---

## 7. File Handling

### 7.1 Reading Files

```python
# Method 1: Manual close
file = open("abd.txt")
print(file.read())
file.close()

# Method 2: Context manager (recommended)
with open("abd.txt") as file:
    print(file.read())
# File automatically closed after block
```

**Context Manager Benefits:**
- ✅ Automatic resource cleanup
- ✅ No need for explicit close()
- ✅ Exception-safe

### 7.2 Reading Lines

```python
with open("abd.txt") as file:
    data = file.readlines()  # List of lines
    for i in data:
        word = i.split()  # Split line into words
        print(word)
```

**Methods:**
- `.read()` - Entire file as string
- `.readline()` - Single line
- `.readlines()` - List of all lines

### 7.3 Writing Files

```python
# Mode 'w' - Overwrite file
with open("abd.txt", mode="w") as file:
    file.write("Hello Brother, How you doing Mister\n")
    file.write("How you doing Mister\n")
    file.write("How you doing Brother\n")

# Mode 'a' - Append to file
with open("abd.txt", mode="a") as file:
    file.write("Hello Didi, Date pe chale\n")
```

**File Modes:**
- `'r'` - Read (default)
- `'w'` - Write (overwrites)
- `'a'` - Append
- `'r+'` - Read and write

### 7.4 Bulk Writing

```python
mydata = ["Python ", "Java", "C++", "C#", "JavaScript"]

with open("abd.txt", mode="a") as file:
    for i in mydata:
        file.write(i + "\n")

# Generate numbered lines
for i in range(11):
    with open("abd.txt", mode="a") as file:
        file.write(f"Line: {i}\n")
```

**DevOps Use Case:** Writing configuration files, log entries, automation reports.

---

## 8. JSON Processing

### 8.1 Reading JSON

```python
import json

jsonfile = r"C:\Users\User\PycharmProjects\pythonProject3\my.json"

with open(jsonfile, "r") as myfile:
    my_dict = json.load(myfile)
    print(my_dict)

# Access values
for key, value in my_dict.items():
    print(key, ":", value)

password_nginx = my_dict['password_nginx']
print(f"My NGINX password is: {password_nginx}")
```

**JSON Structure:**
```json
{
  "password_nginx": "abd$123",
  "password_apache": "W3lcome1234",
  "password_tomcat": "abd#123"
}
```

### 8.2 Processing JSON Arrays

```python
jsonfile1 = r"C:\Users\User\PycharmProjects\pythonProject3\user.json"

with open(jsonfile1, "r") as jf:
    my_dict1 = json.load(jf)  # Returns list of dicts

for i in my_dict1:
    print(f"My Dictionary is: {i}")
    for key, value in i.items():
        print(key, ":", value)
    
    # Conditional processing
    for k, v in i.items():
        if v == 'Ubuntu':
            print("My Ubuntu version is", i["Version"])
        if v == 'CentOS':
            print("My CentOS version is", i["Version"])
```

**JSON Array Structure:**
```json
[
  {
    "Name": "CentOS",
    "Version": "7",
    "Install": "yum"
  },
  {
    "Name": "Ubuntu",
    "Version": "17.10",
    "Install": "apt"
  }
]
```

### 8.3 Writing JSON

```python
import json

myinfo = {
    "server1": {
        "IBM": {
            "datacenter": "Bangalore",
            "env": {
                "PR": "192.168.1.1",
                "DR": "192.168.1.2"
            }
        }
    }
}

mypath = "user_details.json"
with open(mypath, "w") as myfile:
    json.dump(myinfo, myfile, indent=4)  # indent=4 for pretty printing
```

**DevOps Application:** Storing infrastructure configurations, API responses, secrets management.

---

## 9. CSV Data Processing

### 9.1 Reading CSV Files

```python
import csv

mypath = r"C:\Users\User\PycharmProjects\pythonProject3\servershealth.csv"

with open(mypath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)  # Each row is a list
```

### 9.2 Writing CSV Files

```python
import csv

# Write with DictWriter
with open('output.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write column names
    
    data = [
        {"Name": "Ali", "Age": 25, "City": "Dhaka"},
        {"Name": "Ahmed", "Age": 30, "City": "Bangalore"}
    ]
    
    for row in data:
        writer.writerow(row)
```

**CSV Applications:**
- Server health reports
- Log aggregation
- Data exports for analysis

---

## 10. Regular Expressions

### 10.1 Basic Pattern Matching

```python
import re

myword = "python python2 python3 Python courses"

# Find all matches
pattern = r'\bpython\d\b'  # \b = word boundary, \d = digit
print(re.findall(pattern, myword))
# Output: ['python2', 'python3']
```

### 10.2 IP Address Extraction

```python
import re

mytext = """
My Broadcast Address is 255.255.255.255 
jboss server ip address is 192.168.1.8 
Docker server ip address is 192.168.1.11
"""

# Pattern for IP addresses
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(re.findall(pattern, mytext))
# Output: ['255.255.255.255', '192.168.1.8', '192.168.1.11']
```

**Regex Syntax:**
- `\d` - Any digit (0-9)
- `{1,3}` - Repeat 1 to 3 times
- `\.` - Literal dot (escaped)
- `\b` - Word boundary
- `+` - One or more
- `*` - Zero or more
- `?` - Zero or one

### 10.3 Advanced Regex

```python
import re

# Search (finds first match)
mytext = "My IP is 192.168.1.8"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind = re.search(pattern, mytext)

print(f"Found: {myfind.group()}")
print(f"Starting Index: {myfind.start()}")
print(f"Ending Index: {myfind.end()}")

# Split by pattern
mytext = "192.168.1.8 jboss server 192.168.1.11 docker"
mymatch = re.split(pattern, mytext)
print(mymatch)
# Output: ['', ' jboss server ', ' docker']

# Substitute (replace)
myword = "python course and python course"
pattern = r"\bcourse\b"
print(re.sub(pattern, 'COURSE', myword))
# Output: python COURSE and python COURSE
```

**DevOps Use Cases:**
- Log parsing
- Configuration validation
- IP/MAC address extraction
- Error pattern detection

---

## 11. Remote Server Management

### 11.1 SSH with Paramiko

```python
import paramiko

hostname = "192.168.0.150"
username = "kali"
password = "kali"

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Execute command
mycmd = "df -h"
stdin, stdout, stderr = client.exec_command(mycmd)

# Read output
mycmdout = stdout.readlines()
for line in mycmdout:
    print(line.strip('\n'))

client.close()
```

**Real-World Application:** Remote server health checks, automated deployments.

### 11.2 SFTP File Operations

```python
import paramiko

hostname = "192.168.0.150"
username = "kali"
password = "kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Open SFTP session
mysftp = client.open_sftp()

# Download file
mysftp.get('/home/kali/server.csv', 'test.csv')

# Upload file
mysftp.put('test.csv', '/home/kali/Downloads/test1.csv')

# Navigate directories
mysftp.chdir('/home/kali/Downloads/')

# Read remote file
file = mysftp.open('test4.csv', 'r')
print(file.read())

# List directory
print(mysftp.listdir())

# File stats
print(mysftp.stat('test4.csv').st_size)

mysftp.close()
client.close()
```

**SFTP Methods:**
- `.get()` - Download file
- `.put()` - Upload file
- `.chdir()` - Change directory
- `.listdir()` - List files
- `.stat()` - File information

---

## 12. Database Operations (MySQL)

### 12.1 Connection Setup

```python
import mysql.connector
from datetime import datetime

# Connection parameters
mydb = mysql.connector.connect(
    host="192.168.0.150",
    user="mysql_user",
    password="test123",
    database="alnafi"
)

# Create cursor
cur = mydb.cursor()
```

### 12.2 SELECT Operations

```python
# Fetch all records
sql = "SELECT * FROM trainer_details"
cur.execute(sql)
result = cur.fetchall()

for row in result:
    print(row)

# Fetch one record
result = cur.fetchone()
print(result)
```

### 12.3 INSERT Operations

```python
# Simple insert
sql = """
INSERT INTO trainer_details 
(fname, lname, desig, username, password, salary, datetime) 
VALUES ('Yousuf', 'Ali', 'Businessman', 'Yousuf', 'ramzan123', 900000, '2022-10-02')
"""
cur.execute(sql)
mydb.commit()  # MUST commit for changes!
print("Data has been inserted")

# Parameterized insert (secure!)
time = datetime.now()
mycustom = time.strftime("%Y-%m-%d %H:%M:%S")

sql = """
INSERT INTO trainer_details 
(fname, lname, desig, username, password, salary, datetime) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
data = ('rehan', 'pathan', 'POS', 'rehan', 'rehan123', '75000', mycustom)
cur.execute(sql, data)
mydb.commit()
```

**Why Parameterized Queries?**
- ✅ **SQL Injection Prevention**
- ✅ **Type Safety**
- ✅ **Better Performance**

### 12.4 UPDATE Operations

```python
data = "'zoya@855'"
sql = f"UPDATE trainer_details SET password={data} WHERE t_id=11"
cur.execute(sql)
mydb.commit()
print("Data has been updated")
```

### 12.5 DELETE Operations

```python
mydata = input("Enter the fname which you want to remove: ")
sql = f"DELETE FROM trainer_details WHERE fname = '{mydata}'"
cur.execute(sql)
mydb.commit()
print("Your command was Successful")
```

⚠️ **Security Warning:** Always use parameterized queries in production!

### 12.6 Complete CRUD Example

```python
try:
    import mysql.connector
    from datetime import datetime

    mydb = mysql.connector.connect(
        host="192.168.0.150",
        user="mysql_user",
        password="test123",
        database="alnafi"
    )
    
    cur = mydb.cursor()
    
    # Your operations here
    
    mydb.close()

except Exception as e:
    print("Something issue please check your input", e)
```

**Best Practices:**
- Use try-except for error handling
- Close connections properly
- Commit after modifications
- Use parameterized queries

---

## 13. Email Automation (SMTP)

### 13.1 Basic Email

```python
import smtplib
from email.message import EmailMessage

my_mail = "saleemali.mohammad211126@gmail.com"
my_password = "cpif twnk otqr osnc"  # App-specific password!

# Connect to SMTP
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()  # TLS encryption
connection.login(user=my_mail, password=my_password)

# Create message
msg = EmailMessage()
msg['Subject'] = "SMTP Report Status"
msg['From'] = my_mail
msg['To'] = my_mail
msg['Cc'] = ["saleemali.mohammad@gmail.com", "yousuf3597494@gmail.com"]
msg.set_content("Hi team, this is saleem ali testing from python")

# Send
connection.send_message(msg)
connection.close()
print("Your Mail has been sent")
```

**Gmail Setup:**
1. Enable 2-factor authentication
2. Generate app-specific password
3. Use 587 port with TLS

### 13.2 Email with Attachments

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Setup
my_mail = "saleemali.mohammad211126@gmail.com"
my_password = "cpif twnk otqr osnc"

msg = MIMEMultipart()
msg['Subject'] = "Report with Attachment"
msg['From'] = my_mail
msg['To'] = my_mail

# Body
body = "Please find attached report"
msg.attach(MIMEText(body, 'plain'))

# Attachment
filename = "abd.txt"
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={filename}")
    msg.attach(part)

# Send
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(my_mail, my_password)
connection.send_message(msg)
connection.close()
```

### 13.3 HTML Email with Images

```python
from email.mime.image import MIMEImage

msg = MIMEMultipart()

# HTML body with image
body = """
<html>
<body>
<h1>Server Health Report</h1>
<p>Status: <b>All systems operational</b></p>
<img src="cid:logo" width="100" height="60">
</body>
</html>
"""
msg.attach(MIMEText(body, 'html'))

# Embed image
mylogo = r"C:\Users\User\PycharmProjects\pythonProject3\mahir.JPG"
with open(mylogo, 'rb') as filelogo:
    msgIMAGE = MIMEImage(filelogo.read())
msgIMAGE.add_header('Content-ID', '<logo>')
msg.attach(msgIMAGE)
```

**DevOps Use Cases:**
- Automated monitoring alerts
- Daily health reports
- Deployment notifications
- Incident reports

---

## 14. Task Scheduling

### 14.1 Schedule Library

```python
import schedule
import time
from datetime import datetime

def abd():
    now = datetime.today()
    print("current time is", now)
    print("This is test Schedule")

# Schedule patterns
schedule.every(10).seconds.do(abd)
schedule.every(10).minutes.do(abd)
schedule.every(10).hours.do(abd)
schedule.every().day.at("15:18").do(abd)
schedule.every(5).weeks.at("15:18").do(abd)
schedule.every().monday.at("15:18").do(abd)

# Run continuously
while True:
    schedule.run_pending()
    time.sleep(1)
```

**Scheduling Options:**
- `every(n).seconds` - Every n seconds
- `every(n).minutes` - Every n minutes
- `every().day.at("HH:MM")` - Daily at specific time
- `every().monday` - Weekly on specific day

### 14.2 Windows Task Scheduler Integration

**Create batch file (windows_task.bat):**
```batch
@ECHO OFF
"C:\Users\User\PycharmProjects\pythonProject3\.venv\Scripts\python.exe" "C:\Users\User\PycharmProjects\pythonProject3\my_scheduler-2.py"
EXIT
```

**Steps:**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily/Weekly
4. Action: Start a program
5. Program: `windows_task.bat`

### 14.3 Real-World Example: Automated Email Reports

```python
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_report():
    day = datetime.today()
    time_now = datetime.now()
    
    my_custom = day.strftime("%B %d %Y")
    current_time = time_now.strftime("%I:%M:%S %p")
    
    msg = MIMEMultipart()
    msg['Subject'] = f"Server Health Report {my_custom} {current_time}"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "recipient@gmail.com"
    
    body = "All systems operational"
    msg.attach(MIMEText(body, 'plain'))
    
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login("your_email@gmail.com", "app_password")
    connection.send_message(msg)
    connection.close()
    
    print(f"Report sent at {current_time}")

schedule.every().day.at("09:00").do(send_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 15. Encryption & Security

### 15.1 Fernet Encryption

```python
from cryptography.fernet import Fernet
import json

# Load password from JSON
jsonfile = 'mypass.json'
with open(jsonfile) as jf:
    my_dict = json.load(jf)

mypass = my_dict['password']
print("Original Password:", mypass)

# Encrypt
message = mypass.encode("utf-8")
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(message)
print("Encrypted:", encrypted)

# Decrypt
decrypted = f.decrypt(encrypted)
my_new_pass = decrypted.decode("utf-8")
print("Decrypted:", my_new_pass)
```

**Security Best Practices:**
- Store keys separately (environment variables)
- Never commit keys to version control
- Use different keys for different environments
- Rotate keys regularly

### 15.2 Secure Database Connections

```python
import json
import mysql.connector
from cryptography.fernet import Fernet

jsonfile = 'mypass.json'
with open(jsonfile) as jf:
    my_dict = json.load(jf)
    
    username_mysql = my_dict["username"]
    password_mysql = my_dict["password"]
    
    # Encrypt password
    message = password_mysql.encode("utf-8")
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    
    # Decrypt for use
    decrypted_message = f.decrypt(encrypted_message)
    passwd_mysql = decrypted_message.decode("utf-8")
    
    # Connect securely
    mydb = mysql.connector.connect(
        host="192.168.0.150",
        user=username_mysql,
        passwd=passwd_mysql,
        database="alnafi"
    )
```

**Production Recommendations:**
- Use environment variables for secrets
- Implement secrets management (AWS Secrets Manager, HashiCorp Vault)
- Enable SSL/TLS for database connections

---

## 16. Mini CLI Data Processor

### 16.1 Complete Project Structure

```python
import requests
import json
import argparse
import logging

def fetch_data(api_url):
    """Fetch data from API"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")

def save_data_to_file(data, file_path):
    """Save JSON data to file"""
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")

def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='CLI Data Processor')
    parser.add_argument('--api_url', type=str, required=True, 
                        help='API URL to fetch data from')
    parser.add_argument('--file_path', type=str, required=True, 
                        help='Path to save JSON data')
    return parser.parse_args()

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    args = parse_arguments()
    logging.info("Started fetching data...")
    data = fetch_data(args.api_url)
    if data:
        save_data_to_file(data, args.file_path)
```

**Run from command line:**
```bash
python Mini_project.py --api_url "https://jsonplaceholder.typicode.com/posts" --file_path "output.json"
```

**Project Features:**
- ✅ API data fetching
- ✅ Error handling
- ✅ Logging
- ✅ Command-line interface
- ✅ JSON processing

---

## 17. Real-World DevOps Projects

### 17.1 Server Health Monitoring

```python
import paramiko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

hostname = "192.168.0.150"
username = "kali"
password = "kali"

# Connect to server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Check free memory
mycmd = "free -g | grep Mem | awk '{print $7}'"
stdin, stdout, stderr = client.exec_command(mycmd)
mycmdout = stdout.read().decode()

# Alert if low memory
if int(mycmdout) <= 2:
    # Send alert email
    msg = MIMEMultipart()
    msg['Subject'] = "Low Memory Alert"
    msg['From'] = "admin@example.com"
    msg['To'] = "team@example.com"
    
    body = f"Server {hostname} has only {mycmdout}GB free memory"
    msg.attach(MIMEText(body, 'plain'))
    
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login("admin@example.com", "app_password")
    connection.send_message(msg)
    connection.close()
    
    print("Alert email sent")
else:
    print("Memory is sufficient")

client.close()
```

### 17.2 CSV to MySQL Data Pipeline

```python
import csv
import json
import mysql.connector
from cryptography.fernet import Fernet

# Load credentials
linux_jsonfile = "mylinux.json"
with open(linux_jsonfile) as jf:
    my_dict = json.load(jf)
    username_mysql = my_dict["username"]
    password_mysql = my_dict["password"]
    
    # Decrypt password
    message = password_mysql.encode("utf-8")
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    decrypted_message = f.decrypt(encrypted_message)
    passwd_mysql = decrypted_message.decode("utf-8")
    
    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="192.168.0.150",
        user=username_mysql,
        passwd=passwd_mysql,
        database="alnafi"
    )
    
    # Read CSV
    csvpath = "mycsvfile.csv"
    with open(csvpath) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        all_values = []
        
        headers = next(readCSV, None)
        
        for row_num, row in enumerate(readCSV, start=2):
            if len(row) == 9:
                try:
                    usage_percent = row[4].replace('%', '').strip()
                    usage_value = int(usage_percent) if usage_percent.isdigit() else 0
                    
                    value = (row[0], row[1], row[2], row[3], usage_value,
                            row[5], row[6], row[7], row[8])
                    all_values.append(value)
                except Exception as e:
                    print(f"Error processing row {row_num}: {e}")
    
    # Insert into MySQL
    if all_values:
        query = """
        INSERT INTO my_df_data 
        (filesystem, size, used, avail, usage_with_per, 
         mounted_on, datetime, ip_address, hostname) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        mycursor = mydb.cursor()
        mycursor.executemany(query, all_values)
        mydb.commit()
        print(f"Successfully inserted {mycursor.rowcount} rows")
        mycursor.close()
    
    mydb.close()
```

**Use Case:** Automated disk usage monitoring and database storage.

---

## 18. Error Handling & Debugging

### 18.1 Try-Except Blocks

```python
try:
    x = "ABD"
    print("My value is", x)
    print("My value is", y)  # NameError!
except:
    print("Something having issue")
```

### 18.2 Specific Exception Handling

```python
try:
    import os
    x = "ABD"
    y = "Ali"
    print("My value is", x)
    print("My value is", y)
    
    mylist = [2, 7, 8, 9]
    print(mylist[3])
    
    os.system('hostname')
    
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    result = a / b
    print(result)
    
except NameError:
    print("Variable not defined")
except IndexError:
    print("Index out of range")
except ModuleNotFoundError:
    print("Module not available")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value type")
except Exception as e:
    print("Something having issue:", e)
else:
    print("Everything executed successfully")
finally:
    print("This always executes")
```

### 18.3 Debugging with Print Statements

```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        print("Debug: Adding", num, "Total so far:", total)
    return total

numbers = [5, 10, 15]
print("Final Sum:", calculate_sum(numbers))
```

**Output:**
```
Debug: Adding 5 Total so far: 5
Debug: Adding 10 Total so far: 15
Debug: Adding 15 Total so far: 30
Final Sum: 30
```

### 18.4 Python Debugger (pdb)

```python
import pdb

def divide_numbers(a, b):
    pdb.set_trace()  # Breakpoint
    result = a / b
    print("Result:", result)
    return result

divide_numbers(10, 0)
```

**PDB Commands:**
- `n` (next) - Execute next line
- `c` (continue) - Continue execution
- `p variable` - Print variable value
- `q` (quit) - Exit debugger

---

## 19. Python Modules & Packages

### 19.1 OS Module

```python
import os

# Common methods
print(os.getcwd())         # Current directory
print(os.listdir())        # List files
print(os.system('dir'))    # Execute system command
print(os.getpid())         # Process ID

# Path operations
mypath = "C:\\Users\\User\\Desktop\\Python"
print(os.path.basename(mypath))   # 'Python'
print(os.path.dirname(mypath))    # 'C:\\Users\\User\\Desktop'
print(os.path.exists(mypath))     # True/False
print(os.path.isfile(mypath))     # True/False
print(os.path.isdir(mypath))      # True/False
```

### 19.2 Platform Module

```python
import platform

print(platform.system())          # 'Windows', 'Linux', 'Darwin'
print(platform.machine())         # 'AMD64', 'x86_64'
print(platform.processor())       # Processor info
print(platform.python_version())  # Python version
print(platform.platform())        # Full platform info

# Cross-platform commands
if platform.system() == 'Windows':
    os.system("ipconfig")
elif platform.system() == 'Linux':
    os.system("ifconfig")
else:
    print("Unsupported OS")
```

### 19.3 Datetime Module

```python
import datetime

# Current date/time
current = datetime.datetime.now()
print(current)  # 2025-12-20 15:30:45.123456

# Extract components
print(current.year)        # 2025
print(current.month)       # 12
print(current.day)         # 20
print(current.hour)        # 15
print(current.minute)      # 30
print(current.second)      # 45
print(current.weekday())   # 0 (Monday) to 6 (Sunday)

# Format date/time
year = current.strftime("%Y")           # 2025
month = current.strftime("%m")          # 12
day = current.strftime("%d")            # 20
time = current.strftime("%H:%M:%S")     # 15:30:45
custom = current.strftime("%B %d, %Y")  # December 20, 2025
```

### 19.4 Time Calculations

```python
from datetime import datetime

start_time = datetime.strptime("2:13:57", "%H:%M:%S")
end_time = datetime.strptime("11:47:52", "%H:%M:%S")

diff = end_time - start_time
print("Difference:", diff)

seconds = diff.total_seconds()
minutes = seconds / 60
hours = minutes / 60

print(f"Difference in seconds: {seconds}")
print(f"Difference in minutes: {minutes}")
print(f"Difference in hours: {hours}")
```

---

## 20. Best Practices & Tips

### 20.1 Code Style

**PEP 8 Standards:**
```python
# Good
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Bad
def calculate_sum( numbers ):
  total=0
  for num in numbers:
    total+=num
  return total
```

**Tools:**
- `flake8` - Style checker
- `black` - Auto-formatter
- `autopep8` - Auto-formatter

### 20.2 Virtual Environments

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Linux/Mac)
source myenv/bin/activate

# Install packages
pip install requests pandas

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### 20.3 Project Structure

```
project/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── config/
    └── settings.json
```

---

## 21. DevOps Career Tips

### 21.1 Skills to Master

**Essential Python Skills:**
- ✅ Data structures & algorithms
- ✅ File handling & data processing
- ✅ API interactions (requests library)
- ✅ Database operations
- ✅ SSH/SFTP automation
- ✅ Error handling & logging
- ✅ Regular expressions

**DevOps Tools Integration:**
- **Infrastructure as Code:** Terraform, Ansible
- **CI/CD:** Jenkins, GitLab CI, GitHub Actions
- **Containers:** Docker, Kubernetes
- **Monitoring:** Prometheus, Grafana
- **Cloud:** AWS, Azure, GCP

### 21.2 Portfolio Projects

**Recommended Projects:**
1. ✅ Automated server health monitoring
2. ✅ CI/CD pipeline script
3. ✅ Log aggregation & analysis tool
4. ✅ Infrastructure automation suite
5. ✅ Database backup automation

### 21.3 Interview Preparation

**Common Python Interview Questions:**

1. **What is the difference between list and tuple?**
   - Lists are mutable, tuples are immutable
   - Lists use [], tuples use ()
   - Tuples are faster for read-only data

2. **Explain *args and **kwargs**
   - *args: variable positional arguments (tuple)
   - **kwargs: variable keyword arguments (dictionary)

3. **How do you handle exceptions in Python?**
   - Use try-except blocks
   - Catch specific exceptions
   - Use finally for cleanup

4. **What is list comprehension?**
   ```python
   # Traditional
   squares = []
   for i in range(10):
       squares.append(i**2)
   
   # Comprehension
   squares = [i**2 for i in range(10)]
   ```

---

## 22. Next Steps & Resources

### 22.1 Continue Learning

**Advanced Topics:**
- Async/await programming
- Testing (pytest, unittest)
- Type hints & mypy
- Design patterns
- Performance optimization

**DevOps-Specific:**
- Ansible playbooks with Python
- AWS boto3 library
- Kubernetes Python client
- Prometheus metrics
- Terraform with Python

### 22.2 Recommended Resources

**Books:**
- "Automate the Boring Stuff with Python"
- "Python for DevOps"
- "Effective Python"

**Online Platforms:**
- Real Python
- Python.org documentation
- Stack Overflow
- GitHub repositories

### 22.3 Certification Paths

**Python Certifications:**
- PCAP (Certified Associate in Python Programming)
- PCPP (Certified Professional in Python Programming)

**DevOps Certifications:**
- AWS Certified DevOps Engineer
- Google Cloud DevOps Engineer
- CKA (Certified Kubernetes Administrator)

---

## 23. Conclusion

### 23.1 Key Takeaways

**Python Fundamentals:**
✅ Master data structures (lists, tuples, dicts, sets)
✅ Understand control flow (if/else, loops)
✅ Write reusable functions
✅ Handle errors gracefully

**File & Data Processing:**
✅ Read/write files (text, CSV, JSON)
✅ Parse and transform data
✅ Use regular expressions
✅ Work with databases

**DevOps Automation:**
✅ Remote server management (SSH/SFTP)
✅ Email automation
✅ Task scheduling
✅ Encryption & security

**Professional Skills:**
✅ Write clean, maintainable code
✅ Use version control (Git)
✅ Document your projects
✅ Build a strong portfolio

### 23.2 Your Python Journey

**You've learned:**
- 📚 51 Python scripts covering fundamentals to advanced
- 🔧 Real-world DevOps automation projects
- 💼 Professional development practices
- 🎯 Career-ready skills for DevOps/SRE roles

**Next steps:**
1. Practice coding daily
2. Build your own projects
3. Contribute to open source
4. Network on LinkedIn
5. Apply for DevOps positions

### 23.3 Final Words

**Congratulations!** You've completed a comprehensive Python training program designed specifically for DevOps professionals. The skills you've learned here are directly applicable to real-world infrastructure automation, monitoring, and management tasks.

**Remember:**
- 💪 Practice makes perfect
- 📖 Keep learning and staying updated
- 🤝 Collaborate and share knowledge
- 🚀 Build projects that solve real problems

**Your Python DevOps journey starts now. Good luck!**

---

## Appendix

### A. Quick Reference Commands

```python
# File Operations
with open('file.txt', 'r') as f: data = f.read()

# JSON
import json
with open('data.json') as f: data = json.load(f)

# CSV
import csv
with open('data.csv') as f: reader = csv.reader(f)

# SSH
import paramiko
client = paramiko.SSHClient()
client.connect(host, username, password)

# MySQL
import mysql.connector
db = mysql.connector.connect(host, user, password, database)

# Email
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
```

### B. Common Error Solutions

**ImportError:** Module not found
```bash
pip install module_name
```

**NameError:** Variable not defined
```python
# Define variable before use
x = 10
print(x)
```

**IndexError:** List index out of range
```python
# Check list length
if len(mylist) > index:
    print(mylist[index])
```

**KeyError:** Dictionary key doesn't exist
```python
# Use .get() method
value = mydict.get('key', 'default')
```

---

**End of Master Guide**

**
