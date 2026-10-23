# Phase 1: Python Fundamentals Revision
## Topic 3: Operators

## 1. Introduction to Operators

An **operator** is a symbol or keyword used to perform an operation on one or more values.

The values on which operators work are called **operands**.

Example:

```python
a = 10
b = 5

result = a + b

print(result)
```

Output:

```text
15
```

Here:
- `+` is the operator.
- `a` and `b` are operands.
- `result` stores the result of the operation.

Python provides several categories of operators:

1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Assignment operators
5. Membership operators
6. Identity operators
7. Bitwise operators

---

## 2. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

Assume:

```python
a = 10
b = 3
```

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | True division | `a / b` | `3.333...` |
| `//` | Floor division | `a // b` | `3` |
| `%` | Modulus | `a % b` | `1` |
| `**` | Exponentiation | `a ** b` | `1000` |

### 2.1 Addition (`+`)

Adds two numbers.

```python
x = 10
y = 20

print(x + y)
```

Output:

```text
30
```

The `+` operator can also concatenate strings.

```python
print("Hello " + "Python")
```

Output:

```text
Hello Python
```

### 2.2 Subtraction (`-`)

Subtracts one number from another.

```python
print(20 - 8)
```

Output:

```text
12
```

### 2.3 Multiplication (`*`)

Multiplies two numbers.

```python
print(6 * 4)
```

Output:

```text
24
```

It can also repeat sequences.

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

### 2.4 True Division (`/`)

Divides two numbers and returns a floating-point result.

```python
print(10 / 2)
print(10 / 3)
```

Output:

```text
5.0
3.3333333333333335
```

### 2.5 Floor Division (`//`)

Divides two numbers and rounds the result down to the nearest integer when both operands are integers.

```python
print(10 // 3)
print(7 // 2)
```

Output:

```text
3
3
```

**Important:** Floor division rounds toward negative infinity, not toward zero.

```python
print(-7 // 2)
```

Output:

```text
-4
```

### 2.6 Modulus (`%`)

Returns the remainder after division.

```python
print(10 % 3)
print(12 % 4)
```

Output:

```text
1
0
```

A common use is checking whether a number is even or odd.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

### 2.7 Exponentiation (`**`)

Raises a number to a power.

```python
print(2 ** 3)
print(5 ** 2)
```

Output:

```text
8
25
```

### Important points

- Division by zero raises `ZeroDivisionError`.
- `/` and `//` have different meanings.
- `%` is useful for remainders and divisibility checks.
- `**` performs exponentiation, not bitwise XOR.

---

## 3. Comparison Operators

Comparison operators compare values and produce a Boolean result: `True` or `False`.

Assume:

```python
a = 10
b = 5
```

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `True` |
| `<` | Less than | `a < b` | `False` |
| `>=` | Greater than or equal to | `a >= b` | `True` |
| `<=` | Less than or equal to | `a <= b` | `False` |

### Example

```python
age = 20

print(age >= 18)
print(age == 20)
print(age != 20)
```

Output:

```text
True
True
False
```

### Chained comparisons

Python allows multiple comparisons in one expression.

```python
age = 22

print(18 <= age <= 60)
```

Output:

```text
True
```

This is equivalent to:

```python
print(18 <= age and age <= 60)
```

### Comparing strings

Strings are compared lexicographically using their character values.

```python
print("apple" == "apple")
print("apple" < "banana")
```

Output:

```text
True
True
```

String comparisons are case-sensitive.

```python
print("Python" == "python")
```

Output:

```text
False
```

### Important distinction

`=` assigns a value, while `==` compares values.

```python
x = 10       # Assignment
print(x == 10)  # Comparison
```

---

## 4. Logical Operators

Logical operators combine or reverse truth values.

Python has three main logical operators:

- `and`
- `or`
- `not`

### 4.1 Logical AND (`and`)

Returns a truthy result only when both operands are truthy. With Boolean operands, it is `True` only when both are `True`.

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

Example:

```python
age = 22
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

Both conditions are true.

### 4.2 Logical OR (`or`)

Returns a truthy result when at least one operand is truthy.

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

Example:

```python
is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
```

Output:

```text
True
```

### 4.3 Logical NOT (`not`)

Reverses the truth value of an expression.

```python
is_logged_in = False

