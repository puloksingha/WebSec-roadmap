# Phase 1: Python Fundamentals Revision

## Topic 1: Python Environment and Setup

> **Goal:** Be able to check your Python installation, run scripts from
> the terminal, understand common errors, and manage project
> dependencies with `venv` and `pip`.

------------------------------------------------------------------------

## 1. Installing and Checking Python

Python is a high-level, general-purpose programming language. To run
Python code, your computer needs a Python interpreter.

### Check whether Python is installed

Open a terminal.

**Windows (Command Prompt or PowerShell):**

``` bash
python --version
```

If that does not work, try:

``` bash
py --version
```

**Linux / macOS:**

``` bash
python3 --version
```

Example output:

``` text
Python 3.12.4
```

The exact version on your computer may be different.

### Check where Python is installed

**Windows:**

``` bash
where python
where py
```

**Linux / macOS:**

``` bash
which python3
```

### Run a quick test

Windows:

``` bash
python -c "print('Python is working!')"
```

Linux / macOS:

``` bash
python3 -c "print('Python is working!')"
```

**Remember:** On some systems, the command is `python`; on others, it is
`python3` or `py`. Use whichever command works on your system.

------------------------------------------------------------------------

## 2. Python Interpreter and Interactive Shell

The **Python interpreter** reads and executes Python code. The
**interactive shell** lets you enter statements one at a time and see
the results immediately.

Start the shell:

``` bash
python
```

Or, where required:

``` bash
python3
```

You may see a prompt like:

``` text
>>>
```

Try these expressions:

``` python
>>> 2 + 3
5
>>> name = "Pulok"
>>> print(name)
Pulok
>>> len("Python")
6
```

Exit the shell:

``` python
exit()
```

You can also use `Ctrl+Z` then `Enter` on Windows, or `Ctrl+D` on
Linux/macOS.

### When should you use the interactive shell?

-   Testing a short expression.
-   Checking how a function behaves.
-   Quickly inspecting a data type or object.
-   Practising syntax without creating a file.

For larger programs, save your code in a `.py` file.

------------------------------------------------------------------------

## 3. Running Python Scripts from the Terminal

A Python script is a file containing Python code, usually saved with the
`.py` extension.

### Create a script

Create a file named `hello.py`:

``` python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Open a terminal in the folder containing the file, then run:

**Windows:**

``` bash
python hello.py
```

Or:

``` bash
py hello.py
```

**Linux / macOS:**

``` bash
python3 hello.py
```

Example:

``` text
Enter your name: Alex
Hello, Alex!
```

### Useful terminal commands

  Task                  Windows            Linux / macOS
  --------------------- ------------------ ------------------
  Show current folder   `cd`               `pwd`
  List files            `dir`              `ls`
  Move into a folder    `cd folder_name`   `cd folder_name`
  Move up one folder    `cd ..`            `cd ..`
  Clear terminal        `cls`              `clear`

In Windows PowerShell, `pwd` and `ls` may also work as aliases.

### Common script-running problems

-   **File not found:** Check the filename and current folder.
-   **Command not recognized:** Try `py` or `python3`; check whether
    Python is installed and added to `PATH`.
-   **Wrong Python version:** Check which command is being used with
    `python --version` or its equivalent.
-   **Permission or path problems:** Confirm that you have access to the
    folder and that the path is correct.

------------------------------------------------------------------------

## 4. Using an IDE or Code Editor

A code editor helps you write and organize code. An **IDE** (Integrated
Development Environment) usually provides editing, running, debugging,
and project tools in one application.

Examples include:

-   **Visual Studio Code (VS Code):** Lightweight editor with Python
    extensions.
-   **PyCharm:** IDE with Python-focused development features.
-   **IDLE:** A simple editor and shell included with many Python
    installations.
-   **Jupyter Notebook:** Useful for interactive, cell-based experiments
    and data analysis.

### Basic workflow in VS Code

1.  Install Python.
2.  Install VS Code.
3.  Install the Python extension in VS Code.
4.  Open your project folder.
5.  Create a file such as `main.py`.
6.  Select the intended Python interpreter.
7.  Run the file and inspect the output in the terminal.

**Important:** Installing a code editor does not necessarily install
Python itself. The editor must use an installed interpreter.

### Recommended project structure

``` text
python-revision/
├── main.py
├── notes.md
└── practice/
    ├── strings.py
    └── lists.py
