# Python Revision — Topic 9: Exception Handling

## 1. What Is Exception Handling?

An exception is an event that occurs during program execution and interrupts the normal flow of instructions.

Exception handling allows you to detect and respond to certain runtime problems so that your program can fail gracefully or recover when appropriate.

For example, a program might encounter:
- A user entering text when a number is required.
- A file that does not exist.
- Division by zero.
- Invalid data received from an API.
- A network connection that times out.

Python provides `try`, `except`, `else`, `finally`, and `raise` to help handle these situations.

### Example without exception handling

```python
number = int(input("Enter a number: "))
print(100 / number)
```

If the user enters `"hello"`, Python raises `ValueError`.

If the user enters `0`, Python raises `ZeroDivisionError`.

### Example with exception handling

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("The number cannot be zero.")

else:
    print("Result:", result)
```

This program handles two specific errors and displays a meaningful message.

**Important:** Exception handling should handle expected problems, not conceal programming mistakes.

---

## 2. Syntax Errors vs. Runtime Errors

Errors can occur at different stages of a program.

### 2.1 Syntax errors

A syntax error occurs when code violates Python's grammatical rules.

Example:

```python
if True
    print("Hello")
```

Python raises a `SyntaxError` because the colon is missing after the condition.

Correct version:

```python
if True:
    print("Hello")
```

Other examples of syntax problems include:
- Missing parentheses.
- Missing colons after statements that require them.
- Incorrect indentation that violates Python's syntax rules.
- Unclosed string literals.

Example:

```python
# print("Hello)
```

The string is not closed, so Python cannot parse the code.

### 2.2 Runtime errors and exceptions

Runtime errors occur while the program is running.

Example:

```python
number = 10
result = number / 0
```

Python raises:

```text
ZeroDivisionError: division by zero
```

The code is syntactically valid, but the operation is invalid.

Another example:

```python
numbers = [10, 20, 30]
print(numbers[10])
```

This raises `IndexError` because the requested index does not exist.

### 2.3 Logical errors

A logical error occurs when the program runs but produces the wrong result.

```python
length = 10
width = 5

area = length + width  # Incorrect formula
print(area)
```

Output:

```text
15
```

The code runs successfully, but the area of a rectangle should be `length * width`, which equals `50`.

Logical errors are usually found through testing, debugging, and checking expected results rather than through exception handling.

### Quick comparison

| Error type | When detected | Example |
|---|---|---|
| Syntax error | While parsing or compiling code | Missing colon |
| Runtime exception | During execution | Division by zero |
| Logical error | When checking program behavior | Incorrect calculation |

**Note:** Many built-in exceptions can be handled with `try` and `except`. A syntax error in the same code block generally prevents that block from being parsed, so its own `try` statement cannot catch it.

---

## 3. Common Built-in Exceptions

Python has many built-in exception classes. Learn the ones you are likely to encounter in everyday programming.

### 3.1 `ValueError`

Raised when a value has the correct general type but is unsuitable for an operation.

```python
number = int("hello")
```

Example error:

```text
ValueError: invalid literal for int()
```

### 3.2 `TypeError`

Raised when an operation or function receives an inappropriate type.

```python
result = "10" + 5
```

Python cannot directly concatenate a string and an integer using `+`.

### 3.3 `ZeroDivisionError`

Raised when dividing by zero.

```python
print(10 / 0)
```

### 3.4 `IndexError`

Raised when a sequence index is out of range.

```python
items = [10, 20, 30]
print(items[5])
```

### 3.5 `KeyError`

Raised when a dictionary lookup requests a missing key.

```python
student = {"name": "Rahul"}
print(student["age"])
```

If a missing key is expected, consider using:

```python
print(student.get("age", "Unknown"))
```

### 3.6 `NameError`

Raised when Python cannot find a name in the applicable scopes.

```python
print(username)
```

If `username` has not been defined, Python raises `NameError`.

### 3.7 `AttributeError`

Raised when an object does not have the requested attribute.

```python
number = 10
number.append(20)
```

Integers do not have an `append()` method.

### 3.8 `FileNotFoundError`

Raised when a requested file cannot be found.

```python
with open("missing_file.txt", "r") as file:
    content = file.read()
