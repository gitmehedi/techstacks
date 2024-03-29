<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="Tech Stacks">
    <h1>Python</h1>
    <strong>A tech stack is the combination of technologies a company uses to build and run an application or project.</strong>
</div>


- [Introduction](#introduction)
- [Python Version](#python-version)
- [Learning Index](#learning-index)
  - [Decorators](#decorators)
    - [Definition](#definition)
    - [Prerequisites of Decorators](#prerequisites-of-decorators)
    - [Example](#example)
    - [References](#references)
  - [Python Data Types](#python-data-types)
    - [References](#references-1)
- [Interview Questions](#interview-questions)
  - [References](#references-2)
  - [Questions](#questions)
- [Chapters](#chapters)
- [References](#references-3)



# Introduction
Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.

Python is a programming language that lets you work quickly and integrate systems more efficiently.



# Python Version
There are two major Python versions: Python 2 and Python 3. Both are quite different.
- Python 2
- Python 3

# Learning Index    
## Decorators
### Definition
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. In Python, everything is a object.

Decorator takes a function as arguments and returns a function by adding some functionality.

```python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
```
> Note: `@` is used to call the decorated function more eligantly.

### Prerequisites of Decorators
Decorator closely related to some python concepts which are basic building block for decorators.
- Nested Fuctions
- Pass Functions as Arguments
- Return a Function as Value

Details also available here
**Nested Functions**

We can include one function inside another, known as a nested function. For example,

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)  # prints 11

# Output: 11
```

**Pass Functions as Arguments**  

We can pass a function as an argument to another function in Python. For Example,
```python
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10
```

**Return a Function as a Value**  
we can also return a function as a return value. For example,

```python
def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!
```

### Example

Before Decorator `@` symbol
```python
def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()
```

After Decorator `@` symbol

```python
def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  
```

### References
- https://www.programiz.com/python-programming/decorator

## Python Data Types
Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are classes and variables are instances (objects) of these classes. 

The following are the standard or built-in data types in Python:

- Numeric
  - Integer
  - Float
  - Complex Number 
- Dictionary
- Boolean
- Set
- Sequence Type
  - String
  - List
  - Tuple 

![Pthon Data Types](img/python_data_types.png)

**1. Numbers** – They include integers, floating-point numbers, and complex numbers. eg. 1, 7.9,3+4i

**2. List** – An ordered sequence of items is called a list. The elements of a list may belong to different data types. Eg. [5,’market’,2.4]

**3. Tuple** – It is also an ordered sequence of elements. Unlike lists , tuples are immutable, which means they can’t be changed. Eg. (3,’tool’,1)

**4. String** – A sequence of characters is called a string. They are declared within single or double-quotes. Eg. “Sana”, ‘She is going to the market’, etc.

**5. Set** – Sets are a collection of unique items that are not in order. Eg. {7,6,8}

**6. Dictionary** – A dictionary stores values in key and value pairs where each value can be accessed through its key. The order of items is not important. Eg. {1:’apple’,2:’mango}

**7. Boolean** – There are 2 boolean values - True and False.     


```python
# Numbers Data Types
a = 5
print("Type of a: ", type(a)) 
  
b = 5.0
print("\nType of b: ", type(b)) 
  
c = 2 + 4j
print("\nType of c: ", type(c)) 

# Sequence Types

# String Types
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 

```

> Note: `type()` function is used to determine the type of data type. 



### References
- https://www.geeksforgeeks.org/python-data-types/


# Interview Questions
## References 
- https://www.edureka.co/blog/interview-questions/python-interview-questions/
  
  
## Questions
  > 1. How is memory managed in Python?  

Ans: Memory is managed in Python in the following ways:

1.  Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
2. The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
3. Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

> 2. Q29.What is a lambda function?

Ans: An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.

Example:
```python
a = lambda x,y : x+y
print(a(5, 6))
```

> Q3: What are the generators in python?  

Ans: Functions that return an iterable set of items are called generators.

> Q4. What does this mean: *args, **kwargs? And why would we use it?

- `*args` when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
  
- `**kwargs` is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and **billy but that would not be wise.

> Q5. What are Python packages?

- Modules: are python file with `.py` extension
- Packages: are folder with containing many python files with a special `__init__.py` file.









# Chapters
1. Whetting Your Appetite  
2. Using the Python Interpreter  
2.1. Invoking the Interpreter  
2.1.1. Argument Passing  
2.1.2. Interactive Mode  
2.2. The Interpreter and Its Environment  
2.2.1. Source Code Encoding  
3. An Informal Introduction to Python  
3.1. Using Python as a Calculator  
3.1.1. Numbers  
3.1.2. Strings  
3.1.3. Lists  
3.2. First Steps Towards Programming  
4. More Control Flow Tools  
4.1. if Statements  
4.2. for Statements  
4.3. The range() Function  
4.4. break and continue Statements, and else Clauses on Loops  
4.5. pass Statements  
4.6. match Statements  
4.7. Defining Functions  
4.8. More on Defining Functions  
4.8.1. Default Argument Values  
4.8.2. Keyword Arguments  
4.8.3. Special parameters  
4.8.3.1. Positional-or-Keyword Arguments  
4.8.3.2. Positional-Only Parameters  
4.8.3.3. Keyword-Only Arguments  
4.8.3.4. Function Examples  
4.8.3.5. Recap  
4.8.4. Arbitrary Argument Lists  
4.8.5. Unpacking Argument Lists  
4.8.6. Lambda Expressions  
4.8.7. Documentation Strings  
4.8.8. Function Annotations  
4.9. Intermezzo: Coding Style  
5. Data Structures  
5.1. More on Lists  
5.1.1. Using Lists as Stacks  
5.1.2. Using Lists as Queues  
5.1.3. List Comprehensions  
5.1.4. Nested List Comprehensions  
5.2. The del statement  
5.3. Tuples and Sequences  
5.4. Sets  
5.5. Dictionaries  
5.6. Looping Techniques  
5.7. More on Conditions  
5.8. Comparing Sequences and Other Types  
6. Modules  
6.1. More on Modules  
6.1.1. Executing modules as scripts  
6.1.2. The Module Search Path  
6.1.3. “Compiled” Python files  
6.2. Standard Modules  
6.3. The dir() Function  
6.4. Packages  
6.4.1. Importing * From a Package  
6.4.2. Intra-package References  
6.4.3. Packages in Multiple Directories  
7. Input and Output  
7.1. Fancier Output Formatting  
7.1.1. Formatted String Literals  
7.1.2. The String format() Method    
7.1.3. Manual String Formatting  
7.1.4. Old string formatting  
7.2. Reading and Writing Files  
7.2.1. Methods of File Objects  
7.2.2. Saving structured data with json  
8. Errors and Exceptions  
8.1. Syntax Errors  
8.2. Exceptions  
8.3. Handling Exceptions  
8.4. Raising Exceptions  
8.5. Exception Chaining  
8.6. User-defined Exceptions  
8.7. Defining Clean-up Actions  
8.8. Predefined Clean-up Actions  
9. Classes  
9.1. A Word About Names and Objects  
9.2. Python Scopes and Namespaces  
9.2.1. Scopes and Namespaces Example  
9.3. A First Look at Classes  
9.3.1. Class Definition Syntax  
9.3.2. Class Objects  
9.3.3. Instance Objects  
9.3.4. Method Objects  
9.3.5. Class and Instance Variables  
9.4. Random Remarks  
9.5. Inheritance  
9.5.1. Multiple Inheritance  
9.6. Private Variables  
9.7. Odds and Ends  
9.8. Iterators  
9.9. Generators  
9.10. Generator Expressions  
10. Brief Tour of the Standard Library  
10.1. Operating System Interface  
10.2. File Wildcards  
10.3. Command Line Arguments  
10.4. Error Output Redirection and Program Termination  
10.5. String Pattern Matching  
10.6. Mathematics  
10.7. Internet Access  
10.8. Dates and Times  
10.9. Data Compression  
10.10. Performance Measurement  
10.11. Quality Control  
10.12. Batteries Included  
11. Brief Tour of the Standard Library — Part II  
11.1. Output Formatting  
11.2. Templating  
11.3. Working with Binary Data Record Layouts  
11.4. Multi-threading  
11.5. Logging  
11.6. Weak References  
11.7. Tools for Working with Lists  
11.8. Decimal Floating Point Arithmetic  
12. Virtual Environments and Packages  
12.1. Introduction  
12.2. Creating Virtual Environments  
12.3. Managing Packages with pip  
13. What Now?  
14. Interactive Input Editing and History Substitution  
14.1. Tab Completion and History Editing  
14.2. Alternatives to the Interactive Interpreter  
15. Floating Point Arithmetic: Issues and Limitations  
15.1. Representation Error  
16. Appendix  
16.1. Interactive Mode  
16.1.1. Error Handling  
16.1.2. Executable Python Scripts    
16.1.3. The Interactive Startup File  
16.1.4. The Customization Modules  

# References
- https://docs.python.org/3.10/tutorial/index.html
- https://mindmajix.com/top-20-python-frameworks-list



