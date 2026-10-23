# Python Revision — Topic 5: Loops

## 1. What Are Loops in Python?

A loop is a programming structure that executes a block of code repeatedly.

Instead of writing the same code many times, you can use a loop to repeat an operation automatically.

### Without a loop

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

### Using a loop

```python
for i in range(5):
    print("Hello")
```

**Output:**

```text
Hello
Hello
Hello
Hello
Hello
```

Loops are useful for:

- Processing lists, tuples, sets, and dictionaries.
- Repeating calculations.
- Reading files line by line.
- Validating user input.
- Automating repetitive tasks.
- Processing network or security-related data.
- Running repeated checks until a condition is met.

Python provides two primary loop statements:

1. `for` loops
2. `while` loops

---

## 2. The `for` Loop

A `for` loop iterates over the items of an iterable, such as a string, list, tuple, set, dictionary, or range.

### Syntax

```python
for variable in iterable:
    # Code to execute for each item
```

The loop takes one item at a time from the iterable and assigns it to the loop variable.

### Example 1: Loop Through a List

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

**Output:**

```text
Python
Java
C++
```

### Example 2: Loop Through a String

```python
word = "Python"

for character in word:
    print(character)
```

**Output:**

```text
P
y
t
h
o
n
```

A string is iterable, so Python visits each character in order.

### Example 3: Loop Through a Tuple

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

**Output:**

```text
10
20
30
```

### Example 4: Calculate the Sum of Numbers

```python
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print("Total:", total)
```

**Output:**

```text
Total: 100
```

Here, `total += number` adds each number to the running total.

### Example 5: Count Matching Items

```python
numbers = [2, 5, 8, 11, 14, 17]
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)
```

**Output:**

```text
Even numbers: 3
```

This example combines a `for` loop with an `if` statement.

---

## 3. The `range()` Function

The `range()` function generates a sequence of integers. It is commonly used when you want to repeat an operation a specific number of times.

### 3.1 `range(stop)`

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

`range(5)` starts at `0` and stops before `5`.

Remember: the stop value is excluded.

### 3.2 `range(start, stop)`

```python
for i in range(2, 7):
    print(i)
```

**Output:**

```text
2
3
4
5
6
```

The sequence starts at `2` and stops before `7`.

### 3.3 `range(start, stop, step)`

The third argument determines how much the number changes each time.

```python
for i in range(0, 11, 2):
    print(i)
```

**Output:**

```text
0
2
4
6
8
10
```

The step is `2`, so Python generates every second integer.

### 3.4 Counting Backward

Use a negative step to count backward.

```python
for i in range(5, 0, -1):
    print(i)
```

**Output:**

```text
5
4
3
2
1
```

Notice that `0` is excluded.

### 3.5 Generating Multiplication Tables

```python
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

**Output:**

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Important Rules for `range()`

- `range(stop)` starts at `0`.
- `range(start, stop)` excludes `stop`.
- `range(start, stop, step)` uses the specified step.
- The step cannot be `0`.
- A negative step is useful for descending sequences.
- `range()` produces a range object rather than a list.

If you need a list of the generated values, use:

```python
numbers = list(range(1, 6))
print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

---

## 4. The `while` Loop

A `while` loop repeats a block of code as long as its condition remains true.

Unlike a `for` loop, which commonly iterates over an iterable, a `while` loop is useful when repetition depends on a condition.

### Syntax

```python
while condition:
    # Code repeats while condition is True
```

### Example 1: Print Numbers

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

**Output:**

```text
1
2
3
4
5
```

How it works:

1. `number` starts at `1`.
2. Python checks whether `number <= 5`.
3. If true, it prints the number.
4. `number += 1` increases it by one.
5. The condition is checked again.
6. When `number` becomes `6`, the condition is false and the loop ends.

### Example 2: Countdown

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Finished!")
```

**Output:**

```text
5
4
3
2
1
Finished!
```

### Example 3: Repeat Until Valid Input

```python
while True:
    answer = input("Enter yes or no: ").strip().lower()

    if answer in ("yes", "no"):
        print("Valid answer")
        break

    print("Invalid input. Try again.")
