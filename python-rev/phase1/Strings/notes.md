# Python Revision — Topic 6: Strings

## 1. What Is a String in Python?

A string is a sequence of characters used to represent text. In Python, the `str` type is used for strings.

Strings can contain letters, numbers, symbols, spaces, and Unicode characters.

### Example

```python
name = "Python"
message = "Hello, World!"
password = "abc123!@#"
number_text = "12345"

print(name)
print(message)
print(password)
print(number_text)
```

**Output:**

```text
Python
Hello, World!
abc123!@#
12345
```

Even though `number_text` contains digits, it is a string because it is enclosed in quotes.

```python
number_text = "123"
number = 123

print(type(number_text))
print(type(number))
```

**Output:**

```text
<class 'str'>
<class 'int'>
```

You can create strings using single quotes, double quotes, or triple quotes.

```python
first = 'Hello'
second = "Python"
third = """This is a
multiline string."""

print(first)
print(second)
print(third)
```

**Important:** A string is an immutable sequence of Unicode code points. This means you can read its characters, but you cannot change individual characters in place.

---

## 2. String Indexing

Indexing allows you to access an individual character in a string.

Python uses zero-based indexing, meaning the first character has index `0`.

### Example

```python
language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
```

**Output:**

```text
P
y
t
h
```

The string `"Python"` has six characters.

| Character | P | y | t | h | o | n |
|---|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

### 2.1 Negative Indexing

Negative indexing starts from the end of the string.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-3])
```

**Output:**

```text
n
o
h
```

Common uses include getting the last character or checking a filename's ending.

```python
filename = "report.pdf"

print(filename[-3:])
```

**Output:**

```text
pdf
```

Note that this example extracts the last three characters; it is not a complete filename-extension validation method.

### 2.2 Index Out of Range

Accessing an index that does not exist raises an `IndexError`.

```python
word = "Python"

print(word[10])
```

**Error:**

```text
IndexError: string index out of range
```

You can check the string's length before accessing a particular index.

```python
word = "Python"
index = 10

if 0 <= index < len(word):
    print(word[index])
else:
    print("Index out of range")
```

**Output:**

```text
Index out of range
```

---

## 3. String Slicing

Slicing extracts a portion of a string.

### Syntax

```python
string[start:stop:step]
```

- `start`: index where slicing begins; included.
- `stop`: index where slicing ends; excluded.
- `step`: number of positions to move each time; defaults to `1`.

### 3.1 Basic Slicing

```python
text = "Python Programming"

print(text[0:6])
print(text[7:18])
```

**Output:**

```text
Python
Programming
```

The ending index is excluded.

### 3.2 Omitting Start or Stop

```python
text = "Python"

print(text[:3])
print(text[3:])
print(text[:])
```

**Output:**

```text
Pyt
hon
Python
```

- `text[:3]` starts from the beginning.
- `text[3:]` continues to the end.
- `text[:]` creates a new string with the same contents.

### 3.3 Slicing with Negative Indices

```python
text = "Python"

print(text[-3:])
print(text[:-2])
print(text[-4:-1])
```

**Output:**

```text
hon
Pyth
tho
```

### 3.4 Slicing with a Step

```python
text = "0123456789"

print(text[::2])
print(text[1::2])
```

**Output:**

```text
02468
13579
```

### 3.5 Reversing a String

A negative step can reverse a string.

```python
text = "Python"

print(text[::-1])
```

**Output:**

```text
nohtyP
```

### 3.6 Slicing Does Not Normally Raise an Index Error

Unlike indexing, slicing handles out-of-range boundaries without raising an `IndexError`.

```python
text = "Python"

print(text[0:100])
print(text[100:200])
```

**Output:**

```text
Python

```

The second slice is an empty string.

### Practical Example: Masking a Phone Number

```python
phone = "9876543210"

masked_phone = "*" * 6 + phone[-4:]

print(masked_phone)
```

**Output:**

```text
******3210
```

This is a display-masking example. Real applications should avoid exposing sensitive values unnecessarily.

---

## 4. String Immutability

Strings are immutable, meaning their characters cannot be changed after the string has been created.

### Incorrect Example

```python
text = "Python"
text[0] = "J"
```

**Error:**

```text
TypeError: 'str' object does not support item assignment
```

### Correct Example: Create a New String

```python
text = "Python"
text = "J" + text[1:]

print(text)
```

**Output:**

```text
Jython
```

The original string was not modified. A new string was created and assigned to the variable.

### Example: Replacing Text

```python
text = "I like Java"