```

Keep related code in a project folder instead of scattering files across
your computer.

------------------------------------------------------------------------

## 5. Python Indentation and Syntax

**Syntax** is the set of rules for writing valid Python code.
**Indentation** is the whitespace at the beginning of a line. Python
uses indentation to define code blocks.

Correct:

``` python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Incorrect:

``` python
if age >= 18:
print("Adult")  # IndentationError
```

### Indentation rules

-   Use consistent indentation; **4 spaces per level** is the standard
    convention.
-   Do not mix tabs and spaces.
-   Statements ending in `:` commonly begin an indented block, such as
    `if`, `for`, `while`, `def`, `class`, and `try`.
-   Keep statements in the same block aligned.

### Common syntax errors

Missing colon:

``` python
if True
    print("Hello")
```

Unclosed parenthesis:

``` python
print("Hello"
```

Incorrect assignment operator:

``` python
if age = 18:  # Invalid in a condition
    print("18")
```

Correct comparison:

``` python
if age == 18:
    print("18")
```

------------------------------------------------------------------------

## 6. Comments and Docstrings

### Comments

Comments explain code to human readers. Python ignores comments during
normal execution.

``` python
# Calculate the total price
price = 100
tax = 5
total = price + tax
```

Inline comment:

``` python
count = 10  # Number of attempts
```

Use comments to explain **why** something is done, especially when the
reason is not obvious. Avoid comments that merely repeat the code.

### Docstrings

A **docstring** documents a module, function, class, or method. It is
usually written as a string literal immediately after the definition.

``` python
def square(number):
    """Return the square of a number."""
    return number * number
```

Read the docstring:

``` python
print(square.__doc__)
```

Use `help()` to inspect documentation:

``` python
help(square)
```

A docstring is not the same as a comment: Python makes docstrings
available at runtime through attributes such as `__doc__`.

------------------------------------------------------------------------

## 7. Understanding Tracebacks and Error Messages

When an error occurs, Python often prints a **traceback**. It shows the
sequence of calls that led to the error and identifies where Python
detected the problem.

Example:

``` python
numbers = [10, 20, 30]
print(numbers[5])
```

This raises an `IndexError` because index `5` is outside the list's
valid index range.

### How to read a traceback

1.  Read the final line first: it usually gives the exception type and
    message.
2.  Find the filename and line number where the problem occurred.
3.  Inspect the code on that line.
4.  Check the values and types involved.
5.  Fix the cause, then run the program again.

### Common errors

  -----------------------------------------------------------------------
  Error                               Typical meaning
  ----------------------------------- -----------------------------------
  `SyntaxError`                       Python cannot parse the code as
                                      written.

  `IndentationError`                  Indentation is missing or
                                      inconsistent.

  `NameError`                         A name is used before it has been
                                      defined in the current scope.

  `TypeError`                         An operation or function received
                                      an unsuitable type of value.

  `ValueError`                        The type is acceptable, but the
                                      value is unsuitable.

  `IndexError`                        A sequence index is out of range.

  `KeyError`                          A dictionary key is not present.

  `ModuleNotFoundError`               Python cannot find the requested
                                      module.

  `ImportError`                       An import cannot be completed.

  `FileNotFoundError`                 A requested file or directory was
                                      not found.

  `ZeroDivisionError`                 A number was divided by zero.
  -----------------------------------------------------------------------

### Example: diagnose a `NameError`

``` python
print(user_name)
```

If `user_name` has not been defined, Python raises `NameError`.

Fix:

``` python
user_name = "Alex"
print(user_name)
```

### Debugging habit

Do not just copy an error into a search engine. First identify: - the
exception type; - the relevant line; - the value or operation
involved; - what you expected to happen.

Then make one change at a time and test again.

------------------------------------------------------------------------

## 8. Using `help()` and `dir()`

These built-in functions help you explore Python objects.

### `help()`

`help()` displays documentation about a module, type, function, or
object.

``` python
help(str)
help(len)
help(list.append)
```

You can also use it in the interactive shell:

``` python
help()
```

Press `q` to leave the help viewer in many terminal environments.

### `dir()`

`dir()` returns a list of names and attributes associated with an
object. With no argument, it lists names in the current scope.

``` python
text = "python"

print(dir(text))
print(dir(list))
```

You can then inspect a particular method:

``` python
help(str.upper)
```

**Note:** `dir()` is useful for exploration, but it does not explain
what every attribute does. Use `help()` or official documentation for
details.

