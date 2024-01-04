<div align="center">
    <img src="img/logo.jpeg" height="320" width="830" alt="OOP Concepts">
    <h1>Object Oriented Programming</h1>
    <strong>Object-Oriented Programming (OOP) is the term used to describe a programming approach based on objects and classes.</strong>
</div>

- [Introduction](#introduction)
- [Pillars of OOPs](#pillars-of-oops)
  - [Abstraction](#abstraction)
  - [Encapsulation](#encapsulation)
    - [References:](#references)
  - [Inheritance](#inheritance)
    - [References](#references-1)
  - [Polymorph](#polymorph)
- [SOLID Principle](#solid-principle)
  - [Single-Responsibility Principle](#single-responsibility-principle)
  - [Open-Closed Principle](#open-closed-principle)
  - [Liskov Substitution Principle](#liskov-substitution-principle)
  - [Interface Segregation Principle](#interface-segregation-principle)
  - [Dependency Inversion Principle](#dependency-inversion-principle)
- [References](#references-2)
  - [Source Code](#source-code)
  - [Documentation](#documentation)


# Introduction
Object-oriented programming is a programming paradigm based on the concept of objects, which can contain data and code: data in the form of fields, and code in the form of procedures. A common feature of objects is that methods are attached to them and can access and modify the object's data fields.


The OOPs concepts include the following:
- Class
- Object
- Inheritance
- Polymorphism
- Abstraction
- Encapsulation


# Pillars of OOPs
The major concepts that we have discussed above are known as pillars of OOPs. There are four pillars on which OOP rests.

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

Details of are given below
## Abstraction
## Encapsulation
The wrapping up of data and method into a single unit is known as encapsulation. It is also known as information hiding concept.

In a simple way, when you create a class with data and methods, you are implementing a encapsulation.

Also, encapsulation allows us to restrict accessing variables and methods directly and prevent accidental data modification by creating private data members and methods within a class.


**Access Modifiers in Python**

Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using `single underscore` and `double underscores`.

Python provides three types of access modifiers private, public, and protected.

- Public Member: Accessible anywhere from outside class
- Private Member: Accessible within the class
- Protected Member: Accessible within the class and its subclasses

Example

```python

class Employee:
    def __init__(self,name,salary):
        # Public Member (accessible within or outside of a class) 
        self.name = name 

        # Protected Member (accessible within the class and it's subclass)
        self._project = project

        # Private Member (accessible only within a class)
        self.__salary = salary

```

**Examples of Encapsulation**

In this example, we create an Employee class by defining employee attributes such as name and salary as an instance variable and implementing behavior using `work()` and `show()` instance methods.

```python
class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()
```

**Output:**

> Name:  Jessa Salary: 8000  
> Jessa is working on NLP

### References:
- https://pynative.com/python-encapsulation/

## Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

`Parent Class` is the class being inherited from, also called base class.

`Child Class` is the class that inherits from another class, also called derived class.

```python
class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()
```

Types of Inheritance

* Single Inheritance: 
* Multiple Inheritance: 
* Multilevel Inheritance :
* Hierarchical Inheritance: 
* Hybrid Inheritance: 

### References
- https://www.geeksforgeeks.org/types-of-inheritance-python/

## Polymorph

# SOLID Principle
SOLID is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin
SOLID stands for:
- S - Single-responsiblity Principle
- O - Open-closed Principle
- L - Liskov Substitution Principle
- I - Interface Segregation Principle
- D - Dependency Inversion Principle

## Single-Responsibility Principle
Single-responsibility Principle (SRP) states:

> A class should have one and only one reason to change, meaning that a class should have only one job.


## Open-Closed Principle
Open-closed Principle (OCP) states:

> Objects or entities should be open for extension but closed for modification.


## Liskov Substitution Principle
Liskov Substitution Principle states:

> Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.


## Interface Segregation Principle
Interface segregation principle states:

> A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.


## Dependency Inversion Principle
Dependency inversion principle states:
> Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.




# References

## Source Code
- 
## Documentation
- https://www.javatpoint.com/what-is-object-oriented-programming
- https://www.geeksforgeeks.org/encapsulation-in-java/
- https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
- 



