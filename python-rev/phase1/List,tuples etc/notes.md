# Python Revision — Topic 7: Lists, Tuples, Sets, and Dictionaries

## 1. Introduction to Python Collections

Python provides several built-in data structures for storing and organizing multiple values.

| Data Structure | Ordered | Mutable | Allows Duplicates | Syntax |
|---|---|---|---|---|
| List | Yes | Yes | Yes | `[]` |
| Tuple | Yes | No | Yes | `()` |
| Set | No guaranteed order | Yes | No | `{}` or `set()` |
| Dictionary | Yes (insertion order) | Yes | Keys must be unique | `{key: value}` |

**Important:** A dictionary preserves insertion order in modern Python. A set does not guarantee a meaningful iteration order.

### When should you use each one?

- **List:** When you need an ordered collection that can change.
- **Tuple:** When you need a fixed collection of values.
- **Set:** When you need unique values or set operations.
- **Dictionary:** When you need to associate keys with values.

Example:

```python
names = ["Rahul", "Amit", "Priya"]  # List

coordinates = (10, 20)              # Tuple

unique_numbers = {1, 2, 3, 4}       # Set

student = {
    "name": "Rahul",
    "age": 21
}                                   # Dictionary
```

---

# Part 1: Lists

## 2. Creating Lists

A list stores multiple items in a single variable.

```python
numbers = [10, 20, 30, 40]
names = ["Rahul", "Amit", "Priya"]
mixed = [10, "Python", 3.14, True]
empty_list = []
```

A list can contain different data types, although using a consistent type is often easier to maintain.

You can also create a list using `list()`.

```python
numbers = list((10, 20, 30))
letters = list("Python")

print(numbers)
print(letters)
```

Output:

```text
[10, 20, 30]
['P', 'y', 't', 'h', 'o', 'n']
```

## 3. Accessing List Elements

Python uses zero-based indexing.

```python
languages = ["Python", "Java", "C++", "JavaScript"]

print(languages[0])
print(languages[1])
print(languages[-1])
print(languages[-2])
```

Output:

```text
Python
Java
JavaScript
C++
```

Positive indexing starts from `0`, while negative indexing starts from `-1` at the end.

```text
List:     ["Python", "Java", "C++", "JavaScript"]
Positive:     0        1      2          3
Negative:    -4       -3     -2         -1
```

### Modifying list elements

Lists are mutable, so their elements can be changed.

```python
numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)
```

Output:

```text
[10, 99, 30]
```

### Common mistake: IndexError

```python
numbers = [10, 20, 30]

print(numbers[5])
```

This raises `IndexError` because index `5` does not exist.

Use `len()` to check the length:

```python
print(len(numbers))  # 3
```

Valid positive indexes range from `0` to `len(numbers) - 1`.

## 4. List Slicing

Slicing extracts a portion of a list.

Syntax:

```python
list[start:stop:step]
```

- `start`: Index where slicing begins; included.
- `stop`: Index where slicing ends; excluded.
- `step`: Number of positions to move each time.

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
[20, 30, 40]
[10, 20, 30]
[40, 50, 60]
[10, 30, 50]
[60, 50, 40, 30, 20, 10]
```

Useful slicing patterns:

```python
items = [1, 2, 3, 4, 5]

items[:]
items[1:4]
items[-3:]
items[:-1]
items[::2]
items[::-1]
```

**Important:** A slice normally creates a new, shallow list rather than returning the original list object.

```python
original = [1, 2, 3]
copied = original[:]

copied[0] = 99

print(original)  # [1, 2, 3]
print(copied)   # [99, 2, 3]
```

For nested lists, however, a slice does not independently copy the inner lists. This is explained later.

## 5. Important List Methods

### `append()`

Adds one element to the end.

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

Appending another list adds that list as a single nested element.

```python
numbers = [1, 2]
numbers.append([3, 4])

print(numbers)
```

Output:

```text
[1, 2, [3, 4]]
```

### `extend()`

Adds each element from an iterable to the list.

```python
numbers = [1, 2]
numbers.extend([3, 4])

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

**Difference between `append()` and `extend()`:**

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]
```

### `insert()`

Inserts an element at a specified index.

```python
numbers = [10, 30, 40]
numbers.insert(1, 20)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### `remove()`

Removes the first matching value.

```python
numbers = [10, 20, 20, 30]
numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

If the value does not exist, `remove()` raises `ValueError`.

### `pop()`

Removes and returns an element. If no index is provided, it removes the last element.

```python
numbers = [10, 20, 30]

