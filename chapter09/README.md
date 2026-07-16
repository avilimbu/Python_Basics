# Chapter 09 | File I/O

## Introduction

**File I/O (Input/Output)** in Python is used to read data from files and write data to files. It allows programs to store information permanently instead of keeping it only in memory.

Python provides built-in functions to create, read, write, update, and manage files easily.

---

## Types of Files

Python mainly works with two types of files:

### 1. Text Files

Text files store data in a human-readable format.

**Examples:**
- `.txt`
- `.py`
- `.c`
- `.html`
- `.csv`

Example:

```text
Hello, World!
Welcome to Python.
```

---

### 2. Binary Files

Binary files store data in binary (0s and 1s) and are not human-readable.

**Examples:**
- `.jpg`
- `.png`
- `.mp3`
- `.mp4`
- `.dat`
- `.pdf`

---

## Opening a File

Before performing any operation on a file, it must be opened using the `open()` function.

### Syntax

```python
file = open("filename", "mode")
```

### Parameters

- **filename** → Name or path of the file.
- **mode** → Specifies how the file should be opened.

Example:

```python
file = open("sample.txt", "r")
```

---

## Reading a File

### `read()`

The `read()` method reads the entire contents of a file.

### Syntax

```python
file.read()
```

### Example

```python
file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()
```

---

## Writing to a File

### `write()`

The `write()` method writes data into a file.

If the file does not exist, Python creates it.

If the file exists in **write mode (`w`)**, its previous content is removed.

### Syntax

```python
file.write(data)
```

### Example

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

---

## Appending to a File

### `append()`

Appending means adding new data at the end of an existing file without deleting its previous content.

Python uses the **append mode (`a`)** with the `write()` method.

### Example

```python
file = open("sample.txt", "a")

file.write("\nWelcome to File Handling.")

file.close()
```

---

## Other Methods to Read Files

### `readline()`

Reads only one line from the file at a time.

### Example

```python
file = open("sample.txt", "r")

print(file.readline()) ```this prints first line```
print(file.readline())  ```this prints secont line```

file.close()
```

---

### `readlines()`

Reads all lines from a file and returns them as a list.

### Example

```python
file = open("sample.txt", "r")

lines = file.readlines()
print(lines)

file.close()
```

Output:

```python
['Hello\n', 'Welcome\n', 'Python\n']
```

---

## Modes of Opening a File

| Mode | Description |
|------|-------------|
| `r` | Read a file (default mode). |
| `w` | Write to a file (overwrites existing content). |
| `a` | Append data to the end of a file. |
| `x` | Create a new file. Returns an error if the file already exists. |
| `rb` | Read a binary file. |
| `wb` | Write to a binary file. |
| `ab` | Append to a binary file. |
| `r+` | Read and write a file. |
| `w+` | Read and write (overwrites existing content). |
| `a+` | Read and append to a file. |

---

## Writing Files in Python

Example:

```python
file = open("message.txt", "w")

file.write("Python File Handling")

file.close()
```

Output inside **message.txt**

```text
Python File Handling
```

---

## With Statement

The **`with` statement** automatically closes the file after its operations are completed.

Using `with` is considered the best practice because you do not need to call `close()` manually.

### Syntax

```python
with open("filename", "mode") as file:
    #file operations
```

### Example

```python
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
```

---

## Advantages of Using `with`

- Automatically closes the file.
- Cleaner and more readable code.
- Prevents resource leaks.
- Recommended for all file operations.

---

## Summary

- File I/O allows programs to store and retrieve data from files.
- Python supports both **text** and **binary** files.
- Use `open()` to open a file before performing any operation.
- `read()` reads the entire file.
- `write()` writes data to a file.
- Append mode (`a`) adds data without removing existing content.
- `readline()` reads one line at a time.
- `readlines()` returns all lines as a list.
- Different file modes control how a file is opened.
- The `with` statement automatically closes the file and is the recommended way to work with files.