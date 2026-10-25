# Python Revision — Topic 8: Functions

## 1. What Is a Function?

A function is a reusable block of code that performs a particular task. You define it once and call it whenever you need it.

Functions help you:
- Avoid repeating code.
- Break large problems into smaller tasks.
- Make programs easier to read, test, and debug.
- Reuse logic across different projects.

### Example without a function

```python
print("Welcome to Python!")
print("Welcome to Python!")
print("Welcome to Python!")
```

### Example using a function

```python
def welcome():
    print("Welcome to Python!")


welcome()
welcome()
welcome()
```

Output:

```text
Welcome to Python!
Welcome to Python!
Welcome to Python!
```

The second approach is easier to maintain because the message is defined in one place.

---

## 2. Defining and Calling Functions

Use the `def` keyword to define a function.

### Syntax

```python
def function_name(parameters):
    # Function body
    statements
```

- `def`: Begins a function definition.
- `function_name`: The name used to call the function.
- `parameters`: Optional inputs.
- Function body: The code executed when the function is called.

### Example

```python
def greet():
    print("Hello!")


greet()
```

Output:

```text
Hello!
```

### A function with multiple statements

```python
def introduce():
    print("My name is Rahul.")
    print("I am learning Python.")
    print("I want to become a programmer.")


introduce()
```

### Important: Defining versus calling

Defining a function does not execute its body.

```python
def test():
    print("Function executed")


print("Before calling")
test()
print("After calling")
```

Output:

```text
Before calling
Function executed
After calling
```

Python executes the function body when the function is called.

### Naming conventions

Use descriptive names written in `snake_case`.

```python
def calculate_total():
    pass


def check_password():
    pass


def extract_domain():
    pass
```

Avoid unclear names such as `f1()`, `x()`, or `do_it()` when a descriptive name would be more helpful.

---

## 3. Parameters and Arguments

Parameters and arguments are related but different.

- **Parameter:** A variable listed in the function definition.
- **Argument:** The actual value supplied when calling the function.

Example:

```python
def greet(name):       # name is a parameter
    print(f"Hello, {name}!")


greet("Rahul")         # "Rahul" is an argument
greet("Amit")
```

Output:

```text
Hello, Rahul!
Hello, Amit!
```

### Multiple parameters

```python
def add(a, b):
    print(a + b)


add(10, 20)
add(5, 7)
```

Output:

```text
30
12
```

Here, `a` and `b` are parameters. The values passed to them are arguments.

### Example with practical data

```python
def create_username(first_name, last_name):
    username = f"{first_name.lower()}_{last_name.lower()}"
    print(username)


create_username("Pulok", "Singha")
```

Output:

```text
pulok_singha
```

### Common mistake: Missing arguments

```python
def add(a, b):
    return a + b


# add(10)  # TypeError: missing a required argument
```

Unless the function provides a default value or uses flexible arguments, you must supply the required arguments.

---

## 4. Positional and Keyword Arguments

Python supports different ways to pass arguments.

### 4.1 Positional arguments

Arguments are matched to parameters by their position.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Rahul", 21)
```

Output:

```text
My name is Rahul and I am 21 years old.
```

The first argument goes to `name`, and the second goes to `age`.

Changing the order can change the meaning:

```python
introduce(21, "Rahul")
```

This runs, but the values are assigned to the wrong parameters. Python does not automatically know that the arguments were intended to represent a name and an age.

### 4.2 Keyword arguments

Keyword arguments identify parameters by name.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce(name="Rahul", age=21)
introduce(age=21, name="Rahul")
```

Both calls produce the same result.

### 4.3 Mixing positional and keyword arguments

Positional arguments must come before keyword arguments.

Correct:

```python
def describe_person(name, age, country):
    print(name, age, country)


describe_person("Rahul", age=21, country="India")
```

Incorrect:

```python
# describe_person(name="Rahul", 21, country="India")
```

This raises a `SyntaxError` because a positional argument follows a keyword argument.

### 4.4 Positional-only and keyword-only parameters

Python allows you to control how callers supply arguments.