```

This loop keeps asking until the user enters an accepted response.

`while True` creates a loop whose condition is always true. In this example, `break` provides the exit.

### When Should You Use a `while` Loop?

Use a `while` loop when:

- The number of repetitions is not known in advance.
- You need to repeat until a condition changes.
- You are validating user input.
- You are waiting for a particular state or response.
- You are implementing a menu that continues until the user exits.

---

## 5. `for` Loop vs. `while` Loop

| Feature | `for` loop | `while` loop |
|---|---|---|
| Common use | Iterate over an iterable | Repeat while a condition is true |
| Number of repetitions | Often determined by the iterable | Depends on the condition |
| Automatic progression | Moves to the next iterable item | You usually update relevant state yourself |
| Common example | Processing a list | Asking until valid input |
| Main risk | Incorrect iteration or modifying data unexpectedly | Infinite loop if the condition never becomes false |

### Example: Same Task Using Both Loops

Using a `for` loop:

```python
for i in range(1, 6):
    print(i)
```

Using a `while` loop:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Both print the integers from `1` through `5`.

**Practical guideline:** Prefer a `for` loop when iterating over a collection or a known sequence. Prefer a `while` loop when repetition depends on a changing condition.

---

## 6. The `break` Statement

The `break` statement immediately terminates the nearest enclosing loop.

Execution continues with the first statement after that loop.

### Example 1: Stop at a Specific Number

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

**Output:**

```text
1
2
3
4
```

When `number` becomes `5`, the loop ends immediately.

### Example 2: Search for an Item

```python
names = ["Amit", "Riya", "Rahul", "Neha"]
target = "Rahul"

for name in names:
    if name == target:
        print("Found:", name)
        break
```

**Output:**

```text
Found: Rahul
```

The loop stops once it finds the target.

### Example 3: Stop a `while` Loop

```python
number = 1

while number <= 10:
    if number == 4:
        break

    print(number)
    number += 1
```

**Output:**

```text
1
2
3
```

### Key Point

`break` exits only the nearest enclosing loop. If you have nested loops, breaking the inner loop does not automatically terminate the outer loop.

---

## 7. The `continue` Statement

The `continue` statement skips the rest of the current iteration and moves to the next iteration.

It does not terminate the entire loop.

### Example 1: Skip a Number

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

**Output:**

```text
1
2
4
5
```

When `number` is `3`, Python skips the `print()` statement for that iteration.

### Example 2: Print Only Odd Numbers

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)
```

**Output:**

```text
1
3
5
7
9
```

Even numbers are skipped.

### Example 3: Skip Empty Values

```python
names = ["Amit", "", "Riya", "", "Neha"]

for name in names:
    if not name:
        continue

    print(name)
```

**Output:**

```text
Amit
Riya
Neha
```

### Important Warning with `while`

Be careful when using `continue` in a `while` loop. If the variable that controls the condition is updated later in the loop, `continue` might skip that update and cause an infinite loop.

Incorrect:

```python
number = 0

while number < 5:
    if number == 2:
        continue

    number += 1
```

When `number` reaches `2`, the loop repeatedly continues without increasing the number.

Correct:

```python
number = 0

while number < 5:
    number += 1

    if number == 2:
        continue

    print(number)
```

**Output:**

```text
1
3
4
5
```

---

## 8. The `pass` Statement

The `pass` statement does nothing. It acts as a placeholder where Python requires a statement syntactically.

It is useful when you want to define a block now and implement it later.

### Example 1: Placeholder in a Loop

```python
for number in range(5):
    pass
```

The loop runs, but no visible action occurs.

### Example 2: Placeholder in a Conditional

```python
age = 20

if age >= 18:
    pass
else:
    print("Minor")
```

Nothing happens in the `if` block.

### Example 3: Placeholder for Future Work

```python
def scan_file():
    pass
```

This defines a function whose implementation can be added later.

### Difference Between `pass`, `break`, and `continue`

| Statement | Purpose |
|---|---|
| `pass` | Does nothing |
| `break` | Terminates the nearest enclosing loop |
| `continue` | Skips the remainder of the current iteration |

Do not confuse `pass` with `continue`. The `pass` statement does not skip an iteration or end the loop.

---

## 9. Nested Loops

A nested loop is a loop inside another loop.

The inner loop executes as part of each iteration of the outer loop.

### Example 1: Basic Nested Loop

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

**Output:**

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

For each value of `i`, the inner loop runs through all values of `j`.

### Example 2: Print a Rectangle of Stars

```python
for row in range(3):
    for column in range(5):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * * *
* * * * *
* * * * *
```

The inner loop prints five stars per row. The outer loop repeats this for three rows.

`end=" "` keeps the stars on the same line. The final `print()` moves to the next line.

### Example 3: Multiplication Table Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")

    print()