text = text.replace("Java", "Python")

print(text)
```

**Output:**

```text
I like Python
```

The `replace()` method returns a new string.

### Why Does Immutability Matter?

- String methods usually return new strings instead of modifying the original.
- Strings can be used as dictionary keys because they are immutable.
- Repeatedly concatenating strings in large loops may be inefficient.
- Understanding immutability helps prevent unexpected behavior.

### Efficient String Building

Instead of repeatedly concatenating a string inside a large loop:

```python
result = ""

for word in ["Python", "is", "useful"]:
    result += word + " "
```

You can collect the parts and join them:

```python
words = ["Python", "is", "useful"]

result = " ".join(words)

print(result)
```

**Output:**

```text
Python is useful
```

---

## 5. Important String Methods

String methods make it easier to clean, inspect, transform, and validate text.

### 5.1 `lower()`

Converts letters to lowercase.

```python
text = "PYTHON Programming"

print(text.lower())
```

**Output:**

```text
python programming
```

### 5.2 `upper()`

Converts letters to uppercase.

```python
text = "Python"

print(text.upper())
```

**Output:**

```text
PYTHON
```

### 5.3 `capitalize()`

Makes the first character uppercase and the remaining characters lowercase.

```python
text = "pYTHON PROGRAMMING"

print(text.capitalize())
```

**Output:**

```text
Python programming
```

### 5.4 `title()`

Capitalizes the beginning of words.

```python
text = "python programming language"

print(text.title())
```

**Output:**

```text
Python Programming Language
```

Be aware that `title()` is not a perfect formatter for every name or language.

### 5.5 `strip()`

Removes leading and trailing whitespace by default.

```python
text = "   Hello Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

**Output:**

```text
Hello Python
Hello Python   
   Hello Python
```

You can also specify characters to remove from the ends.

```python
text = "***hello***"

print(text.strip("*"))
```

**Output:**

```text
hello
```

The argument is a set of characters, not a complete substring.

### 5.6 `startswith()` and `endswith()`

Check the beginning or ending of a string.

```python
filename = "report.pdf"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))
```

**Output:**

```text
True
True
```

These are useful for simple text checks. For security-sensitive file validation, do not rely only on a filename's extension.

### 5.7 `count()`

Counts non-overlapping occurrences of a substring.

```python
text = "banana"

print(text.count("a"))
print(text.count("an"))
```

**Output:**

```text
3
2
```

### 5.8 `find()`

Returns the index of the first occurrence of a substring. If it is not found, it returns `-1`.

```python
text = "Python Programming"

print(text.find("Programming"))
print(text.find("Java"))
```

**Output:**

```text
7
-1
```

### 5.9 `index()`

Similar to `find()`, but raises `ValueError` when the substring is not found.

```python
text = "Python"

print(text.index("th"))
```

**Output:**

```text
2
```

If the substring is not present, `index()` raises an error instead of returning `-1`.

### 5.10 `replace()`

Replaces occurrences of a substring.

```python
text = "I like Java. Java is popular."

print(text.replace("Java", "Python"))
```

**Output:**

```text
I like Python. Python is popular.
```

You can limit the number of replacements.

```python
text = "one one one"

print(text.replace("one", "two", 2))
```

**Output:**

```text
two two one
```

### 5.11 `split()`

Splits a string into a list of strings.

```python
text = "Python Java C++"

print(text.split())
```

**Output:**

```text
['Python', 'Java', 'C++']
```

By default, consecutive whitespace characters act as separators.

### 5.12 `join()`

Joins an iterable of strings using a separator.

```python
words = ["Python", "is", "powerful"]

print(" ".join(words))
print("-".join(words))
print(", ".join(words))
```

**Output:**

```text
Python is powerful
Python-is-powerful
Python, is, powerful
```

Every element must be a string.

Incorrect:

```python
numbers = [1, 2, 3]

print(",".join(numbers))
```

This raises a `TypeError`.

Correct:

```python
numbers = [1, 2, 3]

print(",".join(str(number) for number in numbers))
```

**Output:**

```text
1,2,3
```

### 5.13 String Validation Methods

Python provides several methods for checking the characters in a string.

```python
print("Python".isalpha())
print("12345".isdigit())
print("abc123".isalnum())
print("   ".isspace())
print("hello".islower())
print("HELLO".isupper())
```

**Output:**

```text
True
True
True
True
True
True
```

