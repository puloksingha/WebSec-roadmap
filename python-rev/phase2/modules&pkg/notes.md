# Python Revision — Topic 11: Modules and Packages

## 1. Introduction to Modules and Packages

As Python programs become larger, writing all the code in one file becomes difficult to manage.

Python solves this problem using **modules and packages**.

### What is a module?

A module is a Python file (`.py`) containing code such as:

- Variables
- Functions
- Classes
- Statements

You can import a module into another Python file and reuse its code.

Example:

```text
math_utils.py
```

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

This file is a module named `math_utils`.

### What is a package?

A package is a way to organize related Python modules into a directory structure.

Example:

```text
my_project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

Here:

- `my_project` is the project directory.
- `utilities` is a package.
- `math_utils.py` and `string_utils.py` are modules.
- `__init__.py` traditionally marks a regular Python package.

Modern Python also supports namespace packages without `__init__.py`.

### Module vs. Package

| Module | Package |
|---|---|
| Usually a single `.py` file | Usually a directory containing modules |
| Contains functions, classes, and variables | Organizes related modules |
| Imported using its module name | Imported using its package path |
| Example: `math_utils.py` | Example: `utilities/` |

---

## 2. Importing Modules

Python provides the `import` statement to use code from other modules.

### 2.1 Import an entire module

Syntax:

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

Here:

- `math` is the module.
- `sqrt()` is a function inside the module.
- `pi` is a constant inside the module.

You access its members using the dot operator.

### 2.2 Import specific members

You can import only the functions or variables you need.

```python
from math import sqrt, pi

print(sqrt(36))
print(pi)
```

Output:

```text
6.0
3.141592653589793
```

You do not need to write `math.sqrt()` because `sqrt` is imported directly.

### 2.3 Import using an alias

The `as` keyword gives a module or imported member another name.

```python
import math as m

print(m.sqrt(49))
```

Output:

```text
7.0
```

You can also alias individual functions:

```python
from math import factorial as fact

print(fact(5))
```

Output:

```text
120
```

### 2.4 Import everything using `*`

```python
from math import *

print(sqrt(64))
print(pow(2, 3))
```

This imports names that the module makes available for star imports.

However, this approach is generally discouraged because:

- It can create naming conflicts.
- It becomes difficult to identify where a function came from.
- It makes code harder to understand.

Prefer explicit imports.

### 2.5 Import multiple modules

```python
import os
import sys
import math
import random
```

You can also import multiple modules in one statement:

```python
import os, sys, math
```

However, separate import statements are often easier to read.

### 2.6 Import a submodule

```python
import urllib.parse

url = "https://example.com/search?q=python"

result = urllib.parse.urlparse(url)

print(result.hostname)
print(result.path)
```

Output:

```text
example.com
/search
```

### 2.7 Understanding `dir()`

The `dir()` function lists names available in a module or object.

```python
import math

print(dir(math))
```

This helps you explore module contents.

### 2.8 Understanding `help()`

The `help()` function displays documentation.

```python
import math

help(math)
```

You can also inspect a specific function:

```python
help(math.sqrt)
```

**Important:** Use `dir()` to explore available names and `help()` to understand how they work.

---

## 3. Standard Library Overview

Python comes with a large collection of built-in modules called the **Python Standard Library**.

You do not need to install these modules separately.

They provide functionality for:

- File and directory management
- Operating-system interaction
- Networking
- Data processing
- Mathematics
- Date and time operations
- Security-related utilities
- Logging
- Testing
- Serialization

### Important standard library modules

#### 3.1 `os`

Used for operating-system interactions.

```python
import os

print(os.getcwd())
print(os.listdir("."))
```

Common uses:

- Getting the current working directory.
- Listing directory contents.
- Working with environment variables.
- Creating directories.
- Managing operating-system processes.

#### 3.2 `sys`

Provides access to Python interpreter information and functionality.

```python
import sys

print(sys.version)
print(sys.platform)
print(sys.path)
```

Common uses:

- Checking Python version.
- Accessing command-line arguments.
- Inspecting module search paths.
- Controlling interpreter behavior.

#### 3.3 `pathlib`

Provides object-oriented file and directory path handling.

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.name)
```