```python
def calculate(a, b, /, *, operation):
    if operation == "add":
        return a + b
    return a - b


print(calculate(10, 5, operation="add"))
```

Output:

```text
15
```

In this definition:
- Parameters before `/` are positional-only.
- Parameters after `*` are keyword-only.
- `a` and `b` must be supplied positionally.
- `operation` must be supplied by keyword.

These features are useful when designing clear and reliable function interfaces.

---

## 5. Default Parameters

A default parameter has a value that Python uses when the caller does not supply an argument for it.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Rahul")
```

Output:

```text
Hello, Guest!
Hello, Rahul!
```

### Multiple default parameters

```python
def create_profile(name, country="India", role="Student"):
    print(f"Name: {name}")
    print(f"Country: {country}")
    print(f"Role: {role}")


create_profile("Rahul")
create_profile("Amit", country="Canada")
create_profile("Priya", role="Developer")
```

### Rule: Required parameters before default parameters

Correct:

```python
def add(a, b=0):
    return a + b
```

Incorrect:

```python
# def add(a=0, b):
#     return a + b
```

A required positional parameter cannot follow a defaulted positional parameter in the same parameter group.

### Important mistake: Mutable default values

Avoid using a mutable list or dictionary as a default parameter when you expect a fresh object on each call.

Problematic:

```python
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("Python"))
print(add_item("Linux"))
```

Output:

```text
['Python']
['Python', 'Linux']
```

Why? The default list is created once when the function is defined, then reused across calls that omit `items`.

### Correct approach

Use `None` as the default and create the list inside the function.

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("Python"))
print(add_item("Linux"))
```

Output:

```text
['Python']
['Linux']
```

This avoids accidentally sharing the same list between calls.

---

## 6. `*args` and `**kwargs`

These allow functions to accept a variable number of arguments.

### 6.1 `*args`

`*args` collects additional positional arguments into a tuple.

```python
def add_numbers(*args):
    print(args)
    print(sum(args))


add_numbers(10, 20)
add_numbers(1, 2, 3, 4)
```

Output:

```text
(10, 20)
30
(1, 2, 3, 4)
10
```

The name `args` is conventional, but the asterisk is what matters. You could use another valid name.

### Practical example

```python
def find_maximum(*numbers):
    if not numbers:
        return None

    return max(numbers)


print(find_maximum(10, 40, 25))
print(find_maximum(5, 8, 2, 100))
print(find_maximum())
```

Output:

```text
40
100
None
```

### 6.2 `**kwargs`

`**kwargs` collects additional keyword arguments into a dictionary.

```python
def show_profile(**kwargs):
    print(kwargs)


show_profile(name="Rahul", age=21, country="India")
```

Output:

```text
{'name': 'Rahul', 'age': 21, 'country': 'India'}
```

### Iterating through `kwargs`

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_profile(name="Rahul", age=21, role="Student")
```

Output:

```text
name: Rahul
age: 21
role: Student
```

### Using normal parameters with `*args` and `**kwargs`

```python
def example(required, *args, **kwargs):
    print("Required:", required)
    print("Extra positional:", args)
    print("Extra keyword:", kwargs)


example("Python", 10, 20, level="Beginner", duration=30)
```

Output:

```text
Required: Python
Extra positional: (10, 20)
Extra keyword: {'level': 'Beginner', 'duration': 30}
```

### Common parameter order

A common function definition order is:

```python
def function(positional_parameters, *args, keyword_only=None, **kwargs):
    pass
```

For example:

```python
def configure(name, *features, debug=False, **options):
    print(name)
    print(features)
    print(debug)
    print(options)


configure("scanner", "ports", "headers", debug=True, timeout=5)
```

Output:

```text
scanner
('ports', 'headers')
True
{'timeout': 5}
```

### Unpacking with `*` and `**`

The same symbols can unpack arguments when calling a function.

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]
print(add(*numbers))
```

Output:

```text
60
```

For keyword arguments:

```python
def introduce(name, age):
    print(name, age)


person = {"name": "Rahul", "age": 21}
introduce(**person)
```

Output:

```text
Rahul 21
```