| Method | Meaning |
|---|---|
| `isalpha()` | All characters are alphabetic and the string is non-empty |
| `isdigit()` | All characters are digits and the string is non-empty |
| `isalnum()` | All characters are alphabetic or numeric and the string is non-empty |
| `isspace()` | All characters are whitespace and the string is non-empty |
| `islower()` | Cased characters are lowercase, with at least one cased character |
| `isupper()` | Cased characters are uppercase, with at least one cased character |

Important: These methods check character categories, not whether a value meets every requirement of an application. For example, `isdigit()` does not accept a negative sign or decimal point.

---

## 6. Searching and Replacing Text

Searching and replacing are common tasks when cleaning data, examining logs, and processing text.

### 6.1 Check Whether Text Exists

Use the `in` operator.

```python
text = "Python is useful for automation"

print("Python" in text)
print("Java" in text)
```

**Output:**

```text
True
False
```

String matching is case-sensitive by default.

```python
text = "Python"

print("python" in text)
print("python" in text.lower())
```

**Output:**

```text
False
True
```

### 6.2 Find the Position of a Word

```python
text = "Learn Python programming"

position = text.find("Python")

if position != -1:
    print("Found at index:", position)
else:
    print("Not found")
```

**Output:**

```text
Found at index: 6
```

### 6.3 Replace Sensitive-Looking Text for a Demonstration

```python
message = "Contact: 9876543210"

masked_message = message.replace("9876543210", "**********")

print(masked_message)
```

**Output:**

```text
Contact: **********
```

This replaces an exact sequence. If the text varies, you may need a more general approach, such as regular expressions.

### 6.4 Replace Only the First Occurrence

```python
text = "error error error"

print(text.replace("error", "warning", 1))
```

**Output:**

```text
warning error error
```

### 6.5 Search Without Case Sensitivity

```python
text = "PYTHON is GREAT"

search_term = "python"

if search_term.lower() in text.lower():
    print("Text found")
else:
    print("Text not found")
```

**Output:**

```text
Text found
```

This approach works for simple case-insensitive searches. More advanced language-aware matching can require additional tools.

---

## 7. Splitting and Joining Strings

Splitting and joining are especially useful when processing CSV-like data, command output, and simple structured text.

### 7.1 Split by Whitespace

```python
text = "Python   is    easy"

words = text.split()

print(words)
```

**Output:**

```text
['Python', 'is', 'easy']
```

### 7.2 Split by a Specific Separator

```python
text = "red,green,blue"

colors = text.split(",")

print(colors)
```

**Output:**

```text
['red', 'green', 'blue']
```

### 7.3 Limit the Number of Splits

```python
text = "one-two-three-four"

print(text.split("-", 2))
```

**Output:**

```text
['one', 'two', 'three-four']
```

The maximum number of splits is two.

### 7.4 Split into Lines

```python
text = "First line\nSecond line\nThird line"

lines = text.splitlines()

print(lines)
```

**Output:**

```text
['First line', 'Second line', 'Third line']
```

### 7.5 Join Words

```python
words = ["Learn", "Python", "daily"]

sentence = " ".join(words)

print(sentence)
```

**Output:**

```text
Learn Python daily
```

### 7.6 Remove Extra Whitespace from Every Word

```python
text = "  Python   is   useful  "

words = text.split()
cleaned_text = " ".join(words)

print(cleaned_text)
```

**Output:**

```text
Python is useful
```

This is a convenient way to normalize repeated whitespace in ordinary text.

### Important: `split()` Is Not a Complete CSV Parser

Consider:

```text
name,city
Alex,"New York, USA"
```

Simply splitting every line on commas will incorrectly divide `"New York, USA"` into two fields.

For actual CSV files, use Python's `csv` module.

```python
import csv

with open("people.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["city"])
```

This correctly handles quoted CSV fields according to the CSV format.

---

## 8. String Formatting and f-Strings

String formatting allows you to insert values into text.

### 8.1 f-Strings

An f-string starts with `f` or `F` before the opening quote. Expressions inside curly braces `{}` are evaluated and inserted into the string.

```python
name = "Alex"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)
```

**Output:**

```text
My name is Alex and I am 25 years old.
```

### 8.2 Expressions Inside f-Strings

```python
a = 10
b = 5

print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Is a greater than b? {a > b}")
```

**Output:**

```text
Sum: 15
Product: 50
Is a greater than b? True
```

### 8.3 Formatting Decimal Places

