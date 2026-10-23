# Python Revision — Topic 4: Conditional Statements

## 1. What Are Conditional Statements?

Conditional statements allow a program to make decisions based on whether a condition is `True` or `False`.

They help a program choose which block of code to execute.

### Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

**Output:**
```text
You are an adult.
```

Here:
- `age >= 18` is the condition.
- If the condition is `True`, Python executes the indented statement.
- If the condition is `False`, Python skips that block.

### Why Are Conditional Statements Important?

They are used for:
- Validating user input.
- Checking passwords and login credentials.
- Making decisions in applications.
- Handling errors and unexpected values.
- Controlling program behavior.
- Writing security-related scripts that check conditions before performing an action.

---

## 2. The `if` Statement

The `if` statement executes a block of code only when its condition evaluates to `True`.

### Syntax

```python
if condition:
    # Code executes if condition is True
```

### Example 1: Checking a Number

```python
number = 10

if number > 0:
    print("The number is positive.")
```

**Output:**
```text
The number is positive.
```

### Example 2: Checking Login Status

```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")
```

**Output:**
```text
Welcome back!
```

### Example 3: Checking a Password Length

```python
password = "python123"

if len(password) >= 8:
    print("Password length is acceptable.")
```

**Output:**
```text
Password length is acceptable.
```

Note: This checks only the password's length. It does not prove that the password is secure.

### Important Rules

1. Write a colon (`:`) after the condition.
2. Indent the code inside the `if` block.
3. The condition must evaluate to a Boolean result or another value Python can interpret as truthy or falsy.

---

## 3. The `if-else` Statement

Use `else` when you want one block to run if the condition is `True` and another block to run if it is `False`.

### Syntax

```python
if condition:
    # Runs when condition is True
else:
    # Runs when condition is False
```

### Example 1: Even or Odd

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Output:**
```text
Odd number
```

The modulo operator (`%`) returns the remainder after division. An even integer has a remainder of `0` when divided by `2`.

### Example 2: Age Check

```python
age = 16

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

**Output:**
```text
Not eligible by age
```

### Example 3: Checking Whether a Number Is Zero

```python
number = 0

if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

**Output:**
```text
Zero or negative
```

Notice that the `else` block includes zero as well as negative numbers. If you need to distinguish all three cases, use `if-elif-else`.

---

## 4. The `if-elif-else` Statement

Use `elif` (short for "else if") when you need to check multiple conditions.

Python checks the conditions from top to bottom. The first condition that evaluates to `True` has its block executed. The remaining conditions are skipped.

### Syntax

```python
if condition_1:
    # First block
elif condition_2:
    # Second block
elif condition_3:
    # Third block
else:
    # Default block
```

You can use as many `elif` branches as necessary. The final `else` is optional.

### Example 1: Positive, Negative, or Zero

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Output:**
```text
Negative
```

### Example 2: Grading System

```python
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

**Output:**
```text
Grade A
```

**Why does the order matter?**

Suppose you check `marks >= 60` first. A score of `85` satisfies that condition, so Python executes that block and skips the later branches.

For ranges such as grades, put the highest threshold first.

### Example 3: Time-Based Greeting

```python
hour = 14

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")
```

**Output:**
```text
Good afternoon
```

The conditions are evaluated in order. Since `14 < 12` is false but `14 < 17` is true, Python prints `"Good afternoon"`.

---

## 5. Nested Conditional Statements

A nested conditional is a conditional statement inside another conditional statement.

Use nesting when a decision depends on an earlier decision.

### Example 1: Login Validation

```python
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown username")
```

**Output:**
```text
Login successful
```

The password condition is checked only if the username condition is true.

Important: This is a learning example, not a secure authentication system. Real applications should use properly stored password hashes and established authentication practices.

### Example 2: Checking Age and Permission

```python
age = 20
has_permission = True

if age >= 18:
    if has_permission:
        print("Access granted")
    else:
        print("Permission required")
else:
    print("Age requirement not met")
```

**Output:**
```text
Access granted
```

### Nested Conditions vs. Combined Conditions

The previous example can also be written using a logical operator:

```python
age = 20
has_permission = True