**Remember:**
- In a function definition, `*args` collects positional arguments.
- In a function definition, `**kwargs` collects keyword arguments.
- In a function call, `*iterable` unpacks positional arguments.
- In a function call, `**dictionary` unpacks keyword arguments.

---

## 7. Return Values

The `return` statement sends a result back to the caller.

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

Output:

```text
30
```

### `return` versus `print()`

`print()` displays something. `return` gives a value back to the caller.

```python
def add_with_print(a, b):
    print(a + b)


def add_with_return(a, b):
    return a + b


x = add_with_print(10, 20)
y = add_with_return(10, 20)

print("x:", x)
print("y:", y)
```

Output:

```text
30
30
x: None
y: 30
```

The first function prints the answer but returns no explicit value, so its result is `None`.

### Returning multiple values

```python
def calculate(a, b):
    return a + b, a - b, a * b


addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)
```

Output:

```text
15
5
50
```

Python packages these returned values into a tuple, which can be unpacked.

### A function returns `None` when no value is returned explicitly

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

A bare `return` also returns `None`.

### `return` ends the current function execution

```python
def check_number(number):
    if number < 0:
        return "Negative"

    return "Zero or positive"


print(check_number(-5))
print(check_number(10))
```

Output:

```text
Negative
Zero or positive
```

Once `return` executes, the function exits immediately.

### Returning a collection

```python
def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)
```

Output:

```text
[2, 4, 6]
```

Returning data makes functions easier to reuse in other parts of a program.

---

## 8. Scope and Namespaces

A namespace is a mapping between names and the objects they refer to.

Scope determines where a name can be accessed directly.

Python commonly uses the **LEGB** rule when resolving ordinary variable names:

1. **L — Local:** Names inside the current function.
2. **E — Enclosing:** Names in enclosing function scopes.
3. **G — Global:** Names defined at the module level.
4. **B — Built-in:** Names provided by Python, such as `len()` and `sum()`.

### Local variable

```python
def greet():
    message = "Hello"
    print(message)


greet()
```

The variable `message` is local to `greet()`.

```python
def greet():
    message = "Hello"


# print(message)  # NameError
```

The name is not available directly outside the function.

### Global variable

```python
language = "Python"


def show_language():
    print(language)


show_language()
```

Output:

```text
Python
```

The function can read the global variable because it does not assign to that name locally.

### Local variables can shadow global variables

```python
name = "Global"


def show_name():
    name = "Local"
    print(name)


show_name()
print(name)
```

Output:

```text
Local
Global
```

The assignment inside the function creates a local variable because the function does not declare `name` as global.

### Enclosing scope

```python
def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    inner()


outer()
```

Output:

```text
Hello from outer
```

The inner function can access the variable from its enclosing function.

### The `nonlocal` keyword

`nonlocal` allows an inner function to reassign a name in an enclosing function scope.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    inner()

    return count


print(outer())
```

Output:

```text
2
```

`nonlocal` does not refer to a module-level global variable; it refers to a binding in an enclosing function scope.

### The `global` keyword

Use `global` when a function needs to reassign a module-level variable.

```python
count = 0


def increment():
    global count
    count += 1


increment()
increment()

print(count)
```

Output:

```text
2
```

**Best practice:** Prefer returning new values or using explicit objects rather than relying heavily on `global`. Excessive global state can make programs harder to test and maintain.

---

## 9. Lambda Functions

A lambda is a small anonymous function created with the `lambda` keyword.

Syntax:

```python
lambda parameters: expression
```

A lambda evaluates one expression and returns its result.

### Example

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Equivalent normal function:

```python
def square(x):
    return x ** 2
```

### Multiple parameters

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

### Lambda with `sorted()`

Suppose you have a list of tuples:

```python
students = [
    ("Rahul", 85),
    ("Amit", 70),
    ("Priya", 92)
]

students_sorted = sorted(students, key=lambda student: student[1])

print(students_sorted)
```

Output:

```text
[('Amit', 70), ('Rahul', 85), ('Priya', 92)]
```

The `key` function tells `sorted()` to sort by the second element of each tuple.

For descending order:

```python
students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

### Lambda with `map()`

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

