# Python Programming Series — Video #4

# Variables & Data Types in Python

**Channel:** PulokSec  
**Level:** Complete Beginner  
**Series:** Python Programming Series

> **Learn • Code • Build**

---

# 1. What We'll Learn

In this lesson, we'll understand:

- What is a variable?
- Why variables are useful
- Creating and assigning variables
- Variable naming rules
- Valid and invalid variable names
- Multiple variable assignment
- Reassigning variables
- What is a data type?
- Common Python data types
- Checking data types with `type()`

---

# 2. What Is a Variable?

A **variable** is a name that refers to a value stored in a program.

You can think of a variable as a labeled box. The label is the variable name, and the value is the data inside it.

```text
Variable name  →  Value
    age        →   20
```

In Python:

```python
age = 20
```

Here:

- `age` is the variable name.
- `20` is the value.
- `=` assigns the value to the variable.

> A variable allows us to give a meaningful name to data so we can use it later.

---

# 3. Why Do We Need Variables?

Without variables, we would have to repeat values throughout our program.

```python
print("Ahnaf")
print("Sanjay")
print("Vikas")
```

With a variable, the code becomes easier to read and update:

```python
name = "Pankaj"

print(name)
print(name)
print(name)
```

Variables help us to:

- store information
- reuse values
- make code easier to understand
- update data easily
- perform calculations

### Example

```python
price = 100
tax = 15

total = price + tax

print(total)
```

Output:

```text
115
```

---

# 4. Creating and Assigning Variables

In Python, we create a variable by assigning a value to a name.

```python
name = "Alice"
age = 25
country = "USA"
```

Python does not require us to declare the data type separately. It understands the type from the value we assign.

```python
score = 95
message = "Good job"
```

The assignment operator is the equal sign (`=`).

```python
variable_name = value
```

Do not confuse assignment with mathematical equality:

```python
number = 10
```

This means “store `10` in `number`.”

---

# 5. Variable Naming Rules

Follow these rules when naming variables in Python:

1. A name can contain letters, numbers, and underscores (`_`).
2. A name cannot start with a number.
3. A name cannot contain spaces.
4. A name cannot contain special characters such as `-`, `@`, or `!`.
5. A name is case-sensitive.
6. A name cannot be a Python keyword.

### Case-sensitive names

These are different variables:

```python
name = "Alice"
Name = "Bob"
```

`name` and `Name` are not the same because Python treats uppercase and lowercase letters differently.

### Use descriptive names

```python
student_name = "Rahim"
student_age = 21
```

Descriptive names are better than unclear names:

```python
x = "Rahim"
y = 21
```

For variables with multiple words, Python programmers commonly use **snake_case**.

```python
first_name = "Rahim"
phone_number = "123456789"
```

---

# 6. Valid Variable Names

The following variable names are valid:

```python
name = "Alice"
age2 = 25
_total = 100
first_name = "Bob"
user_email = "user@example.com"
```

---

# 7. Invalid Variable Names

The following names are invalid:

```text
2age = 25          # Cannot start with a number
first-name = "Bob" # Hyphens are not allowed
first name = "Bob" # Spaces are not allowed
user@email = "x"   # Special characters are not allowed
```

These examples are shown as text because they cause syntax errors if run.

### Python keywords cannot be used as variable names

Python keywords already have a special meaning:

```text
class
if
for
while
True
False
None
```

For example, this is invalid:

```python
class = "Python"
```

---

# 8. Multiple Variable Assignment

Python allows us to assign values to multiple variables in one line.

```python
name, age, country = "Alice", 25, "Bangladesh"

print(name)
print(age)
print(country)
```

Each value is assigned to the matching variable from left to right.

### Assign the same value to multiple variables

```python
x = y = z = 0

print(x)
print(y)
print(z)
```

Output:

```text
0
0
0
```

The number of variables and values must match:

```python
first_name, last_name = "Alice", "Smith"
```

---

# 9. Reassigning Variables

A variable can be given a new value after it has already been created.

```python
score = 50
print(score)

score = 80
print(score)
```

Output:

```text
50
80
```

The variable `score` first refers to `50`, then it refers to `80`.

A variable can also change from one data type to another:

```python
value = 10
print(value)

value = "ten"
print(value)
```

This flexibility is one of Python's features, but clear and consistent code is still important.

---

# 10. What Is a Data Type?

A **data type** describes the kind of value stored in a variable.

For example:

- `25` is an integer.
- `3.14` is a floating-point number.
- `"Hello"` is a string.
- `True` is a Boolean value.
- `None` represents no value.