if age >= 18 and has_permission:
    print("Access granted")
else:
    print("Access denied")
```

This is shorter when both conditions must be true.

**When should you use nesting?**
- Use nested conditions when the second decision logically depends on the first.
- Use combined conditions when the checks are simple and belong together.
- Avoid unnecessary nesting because deeply indented code can become difficult to read.

---

## 6. Truthy and Falsy Values

Python does not require every condition to be explicitly written as `True` or `False`.

It can interpret other values as truthy or falsy.

### Falsy Values

Common falsy values include:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

These values evaluate to false in a Boolean context.

### Truthy Values

Most other values are truthy, including:

```python
True
1
-1
3.14
"hello"
"0"
[1, 2, 3]
{"name": "Alex"}
```

Notice that `"0"` is a non-empty string, so it is truthy. The integer `0`, however, is falsy.

### Example 1: Checking an Empty String

```python
username = ""

if username:
    print("Username provided")
else:
    print("Username is empty")
```

**Output:**
```text
Username is empty
```

### Example 2: Checking a List

```python
items = [10, 20, 30]

if items:
    print("The list contains items")
else:
    print("The list is empty")
```

**Output:**
```text
The list contains items
```

An empty list is falsy, while a non-empty list is truthy.

### Example 3: Checking User Input

```python
name = input("Enter your name: ").strip()

if name:
    print(f"Hello, {name}!")
else:
    print("Name cannot be empty.")
```

The `.strip()` method removes leading and trailing whitespace. This prevents input containing only spaces from being accepted as a name.

### Using `bool()`

You can explicitly convert a value to its Boolean equivalent using `bool()`.

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))
```

**Output:**
```text
False
True
False
True
False
True
```

### Important Warning

Truthy does not mean valid.

For example:

```python
age = -10

if age:
    print("Age provided")
```

**Output:**
```text
Age provided
```

The number `-10` is truthy, but a negative age is not valid for most age-related applications.

Use explicit validation when you need to check whether a value meets particular requirements.

---

## 7. Conditional Expressions (Ternary Expressions)

A conditional expression allows you to choose between two values in one line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example 1: Even or Odd

```python
number = 8

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

**Output:**
```text
Even
```

### Example 2: Adult or Minor

```python
age = 17

status = "Adult" if age >= 18 else "Minor"

print(status)
```

**Output:**
```text
Minor
```

### Example 3: Finding the Larger Number

```python
a = 10
b = 20

larger = a if a > b else b

print(larger)
```

**Output:**
```text
20
```

### Traditional `if-else` vs. Conditional Expression

Traditional version:

```python
number = 5

if number > 0:
    result = "Positive"
else:
    result = "Not positive"

print(result)
```

Conditional expression:

```python
number = 5

result = "Positive" if number > 0 else "Not positive"

print(result)
```

Both produce the same result.

**Best practice:** Use conditional expressions for short, simple choices. Use regular `if-elif-else` statements when you have several branches or more complicated logic.

---

## 8. Combining Logical Conditions

Python provides three main logical operators:

- `and`
- `or`
- `not`

They allow you to combine or reverse conditions.

### 8.1 The `and` Operator

`and` evaluates to a truthy result only when both operands are truthy.

For ordinary Boolean conditions:

| Condition A | Condition B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

Example:

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")
```

**Output:**
```text
Access granted
```

Both requirements must be satisfied.

### 8.2 The `or` Operator

`or` evaluates to a truthy result when at least one operand is truthy.

| Condition A | Condition B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

Example:

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("It's a weekday")
```

**Output:**
```text
It's the weekend
```

### 8.3 The `not` Operator

`not` reverses the truth value of an expression.

```python
is_blocked = False

if not is_blocked:
    print("User is not blocked")
```

**Output:**
```text
User is not blocked
```

### 8.4 Combining Multiple Conditions

```python
age = 25
has_account = True
is_blocked = False

if age >= 18 and has_account and not is_blocked:
    print("User can continue")
else:
    print("User cannot continue")