```

### 3.9 `PermissionError`

Raised when an operation is not permitted because of insufficient permissions.

```python
# Example: attempting to open a protected file
# may raise PermissionError.
```

The exact result depends on the operating system and the file's permissions.

### 3.10 `ImportError` and `ModuleNotFoundError`

`ImportError` indicates a problem importing a module or a name from a module.

`ModuleNotFoundError` is a subclass of `ImportError` that is commonly raised when Python cannot find a requested module.

```python
import module_that_does_not_exist
```

### 3.11 `OSError`

`OSError` is a base class for many operating-system-related errors, including some file and network-related failures.

More specific subclasses, such as `FileNotFoundError` and `PermissionError`, provide more precise information.

### 3.12 `AssertionError`

Raised when an assertion fails.

```python
age = 15

assert age >= 18, "Age must be at least 18"
```

Assertions are primarily debugging aids and should not be used as the only validation for untrusted input because Python can disable them with optimization options.

### 3.13 `RuntimeError`

A general exception raised when an error does not fit a more specific built-in category.

### 3.14 `TimeoutError`

A subclass of `OSError` used for certain operations that exceed a time limit.

It may occur in file, operating-system, or network-related operations depending on the API used.

### Useful reference table

| Exception | Common cause |
|---|---|
| `ValueError` | Invalid value |
| `TypeError` | Incompatible type |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid sequence index |
| `KeyError` | Missing dictionary key |
| `NameError` | Undefined name |
| `AttributeError` | Missing object attribute |
| `FileNotFoundError` | File does not exist |
| `PermissionError` | Operation is not permitted |
| `ImportError` | Import operation failed |
| `ModuleNotFoundError` | Module cannot be found |
| `AssertionError` | Assertion condition is false |
| `OSError` | Operating-system-related failure |
| `TimeoutError` | Operation timed out |

---

## 4. The `try` and `except` Blocks

Use `try` to enclose code that may raise an exception and `except` to handle selected exceptions.

### Basic syntax

```python
try:
    # Code that may raise an exception
    risky_operation()

except SomeException:
    # Handle the selected exception
    handle_error()
```

### Example: Convert input to an integer

```python
try:
    number = int(input("Enter an integer: "))
    print("Number:", number)

except ValueError:
    print("Invalid input. Please enter an integer.")
```

If the user enters `25`, the program prints:

```text
Number: 25
```

If the user enters `hello`, the exception handler runs.

### Example: Divide two numbers

```python
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Both inputs must be integers.")

else:
    print("Result:", result)
```

This handles invalid integer input separately from division by zero.

### Important execution rule

When an exception occurs inside the `try` block:
1. Python stops executing the remaining statements in that block.
2. Python looks for a matching `except` handler.
3. If a matching handler exists, it executes that handler.
4. If no handler matches, the exception propagates to a caller or terminates the program if unhandled.

A handler does not automatically restart the `try` block.

---

## 5. Handling Multiple Exceptions

You can handle different exceptions in separate handlers or group exception types into one handler.

### 5.1 Separate handlers

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Enter a valid integer.")

except ZeroDivisionError:
    print("Zero is not allowed.")

else:
    print("Result:", result)
```

Separate handlers allow you to respond differently to each problem.

### 5.2 One handler for multiple exception types

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("The input or calculation is invalid.")
```

The exception types are provided as a tuple.

### 5.3 Handling a base exception class

You can catch a base class when you intentionally want to handle a category of exceptions.

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

except OSError as error:
    print("A file or operating-system error occurred.")
```

This can handle many operating-system-related errors, including file-not-found and permission errors.

However, it may also catch errors you intended to handle differently. Use a narrower exception class when you know the expected failure.