### Lambda with `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
```

Output:

```text
[2, 4, 6]
```

**Best practice:** Use lambda functions for short, simple expressions. Use `def` for complex logic, multiple statements, or functions that need descriptive names and docstrings.

---

## 10. Recursion

Recursion occurs when a function calls itself to solve a smaller version of the same problem.

A recursive function usually needs:

1. **Base case:** Stops the recursion.
2. **Recursive case:** Calls the function again with a smaller or simpler problem.

### Example: Factorial

The factorial of a positive integer is the product of all positive integers up to that number.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Python implementation:

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

Output:

```text
120
```

### How recursion works

```text
factorial(5)
    5 * factorial(4)
        4 * factorial(3)
            3 * factorial(2)
                2 * factorial(1)
                    1
```

Python evaluates the calls as they return:

```text
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
factorial(5) = 120
```

### Example: Sum of numbers from 1 to n

```python
def sum_numbers(n):
    if n <= 0:
        return 0

    return n + sum_numbers(n - 1)


print(sum_numbers(5))
```

Output:

```text
15
```

### Common recursion mistakes

**Missing base case:**

```python
# def infinite_recursion():
#     return infinite_recursion()
```

This continues until Python raises `RecursionError`.

**Not moving toward the base case:**

If each recursive call does not make progress toward stopping, recursion may never terminate.

**Using recursion when a loop is simpler:**

```python
def factorial_loop(n):
    result = 1

    for number in range(2, n + 1):
        result *= number

    return result
```

Python has a recursion depth limit, and recursive calls have overhead. For straightforward repetitive tasks, loops are often more efficient. Recursion is particularly useful for some tree traversals, divide-and-conquer algorithms, and nested structures.

---

## 11. First-Class Functions

In Python, functions are first-class objects. This means you can treat functions as values.

You can:
- Assign a function to a variable.
- Pass a function as an argument.
- Return a function from another function.
- Store functions in collections.

### Assigning a function to a variable

```python
def greet():
    print("Hello!")


say_hello = greet

say_hello()
```

Output:

```text
Hello!
```

Notice the difference:

```python
say_hello = greet    # Stores a reference to the function
say_hello = greet()  # Calls the function and stores its return value
```

The parentheses make a crucial difference.

### Passing a function as an argument

```python
def square(x):
    return x ** 2


def apply_function(function, value):
    return function(value)


print(apply_function(square, 5))
```

Output:

```text
25
```

The `square` function is passed without parentheses and called inside `apply_function()`.

### Returning a function

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
```

Output:

```text
10
15
```

The returned functions remember the `factor` value from their enclosing scope. This behavior is associated with closures.

---

## 12. Basic Higher-Order Functions

A higher-order function either accepts another function as an argument or returns a function.

### 12.1 `map()`

`map()` applies a function to each element of an iterable and returns an iterator.

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

A list comprehension is often a readable alternative:

```python
result = [x * 2 for x in numbers]
```

### 12.2 `filter()`

`filter()` keeps elements for which the function returns a truthy result.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x > 3, numbers)

print(list(result))
```

Output:

```text
[4, 5, 6]
```

Equivalent comprehension:

```python
result = [x for x in numbers if x > 3]
```

### 12.3 `sorted()` with a key function

```python
names = ["Rahul", "Amit", "Priya", "Jo"]

result = sorted(names, key=len)

print(result)
```

Output:

```text
['Jo', 'Amit', 'Rahul', 'Priya']
```

The `key` function calculates the value used for sorting.

### 12.4 `any()` and `all()`

These are built-in functions that evaluate conditions across an iterable.

```python
numbers = [2, 4, 6, 7]