```python
price = 123.45678

print(f"{price:.2f}")
```

**Output:**

```text
123.46
```

The `.2f` format displays two digits after the decimal point.

### 8.4 Formatting Percentages

```python
ratio = 0.875

print(f"{ratio:.1%}")
```

**Output:**

```text
87.5%
```

### 8.5 Width and Alignment

```python
name = "Python"

print(f"{name:>10}")
print(f"{name:<10}")
print(f"{name:^10}")
```

**Output:**

```text
    Python
Python    
  Python  
```

- `>` aligns text to the right.
- `<` aligns text to the left.
- `^` centers text.

### 8.6 Number Formatting

```python
number = 1234567

print(f"{number:,}")
```

**Output:**

```text
1,234,567
```

### 8.7 Displaying Curly Braces

To display literal curly braces in an f-string, double them.

```python
name = "Alex"

print(f"{{Hello, {name}}}")
```

**Output:**

```text
{Hello, Alex}
```

### 8.8 Other Formatting Methods

The older `str.format()` method is also available.

```python
name = "Alex"
age = 25

print("Name: {}, Age: {}".format(name, age))
```

**Output:**

```text
Name: Alex, Age: 25
```

The `%` formatting style also exists, mainly for older code.

```python
name = "Alex"
age = 25

print("Name: %s, Age: %d" % (name, age))
```

For most new Python code, f-strings are a clear and convenient default.

### Security Note: Avoid Using `eval()` for String Formatting

Do not use `eval()` to evaluate arbitrary text from users. It can execute Python expressions and potentially dangerous code.

Prefer f-strings for inserting values into messages.

---

## 9. Escape Sequences

