# Phase 1: Python Fundamentals Revision
## Topic 2: Variables and Data Types

## 1. Variables and Naming Conventions

### What is a variable?

A variable is a name that refers to an object in Python. It allows us to store and access data using a meaningful name.

Example:

```python
name = "Pulok"
age = 22
height = 5.8

print(name)
print(age)
print(height)
```

Output:

```text
Pulok
22
5.8
```

### Variable assignment

The `=` operator assigns an object to a variable name.

```python
x = 10
y = 20

total = x + y

print(total)
```

Output:

```text
30
```

### Multiple assignment

Python allows you to assign values to multiple variables in one statement.

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

You can also assign the same value to multiple variables.

```python
x = y = z = 100
```

### Variable naming rules

Python variable names must follow these rules:

1. A variable name can contain letters, digits, and underscores.
2. A variable name cannot begin with a digit.
3. Variable names are case-sensitive.
4. Python keywords cannot be used as variable names.
5. Spaces and special characters such as `@` and `-` are not allowed in variable names.

Valid examples:

```python
name = "Alex"
user_age = 22
total_marks = 450
_private_value = 100
score2 = 95
```

Invalid examples:

```python
2name = "Alex"       # Cannot begin with a digit
user-name = "Alex"   # Hyphen is not allowed
user age = 22        # Spaces are not allowed
class = "Python"     # class is a keyword
```

### Naming conventions

Python follows the PEP 8 style guide.

| Naming style | Example | Common use |
|---|---|---|
| `snake_case` | `user_name` | Variables and functions |
| `PascalCase` | `UserProfile` | Classes |
| `UPPER_CASE` | `MAX_LIMIT` | Constants |
| Leading underscore | `_internal_value` | Internal-use convention |

Example:

```python
user_name = "Pulok"
total_marks = 450
MAX_ATTEMPTS = 5
```

**Important:** Python does not enforce constants. `MAX_ATTEMPTS` is a naming convention indicating that the value should generally not be changed.

---

## 2. Dynamic Typing

Python is a dynamically typed language. This means you do not need to declare a variable's data type explicitly before assigning a value.

Example:

```python
value = 100
print(value)

value = "Python"
print(value)

value = 3.14
print(value)
```

Output:

```text
100
Python
3.14
```

The name `value` can refer to objects of different types at different times.

### Static typing vs. dynamic typing

| Static typing | Dynamic typing |
|---|---|
| Types are checked according to a language's static type system. | Types are determined at runtime. |
| Examples include Java and C in their usual use. | Python is dynamically typed. |
| Variables often have declared or inferred types checked before execution. | A name can be reassigned to an object of another type. |

### Python is dynamically typed, not typeless

Every object in Python has a type.

```python
x = 10
print(type(x))

x = "Hello"
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

### Names and objects

A variable name refers to an object rather than being a box that permanently owns one data type.

```python
a = 10
b = a

a = 20

print(a)
print(b)
```

Output:

```text
20
10
```

Reassigning `a` does not change the object referenced by `b`.

### Practical example

```python
price = 499
discount = 50

final_price = price - discount

print(final_price)
```

Output:

```text
449
```

---

## 3. Integers and Floating-Point Numbers

Python provides numeric types for representing whole numbers and numbers with fractional parts.

### Integers (`int`)

An integer represents a whole number without a fractional part.

Examples:

```python
age = 22
temperature = -5
population = 1000000

print(type(age))
```

Output:

```text
<class 'int'>
```

Python integers can represent very large whole numbers, limited by available memory.

### Floating-point numbers (`float`)

A floating-point number represents a real-number approximation and can include a fractional part.

Examples:

```python
price = 99.99
height = 5.8
temperature = -2.5

print(type(price))
```

Output:

```text
<class 'float'>
```

Scientific notation is also supported.

```python
x = 2.5e3

print(x)
```

Output:

```text
2500.0
```

Here, `2.5e3` means \(2.5 \times 10^3\).

### Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | True division | `10 / 3` | Approximately `3.3333` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

Example:

```python
a = 10
b = 3