#### 3.4 `math`

Provides mathematical functions.

```python
import math

print(math.sqrt(100))
print(math.factorial(5))
print(math.ceil(4.2))
print(math.floor(4.8))
```

Output:

```text
10.0
120
5
4
```

#### 3.5 `random`

Generates pseudo-random values.

```python
import random

print(random.randint(1, 10))
print(random.choice(["Python", "Linux", "Networking"]))
```

Important functions:

- `randint()`
- `choice()`
- `shuffle()`
- `random()`
- `sample()`

**Security warning:** Do not use `random` for passwords, authentication tokens, or security-sensitive random values. Use `secrets` instead.

#### 3.6 `secrets`

Provides cryptographically strong random values.

```python
import secrets

token = secrets.token_hex(16)

print(token)
```

This generates a random hexadecimal token.

You can also generate a secure random choice:

```python
import secrets

password_char = secrets.choice("abcdefghijklmnopqrstuvwxyz0123456789")

print(password_char)
```

#### 3.7 `datetime`

Used for dates and times.

```python
from datetime import datetime

now = datetime.now()

print(now)
```

Format a date:

```python
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

#### 3.8 `time`

Used for time-related operations.

```python
import time

print(time.time())

time.sleep(2)

print("Finished")
```

#### 3.9 `json`

Used to encode and decode JSON data.

```python
import json

data = {
    "name": "Pulok",
    "skill": "Python"
}

json_data = json.dumps(data)

print(json_data)
```

Convert JSON back into a Python object:

```python
python_data = json.loads(json_data)

print(python_data["name"])
```

#### 3.10 `re`

Provides regular-expression functionality.

```python
import re

text = "Contact: admin@example.com"

result = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

print(result)
```

Output:

```text
['admin@example.com']
```

Useful for:

- Pattern matching.
- Text validation.
- Extracting information.
- Searching structured text.

#### 3.11 `subprocess`

Runs external programs and commands.

```python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

Important: Avoid using `shell=True` with untrusted input. Prefer passing commands as a list of arguments.

#### 3.12 `socket`

Provides low-level networking functionality.

```python
import socket

print(socket.gethostname())
```

Resolve a hostname:

```python
import socket

ip = socket.gethostbyname("example.com")

print(ip)
```

Only test systems and networks you are authorized to access.

#### 3.13 `hashlib`

Provides hashing algorithms.

```python
import hashlib

text = "Python"

result = hashlib.sha256(text.encode()).hexdigest()

print(result)
```

Useful for:

- File integrity checks.
- Hashing data.
- Verifying file contents.

Note: SHA-256 is a general-purpose hash, not a password-storage algorithm. Use dedicated password-hashing schemes such as Argon2 or bcrypt for passwords.

#### 3.14 `logging`

Provides structured application logging.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("High memory usage")
logging.error("Connection failed")
```

#### 3.15 `collections`

Provides specialized container data types.

```python
from collections import Counter

words = ["python", "linux", "python", "networking"]

result = Counter(words)

print(result)
```

Output:

```text
Counter({'python': 2, 'linux': 1, 'networking': 1})
```

Other useful classes include:

- `defaultdict`
- `deque`
- `namedtuple`
- `Counter`

#### 3.16 `argparse`

Used to build command-line interfaces.

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", required=True)

args = parser.parse_args()

print("Hello", args.name)
```

Run it:

```bash
python main.py --name Pulok
```

Output:

```text
Hello Pulok
```

### Standard library quick reference

| Module | Purpose |
|---|---|
| `os` | Operating-system interaction |
| `sys` | Python interpreter information |
| `pathlib` | File paths |
| `math` | Mathematical operations |
| `random` | Pseudo-random values |
| `secrets` | Secure random values |
| `datetime` | Date and time |
| `time` | Time-related functions |
| `json` | JSON processing |
| `re` | Regular expressions |
| `subprocess` | Run external commands |
| `socket` | Network communication |
| `hashlib` | Hashing |
| `logging` | Application logging |
| `collections` | Specialized data structures |
| `argparse` | Command-line arguments |
| `csv` | CSV file processing |
| `sqlite3` | SQLite database |
| `threading` | Thread-based concurrency |
| `multiprocessing` | Process-based concurrency |
| `unittest` | Unit testing |
| `tempfile` | Temporary files |
| `shutil` | High-level file operations |
| `ipaddress` | IPv4 and IPv6 address handling |
| `ssl` | TLS/SSL support |
| `urllib` | URL handling and HTTP utilities |

