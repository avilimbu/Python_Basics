# Chapter 12 | Advanced Python 1

## Introduction

Advanced Python introduces powerful language features that make code more concise, readable, and efficient. These features help developers write cleaner programs, improve code maintainability, and reduce repetitive coding. This chapter covers some of the most useful modern Python features introduced in recent versions.

---

# Newly Added Features in Python

Python is continuously updated with new features to improve developer productivity and code readability.

Some important modern features include:

- Walrus Operator (`:=`)
- Type Hints
- Advanced Type Hints
- Match Case Statement
- Dictionary Merge & Update Operators
- Multiple Context Managers
- Improved Exception Handling
- Pattern Matching

These features are mainly available in Python 3.8, 3.9, and 3.10 onwards.

---

# Walrus Operator (`:=`)

The **Walrus Operator** allows you to assign a value to a variable while evaluating an expression.

### Syntax

```python
variable := expression
```

### Example

```python
numbers = [10, 20, 30, 40]

if (length := len(numbers)) > 3:
    print("Length:", length)
```

### Output

```
Length: 4
```

### Advantages

- Reduces repeated calculations.
- Makes code shorter.
- Improves readability.
- Useful inside loops and conditions.

---

# Type Definition (Type Hints)

Type hints specify the expected data type of variables, function parameters, and return values.

Although Python is dynamically typed, type hints improve readability and help IDEs detect errors.

### Example

```python
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(5, 6))
```

### Output

```
30
```

### Benefits

- Better documentation
- Easier debugging
- Improved IDE support
- Static type checking

---

# Advanced Typing Hints

Python's `typing` module provides advanced data type annotations.

Common types include:

- `List`
- `Tuple`
- `Dict`
- `Set`
- `Optional`
- `Union`
- `Any`
- `Callable`

### Example

```python
from typing import List

def square(numbers: List[int]) -> List[int]:
    return [num ** 2 for num in numbers]

print(square([1, 2, 3, 4]))
```

### Output

```
[1, 4, 9, 16]
```

### Advantages

- Better code clarity
- Easier collaboration
- Improved maintainability

---

# Match Case

The `match-case` statement is Python's version of a switch statement.

Introduced in **Python 3.10**.

### Example

```python
day = 3

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _:
        print("Invalid Day")
```

### Output

```
Tuesday
```

### Advantages

- Cleaner than multiple if-elif statements.
- Supports pattern matching.
- Improves readability.

---

# Dictionary Merge and Update Operator

Python 3.9 introduced operators to merge and update dictionaries.

## Merge Operator (`|`)

```python
student = {"name": "Avik"}
marks = {"python": 95}

result = student | marks

print(result)
```

### Output

```
{'name': 'Avik', 'python': 95}
```

---

## Update Operator (`|=`)

```python
student = {"name": "Avik"}

student |= {"age": 21}

print(student)
```

### Output

```
{'name': 'Avik', 'age': 21}
```

### Advantages

- Short and clean syntax.
- Easy dictionary merging.
- More readable than `update()` in some cases.

---

# Multiple Context Managers

A context manager automatically manages resources such as files or database connections.

Python allows multiple context managers in a single `with` statement.

### Example

```python
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

### Benefits

- Automatically closes all opened files.
- Cleaner and safer code.
- Prevents resource leaks.

---

# Exception Handling in Python

Exception handling prevents programs from crashing when runtime errors occur.

Python provides:

- `try`
- `except`
- `else`
- `finally`

### Example

```python
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Program Finished")
```

### Output

```
Division by zero is not allowed.
Program Finished
```

### Advantages

- Prevents application crashes.
- Handles unexpected errors gracefully.
- Improves reliability.

---

# Raising Exceptions

The `raise` keyword is used to generate exceptions manually.

### Example

```python
age = -2

if age < 0:
    raise ValueError("Age cannot be negative.")
```

### Output

```
ValueError: Age cannot be negative.
```

### Why Use `raise`?

- Validate user input.
- Prevent invalid operations.
- Create custom error messages.

---

# `if __name__ == "__main__"` in Python

Every Python file contains a built-in variable called `__name__`.

When the file is executed directly:

```python
__name__ == "__main__"
```

When the file is imported as a module:

```python
__name__ == module_name
```

### Example

```python
def greet():
    print("Welcome!")

if __name__ == "__main__":
    greet()
```

### Output

```
Welcome!
```

### Advantages

- Separates reusable code from executable code.
- Prevents unwanted execution when importing modules.
- Useful for testing.

---

# Global Keyword

The `global` keyword allows a function to modify a global variable.

### Example

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

### Output

```
1
```

### Note

Without using `global`, Python treats the variable as local inside the function.

---

# enumerate()

The `enumerate()` function returns both the index and the value while iterating through an iterable.

### Syntax

```python
enumerate(iterable, start=0)
```

### Example

```python
fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

### Output

```
1 Apple
2 Banana
3 Orange
```

### Advantages

- No need for manual index variables.
- Cleaner loops.
- Improves readability.

---

# List Comprehension

List comprehension is a concise way to create lists in Python using a single line of code.

### Syntax

```python
[expression for item in iterable]
```

### Example 1

```python
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)
```

### Output

```
[1, 4, 9, 16, 25]
```

---

### Example 2 (Using Condition)

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [num for num in numbers if num % 2 == 0]

print(even)
```

### Output

```
[2, 4, 6]
```

### Advantages

- Shorter than traditional loops.
- Easy to read.
- Faster in many cases.
- Reduces boilerplate code.

---

# Summary

In this chapter:
- Modern Python features introduced in recent versions.
- Using the Walrus Operator (`:=`) for assignment inside expressions.
- Writing cleaner code with Type Hints and Advanced Type Hints.
- Using `match-case` for pattern matching.
- Merging dictionaries using `|` and `|=`.
- Managing multiple resources using multiple context managers.
- Handling errors with `try`, `except`, `else`, and `finally`.
- Raising custom exceptions using `raise`.
- Understanding `if __name__ == "__main__"` for module execution.
- Modifying global variables using the `global` keyword.
- Iterating efficiently using `enumerate()`.
- Creating lists efficiently with list comprehension.

---

# Key info:

- Python's modern features make programs cleaner, shorter, and more maintainable.
- Type hints improve code readability and IDE support.
- The Walrus Operator simplifies assignments inside expressions.
- `match-case` replaces long `if-elif` chains with cleaner syntax.
- Dictionary merge operators make combining dictionaries simple.
- Context managers ensure resources are managed safely.
- Proper exception handling improves application reliability.
- `raise` helps validate input and enforce program rules.
- `if __name__ == "__main__"` is essential for writing reusable modules.
- `enumerate()` simplifies indexed iteration.
- List comprehensions provide a powerful and Pythonic way to create and filter lists.