print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
3.3333333333333335
3
1
1000
```

### Important: floor division with negative numbers

Floor division rounds the result down toward negative infinity.

```python
print(10 // 3)
print(-10 // 3)
```

Output:

```text
3
-4
```

### Floating-point precision

Computers cannot represent every decimal fraction exactly in binary floating-point.

```python
print(0.1 + 0.2)
```

Output:

```text
0.30000000000000004
```

For approximate comparisons, use `math.isclose()` when appropriate.

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

Output:

```text
True
```

For financial calculations requiring exact decimal arithmetic, consider Python's `decimal.Decimal` instead of relying on `float`.

---

## 4. Strings

A string (`str`) is a sequence of Unicode characters used to represent text.

### Creating strings

Strings can be created using single, double, or triple quotes.

```python
name = 'Pulok'
language = "Python"
message = """This is a
multiline string."""

print(name)
print(language)
print(message)
```

### String indexing

Python uses zero-based indexing.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
```

Output:

```text
P
y
n
```

Positive indexing starts from `0`. Negative indexing starts from the end, with `-1` representing the last character.

### String slicing

Slicing extracts part of a string.

Syntax:

```python
string[start:stop:step]
```

The `stop` index is excluded.

```python
text = "Python"

print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[::2])
print(text[::-1])
```

Output:

```text
Pyt
thon
Pyth
Pto
nohtyP
```

### String concatenation

The `+` operator joins strings.

```python
first_name = "Pulok"
last_name = "Singha"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Pulok Singha
```

### String repetition

The `*` operator repeats a string.

```python
print("Hi! " * 3)
```

Output:

```text
Hi! Hi! Hi!
```

### Common string methods

```python
text = "  Hello Python  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "World"))
print(text.find("Python"))
```

Common methods:

| Method | Purpose |
|---|---|
| `lower()` | Converts letters to lowercase |
| `upper()` | Converts letters to uppercase |
| `strip()` | Removes leading and trailing whitespace |
| `replace(old, new)` | Replaces matching text |
| `find(sub)` | Returns the first matching index or `-1` |
| `split()` | Splits a string into a list |
| `startswith(prefix)` | Checks the beginning of a string |
| `endswith(suffix)` | Checks the end of a string |

### f-strings

f-strings allow you to insert expressions into strings.

```python
name = "Pulok"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Pulok and I am 22 years old.
```

You can also format numbers.

```python
price = 123.456

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 123.46
```

### Strings are immutable

Strings cannot be modified in place.

Incorrect:

```python
text = "Python"
text[0] = "J"  # TypeError
```

Correct:

```python
text = "Python"
text = "J" + text[1:]

print(text)
```

Output:

```text
Jython
```

The corrected example creates a new string and reassigns the name `text`.

---

## 5. Booleans

The Boolean type (`bool`) has two values:

- `True`
- `False`

Booleans are commonly used in conditions and comparisons.

### Example

```python
is_student = True
is_employed = False

print(type(is_student))
print(is_student)
```

Output:

```text
<class 'bool'>
True
```

### Comparison operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
age = 22

print(age >= 18)
print(age == 22)
print(age < 18)
```

Output:

```text
True
True
False
```

### Logical operators

Python provides three main logical operators.

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are true |
| `or` | True when at least one condition is true |
| `not` | Reverses a Boolean value |

Example:

```python
age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

Output:

```text
True
True
False
```

### Truthy and falsy values

Python can evaluate many non-Boolean values in a Boolean context.

Common falsy values include:

```python
False
None
0
0.0
""
[]
{}
set()
```

Most other values are truthy.

Example:

```python
name = ""

if name:
    print("Name provided")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

**Important:** `bool("False")` is `True` because `"False"` is a non-empty string.

```python
print(bool("False"))
print(bool(""))
```

Output:

```text
True
False
```

---

## 6. Type Conversion and Casting

Type conversion means converting a value from one type to another.

Python supports explicit conversion using functions such as `int()`, `float()`, `str()`, and `bool()`.

### Convert to integer

```python
x = int("100")

print(x)
print(type(x))
```

Output:

```text
100
<class 'int'>
```

Converting a float to an integer truncates the fractional part toward zero.

```python
print(int(9.8))
print(int(-9.8))
```

Output:

```text
9
-9
```

An invalid integer string raises `ValueError`.

```python
int("hello")  # ValueError
```

### Convert to float

```python
x = float("12.5")

print(x)
print(type(x))
```

Output:

```text
12.5
<class 'float'>
```

### Convert to string

```python
age = 22

message = "Age: " + str(age)

print(message)
```

Output:

```text
Age: 22
```

### Convert to Boolean

```python
print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))
```

Output:

```text
True
False
True
False
```

### Implicit conversion

Python sometimes converts numeric values automatically during an operation.

```python
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

### Common conversion errors

```python
int("25")      # Valid
int("25.5")    # ValueError
float("25.5")  # Valid
```

To convert a decimal string to an integer, convert it to `float` first if truncation is appropriate.

```python
value = int(float("25.5"))

print(value)
```

Output:

```text
25
```

Be careful: this truncates the decimal part rather than rounding.

### Practical example: user input

The `input()` function returns a string, even when the user enters digits.

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters `22`, the type is still `str`.

Convert it when numeric operations are required:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters `22`, the output is `23`.

---

## 7. `None` and `NoneType`

`None` is a special Python object that represents the absence of a value or a missing result.

Its type is `NoneType`.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

### When is `None` used?