print(not is_logged_in)
```

Output:

```text
True
```

### Truthy and falsy values

Python evaluates values in Boolean contexts.

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

if not name:
    print("Name is empty")
```

Output:

```text
Name is empty
```

### Short-circuit evaluation

Python may skip evaluating the second operand of `and` or `or`.

```python
x = 0

print(x != 0 and 10 / x > 1)
```

Output:

```text
False
```

The division is not evaluated because `x != 0` is false.

Similarly:

```python
print(True or 10 / 0)
```

Output:

```text
True
```

The second operand is skipped because the first operand is already truthy.

**Important:** `and` and `or` can return one of their operands rather than always returning a Boolean.

```python
print(0 or 5)
print("Python" and "Programming")
```

Output:

```text
5
Programming
```

This behavior is useful in some expressions, but do not confuse it with always returning `True` or `False`.

---

## 5. Assignment Operators

Assignment operators assign values to variables. Some also perform an operation and assign the result back to a variable.

### 5.1 Basic assignment (`=`)

```python
x = 10
name = "Python"
```

### 5.2 Compound assignment operators

| Operator | Equivalent form |
|---|---|
| `+=` | `x = x + value` |
| `-=` | `x = x - value` |
| `*=` | `x = x * value` |
| `/=` | `x = x / value` |
| `//=` | `x = x // value` |
| `%=` | `x = x % value` |
| `**=` | `x = x ** value` |
| `&=` | `x = x & value` |
| `\|=` | `x = x \| value` |
| `^=` | `x = x ^ value` |
| `>>=` | `x = x >> value` |
| `<<=` | `x = x << value` |

The bitwise assignment operators are covered later in these notes.

### Example: `+=`

```python
x = 10
x += 5

print(x)
```

Output:

```text
15
```

### Example: `*=`

```python
x = 4
x *= 3

print(x)
```

Output:

```text
12
```

### Example: `**=`

```python
x = 2
x **= 4

print(x)
```

Output:

```text
16
```

### Assignment with lists

Compound assignment can behave differently for mutable objects such as lists.

```python
a = [1, 2]
b = a

a += [3]

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3]
```

For lists, `+=` extends the existing list in place, so both names still refer to the updated object.

---

## 6. Membership Operators (`in`, `not in`)

Membership operators check whether a value is present in a sequence or collection.

There are two membership operators:

- `in`
- `not in`

### 6.1 The `in` operator

Returns `True` if the value is present.

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

### 6.2 The `not in` operator

Returns `True` if the value is absent.

```python
languages = ["Python", "Java", "C++"]

print("JavaScript" not in languages)
```

Output:

```text
True
```

### Membership in strings

For strings, membership checks whether a substring exists.

```python
text = "Learn Python"

print("Python" in text)
print("Java" in text)
```

Output:

```text
True
False
```

String membership is case-sensitive.

```python
print("python" in "Python")
```

Output:

```text
False
```

### Membership in dictionaries

For dictionaries, `in` checks keys, not values.

```python
student = {
    "name": "Pulok",
    "age": 22
}

print("name" in student)
print("Pulok" in student)
print("Pulok" in student.values())
```

Output:

```text
True
False
True
```

### Practical example

```python
allowed_users = ["admin", "analyst", "student"]

username = input("Enter username: ")

if username in allowed_users:
    print("Access allowed")
else:
    print("Access denied")
```

This demonstrates a basic membership check. Real authentication and authorization systems require more than checking a username against a list.

---

## 7. Identity Operators (`is`, `is not`)

Identity operators check whether two references point to the same object.

The two identity operators are:

- `is`
- `is not`

### 7.1 The `is` operator

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Both names refer to the same list object.

### 7.2 The `is not` operator

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

Output:

```text
True
```

The lists contain equal values but are different objects.

### Identity vs. equality

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

- `==` compares equality.
- `is` compares identity.

### Recommended use: checking `None`

```python
result = None

if result is None:
    print("No result available")
```

Use `is None` and `is not None` for `None` checks.

**Important:** Do not use `is` to compare ordinary numeric or string values. Python may reuse some objects as an implementation optimization. Use `==` when you want to compare values.

---

## 8. Operator Precedence

Operator precedence determines which operations are performed first when an expression contains multiple operators.

Example:

```python
result = 2 + 3 * 4

print(result)
```

Output:

```text
14
```