---

## 4. Creating Custom Modules

You can create your own Python modules to organize reusable code.

### Step 1: Create a Python file

Create a file named:

```text
calculator.py
```

Add the following code:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

This is your custom module.

### Step 2: Create another Python file

Create:

```text
main.py
```

Add:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
```

### Step 3: Run the program

```bash
python main.py
```

Output:

```text
15
5
50
```

### Import specific functions

Instead of importing the entire module:

```python
from calculator import add, multiply

print(add(10, 5))
print(multiply(10, 5))
```

### Custom module containing variables and functions

File: `security_utils.py`

```python
TOOL_NAME = "Security Toolkit"


def banner():
    print("Welcome to", TOOL_NAME)


def calculate_hash(text):
    import hashlib

    return hashlib.sha256(text.encode()).hexdigest()
```

File: `main.py`

```python
import security_utils

security_utils.banner()

result = security_utils.calculate_hash("hello")

print(result)
```

This is a simple example of reusing functionality across files.

### Important rules

- Module filenames should normally use lowercase letters.
- Use underscores to separate words.
- Avoid naming your files after standard library modules.
- Keep related functions together.
- Avoid unnecessarily large modules.

For example, avoid naming your own files:

```text
random.py
json.py
socket.py
math.py
```

These names can interfere with imports of the corresponding standard library modules.

---

## 5. Creating Packages

A package helps organize multiple related modules.

### Example project structure

```text
security_tool/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── hashing.py
    ├── networking.py
    └── file_utils.py
```

Here:

- `security_tool` is the main project directory.
- `utilities` is a package.
- `hashing.py`, `networking.py`, and `file_utils.py` are modules.
- `__init__.py` marks the package as a regular package.

### Step 1: Create the directory

```bash
mkdir security_tool
cd security_tool

mkdir utilities
```

### Step 2: Create the package initializer

Create:

```text
utilities/__init__.py
```

It can initially be empty.

### Step 3: Create individual modules

File: `utilities/hashing.py`

```python
import hashlib


def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
```

File: `utilities/networking.py`

```python
import socket


def resolve_domain(domain):
    return socket.gethostbyname(domain)
```

File: `utilities/file_utils.py`

```python
from pathlib import Path


def file_exists(filename):
    return Path(filename).exists()
```

### Step 4: Import package modules

File: `main.py`

```python
from utilities import hashing
from utilities import networking
from utilities import file_utils


print(hashing.sha256_hash("hello"))

print(networking.resolve_domain("example.com"))

print(file_utils.file_exists("data.txt"))
```

### Alternative: Import specific functions

```python
from utilities.hashing import sha256_hash
from utilities.file_utils import file_exists

print(sha256_hash("hello"))

print(file_exists("data.txt"))
```

### Understanding `__init__.py`

The `__init__.py` file can contain initialization code and control which names are exposed by a package.

Example:

```python
# utilities/__init__.py

from .hashing import sha256_hash
from .file_utils import file_exists
```

Now you can write:

```python
from utilities import sha256_hash, file_exists
```

You do not have to import every function into `__init__.py`. For larger packages, keeping imports explicit can help avoid unnecessary dependencies and circular imports.

---

## 6. Understanding `if __name__ == "__main__"`

This is one of the most important concepts in Python modules.

Every Python module has a special variable called `__name__`.

Its value depends on how the file is executed.

### Case 1: Running a file directly

File: `calculator.py`

```python
print(__name__)
```

Run:

```bash
python calculator.py
```

Output:

```text
__main__
```

When a Python file is executed directly, its `__name__` variable is set to `"__main__"`.

### Case 2: Importing a file

File: `calculator.py`

```python
print(__name__)


def add(a, b):
    return a + b
