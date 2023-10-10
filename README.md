<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="React">
    <h1>React</h1>
    <strong>A tech stack is the combination of technologies a company uses to build and run an application or project.</strong>
</div>

- [Introduction](#introduction)
- [Installation](#installation)
    - [Knowledge Prerequisites](#knowledge-prerequisites)
        - [Classes](#classes)
        - [Arrow Functions](#arrow-functions)
        - [Variables (var,let,const)](#variables-varletconst)
        - [Array Methods](#array-methods)
        - [Destructuing](#destructuing)
        - [Modules](#modules)
        - [Ternary Operators](#ternary-operators)
        - [Spread Operators](#spread-operators)
    - [Software Prerequisites](#software-prerequisites)
- [React Documentation](#react-documentation)
    - [Basic Features](#basic-features)
        - [React Components](#react-components)
        - [React Class](#react-class)
        - [React Props](#react-props)
        - [React Events](#react-events)
        - [React Conditionals](#react-conditionals)
        - [React Lists](#react-lists)
        - [React Forms](#react-forms)
        - [React Router](#react-router)
    - [Hooks](#hooks)
        - [useState](#usestate)
        - [useEffect](#useeffect)
        - [useContext](#usecontext)
        - [useRef](#useref)
        - [useReducer](#usereducer)
        - [useCallback](#usecallback)
        - [useMemo](#usememo)
        - [Custom Hooks](#custom-hooks)
    - [Create a new React Project](#create-a-new-react-project)
    - [Start React application using below command](#start-react-application-using-below-command)
- [References](#references)

# Introduction

[React](https://react.dev/) is a free and open-source front-end JavaScript library for building user interfaces based on
components. It is maintained by Meta and a community of individual developers and companies. React can be used to
develop single-page, mobile, or server-rendered applications with frameworks.

# Installation

[React Installation](https://react.dev/learn/installation) depends on operating system like linux,ubuntu,mac,windows. We
will install in major os.

## Knowledge Prerequisites

ECMAScript 6 which has a shorter version ES6.  
ECMAScript was created to standardize JavaScript, and ES6 is the 6th version of ECMAScript, it was published in 2015,
and is also known as ECMAScript 2015.

React uses some features of ES6 frequently

- Classes
- Arrow Functions
- Variables (var,let,const)
- Array Methods
- Destructuring
- Modules
- Ternary Operators
- Spread Operators

All Features described in details here

### Classes

In JavaScript, ES6 introduced classes, a class is a type of function, but instead of using a keyword `function` its
using a kayword `class`.

Simple JavaScript Classes Example

```javascript
class Car {
  constructor(name) {
    this.brand = name;
  }
}
```

JavaScript Classes with Inheritence

```javascript
class Car {
  constructor(name) {
    this.brand = name;
  }

  present() {
    return 'I have a ' + this.brand;
  }
}

class Model extends Car {
  constructor(name, mod) {
    super(name);
    this.model = mod;
  }  
  show() {
      return this.present() + ', it is a ' + this.model
  }
}
const mycar = new Model("Ford", "Mustang");
mycar.show();
```

### Arrow Functions

Arrow functions allow us to write shorter function syntax:

Previous Function Definition

```javascript
hello = function() {
  return "Hello World!";
}
```

Arrow Function Definition just changes `function ()` to `()=>` .

```javascript
hello = () => {
  return "Hello World!";
}

hello = () => "Hello World!";
hello = (val) => "Hello " + val;
hello = val => "Hello " + val;
```

### Variables (var,let,const)

In JavaScript, there are 3 scopes to define variables:

- **Global Scope**: Other than Function scope or Blocking scope
- **Function Scope**: Inside a function
- **Block Scope**: Inside a block like loop

Before ES6, JavaScript has only one variable definition using `var`. Depending on javascript it behaves differently.

- If you use var outside of a function, it belongs to the global scope.
- If you use var inside of a function, it belongs to that function.
- If you use var inside of a block, i.e. a for loop, the variable is still available outside of that block.

```javascript
var x = 5.6;
```

But in Es6, JavaScript introduce three keyword for variable definitions, and they are `var, let, const`, although `var`
was already in javascript previously.

> var has a function scope, not a block scope.


**let**  
`let` is the block scoped version of var, and is limited to the block (or expression) where it is defined.

If you use let inside of a block, i.e. a for loop, the variable is only available inside of that loop.

```javascript
let x = 5.6;
```

> let has a block scope.

**const**

`const`` is a variable that once it has been created, its value can never change.
The keyword const is a bit misleading.

It does not define a constant value. It defines a constant reference to a value.

Because of this you can NOT:

Reassign a constant value
Reassign a constant array
Reassign a constant object
But you CAN:

Change the elements of constant array
Change the properties of constant object

```javascript
const x = 5.6;
```

> const has a block scope.

### Array Methods

In JavaScript, arrays aren't primitives but are instead Array
objects. [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) in javascript
uses several methods for operations but most of them few methods mostly used in React frequently. Those methods are

- Array.map()
- Array.filter()
- Array.find()

All methods takes functions as arguments. Details of theose function are in here

[Array Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)   
`Array.map(()=>{})`

**Parameters**  
**callbackFn**, a function to execute for each element in the array. Its return value is added as a single element in
the new array.

**Return value**  
A new array with each element being the result of the callback function.

```javascript
# Mapping an array of numbers to an array of square roots

const numbers = [1, 4, 9];
const roots = numbers.map((num) => Math.sqrt(num));

# Using map to reformat objects in an array

const kvArray = [
  { key: 1, value: 10 },
  { key: 2, value: 20 },
  { key: 3, value: 30 },
];

const reformattedArray = kvArray.map(({ key, value }) => ({ [key]: value }));
```

[Array Find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
`Array.find(()=>{})`

**Parameters**  
**callbackFn**, a function to execute for each element in the array. It should return a truthy value to indicate a
matching element has been found, and a falsy value otherwise.

**Return value**  
The first element in the array that satisfies the provided testing function. Otherwise, undefined is returned.

Example

```javascript
const inventory = [
  { name: "apples", quantity: 2 },
  { name: "bananas", quantity: 0 },
  { name: "cherries", quantity: 5 },
];

const result = inventory.find(({ name }) => name === "cherries");
```

[Array Filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)  
`Array.filter(()=>{})`

**Parameters**  
**callbackFn**, a function to execute for each element in the array. It should return a truthy value to indicate a
matching element has been found, and a falsy value otherwise.

**Return value**  
A shallow copy of the given array containing just the elements that pass the test. If no elements pass the test, an
empty array is returned.

Example

```javascript
function isBigEnough(value) {
  return value >= 10;
}

const filtered = [12, 5, 8, 130, 44].filter(isBigEnough);
```

### Destructuing

```javascript

const vehicles = ['mustang', 'f-150', 'expedition'];

// old way
const car = vehicles[0];
const truck = vehicles[1];
const suv = vehicles[2];
```

### Modules

JavaScript modules allow you to break up your code into separate files.

This makes it easier to maintain the code-base.

ES Modules rely on the import and export statements.

### Ternary Operators

The ternary operator is a simplified conditional operator like if / else.

`Syntax: condition ? <expression if true> : <expression if false>`

```javascript
if (authenticated) {
  renderApp();
} else {
  renderLogin();
}

# Converted to

authenticated ? renderApp() : renderLogin();
```

### Spread Operators

The JavaScript spread operator (...) allows us to quickly copy all or part of an existing array or object into another
array or object.

```javascript
# Example 1
const numbersOne = [1, 2, 3];
const numbersTwo = [4, 5, 6];
const numbersCombined = [...numbersOne, ...numbersTwo];

# Example 2

const numbers = [1, 2, 3, 4, 5, 6];

const [one, two, ...rest] = numbers;

```

## Software Prerequisites

1. Install `nodejs` and `npm` on Ubuntu OS

```shell
$ sudo apt-get install nodejs
```

2. Install `npm` on Ubuntu OS

```shell
$ sudo apt install npm
```

3. Now install `npx` using node

```shell
$ npm install -g npx
```

## Create a new React Project

using below commands, it will create a all the dependencies with default project structure.

```shell
$npx create-react-app <APP_NAME> 
```

> `APP_NAME` name will be any valid name.

Example:

```shell
$ npx create-react-app quiz-apps
```

## Start React application using below command

```shell
$ cd quiz-apps 
$ npm run start or npm start
```

# React Documentation

## Basic Features

### React Components

### React Class

### React Props

### React Events

### React Conditionals

### React Lists

### React Forms

### React Router

## Hooks

React Hooks are simple JavaScript functions that we can use to isolate the reusable part from a functional component.
Hooks can be stateful and can manage side-effects. React provides a bunch of standard in-built hooks

Hooks let you use different React features from your components. You can either use the built-in Hooks or combine them
to build your own. This page lists all built-in Hooks in React.

There almost 15 built-in hooks available in React.

### State Hooks

#### 1. useState

#### 2. useReducer



### Context Hooks

#### 3. useContext



### Ref Hooks

#### 4. useRef
#### 5. useImperativeHandle

### Effect Hooks

#### 6. useEffect


### Performance Hooks

#### 7. useCallback

#### 8. useMemo

#### 9. useTransition

#### 10. useDeferredValue

#### 11. useLayoutEffect

### Resource Hooks

#### 12. useDeferredValue

### Other Hooks

#### 13. useDebugValue

#### 14. useId

#### 15. useSyncExternalStore


### Custom Hooks
You can also [define your own custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks#extracting-your-own-custom-hook-from-a-component) as JavaScript functions.



# References

- https://react.dev/learn/start-a-new-react-project
- https://www.w3schools.com/REACT/react_es6_array_methods.asp
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- https://devdocs.io/react/hooks-intro
- https://react.dev/reference/react