```

**Output:**
```text
User can continue
```

### 8.5 Chained Comparisons

Python lets you compare a value against a range directly.

```python
age = 25

if 18 <= age <= 60:
    print("Age is within the range")
```

**Output:**
```text
Age is within the range
```

This is equivalent to:

```python
if age >= 18 and age <= 60:
    print("Age is within the range")
```

Chained comparisons are often easier to read.

### 8.6 Short-Circuit Evaluation

Python sometimes skips evaluating the second operand of a logical expression because the result is already determined.

With `and`, if the first operand is falsy, Python does not need to evaluate the second operand.

With `or`, if the first operand is truthy, Python does not need to evaluate the second operand.

Example:

```python
username = ""

if username and len(username) >= 3:
    print("Valid username")
else:
    print("Invalid username")
```

**Output:**
```text
Invalid username
```

Because `username` is an empty string, the `and` expression stops there. Python does not need to evaluate the length condition.

Short-circuit evaluation can also prevent certain errors:

```python
items = []

if items and items[0] == "admin":
    print("Admin found")
else:
    print("No admin found")
```

**Output:**
```text
No admin found
```

The expression `items[0]` is not evaluated because the list is empty and therefore falsy.

### Important: Logical Operators Can Return Values

In Python, `and` and `or` do not always return the Boolean values `True` or `False`. They return one of their operands.

```python
print("" or "Default")
print("Python" and "Programming")
print(0 and 100)
```

**Output:**
```text
Default
Programming
0
```

This behavior is useful for understanding Python, although explicit conditions are often clearer for beginners.

---

## 9. Input Validation with Conditions

Input validation means checking whether user-provided data meets the requirements of a program before using it.

This is important because users can enter empty values, invalid numbers, out-of-range values, or unexpected input.

The `input()` function always returns a string. Convert the input when you need a number.

### 9.1 Checking Empty Input

```python
username = input("Enter username: ").strip()

if not username:
    print("Username cannot be empty")
else:
    print(f"Welcome, {username}")
```

**Example input:**
```text
Enter username:
```

**Output:**
```text
Username cannot be empty
```

### 9.2 Validating Numeric Input

A common beginner mistake is trying to compare a string with an integer.

Incorrect:

```python
age = input("Enter your age: ")

if age >= 18:
    print("Adult")
```

This raises a `TypeError` because `age` is a string and `18` is an integer.

Correct approach:

```python
age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)

    if age >= 18:
        print("Adult")
    else:
        print("Minor")
else:
    print("Please enter a valid whole number")
```

**Important:** `.isdigit()` is suitable for checking many strings of non-negative digit characters. It does not accept negative numbers or decimal values such as `-5` or `18.5`. For more general numeric validation, use `try-except`.

### 9.3 Validating Input with `try-except`

```python
age_text = input("Enter your age: ").strip()

try:
    age = int(age_text)

    if age < 0:
        print("Age cannot be negative")
    elif age > 120:
        print("Please enter a realistic age")
    else:
        print(f"Your age is {age}")

except ValueError:
    print("Please enter a valid whole number")
```

This approach handles non-integer input without crashing the program.

**Example inputs and outcomes:**

| Input | Outcome |
|---|---|
| `25` | Your age is 25 |
| `-5` | Age cannot be negative |
| `150` | Please enter a realistic age |
| `hello` | Please enter a valid whole number |
| `18.5` | Please enter a valid whole number |

The upper limit of `120` is an example of an application rule, not a universal definition of a valid age.

### 9.4 Validating a Percentage

```python
marks = float(input("Enter marks (0-100): "))

if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Marks must be between 0 and 100")
```

This validates the range but does not handle non-numeric input. To make it more robust:

```python
marks_text = input("Enter marks (0-100): ").strip()

try:
    marks = float(marks_text)

    if 0 <= marks <= 100:
        print("Valid marks")
    else:
        print("Marks must be between 0 and 100")

except ValueError:
    print("Please enter a numeric value")
```

### 9.5 Validating a Password's Length

```python
password = input("Enter password: ")

if not password:
    print("Password cannot be empty")
elif len(password) < 8:
    print("Password must contain at least 8 characters")