```

File: `main.py`

```python
import calculator
```

Run:

```bash
python main.py
```

Output:

```text
calculator
```

When imported, the module's `__name__` is normally its import name.

### Why use `if __name__ == "__main__"`?

Suppose your module contains testing code.

You do not want that code to execute every time another file imports the module.

Example:

File: `calculator.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":

    print("Calculator testing")

    print(add(10, 5))
    print(subtract(10, 5))
```

If you run:

```bash
python calculator.py
```

Output:

```text
Calculator testing
15
5
```

But if another file imports it:

```python
import calculator

print(calculator.add(20, 10))
```

Output:

```text
30
```

The testing code inside the `if` block does not execute during the import.

### Recommended structure

```python
# Imports

import math


# Constants

PI = 3.14159


# Functions

def calculate_square(number):
    return number ** 2


# Main function

def main():
    print(calculate_square(5))


# Entry point

if __name__ == "__main__":
    main()
```

**Remember:** This condition separates reusable module functionality from code intended to run when the file is executed directly.

---

## 7. Absolute and Relative Imports

Python supports two main import styles:

1. Absolute imports.
2. Relative imports.

### 7.1 Absolute imports

An absolute import specifies the complete path from the top-level package.

Project structure:

```text
project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── hashing.py
    └── networking.py
```

In `main.py`:

```python
from utilities.hashing import sha256_hash
from utilities.networking import resolve_domain
```

These are absolute imports.

### 7.2 Relative imports

Relative imports use dots to refer to the current package and its parent packages.

Suppose the structure is:

```text
project/
│
└── security/
    ├── __init__.py
    ├── hashing.py
    │
    └── tools/
        ├── __init__.py
        ├── scanner.py
        └── reporter.py
```

Inside `security/tools/scanner.py`:

```python
from ..hashing import sha256_hash
from .reporter import generate_report
```

Meaning:

- `.` refers to the current package (`tools`).
- `..` refers to the parent package (`security`).
- `...` refers to one more level above.

### Absolute vs. relative imports

| Absolute import | Relative import |
|---|---|
| Uses the complete package path | Uses dots to refer to package locations |
| Often easier to understand | Useful inside packages |
| Explicit about where code comes from | Can be shorter for nearby modules |
| Example: `from security.hashing import sha256_hash` | Example: `from ..hashing import sha256_hash` |

### Important rule

Relative imports are intended for package modules.

Running a package module directly as a standalone script can cause errors such as:

```text
ImportError: attempted relative import with no known parent package
```

A common solution is to run the module from the project root using:

```bash
python -m security.tools.scanner
```

Use the module's package path and execute it from the appropriate project location.

**Best practice:** Prefer absolute imports for clarity in many projects. Use relative imports when they make internal package relationships easier to maintain.

---

## 8. Module Search Paths

When Python imports a module, it searches specific locations to find it.

These locations are available through:

```python
import sys

print(sys.path)
```

`sys.path` is a list of directories and other entries Python uses to locate modules.

### Common search locations

1. The directory associated with the running script or current execution context.
2. Directories configured through `PYTHONPATH`.
3. Standard library locations.
4. Site-package directories where third-party packages are installed.

The precise search behavior depends on how Python was started and its environment.

### Example

Suppose you have:

```text
project/
│
├── main.py
│
└── helpers/
    └── message.py
```

If `main.py` tries:

```python
import message
```

Python may fail to find it because `message.py` is inside `helpers`, not directly in the import search path.

One option is:

```python
from helpers import message
```

Another option is to organize `helpers` as a package.

### Understanding PYTHONPATH

`PYTHONPATH` is an environment variable that can add directories to Python's module search path.

Linux example:

```bash
export PYTHONPATH="$PYTHONPATH:/home/user/python_projects"
```

Windows PowerShell example:

```powershell
$env:PYTHONPATH = "$env:PYTHONPATH;C:\Users\YourName\python_projects"
```

You can inspect the environment variable in Python:

```python
import os

print(os.environ.get("PYTHONPATH"))
```

### Temporarily modifying sys.path

```python
import sys

sys.path.append("/home/user/python_projects")