### 5.4 Accessing the exception object

Use `as` to bind the exception instance to a variable.

```python
try:
    number = int("hello")

except ValueError as error:
    print("Conversion failed:", error)
```

Possible output:

```text
Conversion failed: invalid literal for int() with base 10: 'hello'
```

The precise wording may differ between Python versions.

**Best practice:** Catch only the exceptions you know how to handle. Avoid catching every possible exception just to make the program continue.

---

## 6. The `else` Block

The `else` block runs only if the `try` block completes without raising an exception.

### Syntax

```python
try:
    risky_operation()

except SomeException:
    handle_error()

else:
    handle_success()
```

### Example

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid integer.")

else:
    print("Conversion successful:", number)
```

If conversion succeeds, `else` executes. If `ValueError` occurs, the `except` handler executes instead.

### Why use `else`?

It separates successful operations from error-handling logic.

```python
try:
    file = open("data.txt", "r", encoding="utf-8")

except FileNotFoundError:
    print("The file does not exist.")

else:
    try:
        content = file.read()
        print(content)
    finally:
        file.close()
```

This example works, but `with open(...)` is usually the better way to manage files because it closes them automatically.

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("The file does not exist.")

else:
    print(content)
```

---

## 7. The `finally` Block

The `finally` block executes when control leaves the associated `try` statement, whether execution succeeds, an exception is handled, or an exception propagates.

It is commonly used for cleanup.

### Example

```python
try:
    number = int("25")
    print(number)

except ValueError:
    print("Invalid value.")

finally:
    print("Execution reached cleanup.")
```

Output:

```text
25
Execution reached cleanup.
```

### Example with an exception

```python
try:
    number = int("hello")

except ValueError:
    print("Conversion failed.")

finally:
    print("Cleanup code executed.")
```

Output:

```text
Conversion failed.
Cleanup code executed.
```

### Common use cases

The `finally` block can be useful for:
- Releasing certain resources.
- Closing manually managed files.
- Cleaning up temporary state.
- Releasing a lock when appropriate.

For resources that support context managers, prefer `with` whenever possible.

