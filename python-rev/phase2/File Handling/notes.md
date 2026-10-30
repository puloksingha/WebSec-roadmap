# Python Revision — Topic 10: File Handling

## 1. Introduction to File Handling

File handling means using a program to create, read, write, update, and manage files stored on a computer.

Python provides built-in functions and modules for working with files.

### Why is file handling important?

You can use file handling to:

- Read and write text files.
- Store information permanently.
- Save program output.
- Read configuration files.
- Process log files.
- Work with CSV and JSON files.
- Read wordlists for security testing.
- Store scan results and reports.
- Work with binary files such as images and PDFs.

### Example

Suppose you want to save usernames entered by users.

Without file handling, the information may disappear when your program stops.

With file handling, you can save the usernames in a file and access them later.

---

## 2. Opening and Closing Files

Python provides the built-in `open()` function to open files.

### Syntax

```python
file = open("filename.txt", "mode")
```

Parameters:

- `filename`: Name or path of the file.
- `mode`: Specifies how the file should be opened.

### Example: Opening a file

```python
file = open("example.txt", "r")

print(file)
```

The file must exist when opened in read mode (`r`).

### Closing a file

After working with a file, you should close it.

```python
file = open("example.txt", "r")

content = file.read()

print(content)

file.close()
```

The `close()` method releases the resources associated with the file.

### Checking whether a file is closed

```python
file = open("example.txt", "r")

print(file.closed)

file.close()

print(file.closed)
```

Output:

```text
False
True
```

### Important methods

| Method | Purpose |
|---|---|
| `open()` | Opens a file |
| `close()` | Closes a file |
| `read()` | Reads file content |
| `readline()` | Reads one line |
| `readlines()` | Reads all lines into a list |
| `write()` | Writes content |
| `writelines()` | Writes multiple strings |

**Important:** If an exception occurs before `close()` is executed, the file might remain open. Context managers solve this problem.

---

## 3. Context Managers with `with`

A context manager automatically manages resources such as files.

Python provides the `with` statement to open and close files safely.

### Syntax

```python
with open("filename.txt", "r") as file:
    content = file.read()
    print(content)
```

When execution leaves the `with` block, Python automatically closes the file.

You do not need to call `file.close()` manually.

### Example

Suppose `notes.txt` contains:

```text
Python is powerful.
File handling is useful.
```

Code:

```python
with open("notes.txt", "r") as file:
    content = file.read()

    print(content)

print(file.closed)
```

Output:

```text
Python is powerful.
File handling is useful.

True
```

### Why use `with`?

1. Automatically closes files.
2. Prevents resource leaks.
3. Makes code cleaner.
4. Handles exceptions more safely.
5. Is the recommended approach for file handling.

**Best practice:** Prefer `with open()` over manually opening and closing files.

---

## 4. Reading Text Files

Python provides several methods to read text files.

Assume `data.txt` contains:

```text
Hello Python
Learning file handling
Python is interesting
```

### 4.1 Using `read()`

The `read()` method reads the file's contents and returns them as a string.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

Output:

```text
Hello Python
Learning file handling
Python is interesting
```

You can also specify how many characters to read.

```python
with open("data.txt", "r") as file:
    content = file.read(5)

print(content)
```

Output:

```text
Hello
```

### 4.2 Using `readline()`

The `readline()` method reads one line at a time.

```python
with open("data.txt", "r") as file:
    first_line = file.readline()

    print(first_line)
```

Output:

```text
Hello Python
```

Read multiple lines:

```python
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

    print(line1)
    print(line2)
```

### 4.3 Using `readlines()`

The `readlines()` method reads all lines and returns them as a list of strings.

```python
with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Output:

```python
[
    'Hello Python\n',
    'Learning file handling\n',
    'Python is interesting'
]
```

Notice that `\n` represents a newline character.

### 4.4 Reading a file using a loop

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Output:

```text
Hello Python
Learning file handling
Python is interesting
```

The `strip()` method removes surrounding whitespace, including newline characters.

**Best practice:** Use direct iteration over the file when reading large text files.

---

## 5. Writing Text Files

Python uses the `write()` method to write text into a file.

### Example

```python
with open("output.txt", "w") as file:
    file.write("Hello Python")
```

This creates `output.txt` if it does not exist.

If the file already exists, its previous content is replaced.

### Writing multiple lines

```python
with open("output.txt", "w") as file:
    file.write("Python\n")
    file.write("Linux\n")
    file.write("Cybersecurity\n")