print(sys.path)
```

This adds a directory to the current Python process's search path.

Use this carefully. It can make imports difficult to reproduce and may introduce security risks if untrusted directories are included.

### Finding the location of an imported module

```python
import math

print(math.__file__)
```

Some built-in or frozen modules do not have a normal filesystem path, so `__file__` is not available for every module.

For many modules, this helps identify which file Python imported.

---

## 9. Package Organization

Good package organization makes projects easier to understand, test, and maintain.

### Poor project organization

```text
security_tool/
│
└── main.py
```

If every function is written in `main.py`, the file can become difficult to maintain.

### Better project organization

```text
security_tool/
│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── core/
│   ├── __init__.py
│   ├── scanner.py
│   └── analyzer.py
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   └── logger.py
│
├── reports/
│   ├── __init__.py
│   └── generator.py
│
├── tests/
│   ├── __init__.py
│   └── test_scanner.py
│
├── requirements.txt
└── README.md
```

### What belongs in each directory?

| Directory/File | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `config/` | Configuration settings |
| `core/` | Main application functionality |
| `utils/` | Reusable helper functions |
| `reports/` | Report generation |
| `tests/` | Automated tests |
| `requirements.txt` | Project dependencies |
| `README.md` | Project documentation |

### Naming conventions

Follow these practices:

- Use lowercase package names.
- Separate words using underscores.
- Give modules meaningful names.
- Keep related functionality together.
- Avoid excessively large modules.
- Avoid unnecessary nested directories.
- Avoid naming modules after standard library modules.

### Example naming

Good:

```text
network_scanner.py
file_analyzer.py
report_generator.py
```

Avoid:

```text
a.py
test123.py
new_final_latest.py
```

### A useful project structure for cybersecurity tools

```text
web_security_toolkit/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── dns_lookup.py
│   ├── http_analyzer.py
│   ├── header_checker.py
│   └── port_checker.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── file_handler.py
│
├── reports/
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

This structure separates different responsibilities and makes it easier to expand the application.

---

## 10. Dependency Management

A dependency is an external library or package that your Python project needs.

For example, a project might depend on:

- `requests`
- `beautifulsoup4`
- `flask`
- `httpx`
- `scapy`

Python has a package installer called `pip`.

### 10.1 Check pip version

```bash
python -m pip --version
```

### 10.2 Install a package

```bash
python -m pip install requests
```

### 10.3 Install a specific version

```bash
python -m pip install requests==2.32.3
```

### 10.4 Upgrade a package

```bash
python -m pip install --upgrade requests
```

### 10.5 Uninstall a package

```bash
python -m pip uninstall requests
```

### 10.6 List installed packages

```bash
python -m pip list
```

### 10.7 Display package information

```bash
python -m pip show requests
```

### 10.8 Save dependencies

```bash
python -m pip freeze > requirements.txt
```

This creates a list of installed packages and their versions.

Example:

```text
requests==2.32.3
```

### 10.9 Install dependencies from requirements.txt

```bash
python -m pip install -r requirements.txt
```

This installs the listed dependencies.

### 10.10 Virtual environments

A virtual environment provides an isolated Python environment for a project.

This helps prevent dependency conflicts between projects.

Create one:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Activate on Linux or macOS:

```bash
source .venv/bin/activate
```

Install a package:

```bash
python -m pip install requests
```

Deactivate:

```bash
deactivate
```

### 10.11 Recommended dependency workflow

For a new project:

```bash
mkdir my_project
cd my_project

python -m venv .venv
```

Activate the environment, then:

```bash
python -m pip install requests
```

Save dependencies:

```bash
python -m pip freeze > requirements.txt
```

Later, another developer can recreate the environment using:

```bash
python -m pip install -r requirements.txt
```

### 10.12 requirements.txt vs. pyproject.toml

`requirements.txt` is commonly used to list packages for installation.

`pyproject.toml` is a modern project configuration file used by Python packaging and development tools.

A simple example:

```toml
[project]
name = "my-security-tool"
version = "0.1.0"
description = "A Python security learning project"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.32"
]
```

For learning, start with `requirements.txt`. Learn `pyproject.toml` when you begin creating more structured and distributable Python projects.

### Dependency management best practices