Escape sequences represent special characters inside strings. Most begin with a backslash (`\`).

| Escape sequence | Meaning |
|---|---|
| `\n` | Newline |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\uXXXX` | Unicode code point using four hexadecimal digits |
| `\UXXXXXXXX` | Unicode code point using eight hexadecimal digits |
| `\xhh` | Character represented by two hexadecimal digits |
| `\ooo` | Character represented by up to three octal digits |

### 9.1 Newline

```python
text = "Hello\nWorld"

print(text)
```

**Output:**

```text
Hello
World
```

### 9.2 Tab

```python
print("Name\tAge")
print("Alex\t25")
```

**Output:**

```text
Name    Age
Alex    25
```

The visual spacing depends on the terminal's tab settings.

### 9.3 Quotes Inside Strings

```python
print("It's Python")
print('He said, "Hello"')
print("It\'s Python")
```

**Output:**

```text
It's Python
He said, "Hello"
It's Python
```

### 9.4 Backslashes

```python
print("C:\\Users\\Alex")
```

**Output:**

```text
C:\Users\Alex
```

### 9.5 Carriage Return

```python
print("Hello\rWorld")
```

A carriage return moves the cursor to the beginning of the current line. The displayed result can vary by terminal because the new text may overwrite existing characters.

### 9.6 Unicode Escape

```python
print("\u2764")
```

**Output:**

```text
❤
```

### 9.7 Raw Strings

Raw strings use the `r` or `R` prefix. They are useful for text containing many backslashes.

```python
path = r"C:\Users\Alex\Documents"

print(path)
```

**Output:**

```text
C:\Users\Alex\Documents
```

Raw strings are particularly useful when writing many regular expressions.

**Important:** A raw string cannot end with an odd number of backslashes because the final backslash would escape the closing quote.

---

## 10. Unicode and Character Encoding Basics

Unicode and character encoding are important when processing text from files, web pages, APIs, and logs.

### 10.1 What Is Unicode?

Unicode assigns a code point to each character in its repertoire.

Examples:

- `A` has code point `U+0041`.
- `a` has code point `U+0061`.
- `₹` has code point `U+20B9`.
- `❤` has code point `U+2764`.

Python strings represent sequences of Unicode code points.

```python
text = "A₹❤"

for character in text:
    print(character, ord(character))
```

**Output:**

```text
A 65
₹ 8377
❤ 10084
```

The `ord()` function returns the Unicode code point of a single character.

The `chr()` function converts a valid Unicode code point into a string containing that character.

```python
print(chr(65))
print(chr(8377))
```

**Output:**

```text
A
₹
```

### 10.2 What Is Character Encoding?

Character encoding defines how text is represented as bytes.

Unicode describes characters and their code points. UTF-8 is a widely used encoding that represents Unicode text as bytes.

A character may use one or more bytes in UTF-8.

### 10.3 Encoding a String

```python
text = "Hello"

encoded = text.encode("utf-8")

print(encoded)
print(type(encoded))
```

**Output:**

```text
b'Hello'
<class 'bytes'>
```

The result is a `bytes` object, not a `str`.

### 10.4 Decoding Bytes

```python
data = b"Hello"

text = data.decode("utf-8")

print(text)
print(type(text))
```

**Output:**

```text
Hello
<class 'str'>
```

Encoding converts text into bytes. Decoding converts bytes into text using a specified encoding.

### 10.5 UTF-8 Example with Unicode

```python
text = "₹"

encoded = text.encode("utf-8")

print(encoded)
print(len(encoded))
```

**Output:**

```text
b'\xe2\x82\xb9'
3
```

The rupee symbol uses three bytes in UTF-8.

### 10.6 Reading a Text File with UTF-8

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Specifying an encoding helps make text processing more predictable across systems.

### 10.7 Writing a Text File with UTF-8

```python
text = "Python supports Unicode: ₹ ❤"

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write(text)
```

### 10.8 Character Count vs. Byte Count

```python
text = "₹"

print(len(text))
print(len(text.encode("utf-8")))
```

**Output:**

```text
1
3
```

`len(text)` counts Unicode code points in the string. The encoded length counts bytes.

A visible symbol can also consist of multiple Unicode code points, such as some emoji sequences. Therefore, string length does not always equal the number of user-perceived characters.

### 10.9 Handling Encoding Errors

```python
data = b"\xff"

try:
    text = data.decode("utf-8")
    print(text)
except UnicodeDecodeError:
    print("The bytes are not valid UTF-8 text")
```

**Output:**

```text
The bytes are not valid UTF-8 text
```

Do not assume that every byte sequence represents valid UTF-8.

---

## 11. Working with Multiline Strings

Triple quotes allow you to create strings spanning multiple lines.

### 11.1 Triple-Quoted Strings

```python
message = """Hello,
Welcome to Python.
Keep practicing."""

print(message)
```

**Output:**

```text
Hello,
Welcome to Python.
Keep practicing.
```

Both triple-single quotes and triple-double quotes can be used.

```python
text = '''This is a
multiline string.'''

print(text)
```

### 11.2 Multiline Strings for Messages

```python
name = "Alex"

message = f"""Hello, {name}!

Welcome to the program.
Have a great day."""

print(message)
```

**Output:**

```text
Hello, Alex!

Welcome to the program.
Have a great day.
```

### 11.3 Multiline Strings and Docstrings

A docstring is a string literal used to document a module, class, or function.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(10, 20))
print(add.__doc__)
```

**Output:**

```text
30
Return the sum of two numbers.
```

A docstring is different from an ordinary comment. It is stored as documentation associated with the object.

### 11.4 Be Careful with Indentation

Triple-quoted strings preserve their whitespace and newlines.

```python
message = """
    Hello
    Python
    """

print(repr(message))
```

`repr()` displays a representation of the string, making leading spaces and newline characters easier to notice.

If you want to remove common indentation, you can use `textwrap.dedent()`.

```python
import textwrap

message = """
    Hello
    Python
"""

print(textwrap.dedent(message).strip())
```

**Output:**

```text
Hello
Python
```

---

## 12. Parsing Structured Text

Parsing structured text means extracting useful information from a string that follows a known format.

Examples include:

- Key-value pairs.
- Simple configuration text.
- Log lines.
- Comma-separated values.
- URL components.
- JSON data.
- Command output.

For simple formats, string methods may be sufficient. For established formats, prefer a dedicated parser.

### 12.1 Parsing Key-Value Text

Suppose you have:

```python
text = "name=Alex;age=25;city=Delhi"
```

You can split the text into individual pairs and then separate each key from its value.

```python
text = "name=Alex;age=25;city=Delhi"

data = {}

for item in text.split(";"):
    key, value = item.split("=", 1)
    data[key] = value

print(data)
```

**Output:**

```text
{'name': 'Alex', 'age': '25', 'city': 'Delhi'}
```

The argument `1` means split at most once. This allows a value to contain an additional equals sign.

For example, `token=abc=123` becomes key `token` and value `abc=123`.

This example assumes that every pair follows the expected format. Real-world data may require additional validation.

### 12.2 Handling Malformed Key-Value Data

```python
text = "name=Alex;age=25;invalid_item;city=Delhi"

data = {}