- To represent the absence of a value.
- As a default value for optional parameters.
- When a function does not explicitly return a value.
- To indicate that a search or operation found no result.

### Example: a function returning `None`

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
Hello
None
```

The function prints a message but has no explicit `return` statement, so it returns `None`.

### Checking for `None`

Use `is None` or `is not None`.

```python
value = None

if value is None:
    print("No value available")
```

Output:

```text
No value available
```

Avoid using `value == None` when checking for `None`; `is None` is the conventional and recommended check.

### `None` is not the same as zero or an empty string

```python
print(None == 0)
print(None == "")
print(None == False)
```

Output:

```text
False
False
False
```

Although `None`, `0`, `False`, and `""` are all falsy in a Boolean context, they represent different values.

---

## 8. Checking Types with `type()` and `isinstance()`

Python provides built-in functions for inspecting object types.

### Using `type()`

`type()` returns the type of an object.

```python
age = 22
price = 99.5
name = "Pulok"
active = True

print(type(age))
print(type(price))
print(type(name))
print(type(active))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### Using `isinstance()`

`isinstance()` checks whether an object is an instance of a specified type or one of its subclasses.

```python
age = 22

print(isinstance(age, int))
print(isinstance(age, str))
```

Output:

```text
True
False
```

### Checking multiple types

You can provide a tuple of types.

```python
value = 10.5

print(isinstance(value, (int, float)))
```

Output:

```text
True
```

### Important difference

In Python, `bool` is a subclass of `int`.

```python
print(isinstance(True, int))
print(type(True) is int)
```

Output:

```text
True
False
```

Use `isinstance()` when checking whether an object supports a particular type relationship. Use `type()` when you specifically need to inspect its exact type.

### Example: input validation

```python
def display_age(age):
    if isinstance(age, int):
        print(f"Age: {age}")
    else:
        print("Age must be an integer")

display_age(22)
display_age("22")
```

Output:

```text
Age: 22
Age must be an integer
```

Note that `isinstance(True, int)` is also `True`. If your validation must reject Boolean values, check for that explicitly.

---

## 9. Mutable vs. Immutable Objects

In Python, mutability describes whether an object can be changed after it is created.

### Mutable objects

A mutable object can be modified in place.

Common mutable types:

- `list`
- `dict`
- `set`
- Many user-defined class instances

Example:

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

The existing list is modified.

### Immutable objects

An immutable object cannot be changed after it is created.

Common immutable types:

- `int`
- `float`
- `bool`
- `str`
- `tuple` (its contained references cannot be reassigned)
- `frozenset`
- `bytes`

Example:

```python
name = "Python"

# name[0] = "J"  # TypeError

name = "Jython"

print(name)
```

Output:

```text
Jython
```

The original string was not modified. The name `name` was reassigned to a new string.

### Mutable objects and references

```python
a = [1, 2, 3]
b = a

a.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Both names refer to the same list object, so changes to that object are visible through both names.

### Copying a list

```python
a = [1, 2, 3]
b = a.copy()

a.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3]
```

`copy()` creates a shallow copy. If the list contains nested mutable objects, those inner objects may still be shared.

### A tuple containing a mutable object

A tuple is immutable, but it can contain a mutable object.

```python
data = ([1, 2], "Python")

data[0].append(3)

print(data)
```

Output:

```text
([1, 2, 3], 'Python')
```

The tuple's references cannot be reassigned, but the list referenced by its first element can be modified.

### Why mutability matters

Understanding mutability helps you avoid bugs involving:

- Shared lists and dictionaries.
- Functions that modify objects passed to them.
- Mutable default arguments.
- Unexpected changes to nested data structures.

---

## 10. Identity vs. Equality (`is` vs. `==`)

Python provides two different operators for comparing objects.

### Equality: `==`

The `==` operator checks whether two objects are equal according to their equality comparison.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

The lists contain equal values in the same order.

### Identity: `is`

The `is` operator checks whether two references point to the exact same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

These are two separate list objects, even though their contents are equal.

### Comparing two references to the same object

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Output:

```text
True
True
```

Both names refer to the same object.

### The correct way to check for `None`

```python
result = None

if result is None:
    print("No result")
```

Use `is None` because `None` is a singleton object.

### Do not rely on identity for numbers or strings

Python may reuse some objects internally as an implementation optimization. Therefore, the result of `is` for separately created numbers or strings should not be used to test whether their values are equal.

Incorrect approach:

```python
a = 1000
b = 1000

