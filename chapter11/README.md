# Chapter 11 | Inheritance and More on OOPs (Python)

Object-Oriented Programming (OOP) helps us write **reusable, organized, and maintainable code**. One of the most powerful features of OOP is **Inheritance**, which allows one class to acquire the properties and methods of another class.

---

# 1. Inheritance

Inheritance is the process by which one class (child class) acquires the properties and methods of another class (parent class).

It promotes:
-  Code Reusability
-  Easy Maintenance
-  Reduced Code Duplication

### Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

Here,

- `Parent` → Base Class / Super Class
- `Child` → Derived Class / Sub Class

---

## Example

```python
class Animal:

    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    pass


d = Dog()

d.eat()
```

### Output

```
Animal can eat
```

Although `Dog` has no `eat()` method, it inherits it from `Animal`.

---

# Types of Inheritance

Python supports five types of inheritance:

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

> **Note:** In this chapter, we focus on Single, Multiple, and Multilevel inheritance.

---

# 2. Single Inheritance

Single inheritance means one child class inherits from one parent class.

### Diagram

```
Animal
   │
   ▼
 Dog
```

### Example

```python
class Animal:

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()
```

### Output

```
Animal eats
Dog barks
```

### Key Points

- Child class inherits all accessible members of the parent class.
- Parent class cannot access child class methods.

---

# 3. Multiple Inheritance

Multiple inheritance means one child class inherits from **more than one parent class**.

### Diagram

```
Father     Mother
     \     /
      \   /
      Child
```

### Example

```python
class Father:

    def skills1(self):
        print("Programming")


class Mother:

    def skills2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()

c.skills1()
c.skills2()
```

### Output

```
Programming
Cooking
```

### Key Points

- Child class can access members of multiple parent classes.
- Python searches parent classes using **Method Resolution Order (MRO)**.

---

# 4. Multilevel Inheritance

Multilevel inheritance means one class inherits from another derived class.

### Diagram

```
Animal
   │
   ▼
Mammal
   │
   ▼
 Dog
```

### Example

```python
class Animal:

    def eat(self):
        print("Animal eats")


class Mammal(Animal):

    def walk(self):
        print("Can walk")


class Dog(Mammal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.walk()
d.bark()
```

### Output

```
Animal eats
Can walk
Dog barks
```

### Key Points

- Child class inherits from another child class.
- The lowest-level class can access all inherited members.

---

# 5. super() Method

The `super()` function is used to call methods or constructors of the parent class.

It is commonly used with `__init__()`.

### Why use `super()`?

Suppose both parent and child classes have constructors.

Without `super()`, the parent constructor is **not called automatically**.

---

### Example

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll


s = Student("John", 101)

print(s.name)
print(s.roll)
```

### Output

```
John
101
```

### What does `super().__init__(name)` do?

It calls the constructor of the parent class (`Person`) and initializes the `name` attribute.

---

# 6. Class Method

A class method works with the **class** instead of an individual object.

It uses the `@classmethod` decorator.

The first parameter is `cls`, which refers to the class itself.

### Syntax

```python
@classmethod
def method_name(cls):
    pass
```

### Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.change_school("XYZ School")

print(Student.school)
```

### Output

```
XYZ School
```

### Difference Between Instance Method and Class Method

| Instance Method | Class Method |
|-----------------|--------------|
| Uses `self` | Uses `cls` |
| Works with object data | Works with class data |
| Called using an object | Can be called using the class |

---

# 7. @property Decorator

The `@property` decorator allows a method to be accessed like an attribute.

It provides a clean way to **read data while hiding method calls**.

### Without `@property`

```python
class Student:

    def get_age(self):
        return 20


s = Student()

print(s.get_age())
```

### Output

```
20
```

---

### With `@property`

```python
class Student:

    @property
    def age(self):
        return 20


s = Student()

print(s.age)
```

### Output

```
20
```

### Why use `@property`?

- Makes code cleaner.
- Allows validation and computation behind the scenes.
- Prevents direct access to internal variables.

---

# 8. Getter and Setter

Getter and Setter are methods used to **control access to data**.

## Getter

A getter returns the value of an attribute.

### Example

```python
class Student:

    def __init__(self):
        self._age = 20

    @property
    def age(self):
        return self._age


s = Student()

print(s.age)
```

### Output

```
20
```

---

## Setter

A setter updates the value of an attribute after validation.

### Example

```python
class Student:

    def __init__(self):
        self._age = 20

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value >= 0:
            self._age = value
        else:
            print("Invalid Age")


s = Student()

s.age = 25

print(s.age)

s.age = -5
```

### Output

```
25
Invalid Age
```

### Important Notes

- `@property` creates the getter.
- `@age.setter` creates the setter for the same property.
- The actual value is stored in `_age`.
- `@property` does **not** store data; it only manages access to it.

---

# 9. Operator Overloading

Operator Overloading allows operators (`+`, `-`, `*`, etc.) to work with user-defined objects.

Python uses special methods (magic methods) to overload operators.

### Example

```python
class Number:

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n


n = Number(20)
m = Number(30)

print(n + m)
```

### Output

```
50
```

### What happens internally?

When you write:

```python
n + m
```

Python automatically calls:

```python
n.__add__(m)
```

The `__add__()` method defines how two `Number` objects should be added.

---

## Common Operator Overloading Methods

| Operator | Magic Method |
|-----------|--------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |
| `len(obj)` | `__len__()` |
| `print(obj)` | `__str__()` |

---

# Summary

| Topic | Definition |
|--------|------------|
| Inheritance | Acquiring properties and methods from another class |
| Single Inheritance | One parent → One child |
| Multiple Inheritance | Multiple parents → One child |
| Multilevel Inheritance | Parent → Child → Grandchild |
| `super()` | Calls the parent class constructor or method |
| `@classmethod` | Method that works with the class using `cls` |
| `@property` | Makes a method behave like an attribute |
| Getter | Returns the value of an attribute |
| Setter | Updates an attribute with validation |
| Operator Overloading | Gives custom behavior to operators for user-defined objects |

---