last = numbers.pop()
first = numbers.pop(0)

print(last)
print(first)
print(numbers)
```

Output:

```text
30
10
[20]
```

### `clear()`

Removes all elements.

```python
numbers = [1, 2, 3]
numbers.clear()

print(numbers)  # []
```

### `index()`

Returns the index of the first matching value.

```python
names = ["Amit", "Rahul", "Priya"]

print(names.index("Rahul"))  # 1
```

### `count()`

Counts how many times a value appears.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))  # 3
```

### `sort()`

Sorts a list in place.

```python
numbers = [5, 2, 8, 1]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

Output:

```text
[1, 2, 5, 8]
[8, 5, 2, 1]
```

For strings:

```python
names = ["Rahul", "Amit", "Priya"]
names.sort()

print(names)
```

Output:

```text
['Amit', 'Priya', 'Rahul']
```

### `reverse()`

Reverses the list in place.

```python
numbers = [1, 2, 3]
numbers.reverse()

print(numbers)  # [3, 2, 1]
```

### `copy()`

Creates a shallow copy of the list.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

### `len()`, `min()`, `max()`, and `sum()`

These are built-in functions, not list methods.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))  # 4
print(min(numbers))  # 10
print(max(numbers))  # 40
print(sum(numbers))  # 100
```

### Important method rule

Many list methods modify the list in place and return `None`.

Incorrect:

```python
numbers = [3, 1, 2]
numbers = numbers.sort()

print(numbers)  # None
```

Correct:

```python
numbers = [3, 1, 2]
numbers.sort()

print(numbers)  # [1, 2, 3]
```

If you need a sorted copy without changing the original, use `sorted()`:

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(numbers)  # [3, 1, 2]
print(result)   # [1, 2, 3]
```

## 6. List Comprehensions

A list comprehension creates a list from an iterable using a compact expression.

General syntax:

```python
[expression for item in iterable]
```

### Example 1: Create a list of squares

```python
squares = [x ** 2 for x in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Equivalent traditional loop:

```python
squares = []

for x in range(1, 6):
    squares.append(x ** 2)
```

### Example 2: Filtering values

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

### Example 3: Transforming strings

```python
names = ["rahul", "amit", "priya"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)
```

Output:

```text
['RAHUL', 'AMIT', 'PRIYA']
```

### Example 4: Conditional expressions

```python
results = [
    "Pass" if marks >= 40 else "Fail"
    for marks in [75, 32, 60, 25]
]

print(results)
```

Output:

```text
['Pass', 'Fail', 'Pass', 'Fail']
```

### Example 5: Nested loops

```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]

print(pairs)
```

Output:

```text
[(1, 3), (1, 4), (2, 3), (2, 4)]
```

**Best practice:** Use comprehensions when the logic is clear. If the expression becomes complicated, use a normal loop for readability.

## 7. Nested Lists

A nested list is a list that contains other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access elements using multiple indexes:

```python
print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6
print(matrix[2][0])  # 7
```

The first index chooses the inner list; the second chooses the element inside it.

### Iterating through a nested list

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in matrix:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
5
6
```

### Common nested-list mistake

Incorrect:

```python
matrix = [[0] * 3] * 3
matrix[0][0] = 99

print(matrix)
```

Output:

```text
[[99, 0, 0], [99, 0, 0], [99, 0, 0]]
```

All three rows refer to the same inner list.

Correct:

```python
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 99

print(matrix)
```

Output:

```text
[[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

# Part 2: Tuples

## 8. Creating Tuples

A tuple is an ordered collection that cannot be modified after creation.

```python
numbers = (10, 20, 30)
names = ("Rahul", "Amit", "Priya")
mixed = (10, "Python", True)
empty_tuple = ()
```

Tuples support indexing, slicing, iteration, and duplicate values.

```python
coordinates = (10, 20, 30)

print(coordinates[0])    # 10
print(coordinates[-1])   # 30
print(coordinates[1:])   # (20, 30)
```

### Creating a one-element tuple

A comma is required.

```python
a = (10)
b = (10,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>
```

Parentheses alone do not create a tuple; the comma does.

You can also create a tuple from an iterable:

```python
numbers = tuple([1, 2, 3])

print(numbers)  # (1, 2, 3)
```

## 9. Tuple Immutability

You cannot replace, add, or remove tuple elements after creation.

```python
numbers = (10, 20, 30)

numbers[0] = 99  # TypeError
```

However, a tuple may contain a mutable object, such as a list. The contained list can still change.

```python
data = (1, [2, 3], 4)

data[1].append(99)

print(data)
```

Output:

```text
(1, [2, 3, 99], 4)
```

The tuple's references cannot be reassigned, but the list object it refers to can be modified.

## 10. Tuple Methods

Tuples have two main methods.

### `count()`

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))  # 3
```

### `index()`

```python
names = ("Amit", "Rahul", "Priya")

print(names.index("Rahul"))  # 1
```

For more extensive modification, convert the tuple into a list:

```python
numbers = (1, 2, 3)

temp = list(numbers)
temp.append(4)

numbers = tuple(temp)

print(numbers)  # (1, 2, 3, 4)
```

## 11. Tuple Unpacking

Unpacking assigns individual tuple elements to variables.

```python
person = ("Rahul", 21, "India")

name, age, country = person

print(name)
print(age)
print(country)
```

Output:

```text
Rahul
21
India
```

The number of variables must normally match the number of unpacked elements.

### Extended unpacking with `*`

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

The starred variable receives a list.

### Swapping variables

```python
a = 10
b = 20

a, b = b, a

print(a, b)  # 20 10
```

This is a common Python idiom.

### Returning multiple values from a function

```python
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)      # 15
print(subtraction)   # 5
```

Python packages multiple returned values into a tuple, which can then be unpacked.

---

# Part 3: Sets

## 12. Creating Sets

A set is a mutable collection of unique, hashable elements.

```python
numbers = {1, 2, 3, 4}
names = {"Rahul", "Amit", "Priya"}
empty_set = set()
```

Repeated values are automatically removed.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)  # {1, 2, 3} (display order may vary)
```