```

**Output:**

```text
1	2	3
2	4	6
3	6	9
```

### Example 4: Nested Loops with Conditions

```python
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print("Equal", end=" ")
        else:
            print("-", end=" ")

    print()
```

**Output:**

```text
Equal - -
- Equal -
- - Equal
```

### How Many Times Does a Nested Loop Run?

If the outer loop runs 3 times and the inner loop runs 4 times for every outer iteration, the inner body runs:

`3 × 4 = 12` times.

This is why nested loops can become expensive for large collections.

If each of two nested loops processes `n` items, the work is commonly proportional to \(n^2\).

Use nested loops when necessary, but avoid them when a simpler approach is available.

---

## 10. Looping Through Collections

Python collections are iterable, meaning you can visit their elements using a loop.

### 10.1 Loop Through a List

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**

```text
apple
banana
mango
```

### 10.2 Loop Through a Tuple

```python
coordinates = (10, 20, 30)

for coordinate in coordinates:
    print(coordinate)
```

**Output:**

```text
10
20
30
```

### 10.3 Loop Through a Set

```python
colors = {"red", "green", "blue"}

for color in colors:
    print(color)
```

This prints all three colors, but the order is not guaranteed. Do not rely on a particular iteration order for a set.

### 10.4 Loop Through a Dictionary's Keys

```python
user = {
    "name": "Alex",
    "age": 25,
    "city": "Delhi"
}

for key in user:
    print(key)
```

This iterates over dictionary keys.

### 10.5 Loop Through Dictionary Values

```python
user = {
    "name": "Alex",
    "age": 25,
    "city": "Delhi"
}

for value in user.values():
    print(value)
```

**Output:**

```text
Alex
25
Delhi
```

### 10.6 Loop Through Dictionary Keys and Values

Use `.items()` when you need both the key and its associated value.

```python
user = {
    "name": "Alex",
    "age": 25,
    "city": "Delhi"
}

for key, value in user.items():
    print(f"{key}: {value}")
```

**Output:**

```text
name: Alex
age: 25
city: Delhi
```

### 10.7 Use `enumerate()` to Get Index and Value

Instead of manually maintaining a counter, use `enumerate()`.

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

**Output:**

```text
0 Python
1 Java
2 C++
```

Start counting from `1` if needed:

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

**Output:**

```text
1 Python
2 Java
3 C++
```

### 10.8 Use `zip()` to Loop Through Multiple Collections

```python
names = ["Amit", "Riya", "Rahul"]
scores = [80, 90, 75]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Output:**

```text
Amit: 80
Riya: 90
Rahul: 75
```

By default, `zip()` stops when the shortest iterable is exhausted.

### Important: Avoid Modifying a Collection While Iterating Over It

Removing elements directly from a list while looping through it can cause items to be skipped.

Risky approach:

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
```

This can produce unexpected results because the list changes while it is being iterated over.

A clearer approach is to create a new list:

```python
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = [
    number for number in numbers
    if number % 2 != 0
]

print(odd_numbers)
```

**Output:**

```text
[1, 3, 5]
```

List comprehensions are a related topic worth learning after you are comfortable with loops.

---

## 11. Loop Control and Termination Conditions

Every loop should have a clear way to progress and, when appropriate, terminate.

### 11.1 A `for` Loop Terminates Naturally

```python
for number in range(1, 4):
    print(number)
```

The loop ends after the iterable has no more items.

### 11.2 A `while` Loop Depends on Its Condition

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

The loop terminates when `number <= 3` becomes false.

### 11.3 Use `break` for Early Termination

```python
numbers = [4, 8, 12, 16, 20]

for number in numbers:
    if number > 10:
        print("First number greater than 10:", number)
        break
```

**Output:**

```text
First number greater than 10: 12
```

### 11.4 Use a Sentinel Value

A sentinel is a special input value that tells a loop to stop.

```python
while True:
    text = input("Enter text, or type 'quit' to stop: ")

    if text.lower() == "quit":
        break

    print("You entered:", text)
```

The user can continue entering text until they type `quit`.

### 11.5 Use a Counter

A counter tracks how many times an operation has happened.

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print("Attempt:", attempts)
```

**Output:**

```text
Attempt: 1
Attempt: 2
Attempt: 3
```

A counter can help limit retries, but real authentication systems should also use appropriate rate limiting and account protection.

### 11.6 Understand Loop `else`

Python loops can have an `else` block. It executes if the loop finishes normally, without being terminated by `break`.

Example:

