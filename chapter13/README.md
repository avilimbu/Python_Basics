# Chapter 13 | Advanced Python 2

## Introduction

Advanced Python provides powerful tools and techniques that help developers write cleaner, more efficient, and maintainable code. This chapter covers virtual environments, anonymous functions, string formatting methods, and functional programming concepts such as `map()`, `filter()`, and `reduce()`.

---

# Virtual Environment

A **Virtual Environment** is an isolated Python environment that allows you to install packages for a specific project without affecting other Python projects or the global Python installation.

Using virtual environments helps avoid dependency conflicts and keeps projects organized.

### Why Use a Virtual Environment?

- Isolates project dependencies.
- Prevents version conflicts.
- Makes projects portable.
- Keeps the global Python installation clean.

---

## Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv myenv
```

---

### Step 2: Activate the Virtual Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### macOS/Linux

```bash
source myenv/bin/activate
```

After activation, the terminal will display the environment name:

```bash
(myenv)
```

---

### Step 3: Install Packages

```bash
pip install pandas
```

---

### Step 4: Deactivate the Environment

```bash
deactivate
```

---

## `pip freeze` Command

The `pip freeze` command displays all installed Python packages and their versions in the current virtual environment.

### Syntax

```bash
pip freeze
```

### Example Output

```text
numpy==2.1.0
pandas==2.2.2
matplotlib==3.9.0
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

### Install from `requirements.txt`

```bash
pip install -r requirements.txt
```

### Advantages

- Keeps track of project dependencies.
- Makes projects easy to share.
- Ensures consistent package versions.

---

# Lambda Function

A **lambda function** is a small anonymous function defined using the `lambda` keyword.

Unlike regular functions, lambda functions can contain only a single expression.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x ** 2

print(square(5))
```

### Output

```
25
```

---

### Example with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```
30
```

### Advantages

- Short and concise.
- Useful for one-time functions.
- Commonly used with `map()`, `filter()`, and `sorted()`.

---

# `join()` Method

The `join()` method combines multiple strings into a single string using a specified separator.

### Syntax

```python
separator.join(iterable)
```

### Example

```python
words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print(sentence)
```

### Output

```
Python is awesome
```

---

### Example with Comma

```python
languages = ["Python", "Java", "C++"]

print(", ".join(languages))
```

### Output

```
Python, Java, C++
```

### Advantages

- Efficient string concatenation.
- Cleaner than using loops.
- Improves readability.

---

# `format()` Method

The `format()` method inserts values into placeholders within a string.

### Syntax

```python
string.format(values)
```

### Example

```python
name = "Avik"
age = 21

print("My name is {} and I am {} years old.".format(name, age))
```

### Output

```
My name is Avik and I am 21 years old.
```

---

### Example with Named Arguments

```python
print("Name: {name}, Age: {age}".format(name="Avik", age=21))
```

### Output

```
Name: Avik, Age: 21
```
>>Not used much as we mostly use fstring for formating nowadays

# `map()`

The `map()` function applies a given function to every item in an iterable and returns a map object.

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
```

### Output

```
[1, 4, 9, 16]
```

### Uses

- Transforming data.
- Applying the same operation to every element.

---

# `filter()`

The `filter()` function filters elements from an iterable based on a condition.

### Syntax

```python
filter(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

### Output

```
[2, 4, 6]
```

### Uses

- Selecting elements that satisfy a condition.
- Removing unwanted data.

---

# `reduce()`

The `reduce()` function repeatedly applies a function to the elements of an iterable until only one value remains.

It is available in the `functools` module.

### Syntax

```python
from functools import reduce

reduce(function, iterable)
```

### Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

### Output

```
10
```

---

### Example: Finding Maximum Value

```python
from functools import reduce

numbers = [12, 45, 7, 89, 34]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)
```

### Output

```
89
```

### Uses

- Calculating sums or products.
- Finding maximum or minimum values.
- Aggregating data into a single result.

---

# Comparison of `map()`, `filter()`, and `reduce()`

| Function | Purpose | Returns |
|----------|---------|---------|
| `map()` | Applies a function to every element | Modified iterable |
| `filter()` | Selects elements based on a condition | Filtered iterable |
| `reduce()` | Combines all elements into one value | Single result |

---

# Summary

In this chapter, you learned:

- What a virtual environment is and why it is important.
- How to create, activate, and deactivate a virtual environment.
- Using the `pip freeze` command to manage project dependencies.
- Creating anonymous functions using `lambda`.
- Combining strings efficiently with the `join()` method.
- Formatting strings using the `format()` method.
- Transforming data with `map()`.
- Filtering data using `filter()`.
- Reducing an iterable to a single value with `reduce()`.

---

# Key Takeaways

- Virtual environments keep project dependencies isolated and organized.
- `pip freeze` helps document and share installed packages.
- Lambda functions provide a concise way to define simple functions.
- The `join()` method is the preferred way to concatenate multiple strings.
- The `format()` method creates readable and dynamic strings.
- `map()` transforms every element in an iterable.
- `filter()` returns only elements that satisfy a condition.
- `reduce()` combines multiple values into a single result, making it useful for aggregation tasks.