else:
    print("Password length is acceptable")
```

This checks only whether the password is empty and whether it meets a minimum length. A production application needs stronger authentication and secure password handling.

### 9.6 Validating a Menu Choice

```python
print("1. View profile")
print("2. Update profile")
print("3. Exit")

choice = input("Choose an option: ").strip()

if choice == "1":
    print("Opening profile...")
elif choice == "2":
    print("Opening profile editor...")
elif choice == "3":
    print("Exiting...")
else:
    print("Invalid choice")
```

Notice that the menu choice is compared with strings such as `"1"`, not integers such as `1`, because `input()` returns a string.

---

## 10. Common Mistakes to Avoid

### Mistake 1: Forgetting the Colon

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

### Mistake 2: Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

Python uses indentation to define code blocks.

### Mistake 3: Using `=` Instead of `==`

Incorrect:

```python
if age = 18:
    print("Age is 18")
```

Correct:

```python
if age == 18:
    print("Age is 18")
```

- `=` assigns a value.
- `==` compares two values.

### Mistake 4: Using `is` for Value Equality

Incorrect for ordinary value comparisons:

```python
name = "Alex"

if name is "Alex":
    print("Matched")
```

Correct:

```python
if name == "Alex":
    print("Matched")
```

Use `==` to compare values. Use `is` when checking object identity, especially for singleton values such as `None`.

```python
result = None

if result is None:
    print("No result")
```

### Mistake 5: Incorrect Condition Ordering

Incorrect:

```python
marks = 95

if marks >= 60:
    print("Grade C")
elif marks >= 90:
    print("Grade A")
```

**Output:**
```text
Grade C
```

The first condition already matches, so the second is never checked.

Correct:

```python
marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade C")
```

**Output:**
```text
Grade A
```

### Mistake 6: Forgetting That `input()` Returns a String

Incorrect:

```python
age = input("Enter age: ")

if age >= 18:
    print("Adult")
```

Correct:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
```

For real user-facing programs, use `try-except` to handle invalid numeric input.

### Mistake 7: Writing a Condition That Is Always True

Incorrect:

```python
day = "Monday"

if day == "Saturday" or "Sunday":
    print("Weekend")
```

This prints `"Weekend"` because `"Sunday"` is a non-empty, truthy string.

Correct:

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

An even clearer option is:

```python
if day in ("Saturday", "Sunday"):
    print("Weekend")
```

### Mistake 8: Using Separate `if` Statements When You Need One Branch

```python
number = 5

if number > 0:
    print("Positive")

if number >= 0:
    print("Non-negative")
```

**Output:**
```text
Positive
Non-negative
```

Both `if` statements are evaluated independently.

If you want exactly one branch to run, use `if-elif-else`:

```python
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
```

---

## 11. Practical Mini Projects

### Project 1: Simple Login Check

```python
username = input("Enter username: ").strip()
password = input("Enter password: ")

if not username or not password:
    print("Username and password are required")
elif username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid username or password")
```

This is only a conditional-logic exercise. It uses hardcoded credentials and must not be used as a real authentication system.

### Project 2: Number Classifier

```python
number_text = input("Enter an integer: ").strip()

try:
    number = int(number_text)

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print("Please enter a valid integer")
```

Example input: `-7`

**Output:**
```text
Negative
Odd
```

### Project 3: Simple Calculator

```python
try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", a + b)
    elif operator == "-":
        print("Result:", a - b)
    elif operator == "*":
        print("Result:", a * b)
    elif operator == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")

except ValueError:
    print("Please enter valid numbers")
```

This project practices:
- `if-elif-else`
- Nested conditions
- Comparison operators
- Input validation
- Exception handling

### Project 4: Access Eligibility Checker

```python
age_text = input("Enter age: ").strip()
has_id_text = input("Do you have an ID? (yes/no): ").strip().lower()

try:
    age = int(age_text)

    if age < 0:
        print("Invalid age")
    elif has_id_text not in ("yes", "no"):
        print("Please answer yes or no")
    elif age >= 18 and has_id_text == "yes":
        print("Access granted")
    else:
        print("Access denied")

except ValueError:
    print("Enter a valid whole number for age")
```