for item in text.split(";"):
    if "=" not in item:
        print("Skipping invalid item:", item)
        continue

    key, value = item.split("=", 1)
    key = key.strip()
    value = value.strip()

    if not key:
        print("Skipping empty key")
        continue

    data[key] = value

print(data)
```

**Output:**

```text
Skipping invalid item: invalid_item
{'name': 'Alex', 'age': '25', 'city': 'Delhi'}
```

This demonstrates basic defensive parsing.

### 12.3 Parsing a Simple Log Line

Suppose a log line looks like this:

```text
2026-10-23 ERROR Failed login
```

You can split it into fields:

```python
log_line = "2026-10-23 ERROR Failed login"

parts = log_line.split(" ", 2)

date = parts[0]
level = parts[1]
message = parts[2]

print("Date:", date)
print("Level:", level)
print("Message:", message)
```

**Output:**

```text
Date: 2026-10-23
Level: ERROR
Message: Failed login
```

The maximum of two splits preserves the remaining message as one field.

This approach assumes the date and level do not contain spaces and that the line has all three fields. Production log parsers should validate those assumptions.

### 12.4 Parsing JSON Properly

JSON is a structured data format. Avoid trying to parse complex JSON using `split()`.

Use Python's built-in `json` module instead.

```python
import json

json_text = '{"name": "Alex", "age": 25, "active": true}'

data = json.loads(json_text)

print(data["name"])
print(data["age"])
print(data["active"])
```

**Output:**

```text
Alex
25
True
```

JSON uses `true`, `false`, and `null` in its text representation. Python converts these to `True`, `False`, and `None` when parsing valid JSON.

### 12.5 Handling Invalid JSON

```python
import json

json_text = '{"name": "Alex", "age": }'

try:
    data = json.loads(json_text)
    print(data)
except json.JSONDecodeError:
    print("Invalid JSON")
```

**Output:**

```text
Invalid JSON
```

### 12.6 Parsing CSV Properly

For comma-separated data, use the `csv` module rather than splitting every line manually.

```python
import csv
from io import StringIO

csv_text = '''name,city
Alex,"New York, USA"
Riya,Delhi'''

file = StringIO(csv_text)
reader = csv.DictReader(file)

for row in reader:
    print(row["name"], "-", row["city"])
```

**Output:**

```text
Alex - New York, USA
Riya - Delhi
```

`StringIO` lets you work with a string as though it were a file.

### 12.7 Parsing Text with Regular Expressions

Regular expressions are useful when you need to identify patterns in text.

For example, to find sequences of digits:

```python
import re

text = "Ticket 123, Ticket 456, Ticket 789"

numbers = re.findall(r"\d+", text)

print(numbers)
```

**Output:**

```text
['123', '456', '789']
```

Here, `\d+` matches one or more digit characters.

Regular expressions are useful for pattern matching, but they are not a substitute for a proper parser when working with complex formats such as JSON or CSV.

### 12.8 Practical Example: Extract Error Lines from a Log

```python
log_text = """INFO Application started
ERROR Invalid input
INFO Processing request
ERROR Connection failed
WARNING Retry suggested"""

for line in log_text.splitlines():
    if "ERROR" in line:
        print(line)
```

**Output:**

```text
ERROR Invalid input
ERROR Connection failed
```

This is a simple example of text processing used in log analysis. In a real system, log parsing should account for the actual log format and avoid treating untrusted log content as executable code.

---

## 13. Common String Mistakes

### Mistake 1: Trying to Modify a String by Index

Incorrect:

```python
text = "Python"
text[0] = "J"
```

Correct:

```python
text = "J" + text[1:]
```

Strings are immutable.

### Mistake 2: Forgetting That the Stop Index Is Excluded

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

The character at index `3` is not included.

### Mistake 3: Using `find()` Incorrectly

Incorrect assumption: `find()` raises an error if the text is missing.

In reality:

```python
print("Python".find("Java"))
```

Output:

```text
-1
```

Always check whether the result is `-1` if you need to know whether a substring was found.

### Mistake 4: Forgetting That String Methods Return New Strings

```python
text = "python"
text.upper()