- Use a separate virtual environment for each project.
- Keep track of dependencies.
- Avoid installing unnecessary packages.
- Pin versions when reproducibility matters.
- Update dependencies carefully.
- Install packages from trusted sources.
- Do not commit virtual environment folders to Git.
- Keep secrets and credentials out of dependency files.

---

## 11. Avoiding Circular Imports

A circular import happens when two or more modules depend on each other in a cycle.

This can cause import errors or partially initialized modules.

### Example of a circular import

Project structure:

```text
project/
│
├── main.py
├── module_a.py
└── module_b.py
```

File: `module_a.py`

```python
from module_b import function_b


def function_a():
    print("Function A")
    function_b()
```

File: `module_b.py`

```python
from module_a import function_a


def function_b():
    print("Function B")
    function_a()
```

Here:

- `module_a` imports `module_b`.
- `module_b` imports `module_a`.

This creates a circular dependency.

Depending on the import sequence and what each module accesses, Python may raise an error involving a partially initialized module.

### Why circular imports are problematic

- Modules depend heavily on each other.
- Code becomes difficult to maintain.
- Import errors become harder to debug.
- Testing becomes more complicated.
- Initialization order becomes important.

### Solution 1: Reorganize shared functionality

Move shared functions into a third module.

Project structure:

```text
project/
│
├── module_a.py
├── module_b.py
└── common.py
```

File: `common.py`

```python
def shared_function():
    print("Shared functionality")
```

File: `module_a.py`

```python
from common import shared_function


def function_a():
    print("Function A")
    shared_function()
```

File: `module_b.py`

```python
from common import shared_function


def function_b():
    print("Function B")
    shared_function()
```

Now both modules depend on `common.py`, rather than depending on each other.

### Solution 2: Use dependency injection

Instead of importing another module's function directly, pass the required function as an argument.

```python
# module_a.py

def function_a(callback):
    print("Function A")
    callback()
```

```python
# module_b.py

def function_b():
    print("Function B")
```

```python
# main.py

from module_a import function_a
from module_b import function_b

function_a(function_b)
```

Output:

```text
Function A
Function B
```

### Solution 3: Use a local import when appropriate

Sometimes a function only needs another module at runtime.

A local import can help:

```python
def function_a():

    from module_b import function_b

    function_b()
```

This delays the import until the function is called.

However, local imports should not be used to hide poor architecture. Prefer reorganizing shared functionality when possible.

### Best practices for avoiding circular imports

1. Keep modules focused on one responsibility.
2. Avoid unnecessary dependencies between modules.
3. Move shared functionality into separate modules.
4. Pass dependencies as function arguments when appropriate.
5. Use local imports only when there is a good reason.
6. Keep the dependency direction clear.

---

## 12. Practical Project: Build a Modular Security Toolkit

Now combine the concepts you have learned.

### Objective

Create a small Python project with separate modules for hashing, domain lookup, and file management.

Use it only with files and domains you are authorized to analyze.

### Project structure

```text
security_toolkit/
│
├── main.py
│
├── utilities/
│   ├── __init__.py
│   ├── hashing.py
│   ├── networking.py
│   └── file_utils.py
│
└── requirements.txt
```

This project uses only Python standard library modules, so it does not need third-party dependencies.

### File 1: utilities/hashing.py

```python
import hashlib


def calculate_sha256(text):

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()
```

### File 2: utilities/networking.py

```python
import socket


def domain_lookup(domain):

    return socket.gethostbyname(domain)
```

### File 3: utilities/file_utils.py

```python
from pathlib import Path


def save_result(filename, content):

    path = Path(filename)

    with path.open("a", encoding="utf-8") as file:
        file.write(content + "\n")


def read_result(filename):

    path = Path(filename)

    if not path.exists():
        return "File not found"

    return path.read_text(encoding="utf-8")
```

### File 4: main.py

```python
from utilities.hashing import calculate_sha256
from utilities.networking import domain_lookup
from utilities.file_utils import save_result, read_result


def main():

    print("Python Security Toolkit")

    text = "hello"

    result = calculate_sha256(text)

    print("SHA-256:", result)

    domain = "example.com"

    try:

        ip = domain_lookup(domain)

        print("Domain IP:", ip)

        save_result(
            "results.txt",
            f"{domain} -> {ip}"
        )

    except OSError as error:

        print("Network lookup failed:", error)

    print(read_result("results.txt"))


if __name__ == "__main__":
    main()
```