```python
numbers = [2, 4, 6, 8]

for number in numbers:
    if number % 2 != 0:
        print("Odd number found")
        break
else:
    print("No odd numbers found")
```

**Output:**

```text
No odd numbers found
```

Because no `break` occurs, the `else` block executes.

Now consider:

```python
numbers = [2, 4, 5, 8]

for number in numbers:
    if number % 2 != 0:
        print("Odd number found")
        break
else:
    print("No odd numbers found")
```

**Output:**

```text
Odd number found
```

The `else` block does not execute because the loop was terminated by `break`.

**Important:** A loop's `else` does not mean the same thing as an `if-else`. It means the loop completed without a `break`.

---

## 12. Avoiding Infinite Loops

An infinite loop continues running because its termination condition is never reached.

Infinite loops are sometimes intentional, such as a server waiting for requests. However, they must have an appropriate exit or shutdown mechanism.

### Example 1: Accidental Infinite Loop

```python
number = 1

while number <= 5:
    print(number)
```

The variable `number` never changes. The condition remains true, so the loop continues indefinitely.

### Correct Version

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Now the variable changes with every iteration, allowing the condition to become false.

### Common Causes of Infinite Loops

1. Forgetting to update the loop variable.
2. Updating the variable in the wrong direction.
3. Writing a condition that can never become false.
4. Using `continue` before the required update.
5. Waiting forever for a condition or input that never occurs.
6. Using the wrong comparison operator.

### Example 2: Updating in the Wrong Direction

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
    number -= 1
```

Because `number` decreases, it remains less than or equal to `5`.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Example 3: A Condition That Never Becomes False

Incorrect:

```python
number = 1

while number != 10:
    print(number)
    number += 2
```

The values are `1, 3, 5, 7, 9, 11, ...`. The number never becomes `10`, so the loop never terminates.

One possible correction is:

```python
number = 1

while number < 10:
    print(number)
    number += 2
```

**Output:**

```text
1
3
5
7
9
```

### A Checklist Before Running a `while` Loop

Ask yourself:

- What condition makes the loop stop?
- Which variable or state changes during each iteration?
- Can the condition eventually become false?
- Can `continue` skip an essential update?
- Is there a suitable exit path for invalid input or unexpected situations?

### How to Stop a Running Loop

If a Python program is stuck in a loop in a typical terminal, press `Ctrl + C` to send a keyboard interrupt.

This is a useful emergency measure, but it is better to design loops with correct termination conditions.

---

## 13. Practical Mini Projects

### Project 1: Number Guessing Game

```python
secret_number = 7

while True:
    guess_text = input("Guess the number (1-10): ").strip()

    try:
        guess = int(guess_text)
    except ValueError:
        print("Enter a valid whole number.")
        continue

    if not 1 <= guess <= 10:
        print("Choose a number from 1 to 10.")
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct guess!")
        break
```

Concepts practiced:
- `while`
- `if-elif-else`
- `continue`
- `break`
- Input validation

### Project 2: Sum of Numbers

```python
total = 0

for number in range(1, 101):
    total += number

print("Sum:", total)
```

**Output:**

```text
Sum: 5050
```

### Project 3: Count Vowels in a String

```python
text = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Number of vowels:", count)
```

Example input:

```text
Python programming
```

**Output:**

```text
Number of vowels: 4
```

### Project 4: Simple Menu System

```python
while True:
    print("\n1. Say hello")
    print("2. Show a message")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Keep practicing Python.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
```

The loop continues until the user selects option `3`.

### Project 5: Count Failed Checks in Sample Data

```python
statuses = ["success", "failed", "success", "failed", "success"]
failed_count = 0

for status in statuses:
    if status == "failed":
        failed_count += 1

