# Chapter 08 | Functions and Recursion

Functions are one of the most important concepts in Python. They help organize code into reusable blocks, making programs easier to read, maintain, and debug. Instead of writing the same code multiple times, you can define a function once and call it whenever needed.

---

## Function Definition

A **function** is a named block of code that performs a specific task. Functions are created using the `def` keyword.

### Syntax

```python
def function_name(parameters):
    # Function body
    # Code to execute
```

### Example

```python
def greet():
    print("Hello, Welcome to Python!")
```

In the above example:

- `def` is the keyword used to define a function.
- `greet` is the function name.
- `()` can contain parameters (empty in this case).
- The indented code is called the function body.

---

## Function Call

A function only executes when it is **called**.

### Syntax

```python
function_name()
```

### Example

```python
def greet():
    print("Hello, Welcome to Python!")

greet()
```

### Output

```
Hello, Welcome to Python!
```

A function can be called multiple times without rewriting its code.

```python
greet()
greet()
```

---

## Types of Functions in Python

Python provides two main types of functions.

### 1. Built-in Functions

These are functions already provided by Python.

Examples:

- `print()`
- `input()`
- `len()`
- `type()`
- `max()`
- `min()`
- `sum()`

```python
numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))
print(sum(numbers))
```

---

### 2. User-defined Functions

These are functions created by the programmer using the `def` keyword.

```python
def square(number):
    return number * number

print(square(5))
```

---

## Functions with Arguments

Arguments are values passed to a function when it is called. They allow the function to work with different data.

### Syntax

```python
def function_name(parameter):
    # code

function_name(argument)
```

### Example

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")
```

### Output

```
Hello, Alice
Hello, Bob
```

### Multiple Arguments

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Return Value

A function can return a value using the `return` keyword.

```python
def add(a, b):
    return a + b

result = add(15, 25)

print(result)
```

### Output

```
40
```

The `return` statement sends the result back to the place where the function was called.

---

## Functions with Default Parameter Value

A **default parameter** allows you to assign a default value to a function parameter. If no argument is provided during the function call, the default value is used.

### Syntax

```python
def function_name(parameter=value):
    # code
```

### Example

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("John")
```

### Output

```
Hello, Guest
Hello, John
```

Default parameters make functions more flexible and reduce the need to pass every argument.

---

## Recursion

**Recursion** is a programming technique in which a function calls itself to solve a smaller version of the same problem.

Every recursive function should have:

- A **base case** that stops the recursion.
- A **recursive case** where the function calls itself.

### Syntax

```python
def function_name():
    if base_condition:
        return value

    return function_name()
```

### Example: Factorial

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

### Output

```
120
```

### How it Works

```
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120
```

### Advantages of Recursion

- Makes code shorter and easier to understand for certain problems.
- Useful for solving problems involving trees, graphs, and divide-and-conquer algorithms.

### Disadvantages of Recursion

- Uses more memory because each function call is stored on the call stack.
- Can be slower than loops for simple repetitive tasks.
- Missing a base case can lead to infinite recursion and a `RecursionError`.

---

## Summary

- A **function** is a reusable block of code that performs a specific task.
- Functions are created using the `def` keyword.
- A function runs only when it is **called**.
- Python has **built-in** and **user-defined** functions.
- **Arguments** allow functions to accept input values.
- The **return** statement sends a value back to the caller.
- **Default parameters** provide values when arguments are not supplied.
- **Recursion** is when a function calls itself and must include a base case to stop the recursion.