```

File content:

```text
Python
Linux
Cybersecurity
```

### Using `writelines()`

The `writelines()` method writes multiple strings into a file.

```python
lines = [
    "Python\n",
    "Linux\n",
    "Networking\n"
]

with open("output.txt", "w") as file:
    file.writelines(lines)
```

**Important:** `writelines()` does not automatically insert newline characters.

You must include `\n` yourself if you want separate lines.

### Understanding the return value of `write()`

```python
with open("output.txt", "w") as file:
    result = file.write("Hello")

print(result)
```

Output:

```text
5
```

The return value represents the number of characters written.

---

## 6. Appending Data to Files

Appending means adding new content to the end of an existing file without deleting its previous content.

Python uses append mode (`a`).

### Example

Suppose `logs.txt` contains:

```text
Program started
```

Code:

```python
with open("logs.txt", "a") as file:
    file.write("\nNew event recorded")
```

Updated file:

```text
Program started
New event recorded
```

### Appending multiple entries

```python
with open("logs.txt", "a") as file:
    file.write("\nUser logged in")
    file.write("\nUser logged out")
```

### Practical example: Saving scan results

```python
result = "example.com - Server responded"

with open("scan_results.txt", "a") as file:
    file.write(result + "\n")
```

This is useful when building scripts that save results over time.

---

## 7. File Modes

File modes determine how Python opens a file.

| Mode | Meaning |
|---|---|
| `r` | Read an existing file |
| `w` | Write; creates or overwrites a file |
| `a` | Append; creates a file if necessary |
| `x` | Create a new file; fails if it already exists |
| `b` | Binary mode |
| `t` | Text mode (default) |
| `+` | Enable both reading and writing |

### 7.1 Read mode (`r`)

```python
with open("data.txt", "r") as file:
    print(file.read())
```

The file must already exist.

### 7.2 Write mode (`w`)

```python
with open("data.txt", "w") as file:
    file.write("New content")
```

Creates a new file or replaces existing content.

### 7.3 Append mode (`a`)

```python
with open("data.txt", "a") as file:
    file.write("\nAdditional content")
```

Adds content to the end.

### 7.4 Exclusive creation mode (`x`)

```python
with open("newfile.txt", "x") as file:
    file.write("Created successfully")
```

Raises `FileExistsError` if the file already exists.

### 7.5 Read and write mode (`r+`)

```python
with open("data.txt", "r+") as file:
    content = file.read()

    print(content)

    file.write("\nNew content")
```

The file must already exist.

### 7.6 Write and read mode (`w+`)

```python
with open("data.txt", "w+") as file:
    file.write("Hello Python")

    file.seek(0)

    print(file.read())
```

Output:

```text
Hello Python
```

`w+` creates or truncates the file and allows reading and writing.

### 7.7 Append and read mode (`a+`)

```python
with open("data.txt", "a+") as file:
    file.write("\nNew entry")

    file.seek(0)

    print(file.read())
```

The file is opened for appending and reading.

### Binary modes

Add `b` to a mode to work with binary data.

Examples:

- `rb`: Read binary data.
- `wb`: Write binary data.
- `ab`: Append binary data.

### Quick comparison

| Mode | Reads | Writes | Creates if missing | Truncates existing file |
|---|---|---|---|---|
| `r` | Yes | No | No | No |
| `w` | No | Yes | Yes | Yes |
| `a` | No | Yes | Yes | No |
| `x` | No | Yes | Yes | No |
| `r+` | Yes | Yes | No | No |
| `w+` | Yes | Yes | Yes | Yes |
| `a+` | Yes | Yes | Yes | No |

---

## 8. File Paths Using `pathlib`

The `pathlib` module provides an object-oriented way to work with file paths.

It is generally more convenient and readable than manually combining path strings.

### Importing pathlib

```python
from pathlib import Path
```

### Creating a path

```python
path = Path("data.txt")

print(path)
```

### Checking whether a file exists

```python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    print("File exists")
else:
    print("File does not exist")
```

### Checking whether a path is a file or directory

```python
path = Path("data.txt")

print(path.is_file())
print(path.is_dir())
```

### Creating a directory

```python
folder = Path("reports")

folder.mkdir(exist_ok=True)
```

`exist_ok=True` prevents an error if the directory already exists.

### Creating nested directories

```python
folder = Path("reports/2026/october")