### Run the project

From inside the `security_toolkit` directory:

```bash
python main.py
```

The program:

1. Imports custom modules.
2. Calculates a SHA-256 hash.
3. Resolves a domain.
4. Saves the result.
5. Reads the saved result.
6. Uses a main entry point.

### Skills practiced

- Importing modules.
- Creating custom modules.
- Creating packages.
- Absolute imports.
- `__name__ == "__main__"`.
- Standard library usage.
- File handling.
- Exception handling.
- Code organization.

---

## 13. Common Mistakes

### Mistake 1: Naming a file after a standard library module

Avoid:

```text
random.py
socket.py
json.py
```

These names can shadow the standard library modules and cause confusing import errors.

### Mistake 2: Forgetting the module's location

If Python cannot find a module, check:

```python
import sys

print(sys.path)
```

Also check the project structure and current working directory.

### Mistake 3: Running a package module directly

This may fail when relative imports are used:

```bash
python security/tools/scanner.py
```

Prefer:

```bash
python -m security.tools.scanner
```

Run it from the correct project directory.

### Mistake 4: Using wildcard imports everywhere

Avoid:

```python
from math import *
```

Prefer:

```python
from math import sqrt, factorial
```

### Mistake 5: Installing packages globally for every project

Prefer creating a virtual environment:

```bash
python -m venv .venv
```

### Mistake 6: Creating unnecessary circular dependencies

Avoid modules importing each other without a clear architectural reason.

Move shared functionality into a separate module.

### Mistake 7: Forgetting to install project dependencies

If a third-party module is missing, you may see:

```text
ModuleNotFoundError: No module named 'requests'
```

Install it in the active environment:

```bash
python -m pip install requests
```

### Mistake 8: Confusing a package with an installed external library

A package can be part of your own project or a third-party library installed through a package manager. They are not necessarily the same thing.

---

## 14. Practice Exercises

### Beginner Level

**Exercise 1: Import modules**

Import `math` and calculate:

- Square root of 144.
- Factorial of 5.
- Ceiling of 4.3.

**Exercise 2: Standard library**

Use `datetime` to print the current date and time.

**Exercise 3: Random values**

Use `random` to select one item from a list of five programming languages.

**Exercise 4: Custom module**

Create a module called `calculator.py` containing addition, subtraction, multiplication, and division functions.

Import those functions into `main.py`.

**Exercise 5: Main entry point**

Create a Python file containing a function and an `if __name__ == "__main__"` block. Test it by running and importing the module.

### Intermediate Level

**Exercise 6: Create a package**

Create a package named `utilities` with three modules:

- `math_utils.py`
- `string_utils.py`
- `file_utils.py`

Import functions from all three modules into `main.py`.

**Exercise 7: Module search paths**

Print `sys.path` and identify the locations Python uses to find modules.

**Exercise 8: Dependency management**

Create a virtual environment, install `requests`, and save the dependencies into `requirements.txt`.

**Exercise 9: Absolute imports**

Create a package containing multiple modules and import them using absolute imports.

**Exercise 10: Relative imports**

Create a nested package and practice importing modules using `.` and `..`.

### Advanced Level

**Exercise 11: Avoid circular imports**

Create two modules with a circular dependency. Reorganize the code using a third shared module.

**Exercise 12: Command-line application**

Use `argparse` to build a program that accepts a domain name as an argument.

**Exercise 13: Modular log analyzer**

Build a project with separate modules for reading logs, analyzing entries, and generating reports.

**Exercise 14: Security toolkit**

Build a modular toolkit with:

- Hash generation.
- File analysis.
- Domain resolution.
- Result storage.

**Exercise 15: Project organization**

Take an existing Python script and divide it into reusable modules and packages.

---

## 15. Quick Revision Questions and Answers

**Q1. What is a Python module?**

A Python module is a `.py` file containing reusable Python code.