print(text)
```

Output:

```text
python
```

Correct:

```python
text = text.upper()
print(text)
```

Output:

```text
PYTHON
```

### Mistake 5: Joining Non-String Values

Incorrect:

```python
numbers = [1, 2, 3]
print(",".join(numbers))
```

Correct:

```python
numbers = [1, 2, 3]
print(",".join(str(number) for number in numbers))
```

### Mistake 6: Assuming All Text Is ASCII

Text may contain Unicode characters, and some characters require multiple bytes in UTF-8.

When reading files, specify the correct encoding where possible.

### Mistake 7: Using String Splitting for Every Data Format

Using `split(",")` for complex CSV or splitting JSON manually can fail when values contain separators or escaping.

Use the standard `csv` and `json` modules for their respective formats.

### Mistake 8: Confusing a String with a Number

```python
number_text = "10"
print(number_text + "5")
```

Output:

```text
105
```

This concatenates two strings.

To perform arithmetic:

```python
number = int(number_text)
print(number + 5)
```

Output:

```text
15
```

### Mistake 9: Forgetting Case Sensitivity

```python
print("Python" == "python")
```

Output:

```text
False
```

Normalize the case if case-insensitive comparison is appropriate.

### Mistake 10: Confusing `is` with `==`

Use `==` to compare string contents.

```python
first = "Python"
second = "Python"

print(first == second)
```

Output:

```text
True
```

Do not use `is` to compare string values. Object identity and value equality are different concepts.

---

## 14. Practical Mini Projects

### Project 1: Word and Character Counter

```python
text = input("Enter a sentence: ")

words = text.split()
characters = len(text)
characters_without_spaces = len("".join(text.split()))

print("Words:", len(words))
print("Characters including spaces:", characters)
print("Characters excluding whitespace:", characters_without_spaces)
```

The last count removes all whitespace, not just ordinary spaces.

### Project 2: Palindrome Checker

A palindrome reads the same forward and backward under a chosen comparison rule.

```python
text = input("Enter a word or phrase: ")

normalized = "".join(
    character.lower()
    for character in text
    if character.isalnum()
)

