<div align="center">
    <img src="img/logo.jpeg" height="320" width="830" alt="OOP Concepts">
    <h1>Object Oriented Programming</h1>
    <strong>Object-Oriented Programming (OOP) is the term used to describe a programming approach based on objects and classes.</strong>
</div>

- [Introduction](#introduction)
- [Class](#class)
  - [Instance Methods](#instance-methods)
  - [Class Methods](#class-methods)
  - [Static Methods](#static-methods)
- [Principal of OOPs](#principal-of-oops)
  - [Abstraction](#abstraction)
  - [Encapsulation](#encapsulation)
    - [References:](#references)
  - [Inheritance](#inheritance)
    - [References](#references-1)
  - [Polymorphism](#polymorphism)
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


# Class

Different types of methods that can be defined in a Python Class

We can define three types of methods
- Instance Methods
- Class Methods
- Static Methods

## Instance Methods

Instance methods are the most used methods in a Python class. These methods are only accessible through class objects. If we want to modify any class variable, this should be done inside an instance method.

The first parameter in these methods is `self`. `self` is used to refer to the current class object’s properties and attributes.

Take a look at the code snippet below to understand this.

```python
class Cricket:
    teamName = None

    def setTeamName(self, name):
        self.teamName = name
    
    def getTeamName(self):
        return self.teamName

c = Cricket()
c.setTeamName('India')
print(c.getTeamName())
```
## Class Methods
Class methods are usually used to access class variables. You can call these methods directly using the class name instead of creating an object of that class.

To declare a class method, we need to use the @classmethod decorator. Also, as in the case of instance methods, self is the keyword used to access the class variables. In class methods, we use use the cls variable to refer to the class.

Take a look at the code snippet below to understand this concept.

```python
class Cricket:
  teamName = 'India'

  @classmethod
  def getTeamName(cls):
    return cls.teamName

print(Cricket.getTeamName())
```


## Static Methods
Static methods are usually used as a utility function or when we do not want an inherited class to modify a function definition. These methods do not have any relation to the class variables and instance variables; so, are not allowed to modify the class attributes inside a static method.

To declare a static method, we need to use the @staticmethod. Again, we will be using the cls variable to refer to the class. These methods can be accessed using the class name as well as class objects.

Take a look at the code snippet below to understand this concept.

```python
class Cricket:
    teamName = 'India'  

    @staticmethod
    def utility():
        print("This is a static method.")

c1 = Cricket()
c1.utility()

Cricket.utility()
```

> Check in details [here...](https://www.educative.io/answers/different-types-of-methods-that-can-be-defined-in-a-python-class)


# Principal of OOPs
The major concepts that we have discussed above are known as pillars of OOPs. There are four pillars on which OOP rests.

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

Details of are given below
## Abstraction
## Encapsulation
The wrapping and controlling access of logically grouped data and method into a single unit called class is known as encapsulation. Controlling access can be implemented using access modifiers (public,protected,private).

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

Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

```python
class Animal:
    name = ""
    age = 20

    def eat(self):
        print("I can eat {}".format(self.name))


class Dog(Animal):
    def display(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))


labrador = Dog()

labrador.name = "Rohu"
labrador.age = 30
labrador.eat()
labrador.display()
```

* Multiple Inheritance: 
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.

```python
# Python program to demonstrate
# multiple inheritance
 
# Base class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
```
* Multilevel Inheritance:
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
```python
# Python program to demonstrate
# multilevel inheritance
 
# Base class
 
 
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
# Intermediate class
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
# Derived class
 
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
 
#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
```

* Hierarchical Inheritance: 
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.

```python
# Python program to demonstrate
# Hierarchical inheritance
 
 
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class1
 
 
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
# Derivied class2
 
 
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
 
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
```

* Hybrid Inheritance: 
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

```python
# Python program to demonstrate
# hybrid inheritance
 
 
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()
```

### References
- https://www.geeksforgeeks.org/types-of-inheritance-python/

## Polymorphism

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