Multiplication is performed before addition.

### Common operator precedence, from higher to lower

This is a simplified reference for commonly used operators.

| Precedence | Operators or expressions |
|---|---|
| Highest | Parentheses and grouping: `( )` |
| High | Exponentiation: `**` |
| High | Unary operators: `+x`, `-x`, `~x` |
| High | Multiplication, division, floor division, modulus: `*`, `/`, `//`, `%` |
| Medium | Addition and subtraction: `+`, `-` |
| Medium | Bit shifts: `<<`, `>>` |
| Medium | Bitwise AND: `&` |
| Medium | Bitwise XOR: `^` |
| Medium | Bitwise OR: `\|` |
| Lower | Comparisons, membership, identity: `<`, `==`, `in`, `is`, etc. |
| Lower | Logical NOT: `not` |
| Lower | Logical AND: `and` |
| Lower | Logical OR: `or` |
| Lowest | Conditional expression: `x if condition else y` |

This table omits some operators and special cases. Consult the official Python precedence table when precision matters.

### Example 1: multiplication before addition

```python
print(10 + 2 * 3)
```

Output:

```text
16
```

### Example 2: using parentheses

```python
print((10 + 2) * 3)
```

Output:

```text
36
```

Parentheses change the order of evaluation.

### Example 3: exponentiation

```python
print(2 ** 3 ** 2)
```

Output:

```text
512
```

Exponentiation is evaluated from right to left, so this is equivalent to:

```python
print(2 ** (3 ** 2))
```

### Example 4: comparison and logical operators

```python
age = 22

print(age > 18 and age < 30)
```

Output:

```text
True
```

Comparisons are evaluated before the logical `and`.

### Example 5: `not` and comparisons

```python
print(not 5 == 5)
```

Output:

```text
False
```

This is interpreted as:

```python
print(not (5 == 5))
```

### Best practice

Use parentheses when an expression may be confusing.

Instead of relying on memory:

```python
result = a + b * c
```

You can make the intended order explicit:

```python
result = a + (b * c)
```

---

## 9. Bitwise Operators (Basic Understanding)

Bitwise operators work on the individual bits of integers.

Computers represent integers using binary digits: `0` and `1`.

For example:

```text
Decimal 5 = Binary 0101
Decimal 3 = Binary 0011
```

Python bitwise operators perform operations on the binary representation of integers.

### 9.1 Bitwise AND (`&`)

A bit is `1` only when both corresponding bits are `1`.

```text
  0101  (5)
& 0011  (3)
------
  0001  (1)
```

Python:

```python
print(5 & 3)
```

Output:

```text
1
```

### 9.2 Bitwise OR (`|`)

A bit is `1` when at least one corresponding bit is `1`.

```text
  0101  (5)
| 0011  (3)
------
  0111  (7)
```

Python:

```python
print(5 | 3)
```

Output:

```text
7
```

### 9.3 Bitwise XOR (`^`)

A bit is `1` when the corresponding bits are different.

```text
  0101  (5)
^ 0011  (3)
------
  0110  (6)
```

Python:

```python
print(5 ^ 3)
```

Output:

```text
6
```

Remember: `^` means bitwise XOR, not exponentiation. Use `**` for powers.

### 9.4 Bitwise NOT (`~`)

Bitwise NOT inverts the bits according to Python's integer model.

```python
print(~5)
```

Output:

```text
-6
```

For Python integers:

```python
~x == -x - 1
```

So:

```text
~5 = -5 - 1 = -6
```

### 9.5 Left shift (`<<`)

Shifts the bits to the left.

```python
print(5 << 1)
```

Output:

```text
10
```

For positive integers, shifting left by one place is equivalent to multiplying by two.

```text
0101 (5) << 1 = 1010 (10)
```

### 9.6 Right shift (`>>`)

Shifts the bits to the right.

```python
print(8 >> 1)
```

Output:

```text
4
```

For non-negative integers, shifting right by one place is equivalent to floor-dividing by two.

```text
1000 (8) >> 1 = 0100 (4)
```

### Bitwise operators summary

| Operator | Name | Example | Result |
|---|---|---|---|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `8 >> 1` | `4` |

### Where are bitwise operators useful?

- Working with binary data.
- Setting, clearing, or checking bit flags.
- Low-level programming.
- Some networking and security-related tasks.
- Certain performance-sensitive algorithms.