if normalized == normalized[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

Example input:

```text
Never odd or even
```

Output:

```text
Palindrome
```

This version ignores case and removes non-alphanumeric characters.

### Project 3: Simple Email Format Check

```python
email = input("Enter email: ").strip()

if not email:
    print("Email cannot be empty")
elif "@" not in email:
    print("Email must contain @")
elif email.startswith("@") or email.endswith("@"):
    print("Invalid email format")
else:
    print("Basic format check passed")
```

This is only a basic check. It does not prove that the email address exists or that the address meets every email standard.

### Project 4: Extract File Extensions

```python
filename = input("Enter filename: ").strip()

if "." not in filename or filename.endswith("."):
    print("No valid extension found")
else:
    extension = filename.rsplit(".", 1)[1].lower()
    print("Extension:", extension)
```

Example input:

```text
report.PDF
```

Output:

```text
Extension: pdf
```

This is a simple filename exercise. A filename can have special cases such as hidden files or multiple dots, so real applications may need more careful rules.

### Project 5: Simple Log Filter

```python
log_text = """INFO Login successful
WARNING Too many requests
ERROR Login failed
INFO Session closed
ERROR Permission denied"""

error_count = 0

for line in log_text.splitlines():
    if "ERROR" in line:
        print(line)
        error_count += 1

print("Total errors:", error_count)
```

**Output:**

```text
ERROR Login failed
ERROR Permission denied
Total errors: 2
```

This combines multiline strings, splitting, searching, and loops.

---

## 15. Practice Exercises

Solve these in your terminal without looking at the solutions.

### Beginner Level

1. Create a string and print its first and last characters.
2. Extract the first five characters of a string using slicing.
3. Reverse a string using slicing.
4. Convert a sentence to lowercase and uppercase.
5. Remove leading and trailing whitespace from user input.
6. Count how many times a particular character appears in a string.
7. Check whether a string contains a given word.
8. Replace every occurrence of one word with another.

### Intermediate Level

9. Split a sentence into words and print each word on a separate line.
10. Join a list of words using hyphens.
11. Count the number of words, characters, and vowels in a sentence.
12. Check whether a string is a palindrome.
13. Mask all but the last four characters of a sample identifier.
14. Use an f-string to display a person's name, age, and score.
15. Extract the extension from a filename.
16. Parse a simple key-value string such as `name=Alex;age=25;city=Delhi`.

### Advanced Practice

17. Read a UTF-8 text file and count its lines.
18. Extract all digit sequences from a sample log using `re.findall()`.
19. Parse a JSON string using the `json` module and handle malformed JSON.
20. Read CSV data with quoted fields using the `csv` module.
21. Write a log filter that finds all lines containing `ERROR`, ignoring case.
22. Build a program that normalizes whitespace in a multiline paragraph.
23. Explain why `len("₹")` and `len("₹".encode("utf-8"))` return different results.
24. Create a basic parser for key-value pairs that skips malformed entries.

---

## 16. Quick Revision Questions and Answers

**Q1. What is a string?**

A sequence of Unicode code points represented by Python's `str` type.

**Q2. Are strings mutable?**

No. Strings are immutable.

**Q3. What is indexing?**

Accessing an individual character using its position.

**Q4. What is slicing?**

Extracting part of a sequence using the syntax `start:stop:step`.

**Q5. Is the stop index included in a slice?**

No.

**Q6. What does `text[::-1]` do?**

It returns a reversed version of the string.

**Q7. What is the difference between `find()` and `index()`?**

`find()` returns `-1` when the substring is absent. `index()` raises `ValueError`.

**Q8. What does `strip()` do?**

It removes leading and trailing whitespace by default.

**Q9. What is the difference between `split()` and `join()`?**

`split()` separates a string into parts. `join()` combines strings using a separator.

**Q10. What is an f-string?**

A string literal prefixed with `f` or `F` that allows expressions inside `{}`.

**Q11. What does `\n` represent?**

A newline character.

**Q12. What is Unicode?**

A standard that assigns code points to characters.

**Q13. What is UTF-8?**

A variable-length encoding used to represent Unicode text as bytes.

**Q14. What is the difference between `str` and `bytes`?**

`str` represents text as Unicode code points. `bytes` represents a sequence of byte values.

**Q15. Why should you use the `json` module for JSON?**

It correctly parses the JSON format and handles its structure more reliably than manual string splitting.

**Q16. What is a raw string?**

A string literal prefixed with `r` or `R` in which backslashes generally remain literal instead of introducing ordinary escape sequences.

**Q17. Why is `",".join([1, 2, 3])` invalid?**

Because `join()` requires string elements.

**Q18. What is the difference between `==` and `is`?**

`==` checks value equality. `is` checks object identity.

---

## 17. Strings Cheat Sheet

| Task | Example |
|---|---|
| Get first character | `text[0]` |
| Get last character | `text[-1]` |
| Slice a string | `text[1:5]` |
| Reverse a string | `text[::-1]` |
| Get string length | `len(text)` |
| Convert to lowercase | `text.lower()` |
| Convert to uppercase | `text.upper()` |
| Remove surrounding whitespace | `text.strip()` |
| Check prefix | `text.startswith("Py")` |
| Check suffix | `text.endswith(".txt")` |
| Find substring | `text.find("word")` |
| Check substring membership | `"word" in text` |
| Replace text | `text.replace("old", "new")` |
| Split into words | `text.split()` |
| Split by comma | `text.split(",")` |
| Join words | `" ".join(words)` |
| Format text | `f"Hello, {name}"` |
| Convert character to code point | `ord("A")` |
| Convert code point to character | `chr(65)` |
| Encode to bytes | `text.encode("utf-8")` |
| Decode bytes | `data.decode("utf-8")` |
| Split into lines | `text.splitlines()` |
| Parse JSON | `json.loads(text)` |
| Read CSV | `csv.reader(file)` or `csv.DictReader(file)` |
| Find pattern matches | `re.findall(pattern, text)` |

---

## Final Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Use positive and negative string indexing.
- [ ] Extract substrings using slicing.
- [ ] Explain why strings are immutable.
- [ ] Use common string methods correctly.
- [ ] Search for and replace text.
- [ ] Split strings and join lists of strings.
- [ ] Format text with f-strings.
- [ ] Understand common escape sequences and raw strings.
- [ ] Explain the difference between Unicode text and encoded bytes.
- [ ] Work with multiline strings.
- [ ] Parse simple key-value text.
- [ ] Use `json` and `csv` for structured data.
- [ ] Extract patterns with basic regular expressions.

## Recommended One-Hour Practice Plan

- **10 minutes:** Indexing, slicing, and immutability.
- **15 minutes:** String methods, searching, splitting, and joining.
- **10 minutes:** f-strings and escape sequences.
- **10 minutes:** Unicode, UTF-8, and file encoding.
- **15 minutes:** Solve one parsing exercise and one mini project.

Focus on writing code yourself rather than memorizing every method. For practical scripting, the most useful skills are cleaning input, searching text, extracting fields, formatting output, and handling text files safely.