# Do not use this to compare numeric values
print(a is b)
```

Correct approach:

```python
print(a == b)
```

### Summary: `is` vs. `==`

| Operator | Meaning | Typical use |
|---|---|---|
| `==` | Checks equality | Compare values |
| `is` | Checks identity | Check `None` or shared object identity |
| `!=` | Checks inequality | Determine whether values differ |
| `is not` | Checks different identity | Check that a value is not `None` |

**Rule to remember:** Use `==` to compare values and `is` to compare object identity.

---

## 11. Practical Exercises

Try these exercises without looking at the solutions immediately.

### Exercise 1: Variables

Create variables for your name, age, and favourite programming language. Print them in one formatted sentence using an f-string.

### Exercise 2: Dynamic typing

Assign an integer to `value`, then assign a string to the same name. Print `type(value)` after each assignment.

### Exercise 3: Numeric operations

Given:

```python
a = 17
b = 5
```

Print the results of addition, subtraction, multiplication, true division, floor division, modulus, and exponentiation.

### Exercise 4: String operations

Given:

```python
text = "  Learn Python  "
```

Print the stripped string, lowercase version, uppercase version, and the string with `"Python"` replaced by `"Programming"`.

### Exercise 5: Type conversion

Ask the user to enter two numbers, convert them to `float`, and print their sum.

### Exercise 6: `None`

Create a variable named `result` containing `None`. Check it using `is None`.

### Exercise 7: Type checking

Create a function that accepts a value and prints whether it is a string, integer, or float. Decide how you want to handle Boolean values, remembering that `bool` is a subclass of `int`.

### Exercise 8: Mutability

Predict the output before running this code:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Explain why both variables show the same list.

### Exercise 9: Equality and identity

Predict the results:

```python
a = [10, 20]
b = [10, 20]
c = a

print(a == b)
print(a is b)
print(a is c)
```

Explain each result.

### Exercise 10: Mini-project

Write a simple program that:

1. Asks for the user's name.
2. Asks for their age.
3. Converts the age to an integer.
4. Calculates the age they will be next year.
5. Prints a formatted sentence.
6. Handles invalid age input using `try` and `except ValueError`.

---

## 12. Quick Revision Questions

1. What is a variable in Python?
2. What are the rules for naming variables?
3. What does dynamic typing mean?
4. What is the difference between `int` and `float`?
5. Why can `0.1 + 0.2` produce an unexpected-looking result?
6. What is string slicing?
7. Why are strings immutable?
8. What is the difference between `True` and the string `"True"`?
9. What does `input()` return?
10. What is the difference between `None` and `0`?
11. How do `type()` and `isinstance()` differ?
12. What is the difference between mutable and immutable objects?
13. Why can changes to a list be visible through two variables?
14. What is the difference between `is` and `==`?
15. Why should you use `is None` to check for `None`?
16. Why is `isinstance(True, int)` true?
17. What is a shallow copy?
18. Why should you not rely on `is` to compare numeric values?

### Short Answers

1. A variable name refers to an object.
2. Names can contain letters, digits, and underscores, but cannot start with a digit or be Python keywords.
3. The type of an object is determined at runtime, and a name can be reassigned to objects of different types.
4. `int` represents whole numbers; `float` represents approximate real numbers.
5. Some decimal fractions cannot be represented exactly in binary floating-point.
6. Slicing extracts part of a sequence using start, stop, and optional step values.
7. Strings cannot be modified in place after creation.
8. `True` is a Boolean value; `"True"` is a string.
9. `input()` returns a string.
10. `None` represents the absence of a value; `0` is an integer value.
11. `type()` returns an object's type; `isinstance()` checks type membership, including subclasses.
12. Mutable objects can be changed in place; immutable objects cannot.
13. Both variables may reference the same list object.
14. `is` checks identity; `==` checks equality.
15. `None` is a singleton, so `is None` is the conventional identity check.
16. Because `bool` is a subclass of `int`.
17. A shallow copy creates a new outer container but may share nested objects.
18. Object identity can depend on implementation optimizations; use `==` for value comparison.

---

## 13. Essential Cheat Sheet

| Concept | Example |
|---|---|
| Variable assignment | `age = 22` |
| Check type | `type(age)` |
| Check type membership | `isinstance(age, int)` |
| Convert to integer | `int("25")` |
| Convert to float | `float("3.14")` |
| Convert to string | `str(25)` |
| Convert to Boolean | `bool(1)` |
| Check for no value | `result is None` |
| Compare values | `a == b` |
| Compare identity | `a is b` |
| String slicing | `text[1:4]` |
| f-string | `f"Hello, {name}"` |
| Make a shallow list copy | `items.copy()` |
| Check truthiness | `if value:` |

---

## Final Revision Advice

For this topic, focus on writing small programs rather than memorizing definitions.

Make sure you can explain and demonstrate these five concepts:

1. Dynamic typing and variable assignment.
2. Type conversion, especially converting `input()` to numbers.
3. String operations and immutability.
4. Mutable objects and shared references.
5. The difference between `is` and `==`.

Once you can use these concepts confidently in the terminal, move to the next topic in your Python revision roadmap.
