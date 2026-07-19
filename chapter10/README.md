# 📘 Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that focuses on creating reusable and organized code by using **classes** and **objects**.

Instead of writing the same code repeatedly, OOP allows us to define a blueprint (class) and create multiple objects from it.

---

# 1. Class

A **class** is a blueprint or template used to create objects.

It defines:
- Attributes (variables)
- Methods (functions)

### Syntax

```python
class Student:
    pass
```

### Example

```python
class Student:
    name = "John"
    age = 20
```

Here,

- `Student` is a class.
- `name` and `age` are attributes.

---

# 2. Object

An **object** is an instance of a class.

Think of it like this:

> Class = Blueprint of a House  
> Object = Actual House built from the blueprint

### Example

```python
class Student:
    name = "John"

student1 = Student()
student2 = Student()

print(student1.name)
print(student2.name)
```

### Output

```
John
John
```

Here,

- `student1` and `student2` are objects.
- Both are created from the `Student` class.

---

# 3. Modeling a Problem Using OOP

When solving a real-world problem using OOP, identify the following:

| Real World | OOP |
|------------|-----|
| Noun | Class |
| Adjective | Attributes |
| Verb | Methods |

### Example

Suppose we want to represent an Employee.

### Noun

Employee

This becomes the class.

```python
class Employee:
    pass
```

---

### Adjectives (Properties)

- Name
- Age
- Salary
- Department

These become attributes.

```python
class Employee:
    name = ""
    age = 0
    salary = 0
```

---

### Verbs (Actions)

- getSalary()
- incrementSalary()
- display()

These become methods.

```python
class Employee:

    def display(self):
        print("Employee details")

    def getSalary(self):
        print("Salary is", self.salary)

    def increment(self):
        self.salary += 5000
```

---

# 4. Class Attributes

A **class attribute** belongs to the class itself.

It is shared among all objects.

### Example

```python
class Employee:

    company = "Google"
```

Creating objects

```python
e1 = Employee()
e2 = Employee()

print(e1.company)
print(e2.company)
```

### Output

```
Google
Google
```

Both objects share the same value.

### Changing Class Attribute

```python
Employee.company = "Microsoft"

print(e1.company)
print(e2.company)
```

Output

```
Microsoft
Microsoft
```

---

# 5. Instance Attributes

Instance attributes belong to individual objects.

Each object can have different values.

### Example

```python
class Student:
    pass

s1 = Student()
s2 = Student()

s1.name = "Alice"
s2.name = "Bob"

print(s1.name)
print(s2.name)
```

### Output

```
Alice
Bob
```

Here,

- `name` is an instance attribute.
- Every object stores its own value.

---

# Difference Between Class Attribute and Instance Attribute

| Class Attribute | Instance Attribute |
|----------------|--------------------|
| Shared by all objects | Unique for every object |
| Declared inside class | Assigned to each object |
| Stored once | Stored separately for every object |

Example

```python
class Student:

    school = "ABC School"

s1 = Student()
s2 = Student()

s1.name = "Ram"
s2.name = "Hari"

print(s1.school)
print(s2.school)

print(s1.name)
print(s2.name)
```

Output

```
ABC School
ABC School
Ram
Hari
```

---

# 6. Self Parameter

`self` refers to the current object.

It is used to access instance attributes and methods.

Whenever we define a method inside a class, the first parameter should be `self`.

### Example

```python
class Student:

    def show(self):
        print("Hello")
```

Creating object

```python
s1 = Student()

s1.show()
```

Python internally converts

```python
s1.show()
```

into

```python
Student.show(s1)
```

---

### Example with Attributes

```python
class Student:

    def setName(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student()

s1.setName("John")
s1.display()
```

Output

```
John
```

---

# Why do we need self?

Without `self`, Python wouldn't know which object's data should be accessed.

Example:

```python
s1.name = "John"
s2.name = "Alice"
```

Using `self.name`, Python knows whether to access `s1.name` or `s2.name`.

---

# 7. Static Method

A static method does **not** depend on the object or class.

It is simply a utility function placed inside a class.

Static methods are created using the `@staticmethod` decorator.

### Example

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))
```

Output

```
30
```

No object is required.

You can also call it using an object.

```python
c = Calculator()

print(c.add(5, 10))
```

Output

```
15
```

---

### When to Use Static Methods?

Use static methods when the method:

- Doesn't use `self`
- Doesn't use `cls`
- Performs a general utility task

Examples

- Addition
- Validation
- Conversion
- Formatting

---

# 8. __init__() Constructor

The `__init__()` method is a special method (constructor) that runs automatically whenever an object is created.

Its main purpose is to initialize object attributes.

### Syntax

```python
class Student:

    def __init__(self):
        print("Object Created")
```

Creating object

```python
s1 = Student()
```

Output

```
Object Created
```

---

### Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("John", 20)

print(s1.name)
print(s1.age)
```

Output

```
John
20
```

---

### Another Example

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Alice", 50000)

e1.display()
```

Output

```
Name: Alice
Salary: 50000
```

---

# Summary

- A **class** is a blueprint.
- An **object** is an instance of a class.
- **Attributes** store data.
- **Methods** define behavior.
- **Class attributes** are shared by all objects.
- **Instance attributes** are unique to each object.
- **`self`** refers to the current object.
- **Static methods** are utility methods that don't depend on object data.
- **`__init__()`** is a constructor used to initialize object attributes automatically.