print(any(x % 2 != 0 for x in numbers))  # True
print(all(x % 2 == 0 for x in numbers))  # False
```

- `any()` returns `True` if at least one element is truthy.
- `all()` returns `True` if every element is truthy. It also returns `True` for an empty iterable.

These are useful when checking collections without writing a manual loop.

---

## 13. Type Hints

Type hints document the expected types of function parameters and return values.

They help developers understand a function and allow tools such as type checkers and IDEs to detect potential mistakes.

### Basic type hints

```python
def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))
```

In this example:
- `a: int` suggests that `a` should be an integer.
- `b: int` suggests that `b` should be an integer.
- `-> int` indicates the intended return type.

**Important:** Python does not automatically enforce these annotations at runtime.

```python
print(add("Hello, ", "Python"))
```

This returns `"Hello, Python"` even though the annotations say `int`. A static type checker may report the mismatch.

### String return type

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Boolean return type

```python
def is_even(number: int) -> bool:
    return number % 2 == 0
```

### List type hints

In modern Python, you can write:

```python
def calculate_squares(numbers: list[int]) -> list[int]:
    return [number ** 2 for number in numbers]


print(calculate_squares([1, 2, 3]))
```

For Python 3.8 and earlier, the `typing` module provides generic types such as `List[int]`.

### Optional values

If a function may return either a string or `None`, use a union type.

```python
def find_username(user_id: int) -> str | None:
    if user_id == 1:
        return "rahul"

    return None
```

The `str | None` syntax requires Python 3.10 or newer. In earlier versions, use `Optional[str]` from `typing`.

### Type hints for dictionaries

```python
def get_scores() -> dict[str, int]:
    return {
        "Rahul": 85,
        "Amit": 75
    }
```

### Type hints for callbacks

```python
from collections.abc import Callable


def apply_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return operation(a, b)


def multiply(a: int, b: int) -> int:
    return a * b


print(apply_operation(multiply, 4, 5))
```

Output:

```text
20
```

**Best practice:** Add type hints where they clarify the function's interface. Use a type checker when you want systematic validation; annotations alone do not guarantee correctness.

---

## 14. Docstrings

A docstring is a string literal placed at the beginning of a function, class, or module to describe its purpose.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

You can access it through the `__doc__` attribute:

```python
print(add.__doc__)
```

Output:

```text
Return the sum of two numbers.
```

You can also use `help()`:

```python
help(add)
```

### Writing a useful docstring

A good docstring explains:
- What the function does.
- Its important parameters.
- What it returns.
- Any important exceptions or assumptions.

Example:

```python
def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: The numerator.
        b: The denominator, which must not be zero.

    Returns:
        The result of dividing a by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
```

The docstring describes the behavior, but the function's division operation itself raises `ZeroDivisionError` when `b` is zero.

### Why docstrings matter

Docstrings make functions easier to understand and maintain, especially when you return to a project after several weeks or share code with other developers.

---

## 15. Writing Reusable Functions

A reusable function should ideally perform one clear task, accept necessary inputs, and return a predictable result.

### Example: Poorly organized code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is not an adult.")
```

This works, but input handling, decision logic, and output are mixed together.

### Improved version

```python
def is_adult(age: int) -> bool:
    """Return True if age is at least 18."""
    return age >= 18


def describe_person(name: str, age: int) -> str:
    """Return a description of a person."""
    if is_adult(age):
        return f"{name} is an adult."

    return f"{name} is not an adult."


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(describe_person(name, age))
```

The functions can now be reused independently of the input and output code.

### Principles for reusable functions

1. **One clear responsibility:** A function should have a focused purpose.
2. **Use parameters:** Supply changing values as inputs instead of hardcoding them.
3. **Return results:** Let callers decide what to do with the result.
4. **Avoid unnecessary global variables:** Pass data explicitly when possible.
5. **Use descriptive names:** Names should communicate the task.
6. **Handle errors deliberately:** Validate inputs or raise meaningful exceptions when appropriate.
7. **Add type hints and docstrings:** Make the expected behavior clear.
8. **Avoid duplicated logic:** Extract repeated behavior into a function.
9. **Keep side effects clear:** Make it obvious when a function prints, modifies data, writes files, or performs network requests.
10. **Test functions independently:** Small functions are easier to verify.

### Example: Reusable password-length validator

This example checks only the length of a string. It does not claim to measure overall password strength.

