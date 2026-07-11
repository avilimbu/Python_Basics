# Chapter 05 | Dictionary and Sets

> **Theory**

## Dictionary

A **dictionary** is a built-in Python data structure that stores data in the form of **key-value pairs**. Each key is unique and is used to access its corresponding value.

### Syntax

```python
student = {
    "name": "Harry",
    "age": 20,
    "course": "Python"
}
```

---

## Dictionary Properties

- Stores data as **key-value pairs**.
- **Mutable** (can be modified after creation).
- Keys must be **unique**.
- Keys must be **immutable** (e.g., strings, integers, tuples).
- Values can be of any data type.
- Preserves **insertion order** (Python 3.7+).
- Access values using their keys.
- Duplicate keys are not allowed.

---

# Dictionary Methods

## 1. `items()`

Returns all key-value pairs as tuple objects.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

print(student.items())
```

### Output

```python
dict_items([('name', 'Harry'), ('age', 20)])
```

---

## 2. `values()`

Returns all the values of the dictionary.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

print(student.values())
```

### Output

```python
dict_values(['Harry', 20])
```

---

## 3. `keys()`

Returns all the keys of the dictionary.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

print(student.keys())
```

### Output

```python
dict_keys(['name', 'age'])
```

---

## 4. `update()`

Updates the dictionary by adding or modifying key-value pairs.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

student.update({"age": 21, "city": "Kathmandu"})

print(student)
```

### Output

```python
{'name': 'Harry', 'age': 21, 'city': 'Kathmandu'}
```

---

## 5. `get()`

Returns the value of the specified key. If the key does not exist, it returns `None`.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

print(student.get("age"))
print(student.get("city"))
```

### Output

```python
20
None
```

---

## 6. `pop()`

Removes the specified key and returns its value.

### Example

```python
student = {
    "name": "Harry",
    "age": 20
}

student.pop("age")

print(student)
```

### Output

```python
{'name': 'Harry'}
```

---

## 7. `popitem()`

Removes and returns the last inserted key-value pair.

### Example

```python
student = {
    "name": "Harry",
    "age": 20,
    "city": "Kathmandu"
}

student.popitem()

print(student)
```

### Output

```python
{'name': 'Harry', 'age': 20}
```

---

# Sets

A **set** is an unordered collection of **unique elements**. Duplicate values are automatically removed.

### Syntax

```python
numbers = {1, 2, 3, 4}
```

---

## Set Properties

- Stores **unique** values only.
- **Mutable** (elements can be added or removed).
- Duplicate values are automatically removed.
- Unordered collection.
- Does not support indexing or slicing.
- Can store different data types.
- Fast membership testing using the `in` keyword.

---

# Set Methods

## 1. `add()`

Adds an element to the set.

### Example

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

### Output

```python
{1, 2, 3, 4}
```

---

## 2. `remove()`

Removes the specified element. Raises a `KeyError` if the element does not exist.

### Example

```python
numbers = {1, 2, 3, 4}

numbers.remove(3)

print(numbers)
```

### Output

```python
{1, 2, 4}
```

---

## 3. `clear()`

Removes all elements from the set.

### Example

```python
numbers = {1, 2, 3}

numbers.clear()

print(numbers)
```

### Output

```python
set()
```

---

## 4. `copy()`

Creates a shallow copy of the set.

### Example

```python
numbers = {1, 2, 3}

new_numbers = numbers.copy()

print(new_numbers)
```

### Output

```python
{1, 2, 3}
```

---

## 5. `intersection()`

Returns the common elements between two sets.

### Example

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))
```

### Output

```python
{3, 4}
```

---

## 6. `union()`

Returns a new set containing all unique elements from both sets.

### Example

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
```

### Output

```python
{1, 2, 3, 4, 5}
```

---

## 7. `difference()`

Returns the elements that are present in the first set but not in the second set.

### Example

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

print(set1.difference(set2))
```

### Output

```python
{1, 2}
```

---

## 8. `issubset()`

Returns `True` if all elements of the first set are present in the second set.

### Example

```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))
```

### Output

```python
True
```

---

## 9. `issuperset()`

Returns `True` if the set contains all elements of another set.

### Example

```python
set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))
```

### Output

```python
True
```

---

# Dictionary vs Set

| Feature | Dictionary | Set |
|----------|------------|-----|
| Stores | Key-value pairs | Unique values |
| Ordered | ✅ Yes (Python 3.7+) | ❌ No |
| Mutable | ✅ Yes | ✅ Yes |
| Duplicate Values | Keys ❌, Values ✅ | ❌ Not Allowed |
| Indexing | ❌ No | ❌ No |
| Uses | Fast key-value lookup | Store unique elements and perform set operations |

---

# Key Takeaways

- A **dictionary** stores data as **key-value pairs**.
- Dictionary **keys must be unique**.
- A **set** stores **only unique values**.
- Sets automatically remove duplicate elements.
- Dictionaries are useful for mapping data, while sets are useful for performing mathematical set operations like **union**, **intersection**, and **difference**.