print("Failed checks:", failed_count)
```

**Output:**

```text
Failed checks: 2
```

This is a simple data-processing exercise. Similar counting logic can be used to summarize application logs or the results of authorized security tests.

---

## 14. Practice Exercises

Try to solve these in your terminal without copying the examples.

### Beginner Level

1. Print the numbers from `1` to `10` using a `for` loop.
2. Print the numbers from `10` down to `1`.
3. Print all even numbers from `1` to `50`.
4. Calculate the sum of numbers from `1` to `100`.
5. Print the multiplication table of a number entered by the user.
6. Loop through a string and print each character on a separate line.

### Intermediate Level

7. Count the number of vowels in a sentence.
8. Count how many even and odd numbers exist in a list.
9. Find the largest number in a list without using `max()`.
10. Search for a value in a list and stop using `break` when it is found.
11. Use `continue` to skip negative numbers in a list.
12. Keep asking for input until the user enters a valid positive integer.
13. Print a rectangle of stars using nested loops.
14. Print a multiplication grid using nested loops.

### Advanced Practice

15. Create a number guessing game with input validation.
16. Create a menu-driven program that continues until the user exits.
17. Process a dictionary of usernames and scores, printing both keys and values.
18. Write a loop that finds all numbers between `1` and `100` divisible by both `3` and `5`.
19. Write a program that counts how many times a particular character occurs in a string.
20. Debug an intentionally broken `while` loop and explain why it does not terminate.

### Challenge: Analyze a List

Given:

```python
numbers = [12, -3, 7, 0, 18, -5, 12, 4]
```

Write a program that prints:

- The count of positive numbers.
- The count of negative numbers.
- The count of zeros.
- The sum of all positive numbers.
- The first number greater than `10`, using `break`.

Try solving this using one or two loops.

---

## 15. Quick Revision Questions and Answers

**Q1. What is a loop?**

A programming structure that repeats a block of code.

**Q2. What is the difference between `for` and `while`?**

A `for` loop iterates over an iterable. A `while` loop repeats while a condition remains true.

**Q3. What does `range(5)` produce?**

The integers `0, 1, 2, 3, 4`.

**Q4. Is the stop value in `range()` included?**

No. The stop value is excluded.

**Q5. What does `break` do?**

It terminates the nearest enclosing loop.

**Q6. What does `continue` do?**

It skips the remainder of the current iteration and proceeds to the next iteration.

**Q7. What does `pass` do?**

Nothing. It serves as a placeholder statement.

**Q8. What is a nested loop?**

A loop placed inside another loop.

**Q9. What is an infinite loop?**

A loop that continues without reaching its termination condition or exit path.

**Q10. How can you avoid an accidental infinite `while` loop?**

Ensure that the loop's state changes appropriately and that its termination condition can eventually become false.

**Q11. How do you get both the index and value from a list?**

Use `enumerate()`.

**Q12. How do you get both keys and values from a dictionary?**

Use `.items()`.

**Q13. What does a loop's `else` block do?**

It executes when the loop finishes normally without being terminated by `break`.

**Q14. What happens when `break` is used inside a nested loop?**

It exits only the nearest enclosing loop.

**Q15. How can you interrupt a stuck Python loop in a typical terminal?**

Press `Ctrl + C`.

---

## 16. Loops Cheat Sheet

| Concept | Example | Purpose |
|---|---|---|
| `for` | `for item in items:` | Iterate through items |
| `while` | `while condition:` | Repeat while a condition is true |
| `range()` | `range(1, 6)` | Generate integers from 1 through 5 |
| `break` | `if found: break` | Exit the loop |
| `continue` | `if invalid: continue` | Skip the current iteration |
| `pass` | `for item in items: pass` | Placeholder statement |
| `enumerate()` | `enumerate(items)` | Get index and item |
| `.items()` | `data.items()` | Get dictionary keys and values |
| `zip()` | `zip(names, scores)` | Iterate over multiple iterables together |
| Nested loops | `for x in a: for y in b:` | Repeat an inner loop for each outer iteration |
| Loop `else` | `for x in items: ... else: ...` | Run if no `break` occurs |
| Infinite-loop prevention | Update loop state | Ensure the loop can terminate |

### Final Revision Checklist

- [ ] Write `for` and `while` loops without syntax errors.
- [ ] Understand `range(start, stop, step)`.
- [ ] Use `break`, `continue`, and `pass` correctly.
- [ ] Write simple nested loops.
- [ ] Iterate through lists, strings, tuples, sets, and dictionaries.
- [ ] Use `enumerate()` and `zip()` when appropriate.
- [ ] Understand loop termination conditions.
- [ ] Identify and fix accidental infinite loops.
- [ ] Complete at least three mini projects without copying the solutions.

## Recommended Practice Plan

If you have one hour for this topic:

- **10 minutes:** Revise `for`, `while`, and `range()`.
- **10 minutes:** Practice `break`, `continue`, and `pass`.
- **15 minutes:** Work with collections and nested loops.
- **15 minutes:** Solve input-validation and loop-termination problems.
- **10 minutes:** Complete one mini project from memory.

Focus on writing and debugging code yourself. You do not need to memorize every example; you need to understand how to control repetition and make loops terminate correctly.