```python
def is_valid_password_length(
    password: str,
    minimum_length: int = 12
) -> bool:
    """
    Check whether a password meets the minimum length.

    Args:
        password: The password string to check.
        minimum_length: The minimum accepted length.

    Returns:
        True if the password meets the length requirement.
    """
    if minimum_length < 1:
        raise ValueError("minimum_length must be positive")

    return len(password) >= minimum_length


print(is_valid_password_length("mysecret"))
print(is_valid_password_length("a-longer-example-password"))
```

Output:

```text
False
True
```

This function can be reused in different programs without duplicating the length-checking logic.

### Example: Reusable URL hostname extraction

```python
from urllib.parse import urlsplit


def extract_hostname(url: str) -> str | None:
    """
    Extract a hostname from an absolute HTTP or HTTPS URL.

    Return None if the URL does not have a supported scheme
    or a hostname.
    """
    parsed = urlsplit(url)

    if parsed.scheme not in ("http", "https"):
        return None

    if not parsed.hostname:
        return None

    return parsed.hostname.lower()


print(extract_hostname("https://Example.com/path"))
print(extract_hostname("ftp://example.com"))
```

Output:

```text
example.com
None
```

This is a basic example of a reusable helper function for processing URLs. For security-sensitive URL validation, additional checks may be required depending on the application.

---

## 16. Common Mistakes to Avoid

### Mistake 1: Forgetting to call the function

```python
def greet():
    print("Hello")

greet      # References the function
greet()    # Calls the function
```

### Mistake 2: Confusing `print()` with `return`

A function that only prints its result generally returns `None`.

### Mistake 3: Forgetting a return statement

```python
def multiply(a, b):
    result = a * b


print(multiply(2, 3))  # None
```

Correct:

```python
def multiply(a, b):
    return a * b
```

### Mistake 4: Using a mutable default argument

Avoid `items=[]` when you want a fresh list for each call. Use `items=None` and create a list inside the function.

### Mistake 5: Incorrect argument order

Use keyword arguments when they make calls clearer and help prevent mistakes.

### Mistake 6: Modifying a global variable unexpectedly

Prefer explicit inputs and return values when practical.

### Mistake 7: Recursion without a base case

Ensure that every recursive path can eventually reach a stopping condition.

### Mistake 8: Overusing lambda functions

A normal `def` is often clearer when logic is complex or needs documentation.

### Mistake 9: Assuming type hints enforce types

Annotations are not automatic runtime validation.

### Mistake 10: Writing one enormous function

Break complex logic into smaller functions with clear responsibilities.

---

# 17. Practice Exercises

Try writing each solution yourself before checking documentation or examples.

## Beginner Level

1. Write a function that prints `"Hello, Python!"`.
2. Write a function that accepts a name and returns a greeting.
3. Write a function that adds two numbers and returns the result.
4. Write a function that determines whether a number is even.
5. Write a function that accepts a number and returns its square.
6. Write a function with a default country parameter.
7. Write a function that accepts three positional arguments and displays them.
8. Write a function that returns the largest of three numbers.
9. Write a function that converts Celsius to Fahrenheit.
10. Write a function with a docstring and appropriate type hints.

## Intermediate Level

11. Write a function that accepts any number of numeric positional arguments and returns their sum using `*args`.
12. Write a function that accepts arbitrary keyword arguments and displays each key-value pair.
13. Write a function that returns a list of even numbers from an input list.
14. Write a recursive function that calculates the factorial of a non-negative integer.
15. Write a recursive function that calculates the sum of integers from `1` to `n`.
16. Write a function that accepts another function and applies it to a value.
17. Sort a list of tuples by the second element using `sorted()` and a lambda function.
18. Write a function that returns both the minimum and maximum of a list.
19. Write a function that safely extracts a hostname from an HTTP or HTTPS URL.
20. Demonstrate the difference between a local variable and a global variable.

## Advanced Practice for This Revision Stage

21. Write a function that accepts a list and returns a new list without duplicates, preserving order.
22. Write a function that counts the frequency of each word in a sentence.
23. Write a function with positional-only and keyword-only parameters.
24. Write a function that returns another function and demonstrate how the returned function retains an enclosing value.
25. Write a function that accepts a callback using a `Callable` type hint.
26. Demonstrate the mutable-default-argument problem and fix it.
27. Write a reusable function with validation, type hints, a docstring, and meaningful errors.
28. Write unit tests for three functions using Python's built-in `unittest` module.