This checks the age input, normalizes the ID answer, and requires both conditions to be satisfied.

---

## 12. Practice Exercises

Try solving these without looking at the examples above. Use the terminal and write the code yourself.

### Beginner Level

1. Write a program to check whether a number is positive or negative.
2. Write a program to check whether a number is even or odd.
3. Ask the user for their age and print whether they are an adult or a minor.
4. Ask the user for a number and determine whether it is zero, positive, or negative.
5. Ask for a username and reject empty input.

### Intermediate Level

6. Create a grading system using marks from 0 to 100.
7. Check whether a number is divisible by both 3 and 5.
8. Ask for a username and password, then check whether both match predefined values.
9. Write a program that finds the largest of three numbers.
10. Ask for a year and determine whether it is a leap year.

### Advanced Practice

11. Create a calculator that supports `+`, `-`, `*`, and `/`, including division-by-zero validation.
12. Validate age input so that letters, negative values, and unrealistic ages are handled.
13. Create a simple menu-driven program with three choices.
14. Write a program that checks whether a username has at least three characters and is not empty.
15. Create a program that checks multiple requirements before allowing a simulated action.

For exercise 10, remember the leap-year rule: a year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.

---

## 13. Quick Revision Questions and Answers

**Q1. What is a conditional statement?**

A statement that allows a program to execute different code depending on a condition.

**Q2. What is the difference between `if` and `elif`?**

`if` begins a conditional chain. `elif` checks another condition if all preceding conditions were false.

**Q3. Is `else` compulsory?**

No. It is optional.

**Q4. What is a nested condition?**

A conditional statement inside another conditional statement.

**Q5. What is a falsy value?**

A value that evaluates to false in a Boolean context, such as `0`, `None`, `False`, `""`, and `[]`.

**Q6. Is the string `"0"` falsy?**

No. It is truthy because it is a non-empty string.

**Q7. What is a conditional expression?**

A one-line expression that chooses one of two values based on a condition.

Example:

```python
result = "Pass" if marks >= 40 else "Fail"
```

**Q8. What is the difference between `and` and `or`?**

`and` requires both operands to be truthy to produce a truthy result. `or` produces a truthy result if at least one operand is truthy.

**Q9. Why is input validation important?**

It prevents invalid or unexpected data from being used without appropriate checks.

**Q10. What does `input()` return?**

A string.

**Q11. What is short-circuit evaluation?**

Python stops evaluating a logical expression when the result is already determined.

**Q12. What is the difference between `=` and `==`?**

`=` assigns a value; `==` compares values.

---

## 14. Conditional Statements Cheat Sheet

| Feature | Example | Purpose |
|---|---|---|
| `if` | `if age >= 18:` | Check one condition |
| `else` | `else:` | Handle the alternative |
| `elif` | `elif marks >= 80:` | Check another condition |
| Nested condition | `if a:` followed by `if b:` | Make a dependent decision |
| `and` | `age >= 18 and has_id` | Require both conditions |
| `or` | `is_admin or is_owner` | Accept either condition |
| `not` | `not is_blocked` | Reverse truth value |
| Membership | `choice in ("1", "2")` | Check membership |
| Conditional expression | `"Pass" if marks >= 40 else "Fail"` | Choose one of two values |
| Truthiness | `if items:` | Check whether a value is truthy |
| Input validation | `try: age = int(text)` | Handle invalid numeric input |

### Final Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Write `if`, `elif`, and `else` statements without syntax errors.
- [ ] Explain nested conditions and when to avoid unnecessary nesting.
- [ ] Identify common truthy and falsy values.
- [ ] Write simple conditional expressions.
- [ ] Combine conditions using `and`, `or`, and `not`.
- [ ] Explain short-circuit evaluation.
- [ ] Validate user input and handle invalid numbers.
- [ ] Build a basic calculator using conditional statements.

**Recommended practice:** Spend about 45–60 minutes writing the examples and solving at least five exercises from memory. Focus on understanding the conditions rather than memorizing the code.