**Important:** `{}` creates an empty dictionary, not an empty set.

```python
a = {}
b = set()

print(type(a))  # <class 'dict'>
print(type(b))  # <class 'set'>
```

Sets do not support indexing or slicing.

```python
numbers = {10, 20, 30}

# numbers[0]  # TypeError
```

To examine elements, iterate over the set:

```python
for number in numbers:
    print(number)
```

The iteration order should not be relied upon.

## 13. Adding and Removing Set Elements

### `add()`

Adds one element.

```python
numbers = {1, 2, 3}
numbers.add(4)

print(numbers)
```

### `update()`

Adds elements from an iterable.

```python
numbers = {1, 2}
numbers.update([3, 4, 5])

print(numbers)
```

### `remove()`

Removes an element. Raises `KeyError` if the element is absent.

```python
numbers = {1, 2, 3}
numbers.remove(2)

print(numbers)  # {1, 3}
```

### `discard()`

Removes an element if present without raising an error if it is absent.

```python
numbers = {1, 2, 3}
numbers.discard(99)

print(numbers)  # {1, 2, 3}
```

### `pop()`

Removes and returns an arbitrary set element. Do not assume which element will be removed.

```python
numbers = {10, 20, 30}
removed = numbers.pop()

print(removed)
print(numbers)
```

### `clear()`

Removes all elements.

```python
numbers = {1, 2, 3}
numbers.clear()

print(numbers)  # set()
```

## 14. Set Operations

Set operations are especially useful for comparing collections and removing duplicates.

Let:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union: `|`

Returns all unique elements from both sets.

```python
print(A | B)
```

Result:

```text
{1, 2, 3, 4, 5, 6}
```

Method form:

```python
A.union(B)
```

### Intersection: `&`

Returns elements common to both sets.

```python
print(A & B)
```

Result:

```text
{3, 4}
```

Method form:

```python
A.intersection(B)
```

### Difference: `-`

Returns elements in the first set but not in the second.

```python
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
```

Method form:

```python
A.difference(B)
```

**Important:** Difference is directional. `A - B` is not generally the same as `B - A`.

### Symmetric difference: `^`

Returns elements found in either set, but not in both.

```python
print(A ^ B)
```

Result:

```text
{1, 2, 5, 6}
```

Method form:

```python
A.symmetric_difference(B)
```

### Subset: `<=`

Checks whether all elements of one set exist in another.

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A <= B)  # True
```

### Superset: `>=`

Checks whether a set contains all elements of another.

```python
print(B >= A)  # True
```

### Disjoint sets

Two sets are disjoint if they have no common elements.

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))  # True
```

### Removing duplicates from a list

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

This removes duplicates, but it does not preserve the original order. If order matters, use:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)  # [1, 2, 3, 4]
```

**Set limitation:** Elements must be hashable. Lists and dictionaries cannot be elements of a set, but tuples containing only hashable elements can be used.

---

# Part 4: Dictionaries

## 15. Creating Dictionaries

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}
```