**Q2. What is a package?**

A package organizes related Python modules into a directory structure.

**Q3. Which keyword is used to import modules?**

`import`.

**Q4. What is the purpose of `from`?**

It imports specific names from a module or package.

**Q5. What is an alias in Python imports?**

An alternative name given using the `as` keyword.

**Q6. What is the Python Standard Library?**

A collection of modules distributed with Python.

**Q7. What is `__init__.py`?**

A file commonly used to mark and initialize regular Python packages.

**Q8. What is `__name__`?**

A special variable that identifies the module's execution or import name.

**Q9. What does `if __name__ == "__main__"` do?**

It runs a block only when the module is executed as the main program.

**Q10. What is an absolute import?**

An import that specifies the full package path from the top-level package.

**Q11. What is a relative import?**

An import that uses dots to refer to the current or parent package.

**Q12. What is `sys.path`?**

A list of locations Python searches when importing modules.

**Q13. What is `PYTHONPATH`?**

An environment variable used to add locations to Python's module search path.

**Q14. What is a dependency?**

An external library or package required by a project.

**Q15. What is pip?**

Python's commonly used package installer.

**Q16. Why use virtual environments?**

To isolate project dependencies and prevent conflicts.

**Q17. What is a circular import?**

A situation where modules depend on each other in an import cycle.

**Q18. How can circular imports be avoided?**

By reorganizing shared functionality, reducing dependencies, or using dependency injection.

**Q19. What is `requirements.txt`?**

A file commonly used to list project dependencies and their versions.

**Q20. What is `pyproject.toml`?**

A modern Python project configuration file used by packaging and development tools.

---

## 16. Modules and Packages Cheat Sheet

```python
# Import a complete module
import math

# Import specific functions
from math import sqrt, factorial

# Import with an alias
import numpy as np

# Import using an alias for a function
from math import sqrt as square_root

# Inspect module members
dir(math)

# Read documentation
help(math)

# Inspect Python version
import sys
print(sys.version)

# Inspect module search paths
print(sys.path)

# Import custom module
import calculator

# Import a specific function
from calculator import add

# Package import
from utilities.hashing import sha256_hash

# Main entry point
if __name__ == "__main__":
    print("Program started")

# Create virtual environment
# python -m venv .venv

# Install dependency
# python -m pip install requests

# Save dependencies
# python -m pip freeze > requirements.txt

# Install saved dependencies
# python -m pip install -r requirements.txt

# Run a package module
# python -m security.tools.scanner
```

---

## 17. Final Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Import complete modules.
- [ ] Import specific functions and variables.
- [ ] Use aliases with `as`.
- [ ] Understand important Python standard library modules.
- [ ] Explore modules using `dir()` and `help()`.
- [ ] Create custom modules.
- [ ] Create packages and understand `__init__.py`.
- [ ] Explain `if __name__ == "__main__"`.
- [ ] Understand absolute and relative imports.
- [ ] Explain how Python searches for modules.
- [ ] Understand `sys.path` and `PYTHONPATH`.
- [ ] Organize a Python project into packages.
- [ ] Install and manage dependencies using pip.
- [ ] Create and activate virtual environments.
- [ ] Understand `requirements.txt` and `pyproject.toml`.
- [ ] Identify and avoid circular imports.
- [ ] Build a small modular Python application.

## 18. Suggested One-Hour Practice Session

| Time | Practice |
|---|---|
| 10 minutes | Revise import syntax and standard library modules |
| 10 minutes | Create two custom modules |
| 10 minutes | Create a package with multiple modules |
| 10 minutes | Practice `__name__ == "__main__"` and imports |
| 10 minutes | Create a virtual environment and install a dependency |
| 10 minutes | Build a small modular Python application |

**Final recommendation:** Spend more time creating your own modules and packages than memorizing every standard library module. You do not need to memorize the entire standard library; learn what each useful module does and become comfortable finding its documentation.

For your cybersecurity path, pay particular attention to `os`, `sys`, `pathlib`, `subprocess`, `socket`, `ipaddress`, `requests` (third-party), `hashlib`, `logging`, `argparse`, and `json`. These will help you build organized Python automation and security tools.