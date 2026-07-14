# Chapter 06 | Conditional Expressions

Conditional expressions allow a program to make decisions based on whether a condition is **True** or **False**. Instead of executing every line of code, Python can choose different execution paths depending on the condition.

---

## If, Else, and Elif Statements

Python uses **conditional statements** to control the flow of a program.

- `if` checks whether a condition is `True`.
- `else` executes when the `if` condition is `False`.
- `elif` (short for **else if**) checks additional conditions if the previous condition is `False`.

These statements help create decision-making programs such as grading systems, login validation, age verification, and more.

### Flow of Execution

```
Condition?

│
├── True  → Execute if block
│
└── False
      │
      ├── Check elif condition
      │      │
      │      ├── True → Execute elif block
      │      └── False
      │
      └── Execute else block
```

---

## Syntax

### if Statement

```python
if condition:
    # code to execute
```

### if...else Statement

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

### if...elif...else Statement

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

---

## Relational Operators

Relational operators compare two values and return either **True** or **False**.

They are commonly used inside conditional statements.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | True |
| `!=` | Not equal to | `5 != 3` | True |
| `>` | Greater than | `8 > 5` | True |
| `<` | Less than | `4 < 2` | False |
| `>=` | Greater than or equal to | `5 >= 5` | True |
| `<=` | Less than or equal to | `2 <= 4` | True |

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### Output

```
Eligible to vote
```

---

## Logical Operators

Logical operators combine multiple conditions into a single expression.

Python provides three logical operators:

| Operator | Meaning |
|----------|---------|
| `and` | Returns True if both conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the Boolean value |

---

### AND Operator

Returns `True` only when **both** conditions are true.

### Example

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

### Output

```
Eligible to vote
```

---

### OR Operator

Returns `True` if **at least one** condition is true.

### Example

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### Output

```
Weekend
```

---

### NOT Operator

Reverses the Boolean value.

### Example

```python
logged_in = False

if not logged_in:
    print("Please log in.")
```

### Output

```
Please log in.
```

---

## Elif Clause

The `elif` clause is short for **else if**.

It is used when there are **multiple conditions** to check. Python evaluates the conditions from top to bottom. As soon as one condition becomes **True**, its corresponding block is executed, and the remaining conditions are skipped.

The `else` block is optional and runs only if none of the conditions are true.

---

## Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

---

## Example

```python
marks = 76

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```

### Output

```
Grade B
```

---

## Another Example

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Output

```
Zero
```
---

# Summary

Conditional expressions are one of the fundamental concepts in Python programming. They enable programs to make intelligent decisions based on different situations. By combining conditional statements with relational and logical operators, we can create interactive and dynamic applications that respond differently depending on user input or program data.