- A **key** identifies a value.
- A **value** stores the associated data.
- Keys must be unique and hashable.
- Values can be of different types.

You can also create an empty dictionary:

```python
student = {}
```

Or use `dict()`:

```python
student = dict(name="Rahul", age=21)

print(student)
```

Output:

```text
{'name': 'Rahul', 'age': 21}
```

If a dictionary literal contains the same key more than once, the last value wins.

```python
data = {"age": 20, "age": 21}

print(data)  # {'age': 21}
```

## 16. Accessing Dictionary Values

Use the key to retrieve its value.

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student["name"])  # Rahul
print(student["age"])   # 21
```

If the key does not exist, square-bracket lookup raises `KeyError`.

### Using `get()`

`get()` allows a default value if a key is missing.

```python
student = {"name": "Rahul"}

print(student.get("name"))          # Rahul
print(student.get("age"))           # None
print(student.get("age", 0))        # 0
```

Use `get()` when a missing key is an expected possibility.

## 17. Adding, Updating, and Deleting Entries

### Add a new key-value pair

```python
student = {"name": "Rahul"}

student["age"] = 21

print(student)
```

### Update an existing value

```python
student = {"name": "Rahul", "age": 20}

student["age"] = 21

print(student)
```

### Update multiple entries with `update()`

```python
student = {"name": "Rahul", "age": 20}

student.update({
    "age": 21,
    "course": "Python"
})

print(student)
```

### Delete an entry with `del`

```python
student = {"name": "Rahul", "age": 21}

del student["age"]

print(student)  # {'name': 'Rahul'}
```

### Remove and return an entry with `pop()`

```python
student = {"name": "Rahul", "age": 21}

age = student.pop("age")

print(age)      # 21
print(student)  # {'name': 'Rahul'}
```

You can supply a default to avoid `KeyError` for a missing key:

```python
student = {"name": "Rahul"}

print(student.pop("age", None))  # None
```

### `popitem()`

Removes and returns the most recently inserted key-value pair.

```python
student = {"name": "Rahul", "age": 21}

item = student.popitem()

print(item)     # ('age', 21)
print(student)  # {'name': 'Rahul'}
```

### `clear()`

Removes all entries.

```python
student = {"name": "Rahul", "age": 21}
student.clear()

print(student)  # {}
```

## 18. Important Dictionary Methods

### `keys()`

Returns a view of the dictionary's keys.

```python
student = {"name": "Rahul", "age": 21}

print(student.keys())
```

### `values()`

Returns a view of the values.

```python
print(student.values())
```

### `items()`

Returns a view of key-value pairs.

```python
print(student.items())
```

Views reflect changes made to the underlying dictionary.

### `setdefault()`

Returns the value for a key. If the key is absent, inserts it with the supplied default and returns that default.

```python
student = {"name": "Rahul"}

result = student.setdefault("age", 21)

print(result)   # 21
print(student)  # {'name': 'Rahul', 'age': 21}
```

If the key already exists, its value is not overwritten.

### `copy()`

Creates a shallow copy.

```python
original = {"name": "Rahul", "age": 21}
copied = original.copy()

copied["age"] = 22

print(original["age"])  # 21
print(copied["age"])    # 22
```

Nested objects remain shared in a shallow copy.

### `len()`

Returns the number of key-value pairs.

```python
student = {"name": "Rahul", "age": 21}

print(len(student))  # 2
```

## 19. Iterating Through Dictionary Keys, Values, and Items

### Iterate through keys

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

for key in student:
    print(key)
```

Iterating directly over a dictionary yields its keys.

You can also write:

```python
for key in student.keys():
    print(key)
```

### Iterate through values

```python
for value in student.values():
    print(value)
```

### Iterate through key-value pairs

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Rahul
age : 21
course : Python
```

### Practical example: Count word frequencies

```python
text = "python is useful and python is popular"

frequency = {}

for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

Output:

```text
{
    'python': 2,
    'is': 2,
    'useful': 1,
    'and': 1,
    'popular': 1
}
```

The dictionary keeps track of how many times each word appears.

### Practical example: Update dictionary values

```python
marks = {
    "Rahul": 75,
    "Amit": 62,
    "Priya": 88
}

for name, score in marks.items():
    print(f"{name} scored {score}")
```

### Important iteration warning

Avoid adding or removing dictionary entries while iterating directly over the same dictionary. It may raise `RuntimeError`.

If you need to remove entries based on a condition, create a separate list of keys first:

```python
scores = {"A": 20, "B": 45, "C": 10}

to_remove = [
    name
    for name, score in scores.items()
    if score < 30
]

for name in to_remove:
    del scores[name]

print(scores)  # {'B': 45}
```

## 20. Dictionary Comprehensions

Dictionary comprehensions create dictionaries concisely.

General syntax:

```python
{key_expression: value_expression for item in iterable}
```

### Example 1: Squares

```python
squares = {x: x ** 2 for x in range(1, 6)}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Example 2: Filtering values

```python
even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)
```

### Example 3: Transforming values

```python
prices = {
    "apple": 50,
    "banana": 20,
    "orange": 40
}

discounted = {
    item: price * 0.9
    for item, price in prices.items()
}

print(discounted)
```

This applies a 10% discount to each price.

### Example 4: Swap keys and values

```python
original = {"a": 1, "b": 2, "c": 3}

reversed_dict = {
    value: key
    for key, value in original.items()
}

print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}
```

This is appropriate only when the values are valid dictionary keys and you are comfortable with any duplicate values becoming duplicate keys.

## 21. Nested Dictionaries

A nested dictionary contains another dictionary as a value.

```python
students = {
    "student1": {
        "name": "Rahul",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "Amit",
        "age": 22,
        "marks": 78
    }
}
```

### Accessing nested values

```python
print(students["student1"]["name"])   # Rahul
print(students["student2"]["marks"])  # 78
```

### Updating nested values

```python
students["student1"]["marks"] = 90

print(students["student1"]["marks"])  # 90
```

### Iterating through nested dictionaries

```python
for student_id, details in students.items():
    print("ID:", student_id)

    for key, value in details.items():
        print(f"{key}: {value}")
```

### Safe nested lookup

When a key may be missing, use `get()` carefully.

```python
student = students.get("student3")

if student is not None:
    print(student.get("name"))
else:
    print("Student not found")
```

Remember that `get()` returns `None` by default for a missing key. If a stored value can itself be `None`, you may need an explicit membership check to distinguish the cases.

---

# Part 5: Unpacking Collections

## 22. Basic Unpacking

Unpacking assigns items from an iterable to multiple variables.

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a, b, c)  # 10 20 30
```

The number of variables must match the number of elements unless extended unpacking is used.

Unpacking works with lists, tuples, and other iterables.

```python
a, b = (1, 2)
x, y = [3, 4]
first, second = "AB"
```

## 23. Extended Unpacking with `*`

The starred target collects remaining elements into a list.

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

You can place the starred variable at different positions:

```python
first, *rest = [1, 2, 3, 4]
*start, last = [1, 2, 3, 4]

print(first, rest)  # 1 [2, 3, 4]
print(start, last)  # [1, 2, 3] 4
```

Only one starred target is allowed in a single unpacking assignment.

## 24. Unpacking in Loops

```python
students = [
    ("Rahul", 85),
    ("Amit", 78),
    ("Priya", 92)
]

for name, marks in students:
    print(f"{name}: {marks}")
```

Output:

```text
Rahul: 85
Amit: 78
Priya: 92
```

This is cleaner than accessing each tuple using indexes.

### Dictionary unpacking with `**`

The `**` operator can unpack a dictionary into keyword arguments.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age}.")

person = {"name": "Rahul", "age": 21}

introduce(**person)
```

Output:

```text
My name is Rahul and I am 21.
```

The dictionary keys must match the function's accepted parameter names unless the function accepts arbitrary keyword arguments.

### List unpacking with `*`

The `*` operator can unpack an iterable into positional arguments.

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers))  # 60
```

### Merging dictionaries with `**`

```python
defaults = {"theme": "dark", "language": "en"}
custom = {"language": "fr"}

settings = {**defaults, **custom}

print(settings)
```

Output:

```text
{'theme': 'dark', 'language': 'fr'}
```

When keys overlap, the later dictionary's value takes precedence.

---

# Part 6: References, Shallow Copies, and Deep Copies

## 25. Variables and Object References

Python variables refer to objects rather than acting as independent containers for values.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

Here, `a` and `b` refer to the same list object.

The assignment:

```python
b = a
```

does not create a new list. It creates another reference to the existing object.

### Checking object identity

```python
a = [1, 2, 3]
b = a
c = a.copy()

print(a is b)  # True
print(a is c)  # False
print(a == c)  # True
```

- `is` checks whether two references point to the same object.
- `==` checks whether two objects have equal values.

For value comparisons, generally use `==`. Use `is` when identity itself matters, commonly with `None`:

```python
result = None

if result is None:
    print("No result available")
```