folder.mkdir(parents=True, exist_ok=True)
```

`parents=True` creates missing parent directories.

### Reading a text file with pathlib

```python
from pathlib import Path

path = Path("data.txt")

content = path.read_text(encoding="utf-8")

print(content)
```

### Writing a text file with pathlib

```python
path = Path("output.txt")

path.write_text(
    "Hello from pathlib",
    encoding="utf-8"
)
```

### Getting file information

```python
path = Path("data.txt")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
```

For a path such as `reports/results.txt`, the output is:

```text
results.txt
results
.txt
reports
```

### Joining paths

Use the `/` operator with `Path` objects.

```python
from pathlib import Path

folder = Path("reports")

file_path = folder / "results.txt"

print(file_path)
```

### Absolute paths

```python
path = Path("data.txt")

print(path.resolve())
```

`resolve()` returns an absolute path.

### Important pathlib methods

| Method | Purpose |
|---|---|
| `exists()` | Checks whether a path exists |
| `is_file()` | Checks whether it is a file |
| `is_dir()` | Checks whether it is a directory |
| `mkdir()` | Creates a directory |
| `rmdir()` | Removes an empty directory |
| `unlink()` | Deletes a file |
| `rename()` | Renames or moves a path |
| `read_text()` | Reads a text file |
| `write_text()` | Writes a text file |
| `glob()` | Finds paths matching a pattern |
| `rglob()` | Searches recursively |
| `resolve()` | Gets an absolute path |

**Important:** `write_text()` replaces existing file content. Use it carefully.

---

## 9. Working with Directories

Python provides `pathlib` and the `os` module for directory operations.

### Listing files and directories with pathlib

```python
from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    print(item)
```

This lists the immediate contents of the current directory.

### Listing only files

```python
from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    if item.is_file():
        print(item.name)
```

### Listing only directories

```python
from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    if item.is_dir():
        print(item.name)
```

### Finding files using glob()

```python
from pathlib import Path

folder = Path(".")

for file in folder.glob("*.txt"):
    print(file)
```

This finds text files in the specified directory.

### Recursive searching with rglob()

```python
from pathlib import Path

folder = Path(".")

for file in folder.rglob("*.txt"):
    print(file)
```

This searches subdirectories too.

### Using the os module

```python
import os

print(os.getcwd())
```

Returns the current working directory.

Change the current working directory:

```python
os.chdir("C:/Users/YourName/Desktop")
```

List directory contents:

```python
print(os.listdir("."))
```

Create a directory:

```python
os.mkdir("new_folder")
```

Create nested directories:

```python
os.makedirs("reports/2026/october", exist_ok=True)
```

Remove an empty directory:

```python
os.rmdir("new_folder")
```

**Note:** `os` remains useful for environment variables, operating-system interactions, and other tasks. For ordinary path manipulation, `pathlib` is usually easier.

---

## 10. Handling Missing Files and Permissions

File operations can fail for several reasons:

- The file does not exist.
- The program does not have permission.
- The path is incorrect.
- The path points to a directory instead of a file.
- The file is being used or locked by another process.

Python provides exceptions to handle these situations.

### 10.1 FileNotFoundError

Occurs when a requested file does not exist.

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

Output:

```text
File not found
```

### 10.2 PermissionError

Occurs when the program does not have the required permission.

```python
try:
    with open("/restricted/data.txt", "w") as file:
        file.write("Hello")

except PermissionError:
    print("Permission denied")
```

The exact behavior depends on the operating system and the permissions of the file or directory.

### 10.3 IsADirectoryError

Occurs when a file operation expects a file but receives a directory.

```python
try:
    with open("reports", "r") as file:
        print(file.read())

except IsADirectoryError:
    print("The path is a directory")
```

### 10.4 Handling multiple exceptions

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("You do not have permission")

except OSError as error:
    print("File operation failed:", error)
```

### 10.5 Checking a path before opening

```python
from pathlib import Path

path = Path("data.txt")

if path.exists() and path.is_file():
    print(path.read_text(encoding="utf-8"))
else:
    print("Valid file not found")
```

Remember that checking first does not eliminate every possible error: the file or permissions could change before the operation. Exception handling is still important.

---

## 11. Reading Large Files Efficiently

Reading an entire large file into memory can consume significant RAM.

For example:

```python
with open("large_log.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

This loads the entire file into memory.

For large files, process one line at a time.

### 11.1 Reading line by line

```python
with open("large_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

This is memory-efficient because the program processes each line instead of loading the entire file.

### 11.2 Counting lines

```python
count = 0

with open("large_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Total lines:", count)
```

### 11.3 Searching for a keyword

```python
keyword = "ERROR"

with open("large_log.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):

        if keyword in line:
            print(line_number, line.strip())
```

This is useful for log analysis.

### 11.4 Reading in chunks

For large files where line-based reading is unsuitable, read fixed-size chunks.

```python
with open("large_file.txt", "r", encoding="utf-8") as file:

    while True:
        chunk = file.read(4096)

        if not chunk:
            break

        print(chunk)
```

Here, `4096` represents the maximum number of characters requested per read.

For binary files, the same approach reads chunks of bytes.

### 11.5 Using a generator

A generator can process file lines without storing all of them.

```python
def read_lines(filename):

    with open(filename, "r", encoding="utf-8") as file:

        for line in file:
            yield line.strip()


for line in read_lines("large_log.txt"):
    print(line)
```

**Cybersecurity application:** You can use this technique to process large server logs, application logs, and authorized security scan results.

---

## 12. File Encoding

Encoding determines how text characters are represented as bytes.

Different languages and symbols require different character representations.

### Common encodings

| Encoding | Description |
|---|---|
| ASCII | Basic English characters and symbols |
| UTF-8 | Widely used Unicode encoding |
| UTF-16 | Unicode encoding using one or more 16-bit code units |
| Latin-1 | Western European character encoding |

### Why UTF-8?

UTF-8 supports a wide range of characters, including:

- English letters.
- Indian languages.
- Special symbols.
- Emojis.
- Characters from many other writing systems.

### Specifying encoding

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

When writing:

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
    file.write("\nনমস্কাৰ")
```

### Encoding errors

A `UnicodeDecodeError` may occur when Python tries to decode bytes using an incompatible encoding.

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

except UnicodeDecodeError:
    print("Unable to decode the file using UTF-8")
```

### Encoding and decoding

Encoding converts text into bytes.

```python
text = "Python"

data = text.encode("utf-8")

print(data)
```

Output:

```text
b'Python'
```

Decoding converts bytes back into text.

```python
data = b'Python'

text = data.decode("utf-8")

print(text)
```

Output:

```text
Python
```

**Important:** Always specify an encoding when working with text files if you know the expected encoding. UTF-8 is a good default for new files.

---

## 13. Binary File Handling

Text files store character data, while binary files store raw bytes.

Examples of binary files:

- Images.
- Videos.
- Audio files.
- PDF files.
- Executable files.
- Compressed archives.

Python uses binary modes such as `rb` and `wb`.

### Reading a binary file

```python
with open("image.png", "rb") as file:
    data = file.read()

print(type(data))
```

Output:

```text
<class 'bytes'>
```

### Writing binary data

```python
data = b"Hello Binary"

with open("sample.bin", "wb") as file:
    file.write(data)
```

### Copying a binary file

```python
with open("source.png", "rb") as source:
    data = source.read()

with open("copy.png", "wb") as destination:
    destination.write(data)
```

This works, but reading the entire file into memory is not ideal for very large files.

### Efficient binary copying

```python
with open("source.png", "rb") as source:
    with open("copy.png", "wb") as destination:

        while True:
            chunk = source.read(4096)

            if not chunk:
                break

            destination.write(chunk)
```

### Using shutil for copying

Python also provides the `shutil` module.

```python
import shutil

shutil.copy2("source.png", "copy.png")
```

`copy2()` attempts to preserve file metadata as well as copying the content.

### Text vs. binary files

| Feature | Text mode | Binary mode |
|---|---|---|
| Modes | `r`, `w`, `a` | `rb`, `wb`, `ab` |
| Data type | `str` | `bytes` |
| Encoding | Used for text conversion | No text decoding |
| Newline translation | May occur | Does not occur |
| Typical use | `.txt`, `.log`, `.csv` | `.png`, `.pdf`, `.zip` |

---

## 14. Temporary Files and Directories

Temporary files and directories are created for short-term use.

They are useful when a program needs to store intermediate data.

Python provides the `tempfile` module.

### Importing tempfile

```python
import tempfile
```

### 14.1 Creating a temporary file

```python
import tempfile

with tempfile.TemporaryFile(mode="w+t") as file:

    file.write("Temporary information")

    file.seek(0)

    print(file.read())
```

Output:

```text
Temporary information
```

The temporary file is automatically cleaned up when the context manager exits.

### 14.2 Creating a named temporary file

```python
import tempfile

with tempfile.NamedTemporaryFile(
    mode="w+",
    encoding="utf-8"
) as file:

    file.write("Temporary data")

    file.seek(0)

    print(file.read())
```

A named temporary file has a filesystem name accessible through:

```python
file.name
```

Its cleanup behavior depends on the options and operating system.

### 14.3 Creating a temporary directory

```python
import tempfile

with tempfile.TemporaryDirectory() as folder:

    print(folder)
```

The directory is automatically removed when the context manager exits.

### 14.4 Using a temporary directory with pathlib

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:

    path = Path(folder) / "data.txt"

    path.write_text(
        "Temporary content",
        encoding="utf-8"
    )

    print(path.read_text(encoding="utf-8"))
```

### Why use temporary files?

- Store intermediate results.
- Test file operations.
- Process downloaded data.
- Create temporary reports.
- Avoid leaving unnecessary files behind.

**Security note:** Use `tempfile` rather than manually inventing predictable temporary filenames. Temporary files may contain sensitive data, so consider their permissions and cleanup requirements.

---

## 15. File Position: tell() and seek()

Python maintains a file position indicating where the next read or write operation occurs.

Two useful methods are:

- `tell()`: Returns the current position.
- `seek()`: Changes the current position.

### Example

```python
with open("data.txt", "r", encoding="utf-8") as file:

    print(file.tell())

    content = file.read(5)

    print(content)

    print(file.tell())
```

If the file begins with `Hello Python`, the output is:

```text
0
Hello
5
```

### Using seek()

```python
with open("data.txt", "r", encoding="utf-8") as file:

    print(file.read(5))

    file.seek(0)

    print(file.read())
```

Output:

```text
Hello
Hello Python
```

`seek(0)` moves the file position back to the beginning.

**Important:** Text-mode file positions are not always simple character counts. For arbitrary positioning, follow the rules documented for text streams. Binary streams provide more straightforward byte-based positioning.

---

## 16. Practical Project: Log File Analyzer

This project combines several file-handling concepts.

### Objective

Read a log file and count:

- Total lines.
- ERROR entries.
- WARNING entries.
- INFO entries.

Suppose `server.log` contains:

```text
INFO: Server started
ERROR: Database connection failed
WARNING: High memory usage
INFO: User logged in
ERROR: Authentication failed
```

### Code

```python
from pathlib import Path

file_path = Path("server.log")

total_lines = 0
errors = 0
warnings = 0
infos = 0

try:

    with file_path.open("r", encoding="utf-8") as file:

        for line in file:

            total_lines += 1

            line = line.strip()

            if "ERROR" in line:
                errors += 1

            elif "WARNING" in line:
                warnings += 1

            elif "INFO" in line:
                infos += 1

    print("Total lines:", total_lines)
    print("Errors:", errors)
    print("Warnings:", warnings)
    print("Info:", infos)

except FileNotFoundError:
    print("Log file not found")

except PermissionError:
    print("Permission denied")

except OSError as error:
    print("File operation failed:", error)
```

### Expected output

```text
Total lines: 5
Errors: 2
Warnings: 1
Info: 2
```

### What you learned

- Opening files.
- Reading line by line.
- Using pathlib.
- Counting and filtering data.
- Handling file-related exceptions.

This is a useful starting point for cybersecurity log-analysis scripts.

---

## 17. Common Mistakes in File Handling

### Mistake 1: Forgetting to close files

Incorrect:

```python
file = open("data.txt", "r")

content = file.read()
```

Better:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Mistake 2: Using write mode accidentally

```python
with open("important.txt", "w") as file:
    file.write("New content")
```

This replaces existing content.

Use append mode (`a`) if you want to preserve previous content.

### Mistake 3: Reading a missing file

```python
with open("missing.txt", "r") as file:
    print(file.read())
```

This raises `FileNotFoundError`.

Handle the exception when the file may not exist.

### Mistake 4: Forgetting newline characters

```python
with open("data.txt", "w") as file:
    file.write("Python")
    file.write("Linux")
```

File content:

```text
PythonLinux
```

Correct:

```python
with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("Linux\n")
```

### Mistake 5: Reading a large file all at once

Avoid:

```python
content = file.read()
```

when the file is too large for available memory.

Prefer:

```python
for line in file:
    print(line)
```

### Mistake 6: Forgetting encoding

For text files, specify an appropriate encoding:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

### Mistake 7: Using text mode for binary data

Incorrect:

```python
with open("image.png", "r") as file:
    data = file.read()
```

Correct:

```python
with open("image.png", "rb") as file:
    data = file.read()
```

### Mistake 8: Confusing relative and absolute paths

A relative path is interpreted from the current working directory.

```python
Path("data.txt")
```

An absolute path identifies a location from the filesystem root or drive.

```python
Path("C:/Users/YourName/Desktop/data.txt")
```

Check the current working directory with:

```python
import os

print(os.getcwd())
```

### Mistake 9: Trusting user-provided file paths

Do not blindly open arbitrary paths supplied by users.

Validate paths against the directory your application is supposed to access. Be especially careful with path traversal, where inputs such as `../../private.txt` may attempt to escape an intended directory.

---

## 18. File Handling in Cybersecurity

File handling is particularly useful when writing cybersecurity tools and automation scripts.

### 18.1 Reading a wordlist

```python
with open("wordlist.txt", "r", encoding="utf-8") as file:

    for word in file:
        word = word.strip()

        if word:
            print(word)
```

### 18.2 Saving scan results

```python
results = [
    "Host: example.com",
    "Port: 443",
    "Status: Open"
]

with open("scan_results.txt", "w", encoding="utf-8") as file:

    for result in results:
        file.write(result + "\n")
```

### 18.3 Searching for suspicious keywords in logs

```python
keywords = ["failed", "unauthorized", "suspicious"]

with open("server.log", "r", encoding="utf-8") as file:

    for line_number, line in enumerate(file, start=1):

        for keyword in keywords:

            if keyword in line.lower():
                print(line_number, line.strip())
                break
```

### 18.4 Saving findings

```python
finding = {
    "target": "example.com",
    "issue": "Missing security header",
    "severity": "Low"
}

with open("findings.txt", "a", encoding="utf-8") as file:

    file.write(str(finding) + "\n")
```

For structured findings, JSON is usually better than storing Python dictionary representations as strings.

### 18.5 File integrity checking with SHA-256

You can calculate a file's SHA-256 hash to help verify whether its contents have changed.

```python
import hashlib

hasher = hashlib.sha256()

with open("sample.txt", "rb") as file:

    for chunk in iter(lambda: file.read(4096), b""):
        hasher.update(chunk)

print(hasher.hexdigest())
```

This is useful for integrity checks and forensic workflows.

Only analyze files and systems you are authorized to access.

---

## 19. Important Concepts to Remember

| Concept | Meaning |
|---|---|
| File handling | Reading, writing, and managing files |
| `open()` | Opens a file |
| `close()` | Closes a file |
| `with` | Automatically manages resources |
| `read()` | Reads file contents |
| `readline()` | Reads one line |
| `readlines()` | Reads all lines into a list |
| `write()` | Writes a string |
| `writelines()` | Writes multiple strings |
| `r` | Read mode |
| `w` | Write mode |
| `a` | Append mode |
| `x` | Exclusive creation mode |
| `rb` | Read binary mode |
| `wb` | Write binary mode |
| `pathlib` | Object-oriented path management |
| `os` | Operating-system interactions |
| `tempfile` | Temporary file and directory management |
| `tell()` | Returns file position |
| `seek()` | Changes file position |
| UTF-8 | Common text encoding |
| `bytes` | Binary data type |

---

## 20. Practice Exercises

Try solving these exercises yourself before checking other people's solutions.

### Beginner Level

**Exercise 1: Create a file**

Create a file named `student.txt` and write your name, age, and course into it.

**Exercise 2: Read a file**

Read `student.txt` and display its complete contents.

**Exercise 3: Append information**

Append your college name to `student.txt` without deleting existing information.

**Exercise 4: Count lines**

Write a program that counts the total number of lines in a text file.

**Exercise 5: Count words**

Read a text file and count how many words it contains.

### Intermediate Level

**Exercise 6: Find a keyword**

Search for a specific keyword in a text file and display matching lines.

**Exercise 7: File extension finder**

Use `pathlib` to find all `.txt` files in a directory.

**Exercise 8: File copy program**

Copy the contents of one text file into another file.

**Exercise 9: Handle missing files**

Write a program that attempts to read a file and handles `FileNotFoundError`.

**Exercise 10: Log analyzer**

Count the number of ERROR, WARNING, and INFO entries in a log file.

### Advanced Practice

**Exercise 11: Large file processor**

Read a large text file line by line and count its total lines without loading the whole file into memory.

**Exercise 12: Duplicate line finder**

Find duplicate lines in a text file.

**Exercise 13: File organizer**

Create a program that organizes files into folders based on their extensions.

**Exercise 14: File integrity checker**

Calculate the SHA-256 hash of a file using the `hashlib` module.

**Exercise 15: Wordlist processor**

Read a wordlist, remove empty lines, remove duplicate entries, and save the cleaned results to another file.

---

## 21. Quick Revision Questions and Answers

**Q1. What is file handling?**

File handling is the process of creating, reading, writing, appending, and managing files using a program.

**Q2. Which function opens a file in Python?**

`open()`.

**Q3. Why should we close a file?**

To release system resources and avoid resource leaks.

**Q4. What is the advantage of using `with`?**

It automatically closes the file when the block exits.

**Q5. What is the difference between `w` and `a`?**

`w` replaces existing content, while `a` adds content to the end.

**Q6. What happens when we use `r` mode on a missing file?**

Python raises `FileNotFoundError`.

**Q7. What is the purpose of `pathlib`?**

It provides convenient, object-oriented file and directory path management.

**Q8. What is the difference between `read()` and `readline()`?**

`read()` reads the requested content, while `readline()` reads one line.

**Q9. Why is UTF-8 useful?**

It supports a wide range of Unicode characters and is widely used for text files.

**Q10. What is the difference between text and binary files?**

Text files are handled as strings, while binary files are handled as bytes.

**Q11. Which mode is used to read binary files?**

`rb`.

**Q12. Which module creates temporary files?**

`tempfile`.

**Q13. How do you read a large file efficiently?**

Process it line by line or in chunks.

**Q14. What is the purpose of `seek()`?**

It changes the current file position.

**Q15. What is the purpose of `tell()`?**

It returns the current file position.

---

## 22. File Handling Cheat Sheet

```python
# Open and read
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Read one line
with open("data.txt", "r", encoding="utf-8") as file:
    line = file.readline()

# Read all lines
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Iterate line by line
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Write
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

# Append
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nNew content")

# Binary read
with open("image.png", "rb") as file:
    data = file.read()

# Binary write
with open("copy.bin", "wb") as file:
    file.write(data)

# Pathlib
from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.is_file())
print(path.name)
print(path.suffix)