Different data types support different operations.

```python
age = 20
name = "Alice"

print(age + 5)
print(name + " is learning Python")
```

---

# 11. `int` — Integers

An `int` is a whole number without a decimal point.

```python
age = 20
count = 100
negative_number = -5
```

Integers can be positive, negative, or zero.

```python
number = 10

print(number + 5)
print(number - 3)
print(number * 2)
```

---

# 12. `float` — Decimal Numbers

A `float` is a number that contains a decimal point.

```python
price = 99.99
temperature = 36.5
```

A calculation involving a decimal value usually produces a float:

```python
result = 10 / 2
print(result)
```

Output:

```text
5.0
```

---

# 13. `str` — Strings

A `str` is a sequence of characters, usually written inside single or double quotation marks.

```python
name = "Alice"
message = 'Welcome to Python'
```

Strings can contain letters, numbers, spaces, and symbols:

```python
password_hint = "Room 42!"
```

The quotation marks tell Python that the value is text. Therefore, these are different:

```python
number = 10       # int
text_number = "10" # str
```

---

# 14. `bool` — Boolean Values

A `bool` stores one of two values:

- `True`
- `False`

The first letter must be uppercase.

```python
is_logged_in = True
has_permission = False
```

Boolean values are often used to represent conditions.

```python
age = 20
is_adult = age >= 18

print(is_adult)
```

Output:

```text
True
```

---

# 15. `None` / `NoneType`

`None` represents the absence of a value.

It does not mean zero, an empty string, or `False`.

```python
result = None
print(result)
```

Output:

```text
None
```

The data type of `None` is `NoneType`.

```python
value = None
print(type(value))
```

Output:

```text
<class 'NoneType'>
```

`None` is useful when a value is not available yet.

```python
username = None

# Later, a username can be assigned.
username = "Alice"
```

---

# 16. Checking Data Types with `type()`

The `type()` function tells us the data type of a value or variable.

```python
age = 20
price = 9.99
name = "Alice"
is_online = True
nothing = None

print(type(age))
print(type(price))
print(type(name))
print(type(is_online))
print(type(nothing))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

We can also check the type of a direct value:

```python
print(type(100))
print(type(3.14))
print(type("Python"))
print(type(False))
```

---

# 17. Complete Example

```python
student_name = "Rahim"
student_age = 22
student_score = 87.5
has_passed = True
extra_note = None

print(student_name)
print(student_age)
print(student_score)
print(has_passed)
print(extra_note)

print(type(student_name))
print(type(student_age))
print(type(student_score))
print(type(has_passed))
print(type(extra_note))
```

This example uses variables containing five different values:

- `student_name` contains a string.
- `student_age` contains an integer.
- `student_score` contains a float.
- `has_passed` contains a Boolean value.
- `extra_note` contains `None`.

---

# 18. Common Beginner Mistakes

### Using a variable before creating it

```python
print(username)
```

This causes a `NameError` because `username` has not been created yet.

Correct version:

```python
username = "Alice"
print(username)
```

### Forgetting quotation marks around text

```python
name = Alice
```

Python treats `Alice` as another variable name. Use quotation marks for text:

```python
name = "Alice"
```

### Using `=` when comparing values

`=` is used for assignment. Comparisons will be introduced later using comparison operators such as `==`.

```python
number = 10
```

---

# 19. Practice Tasks

Try these exercises:

1. Create variables for your name, age, and favorite color.
2. Print all three variables.
3. Create two number variables and print their sum.
4. Create a Boolean variable called `is_learning_python`.
5. Create a variable with the value `None` and check its type.
6. Reassign a variable from an integer to a string.
7. Use `type()` to check the type of five different values.

### Practice example

```python
name = "Your Name"
age = 18
favorite_color = "blue"
is_learning_python = True

print(name)
print(age)
print(favorite_color)
print(is_learning_python)
```

---

# Summary

- A variable is a name that refers to a value.
- Variables allow us to store and reuse information.
- Variables are created with the assignment operator (`=`).
- Variable names can contain letters, numbers, and underscores.
- Variable names cannot start with numbers or contain spaces.
- Python variable names are case-sensitive.
- Python supports multiple assignment.
- Variables can be reassigned.
- A data type describes the kind of value stored in a variable.
- `int` stores whole numbers.
- `float` stores decimal numbers.
- `str` stores text.
- `bool` stores `True` or `False`.
- `None` represents the absence of a value.
- `type()` checks the data type of a value.

That is enough for today.