------------------------------------------------------------------------

## 9. Python Virtual Environments (`venv`)

A **virtual environment** is an isolated Python environment for a
particular project. It helps keep the project's installed packages
separate from packages used by other projects.

For example, one project may require one version of a library while
another project needs a different version. Virtual environments help
prevent those requirements from interfering with one another.

### Create a virtual environment

First, move into your project directory.

**Windows:**

``` bash
python -m venv .venv
```

**Linux / macOS:**

``` bash
python3 -m venv .venv
```

Here, `-m venv` runs Python's built-in `venv` module, and `.venv` is the
directory name.

### Activate the environment

**Windows Command Prompt:**

``` bat
.venv\Scripts\activate.bat
```

**Windows PowerShell:**

``` powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

``` bash
source .venv/bin/activate
```

After activation, the terminal prompt often shows `(.venv)`.

If PowerShell blocks activation because of its execution policy, you can
use Command Prompt or invoke the environment's Python executable
directly. Do not change system-wide security settings without
understanding the consequences.

### Check the active Python

``` bash
python --version
python -m pip --version
```

You can also check the executable path:

**Windows:**

``` bat
where python
```

**Linux / macOS:**

``` bash
which python
```

The path should point to the environment when it is active.

### Install a package inside the environment

``` bash
python -m pip install requests
```

Using `python -m pip` helps ensure that `pip` belongs to the Python
interpreter you are using.

### Deactivate the environment

``` bash
deactivate
```

### Typical project workflow

``` bash
# Create environment
python -m venv .venv

# Activate it (choose the command for your terminal)
# Then install packages
python -m pip install requests

# Run your program
python main.py

