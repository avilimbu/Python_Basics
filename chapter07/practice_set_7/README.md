## Chapter 7 | Practice Questions

---

1. Write a program to print multiplication of a given number using for loop.

2. Write a program to greet all person's names stored in list `l` and which starts with `S`.
```
l = ["Ram", "Shyam", "Suvam", "hari"]
```

3. Attempt problem 1 using while loop.

4. Write a program to find out whether a given number is prime or not.

5. Write a program to find the sum of first n natural numbers using while loop.

6. Write a program to calculate the factorial of a given number using for loop.

7. Write a program to print the following star pattern.
```
*
**
*** for n= 3
```

8. Write a program to print thte following star pattern.
```
  *
 ***
***** for n=3
```

9. Write a program to print the following star pattern.
```
***
* *
*** for n= 3
```

10. Write a progrma to print the multiplication table of n using loop in reverse order.

---


---

## `end` Parameter in Python

The `end` parameter in the `print()` function specifies what should be printed after the output. By default, `print()` ends with a newline (`\n`), which moves the cursor to the next line.

### Syntax

```python
print(value, end="")
```

### Example

```python
print("Hello", end="")
print("World")
```

**Output:**

```text
HelloWorld
```

> **Note:** `end=""` removes the default newline, allowing the next `print()` statement to continue on the same line.