## 26. Shallow Copy

A shallow copy creates a new outer object but does not recursively copy the objects inside it.

For a list:

```python
original = [1, 2, 3]
copied = original.copy()

copied[0] = 99

print(original)  # [1, 2, 3]
print(copied)    # [99, 2, 3]
```

The outer lists are different, so replacing a top-level element in one does not replace the corresponding element in the other.

However, nested mutable objects are shared.

```python
original = [[1, 2], [3, 4]]
copied = original.copy()

copied[0][0] = 99

print(original)
print(copied)
```

Output:

```text
[[99, 2], [3, 4]]
[[99, 2], [3, 4]]
```

Why? Both outer lists refer to the same inner lists.

### Other ways to make shallow copies

For a list:

```python
copied = original.copy()
copied = original[:]
copied = list(original)
```

For a dictionary:

```python
copied = original.copy()
copied = dict(original)
```

These are shallow copies.

### Shallow copy with a dictionary

```python
original = {
    "name": "Rahul",
    "skills": ["Python", "Linux"]
}

copied = original.copy()

copied["name"] = "Amit"
copied["skills"].append("Networking")

print(original)
print(copied)
```

Output:

```text
{'name': 'Rahul', 'skills': ['Python', 'Linux', 'Networking']}
{'name': 'Amit', 'skills': ['Python', 'Linux', 'Networking']}
```

The top-level `"name"` value is reassigned only in the copied dictionary, but the nested `"skills"` list is shared.

## 27. Deep Copy

A deep copy recursively copies nested objects, so the copied structure is independent of the original for ordinary mutable nested data.

Use the `copy` module:

```python
import copy

original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)

copied[0][0] = 99

print(original)  # [[1, 2], [3, 4]]
print(copied)    # [[99, 2], [3, 4]]
```

Now changes to a nested list in the copy do not affect the corresponding list in the original.

### Deep-copying a dictionary

```python
import copy

original = {
    "name": "Rahul",
    "skills": ["Python", "Linux"]
}

copied = copy.deepcopy(original)

copied["skills"].append("Networking")

print(original)
print(copied)
```

Output:

```text
{'name': 'Rahul', 'skills': ['Python', 'Linux']}
{'name': 'Rahul', 'skills': ['Python', 'Linux', 'Networking']}
```

### Shallow copy vs. deep copy vs. assignment

| Operation | New outer object? | Nested mutable objects copied? |
|---|---|---|
| `b = a` | No | No |
| `b = a.copy()` | Yes | No |
| `b = copy.copy(a)` | Yes | No |
| `b = copy.deepcopy(a)` | Yes | Generally yes, recursively |

Deep copying can be more expensive in time and memory. It may also behave differently for custom objects, files, sockets, and other special objects. Use it when independent nested data is genuinely needed.

### Practical rule

- Use ordinary assignment when you intentionally want shared access.
- Use a shallow copy when you need a new outer list or dictionary.
- Use a deep copy when nested mutable objects must also be independent.

---

# Part 7: Practical Examples

## 28. Example: Remove Duplicates from a List

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

This preserves the order of first occurrence.

## 29. Example: Find Common Items

```python
python_students = {"Rahul", "Amit", "Priya"}
linux_students = {"Amit", "Priya", "Rohan"}

common = python_students & linux_students

print(common)
```

The result contains students in both sets. Set display order can vary.

This pattern is useful when comparing usernames, tags, or lists of discovered assets.

## 30. Example: Count Items Using a Dictionary

```python
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

print(counts)
```

Output:

```text
{'apple': 3, 'banana': 2, 'orange': 1}
```

## 31. Example: Store Structured Information

```python
target = {
    "domain": "example.com",
    "subdomains": ["www.example.com", "api.example.com"],
    "ports": [80, 443],
    "technologies": {"server": "nginx", "language": "Python"}
}

print(target["domain"])
print(target["subdomains"][0])
print(target["technologies"]["server"])
```

Output:

```text
example.com
www.example.com
nginx
```

This demonstrates how lists, sets, and dictionaries can be combined to represent structured information. Use only authorized targets when practicing cybersecurity.

## 32. Example: Filter a Dictionary

```python
scores = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 92,
    "Rohan": 28
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 40
}

print(passed)
```

Output:

```text
{'Rahul': 85, 'Priya': 92}
```

---

# Part 8: Common Mistakes

## 33. Mistakes to Avoid

### Mistake 1: Confusing assignment with copying

```python
a = [1, 2, 3]
b = a
```

`b` is another reference to the same list, not an independent copy.