# When finished
deactivate
```

Create the environment once per project, then activate it whenever you
work on that project.

**Best practice:** Do not normally commit or share the `.venv`
directory. Recreate it from dependency information on another computer.

------------------------------------------------------------------------

## 10. Installing Packages Using `pip`

`pip` is Python's commonly used package installer. It downloads and
installs packages from package indexes such as the Python Package Index
(PyPI), subject to your configuration.

### Check `pip`

``` bash
python -m pip --version
```

### Install a package

``` bash
python -m pip install requests
```

### Install a specific version

``` bash
python -m pip install requests==2.32.3
```

The version number above is an example; choose a version compatible with
your project.

### Upgrade a package

``` bash
python -m pip install --upgrade requests
```

### Uninstall a package

``` bash
python -m pip uninstall requests
```

### List installed packages

``` bash
python -m pip list
```

### Show package details

``` bash
python -m pip show requests
```

### Check dependency consistency

``` bash
python -m pip check
```

### Why use `python -m pip`?

A computer may have several Python installations. Running `pip` directly
can accidentally install a package for a different interpreter.
`python -m pip` runs `pip` using the Python interpreter selected by
`python`.

**Important:** Activate the intended virtual environment before
installing project packages.

------------------------------------------------------------------------

## 11. `requirements.txt`

A `requirements.txt` file records Python package requirements so that a
project can be set up again more easily.

### Generate a requirements file

After installing the packages your project needs inside the virtual
environment:

``` bash
python -m pip freeze > requirements.txt
```

This records installed distributions and their versions. It can include
transitive dependencies and may include packages that are not directly
needed by your application.

### Install dependencies from the file

On a new setup, create and activate a virtual environment, then run:

``` bash
python -m pip install -r requirements.txt
```

Example file:

``` text
requests==2.32.3
```

This example pins `requests` to one specific version. The version is
illustrative, not a recommendation that every project should use it.

### Manually maintained requirements

For small projects, you may maintain a short list of direct dependencies
yourself. For reproducible environments, consider how direct and
transitive dependencies are recorded and tested.

### Important distinction

-   `requirements.txt` lists packages to install.
-   `.venv/` contains the local virtual environment and its installed
    packages.
-   A requirements file does not contain the package code itself.

### Recommended project layout

``` text
my_project/
├── .venv/
├── main.py
├── requirements.txt
└── README.md
```

Normally, add `.venv/` to `.gitignore` so the environment is not
committed to version control.

------------------------------------------------------------------------

## 12. Python Versions and Package Compatibility

Python packages may behave differently across Python versions. A package
can require a minimum Python version, exclude certain versions, or
depend on operating-system-specific components.

### Check your version

``` bash
python --version
```

### Why versions matter

-   A package may not support an older Python version.
-   A newer Python version may expose compatibility problems in an older
    dependency.
-   A package may install successfully but fail at runtime.
-   Native extensions may depend on your operating system, architecture,
    and Python version.
-   Two projects may require different versions of the same dependency.

### Check which Python is running

``` bash
python -c "import sys; print(sys.executable); print(sys.version)"
```

### Inspect installed package information

``` bash
python -m pip show requests
python -m pip check
```

### Practical compatibility workflow

1.  Read the project's README and installation instructions.
2.  Check the package's supported Python versions.
3.  Choose a supported Python version for the project.
4.  Create a fresh virtual environment using that interpreter.
5.  Install dependencies from the project's requirements file.
6.  Run the tests or a small import check.
7.  Record the setup instructions so it can be reproduced.

Avoid upgrading Python or all packages in a working project without
checking compatibility first.

------------------------------------------------------------------------

## 13. Practical Revision Exercise

Complete these tasks in your own project folder. Try to do them without
copying the commands blindly.

### Task A --- Verify Python

-   [ ] Check your Python version.
-   [ ] Find the path of the Python executable.
-   [ ] Run a one-line Python command from the terminal.

### Task B --- Create and run a script

-   [ ] Create `main.py`.
-   [ ] Ask the user for their name.
-   [ ] Print a greeting using an f-string.
-   [ ] Run the script from the terminal.

Starter code:

``` python
name = input("Enter your name: ")
print(f"Welcome, {name}!")
```

### Task C --- Explore the interpreter

-   [ ] Open the interactive shell.
-   [ ] Try `help(str)`.
-   [ ] Try `dir(list)`.
-   [ ] Exit the shell.

### Task D --- Practise debugging

Intentionally run this code:

``` python
numbers = [1, 2, 3]
print(numbers[10])
```

-   [ ] Identify the exception type.
-   [ ] Explain why it happened.
-   [ ] Fix the code.

### Task E --- Use a virtual environment

-   [ ] Create `.venv`.
-   [ ] Activate it.
-   [ ] Check the Python and `pip` versions.
-   [ ] Install one package you actually need.
-   [ ] Generate `requirements.txt`.
-   [ ] Deactivate the environment.

------------------------------------------------------------------------

## 14. Quick Revision Questions

1.  What is the difference between the Python interpreter and the
    interactive shell?
2.  How do you run a `.py` file from the terminal?
3.  Why does Python use indentation?
4.  What is the difference between a comment and a docstring?
5.  What information does a traceback provide?
6.  How are `help()` and `dir()` different?
7.  What problem does a virtual environment solve?
8.  Why is `python -m pip install package_name` often safer than
    `pip install package_name`?
9.  What is the purpose of `requirements.txt`?
10. Why should you check package compatibility before changing Python
    versions?

### Short answers

1.  The interpreter executes Python code; the interactive shell is a way
    to enter and execute code interactively.
2.  Use `python filename.py`, `py filename.py`, or
    `python3 filename.py`, depending on the system.
3.  Indentation defines code blocks and their structure.
4.  Comments are explanatory notes ignored by normal execution;
    docstrings document objects and can be accessed at runtime.
5.  It shows the call sequence and the location and type of an error.
6.  `help()` displays documentation; `dir()` lists names and attributes.
7.  It isolates project dependencies.
8.  It ties package installation to the selected Python interpreter.
9.  It records dependencies that can be installed for a project.
10. Packages may not support every Python version.

------------------------------------------------------------------------

## 15. Essential Commands Cheat Sheet

  ---------------------------------------------------------------------------------
  Purpose                             Command
  ----------------------------------- ---------------------------------------------
  Check Python                        `python --version`

  Start interactive shell             `python`

  Run a script                        `python main.py`

  Execute one line                    `python -c "print('Hello')"`

  Create virtual environment          `python -m venv .venv`

  Check `pip`                         `python -m pip --version`

  Install a package                   `python -m pip install package_name`

  List packages                       `python -m pip list`

  Export installed versions           `python -m pip freeze > requirements.txt`

  Install requirements                `python -m pip install -r requirements.txt`

  Check dependencies                  `python -m pip check`

  Leave virtual environment           `deactivate`
  ---------------------------------------------------------------------------------

> **Revision advice:** Since this is a fundamentals revision, focus on
> actually running these commands and diagnosing small errors. You do
> not need to memorize every option; learn what each command is for and
> practise using it correctly.