---

# 18. Quick Revision Questions and Answers

**1. What is a function?**

A reusable block of code that performs a task.

**2. What is the difference between a parameter and an argument?**

A parameter appears in the function definition; an argument is supplied during a call.

**3. What does `return` do?**

It sends a result to the caller and ends the current function execution.

**4. What does a function return if it has no explicit return statement?**

`None`.

**5. What is a default parameter?**

A parameter with a predefined value used when the caller omits the corresponding argument.

**6. What is `*args`?**

A way to collect additional positional arguments into a tuple.

**7. What is `**kwargs`?**

A way to collect additional keyword arguments into a dictionary.

**8. What is the LEGB rule?**

Local, Enclosing, Global, Built-in — the usual order for resolving variable names.

**9. What does `global` do?**

It declares that a name in a function refers to a module-level global binding.

**10. What does `nonlocal` do?**

It allows reassignment of a name in an enclosing function scope.

**11. What is a lambda function?**

A small anonymous function consisting of a single expression.

**12. What is recursion?**

When a function calls itself to solve a smaller version of a problem.

**13. Why does recursion need a base case?**

To ensure that recursive calls eventually stop.

**14. What is a first-class function?**

A function that can be treated like other objects, such as being assigned to variables, passed as an argument, or returned.

**15. What is a higher-order function?**

A function that accepts another function or returns a function.

**16. What does `map()` do?**

It applies a function to each element of an iterable and returns an iterator.

**17. What does `filter()` do?**

It yields elements for which a predicate function returns a truthy result.

**18. What are type hints?**

Annotations that document expected types and support static analysis tools.

**19. What is a docstring?**

A string literal at the beginning of a function, class, or module that documents its purpose.

**20. Why should functions be reusable?**

Reusable functions reduce duplication, improve testing, and make code easier to maintain.

---

# 19. Quick Cheat Sheet

```python
# Define and call
def greet(name):
    return f"Hello, {name}!"

print(greet("Rahul"))


# Default argument
def power(number, exponent=2):
    return number ** exponent


# Positional and keyword arguments
power(3, 3)
power(number=3, exponent=3)


# Variable positional arguments
def add_all(*args):
    return sum(args)


# Variable keyword arguments
def show_data(**kwargs):
    return kwargs


# Multiple return values
def calculate(a, b):
    return a + b, a - b


# Local variable
def example():
    message = "Local"
    return message


# Lambda
square = lambda x: x ** 2


# Recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Higher-order function
def apply_function(function, value):
    return function(value)


# Type hints and docstring
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
```

---

# 20. Final Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Define and call functions.
- [ ] Explain parameters versus arguments.
- [ ] Use positional and keyword arguments correctly.
- [ ] Create functions with default parameters.
- [ ] Explain and use `*args` and `**kwargs`.
- [ ] Return values instead of relying only on `print()`.
- [ ] Explain local, enclosing, global, and built-in scopes.
- [ ] Use `global` and `nonlocal` appropriately.
- [ ] Write simple lambda functions.
- [ ] Implement recursion with a correct base case.
- [ ] Pass functions as arguments and return functions.
- [ ] Use `map()`, `filter()`, and `sorted()` with key functions.
- [ ] Add useful type hints and docstrings.
- [ ] Design small, reusable functions with clear inputs and outputs.
- [ ] Solve at least five exercises without copying the code.

## Suggested one-hour practice session

- **10 minutes:** Function definitions, parameters, and arguments.
- **10 minutes:** Defaults, `*args`, `**kwargs`, and return values.
- **10 minutes:** Scope and namespaces.
- **10 minutes:** Lambda and higher-order functions.
- **10 minutes:** Recursion, type hints, and docstrings.
- **10 minutes:** Write and test two reusable functions from scratch.

**The most important concepts to master:** `return`, argument handling, mutable default arguments, scope, first-class functions, and reusable function design. Once these are comfortable, move on to exception handling and file handling, and keep practicing by writing small functions rather than only reading examples.