### `try`, `except`, `else`, and `finally` together

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Calculation attempt finished.")
```

Remember:

- `try`: Code that may raise an exception.
- `except`: Handles a matching exception.
- `else`: Runs when the `try` block succeeds without an exception.
- `finally`: Runs during normal control-flow cleanup, including when an exception is propagating.

**Important:** `finally` does not guarantee execution if the process is forcibly terminated or the interpreter exits abruptly. Avoid using `return` inside `finally`, because it can suppress a pending exception or override an earlier return value.

---

## 8. Raising Exceptions with `raise`

The `raise` statement allows you to deliberately signal an error.

Use it when a function receives invalid input or cannot perform the requested operation.

### Example: Raise `ValueError`

```python
def calculate_square_root_input(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")

    return number ** 0.5


print(calculate_square_root_input(25))
```

Output:

```text
5.0
```

Calling `calculate_square_root_input(-5)` raises `ValueError`.

### Example: Validate age

```python
def register_user(age: int) -> str:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        return "Registration requires an adult."

    return "Registration allowed."


print(register_user(21))
```

The function rejects impossible age values and returns a result for valid values.

### Re-raising an exception

Inside an exception handler, a bare `raise` re-raises the current exception.

```python
try:
    number = int("hello")

except ValueError:
    print("Conversion failed; propagating the error.")
    raise
```

This logs or displays a message and then allows the original exception to continue propagating.

In production code, avoid printing raw exception details to a public interface. Use appropriate logging and show users a safe, understandable message.

### Exception chaining

If you want to raise a different exception while preserving the original cause, use `raise ... from ...`.

```python
def parse_age(value):
    try:
        return int(value)

    except ValueError as error:
        raise ValueError("Age must be an integer.") from error
```

The original conversion error is preserved as the cause.

This is useful when building a clearer interface around lower-level errors.

---

## 9. Creating Custom Exceptions

Custom exceptions allow you to represent application-specific failures with meaningful names.

They are especially useful in larger projects where different error types need different handling.

### Basic custom exception

```python
class InvalidAgeError(Exception):
    """Raised when an age value is invalid."""


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    return age


try:
    validate_age(-5)

except InvalidAgeError as error:
    print("Validation error:", error)
```

Output:

```text
Validation error: Age cannot be negative.
```

### Why inherit from `Exception`?

Most user-defined exceptions should inherit from `Exception` or an appropriate subclass.

Avoid inheriting directly from `BaseException` for ordinary application errors. `BaseException` also includes special control-flow exceptions such as `KeyboardInterrupt` and `SystemExit`.

### Custom exception with additional information

```python
class InsufficientBalanceError(Exception):
    """Raised when an account lacks sufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Insufficient balance: {balance} available, "
            f"{amount} requested."
        )


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError(balance, amount)

    return balance - amount


try:
    withdraw(500, 800)

except InsufficientBalanceError as error:
    print(error)
    print("Available balance:", error.balance)
```

This allows code to handle the business-specific failure separately from ordinary invalid arguments.

### When should you create a custom exception?

Create one when:
- The error has a clear meaning in your application.
- Callers need to distinguish it from other errors.
- You want to attach useful structured information.
- The same failure type is used across multiple functions.

For a simple script, a suitable built-in exception may be enough.

---

## 10. Understanding and Debugging Tracebacks

A traceback shows the sequence of calls that led to an unhandled exception.

Example:

```python
def divide(a, b):
    return a / b


def calculate():
    return divide(10, 0)


calculate()
```

A simplified traceback looks like this:

```text
Traceback (most recent call last):
  ...
  File "example.py", line ..., in <module>
    calculate()
  File "example.py", line ..., in calculate
    return divide(10, 0)
  File "example.py", line ..., in divide
    return a / b
ZeroDivisionError: division by zero
```

Exact file names, line numbers, and formatting depend on where and how you run the code.

### How to read a traceback

1. **Start at the bottom:** Identify the exception type and message.
2. **Find the last relevant frame:** Locate the line where the exception occurred.
3. **Follow the frames upward:** See which functions called one another.
4. **Inspect the values:** Check whether arguments and variables contain what you expect.
5. **Reproduce the problem:** Create a small test case if possible.
6. **Fix the cause:** Avoid merely hiding the exception.

### Example: Debugging an index error

```python
def get_first_item(items):
    return items[0]


print(get_first_item([]))
```

The traceback identifies the indexing line. The function assumes the list contains at least one item, but the input is empty.

A safer implementation depends on the intended behavior:

```python
def get_first_item(items):
    if not items:
        return None

    return items[0]
```

Alternatively, if an empty list represents invalid input, raise a meaningful exception:

```python
def get_first_item(items):
    if not items:
        raise ValueError("items must not be empty")

    return items[0]
```

Neither behavior is universally correct. Choose the one that matches the function's contract.

### Using `traceback` in Python

```python
import traceback

try:
    number = int("hello")

except ValueError:
    traceback.print_exc()
```

`traceback.print_exc()` prints the active exception's traceback, which is useful for debugging. In a production application, use the logging system to record tracebacks in an appropriate destination.

---

## 11. Avoiding Overly Broad Exception Handling

A common beginner mistake is catching every exception and ignoring it.

### Bad practice

```python
try:
    result = 10 / 0

except:
    pass
```

Problems:
- The error is silently ignored.
- Programming mistakes can go unnoticed.
- The program may continue with invalid or missing data.
- Debugging becomes difficult.

A bare `except:` can catch exceptions derived from `BaseException`, including some special control-flow exceptions.

### Better approach: Catch a specific exception

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Catch a small group when appropriate

```python
try:
    number = int(input("Enter an integer: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("The input or calculation is invalid.")
```

### When is `except Exception` acceptable?

Sometimes a top-level application boundary needs to log an unexpected failure and present a safe message.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    run_application()

except Exception:
    logging.exception("Unexpected application failure.")
    print("An unexpected error occurred. Please try again.")
```

Here, `run_application()` is a placeholder for your actual application function.

This pattern can be appropriate at a deliberate application boundary, provided the error is logged, the user receives a safe message, and the program does not continue as if the operation succeeded.

Do not wrap every individual line of code in `except Exception`.

**Rule of thumb:** Catch an exception only when you can handle it, add useful context, clean up resources, or deliberately report and propagate it.

---

## 12. Safe Error Messages and Logging

Programs often need to show errors to users while retaining enough diagnostic information for developers.

These are two different goals.

### 12.1 Safe messages for users

Users generally need to know:
- What went wrong in understandable terms.
- Whether their action succeeded.
- What they can do next.

Example:

```python
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter your age as a whole number.")
```

This is more helpful than displaying an entire traceback to an ordinary user.

### 12.2 Use logging for diagnostics

Python's `logging` module supports different severity levels.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logging.debug("Detailed diagnostic information")
logging.info("Application started")
logging.warning("An unusual condition occurred")
logging.error("An operation failed")
logging.critical("A serious failure occurred")
```

The common logging levels are:

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed diagnostic information |
| `INFO` | Normal application events |
| `WARNING` | Unexpected or potentially problematic situations |
| `ERROR` | An operation failed |
| `CRITICAL` | A severe failure that may prevent continued operation |

With `level=logging.INFO`, debug messages are normally filtered out.

### 12.3 Log exceptions with a traceback

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    number = int("hello")

except ValueError:
    logging.exception("Could not convert input to an integer.")
    print("Invalid input. Please enter a whole number.")
```

`logging.exception()` is intended for use inside an exception handler and includes traceback information at the error level.

For expected user mistakes, you may not need a full traceback every time. Logging should be proportionate to the situation.

### 12.4 Avoid exposing sensitive information

Do not include passwords, API keys, session tokens, private personal data, or other secrets in logs or public error messages.

For example, avoid logging an entire request object if it may contain authorization headers or cookies.

Prefer:

```python
logging.warning("Authentication failed for the attempted operation.")
```

over logging raw credentials or secret-bearing request data.

### 12.5 Do not discard useful debugging information

Bad:

```python
try:
    process_data()

except Exception:
    print("Something went wrong.")
```

This may hide the reason for failure.

Better at a suitable application boundary:

```python
import logging

logger = logging.getLogger(__name__)

try:
    process_data()

except Exception:
    logger.exception("Data processing failed.")
    print("Unable to process the data right now.")
```

The example assumes that `process_data()` is defined elsewhere. Catching `Exception` is intentional here only as a final boundary; lower-level functions should normally handle specific failures or allow them to propagate.

---

## 13. Practical Example: Safe Integer Input

The following function repeatedly asks the user for an integer until valid input is supplied.

```python
def get_integer(prompt):
    while True:
        value = input(prompt)

        try:
            return int(value)

        except ValueError:
            print("Invalid input. Please enter an integer.")


number = get_integer("Enter a number: ")
print("You entered:", number)
```

This example combines:
- A reusable function.
- A loop.
- Exception handling.
- A meaningful error message.
- Returning a value instead of printing the value inside the helper function.

If you need to restrict the accepted range, add explicit validation after conversion.

```python
def get_positive_integer(prompt):
    while True:
        value = input(prompt)

        try:
            number = int(value)

        except ValueError:
            print("Enter a valid integer.")
            continue

        if number <= 0:
            print("The number must be positive.")
            continue

        return number
```

This distinguishes conversion failures from valid integers that do not meet the application's requirements.

---

## 14. Practical Example: Safe File Handling

Reading a file can fail for several reasons, including a missing path or insufficient permissions.

```python
from pathlib import Path
import logging

logging.basicConfig(level=logging.ERROR)

def read_text_file(path: str) -> str | None:
    """Read a UTF-8 text file, returning None for expected file errors."""

    try:
        return Path(path).read_text(encoding="utf-8")

    except FileNotFoundError:
        logging.warning("Requested text file was not found.")
        print("The requested file does not exist.")
        return None

    except PermissionError:
        logging.warning("Permission denied while reading a text file.")
        print("You do not have permission to read this file.")
        return None

    except UnicodeDecodeError:
        logging.warning("Text file could not be decoded as UTF-8.")
        print("The file is not valid UTF-8 text.")
        return None


content = read_text_file("notes.txt")

if content is not None:
    print(content)
```

This function handles three anticipated failure types. Other failures, such as some filesystem errors, may still propagate.

The return type `str | None` indicates that the function returns text on success or `None` for the handled failures. This syntax requires Python 3.10 or newer.

---

## 15. Practical Example: Validate Data with a Custom Exception

```python
class InvalidPortError(ValueError):
    """Raised when a TCP or UDP port number is outside the valid range."""


def validate_port(port: int) -> int:
    """
    Validate a port number.

    Valid port numbers range from 1 to 65535.
    """
    if not 1 <= port <= 65535:
        raise InvalidPortError("Port must be between 1 and 65535.")

    return port


try:
    port = validate_port(443)
    print("Valid port:", port)

except InvalidPortError as error:
    print("Invalid port:", error)
```

Output:

```text
Valid port: 443
```

A custom exception that subclasses `ValueError` allows callers to catch either the specific `InvalidPortError` or the broader `ValueError` category.

This validates the numeric range only. Whether a port is open or whether you are authorized to test a service is a separate matter.

---

## 16. Common Mistakes to Avoid

1. **Catching everything:** Prefer specific exception types where possible.
2. **Using `pass` to hide failures:** Silent failure makes debugging difficult.
3. **Putting too much code inside `try`:** Keep the protected section focused so unrelated failures are not accidentally caught.
4. **Confusing syntax and runtime errors:** A syntax error prevents invalid code from being parsed.
5. **Using `else` incorrectly:** It executes only when the `try` block completes without an exception.
6. **Misusing `finally`:** Use it for cleanup, not to suppress exceptions.
7. **Raising generic exceptions unnecessarily:** Prefer suitable built-in exceptions or meaningful custom subclasses.
8. **Losing the original cause:** Use `raise ... from error` when translating exceptions and preserving the cause is helpful.
9. **Exposing tracebacks to ordinary users:** Keep technical diagnostics in appropriate logs.
10. **Logging secrets:** Never log passwords, tokens, or sensitive request data.
11. **Continuing after a failed operation as if it succeeded:** Make failure explicit through return values, exceptions, or a documented result type.
12. **Using assertions for user input validation:** Assertions can be disabled and are not a substitute for explicit validation.

---

# 17. Practice Exercises

Try writing these yourself before consulting the examples.

## Beginner Level

1. Write a program that converts user input to an integer and handles `ValueError`.
2. Write a program that divides two integers and handles `ZeroDivisionError`.
3. Create a list and safely handle an `IndexError`.
4. Access a missing dictionary key and handle `KeyError`.
5. Open a text file and handle `FileNotFoundError`.
6. Write a function that validates whether a number is positive.
7. Demonstrate the difference between a syntax error and a runtime exception.
8. Write a program using `try`, `except`, and `else`.
9. Write a program using `finally` to report that cleanup was reached.
10. Raise a `ValueError` when a function receives a negative number.

## Intermediate Level

11. Write a calculator that handles invalid input and division by zero.
12. Handle `ValueError` and `ZeroDivisionError` in separate handlers.
13. Handle multiple related exceptions in one `except` clause.
14. Create a custom exception called `InvalidAgeError`.
15. Create a custom exception for an invalid port number.
16. Re-raise an exception after logging diagnostic information.
17. Translate a low-level `ValueError` into