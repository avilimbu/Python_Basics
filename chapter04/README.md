# Chapter 04 | Lists and Tuples

## Lists

A **list** is an ordered and mutable (changeable) collection in Python. It allows duplicate values and can store different data types.

### Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]
numbers = [10, 20, 30]

print(fruits)
print(numbers)
```

---

## List Indexing

Lists use **zero-based indexing**, meaning the first element has an index of `0`.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])    # Apple
print(fruits[1])    # Banana
print(fruits[-1])   # Mango
```

---

## List Methods

### `sort()`

Sorts the list in ascending order.

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

---

### `reverse()`

Reverses the order of the list.

```python
numbers = [1, 2, 3]

numbers.reverse()

print(numbers)
```

---

### `pop()`

Removes and returns the last element by default.

```python
numbers = [10, 20, 30]

numbers.pop()

print(numbers)
```

You can also remove an element at a specific index.

```python
numbers = [10, 20, 30]

numbers.pop(1)

print(numbers)
```

---

### `insert()`

Inserts an element at a specified position.

```python
numbers = [10, 30]

numbers.insert(1, 20)

print(numbers)
```

---

### `remove()`

Removes the first occurrence of the specified value.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

---

## Tuples

A **tuple** is an ordered and immutable collection in Python. Once created, its elements cannot be modified.

### Creating a Tuple

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

---

## Tuple Methods

Since tuples are immutable, they have only **two built-in methods**.

### `count()`

Returns the number of times a value appears in the tuple.

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

---

### `index()`

Returns the index of the first occurrence of a value.

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

---

## Summary

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Many built-in methods | Only `count()` and `index()` |
| Suitable for changing data | Suitable for fixed data |