### Mistake 2: Using `{}` for an empty set

```python
empty_dict = {}
empty_set = set()
```

### Mistake 3: Expecting a set to preserve order

Sets are designed for membership and uniqueness, not positional access.

### Mistake 4: Forgetting the comma in a single-element tuple

```python
a = (5,)  # Tuple
b = (5)   # Integer
```

### Mistake 5: Assuming dictionary keys can be lists

Incorrect:

```python
# data = {[1, 2]: "value"}  # TypeError
```

Lists are mutable and unhashable, so they cannot be dictionary keys.

A tuple containing hashable values can be a key:

```python
data = {(1, 2): "value"}

print(data[(1, 2)])  # value
```

### Mistake 6: Assuming `sort()` returns a sorted list

```python
numbers = [3, 1, 2]
numbers.sort()
```

`sort()` modifies the list in place and returns `None`. Use `sorted(numbers)` if you want a new sorted list.

### Mistake 7: Modifying a list while iterating over it

This can cause elements to be skipped.

Risky:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

Safer:

```python
numbers = [1, 2, 3, 4, 5]

numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(numbers)  # [1, 3, 5]
```

### Mistake 8: Confusing `remove()` and `pop()`

- `remove(value)` removes the first matching value.
- `pop(index)` removes and returns an element at an index; without an index, it removes the last element.

For sets, `pop()` removes an arbitrary element.

### Mistake 9: Assuming a shallow copy isolates nested data

A shallow copy duplicates the outer container only. Use `copy.deepcopy()` when nested mutable data also needs independent copies.

---

# Part 9: Practice Exercises

Try to solve these using your own code before looking for solutions.

## Beginner Level

1. Create a list of five numbers and print the first and last elements.
2. Extract the middle three elements from a list using slicing.
3. Add an element using `append()` and several elements using `extend()`.
4. Sort a list in ascending and descending order.
5. Create a tuple containing your name, age, and country, then unpack it.
6. Create a set from a list containing duplicates.
7. Find the union and intersection of two sets.
8. Create a dictionary containing a student's name, age, and marks.
9. Print all dictionary keys, values, and key-value pairs.
10. Create a dictionary using a comprehension that maps each number from 1 to 5 to its square.

## Intermediate Level

11. Find all even numbers in a list using a list comprehension.
12. Find the largest and smallest numbers in a list without using `max()` or `min()`.
13. Count the frequency of each word in a sentence.
14. Remove duplicate values from a list while preserving their original order.
15. Create a nested dictionary for three students and print each student's marks.
16. Given two lists of usernames, find the usernames common to both.
17. Use unpacking to separate the first item, middle items, and last item from a list.
18. Make a shallow copy of a nested list and demonstrate why modifying an inner list affects both.
19. Use `copy.deepcopy()` to solve the previous exercise.
20. Create a dictionary comprehension that keeps only values greater than or equal to 50.

## Practical Mini-Projects

### Project 1: Student Marks Manager

Requirements:

- Store student names and marks in a dictionary.
- Add a new student.
- Update a student's marks.
- Display all students and their marks.
- Calculate the average mark.
- Display students who scored at least 40.

### Project 2: Word Frequency Counter

Requirements:

- Accept a sentence from the user.
- Convert it to lowercase.
- Split it into words.
- Count each word using a dictionary.
- Display the most frequent word.

Optional improvement: Handle basic punctuation using string methods or the `string` module.

### Project 3: Unique Username Checker

Requirements:

- Store a collection of existing usernames.
- Accept a candidate username.
- Check whether it already exists.
- Add the username if it is available.

Use a set for efficient membership checks.

### Project 4: Authorized Asset Inventory

Requirements:

- Create a dictionary representing a lab asset.
- Store its hostname, IP address, open lab ports, and technologies.
- Store multiple hostnames in a list.
- Use a set to find unique hostnames.
- Use dictionary iteration to display the inventory.

Keep testing within your own lab or another environment you are explicitly authorized to assess.

---

# Part 10: Quick Revision Questions and Answers

**1. What is a list?**

A mutable, ordered collection that allows duplicate values.

**2. What is a tuple?**

An ordered collection whose element references cannot be reassigned after creation.

**3. What is a set?**

A collection of unique, hashable elements that supports operations such as union and intersection.

**4. What is a dictionary?**

A mapping that associates unique, hashable keys with values.

**5. What is the difference between `append()` and `extend()`?**

`append()` adds one object as an element; `extend()` adds the elements of an iterable.

**6. What is the difference between `remove()` and `pop()`?**