For now, focus on understanding the binary examples and knowing what each operator does.

---

## 10. Practical Exercises

Try each exercise in a Python file or interactive shell before checking the answers.

### Exercise 1: Arithmetic operators

Given:

```python
a = 17
b = 4
```

Print the results of addition, subtraction, multiplication, true division, floor division, modulus, and exponentiation.

### Exercise 2: Comparisons

Ask the user for their age and print whether they are at least 18 years old.

### Exercise 3: Logical operators

Create two variables:

```python
has_account = True
is_verified = False
```

Print the result of `has_account and is_verified`, `has_account or is_verified`, and `not is_verified`.

### Exercise 4: Assignment operators

Start with `number = 10`. Use `+=`, `*=`, and `-=` in sequence. Print the value after each operation.

### Exercise 5: Membership operators

Check whether `"Python"` is present in this list:

```python
languages = ["C", "Java", "Python", "JavaScript"]
```

Then check whether `"Rust"` is absent.

### Exercise 6: Identity operators

Create two separate lists with identical contents. Compare them using `==` and `is`. Then assign one list to another variable and compare again.

### Exercise 7: Operator precedence

Predict the output before running:

```python
print(5 + 2 * 3 ** 2)
print((5 + 2) * 3 ** 2)
print(10 > 5 and 3 < 1)
```

### Exercise 8: Bitwise operators

Predict the output:

```python
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(4 << 1)
print(8 >> 1)
```

### Exercise 9: Even or odd

Write a program that accepts an integer and uses the modulus operator to determine whether it is even or odd.

### Exercise 10: Mini-project — Simple calculator

Write a calculator that:

1. Accepts two numbers.
2. Accepts an arithmetic operator such as `+`, `-`, `*`, or `/`.
3. Performs the selected operation.
4. Handles division by zero.
5. Displays the result.

---

## 11. Quick Revision Questions

1. What is an operator?
2. What is the difference between `/` and `//`?
3. What does the modulus operator do?
4. What is the difference between `=` and `==`?
5. Which operators compare values?
6. What is the difference between `and` and `or`?
7. What is short-circuit evaluation?
8. What are compound assignment operators?
9. What does the membership operator `in` do?
10. What is the difference between `is` and `==`?
11. What is operator precedence?
12. Why are parentheses useful in complex expressions?
13. What does the bitwise AND operator do?
14. What is the difference between `|` and `^`?
15. What is the difference between `**` and `^`?
16. Why does `~5` return `-6` in Python?
17. What do the left-shift and right-shift operators do?
18. How can `%` be used to check whether a number is even?

### Short Answers

1. An operator performs an operation on one or more operands.
2. `/` performs true division; `//` performs floor division.
3. `%` returns the remainder from division.
4. `=` assigns a value; `==` compares values.
5. `==`, `!=`, `<`, `>`, `<=`, and `>=`.
6. `and` requires both operands to be truthy; `or` requires at least one to be truthy.
7. Python skips evaluating the second operand when the first operand determines the result.
8. Operators such as `+=`, `-=`, and `*=` combine an operation with assignment.
9. It checks whether a value is present in a collection or sequence.
10. `is` checks object identity; `==` checks equality.
11. It determines the order in which operators are evaluated.
12. Parentheses make the intended evaluation order explicit.
13. A result bit is `1` only when both corresponding bits are `1`.
14. OR returns `1` when either bit is `1`; XOR returns `1` when the bits differ.
15. `**` performs exponentiation; `^` performs bitwise XOR.
16. Python's integer bitwise NOT satisfies `~x == -x - 1`.
17. They shift integer bits to the left or right.
18. An integer is even if `number % 2 == 0`.

---

## 12. Essential Operators Cheat Sheet

| Category | Operators |
|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical | `and`, `or`, `not` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` |

---

## Final Revision Advice

For this topic, prioritize practical understanding over memorizing every operator.

Make sure you can confidently explain and use:

1. Arithmetic operators, especially `/`, `//`, and `%`.
2. Comparisons combined with logical operators.
3. Assignment operators.
4. Membership checks in lists, strings, and dictionaries.
5. Identity versus equality.
6. Operator precedence and parentheses.
7. Basic bitwise operations on integers.

After practising these concepts, move to the next topic in your Python fundamentals revision roadmap.