# Create directory
Path("reports").mkdir(exist_ok=True)

# Find text files
for file in Path(".").glob("*.txt"):
    print(file)

# Handle missing file
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

# Temporary directory
import tempfile

with tempfile.TemporaryDirectory() as folder:
    print(folder)

# Current working directory
import os

print(os.getcwd())
```

---

## 23. Final Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Open and close files.
- [ ] Explain why context managers are useful.
- [ ] Read files using `read()`, `readline()`, and `readlines()`.
- [ ] Write and append text.
- [ ] Understand all common file modes.
- [ ] Work with paths using `pathlib`.
- [ ] Create, list, and manage directories.
- [ ] Handle missing files and permission errors.
- [ ] Read large files efficiently.
- [ ] Understand UTF-8 encoding and decoding.
- [ ] Read and write binary files.
- [ ] Create temporary files and directories.
- [ ] Use `seek()` and `tell()`.
- [ ] Build a basic log-file analyzer.

## 24. Suggested One-Hour Practice Session

| Time | Task |
|---|---|
| 10 minutes | Revise file modes and context managers |
| 10 minutes | Practice reading, writing, and appending |
| 10 minutes | Practice pathlib and directory operations |
| 10 minutes | Practice exception handling and encoding |
| 10 minutes | Build a small log analyzer |
| 10 minutes | Solve exercises without looking at notes |

**My recommendation:** Don't just memorize the file methods. Open your terminal, create actual files, modify them, and inspect the results. File handling becomes much easier when you work with real files.

For your cybersecurity journey, pay particular attention to reading large files, processing wordlists, analyzing logs, handling paths safely, and calculating file hashes. These skills will be useful when you start building Python automation tools.