`remove()` removes by value; `pop()` removes and returns an element by position for lists, or an arbitrary element for sets.

**7. How do you create an empty set?**

```python
set()
```

**8. How do you access a dictionary value safely when a key might be missing?**

```python
dictionary.get("key", default_value)
```

**9. What is a list comprehension?**

A compact expression for constructing a list from an iterable, optionally with filtering.

**10. What is a dictionary comprehension?**

A compact expression for constructing a dictionary from an iterable.

**11. Can a list be a dictionary key?**

No. Lists are unhashable.

**12. Can a tuple be a dictionary key?**

Yes, if all of its elements are hashable.

**13. What is unpacking?**

Assigning elements from an iterable to multiple variables.

**14. What does `b = a` do when `a` is a list?**

It binds `b` to the same list object; it does not copy the list.

**15. What is a shallow copy?**

A new outer container whose nested objects may still be shared with the original.

**16. What is a deep copy?**

A recursive copy that generally duplicates nested objects too.

**17. What is the difference between `is` and `==`?**

`is` checks object identity; `==` checks value equality.

**18. Why are sets useful?**

They store unique elements and support fast membership checks and mathematical set operations.

**19. Are dictionaries ordered?**

Modern Python dictionaries preserve insertion order.

**20. Which structure is useful for word-frequency counting?**

A dictionary, because each word can be mapped to its count.

---

# Part 11: Quick Cheat Sheet

## Lists

```python
items = [1, 2, 3]

items[0]               # Access
items[-1]              # Last item
items[1:3]             # Slice
items.append(4)        # Add one item
items.extend([5, 6])   # Add iterable's items
items.insert(0, 0)     # Insert at index
items.remove(2)        # Remove first matching value
items.pop()            # Remove and return last item
items.sort()           # Sort in place
items.reverse()        # Reverse in place
items.copy()           # Shallow copy
[x * 2 for x in items] # List comprehension
```

## Tuples

```python
point = (10, 20)

point[0]               # Access
point.count(10)        # Count
point.index(20)        # Find index
x, y = point           # Unpack
single = (10,)         # One-element tuple
```

## Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.add(4)               # Add one element
a.update([5, 6])       # Add multiple elements
a.remove(2)            # Remove; KeyError if absent
a.discard(99)          # Remove if present
a | b                  # Union
a & b                  # Intersection
a - b                  # Difference
a ^ b                  # Symmetric difference
a.issubset(b)          # Subset check
a.issuperset(b)        # Superset check
a.isdisjoint(b)        # No common elements?
```

## Dictionaries

```python
student = {"name": "Rahul", "age": 21}

student["name"]                 # Access by key
student.get("marks", 0)         # Safe lookup with default
student["age"] = 22             # Add or update
student.update({"marks": 90})   # Update multiple entries
student.keys()                  # Keys view
student.values()                # Values view
student.items()                 # Key-value pairs view
student.pop("age", None)        # Remove and return
student.copy()                  # Shallow copy
{k: v**2 for k, v in ...}       # Dictionary comprehension
```

## Copying

```python
b = a                 # Same object
b = a.copy()          # Shallow copy for lists/dictionaries
b = a[:]              # Shallow list copy
```

For nested structures:

```python
import copy

b = copy.deepcopy(a)
```

## Unpacking

```python
a, b = [10, 20]
first, *middle, last = [1, 2, 3, 4, 5]
function(*values)
function(**dictionary)
```

---

# Final Revision Checklist

Before moving to the next Python topic, make sure you can:

- [ ] Create, index, slice, and modify lists.
- [ ] Explain `append()` versus `extend()`.
- [ ] Use common list methods correctly.
- [ ] Write list comprehensions with conditions.
- [ ] Work with nested lists without accidental shared references.
- [ ] Create tuples and unpack their elements.
- [ ] Explain tuple immutability and the single-element tuple comma.
- [ ] Create sets and use union, intersection, and difference.
- [ ] Create, access, update, and delete dictionary entries.
- [ ] Use `get()`, `keys()`, `values()`, and `items()`.
- [ ] Write dictionary comprehensions and nested dictionaries.
- [ ] Unpack collections using `*` and dictionaries using `**`.
- [ ] Explain references, shallow copies, and deep copies.
- [ ] Complete at least two practice projects without copying a solution.

**Suggested practice session:** Spend 15 minutes revising lists, 10 minutes on tuples, 10 minutes on sets, 15 minutes on dictionaries, and the final 10 minutes practicing unpacking and copying. Write the code yourself and predict its output before running it.