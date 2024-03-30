<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="React">
    <h1>React</h1>
    <strong>A tech stack is the combination of technologies a company uses to build and run an application or project.</strong>
</div>

- [Introduction](#introduction)
- [Installation](#installation)
  - [Software Prerequisites](#software-prerequisites)
  - [Create React App](#create-react-app)
  - [Start React App](#start-react-app)
  - [Geeks Prerequisites](#geeks-prerequisites)
    - [Classes](#classes)
    - [Arrow Functions](#arrow-functions)
    - [Variables (var,let,const)](#variables-varletconst)
    - [Array Methods](#array-methods)
    - [Destructuing](#destructuing)
    - [Modules](#modules)
    - [Ternary Operators](#ternary-operators)
    - [Spread Operators](#spread-operators)
- [React Documentation](#react-documentation)
  - [Basic Features](#basic-features)
    - [React Components](#react-components)
      - [Class Component](#class-component)
      - [Function components](#function-components)
    - [React Class](#react-class)
    - [React Props](#react-props)
    - [React Events](#react-events)
    - [React Conditionals](#react-conditionals)
    - [React Lists](#react-lists)
      - [Keys](#keys)
    - [React Forms](#react-forms)
    - [React Router](#react-router)
    - [React Memo](#react-memo)
  - [Hooks](#hooks)
    - [State Hooks](#state-hooks)
      - [1. useState](#1-usestate)
      - [2. useReducer](#2-usereducer)
    - [Context Hooks](#context-hooks)
      - [3. useContext](#3-usecontext)
    - [Ref Hooks](#ref-hooks)
      - [4. useRef](#4-useref)
      - [5. useImperativeHandle](#5-useimperativehandle)
    - [Effect Hooks](#effect-hooks)
      - [6. useEffect](#6-useeffect)
    - [Performance Hooks](#performance-hooks)
      - [7. useCallback](#7-usecallback)
      - [8. useMemo](#8-usememo)
      - [9. useTransition](#9-usetransition)
      - [10. useDeferredValue](#10-usedeferredvalue)
      - [11. useLayoutEffect](#11-uselayouteffect)
    - [Resource Hooks](#resource-hooks)
      - [12. useDeferredValue](#12-usedeferredvalue)
    - [Other Hooks](#other-hooks)
      - [13. useDebugValue](#13-usedebugvalue)
      - [14. useId](#14-useid)
      - [15. useSyncExternalStore](#15-usesyncexternalstore)
    - [Custom Hooks](#custom-hooks)
- [Interview Questions](#interview-questions)
- [References](#references)

# Introduction

[React](https://react.dev/) is a free and open-source front-end JavaScript library for building user interfaces based on
components. It is maintained by Meta and a community of individual developers and companies. React can be used to
develop single-page, mobile, or server-rendered applications with frameworks.

# Installation

[React Installation](https://react.dev/learn/installation) depends on operating system like linux,ubuntu,mac,windows. We
will install in major os.

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

## Create React App

Using below commands, it will create a all the dependencies with default project structure.

```shell
$npx create-react-app <APP_NAME> 
```

> `APP_NAME` name will be any valid name.

Example:

```shell
$ npx create-react-app quiz-apps
```

## Start React App

```shell
$ cd quiz-apps 
$ npm run start or npm start
```

## Geeks Prerequisites

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

# React Documentation

## Basic Features

### React Components

Components are independent and reusable bits of code. They serve the same purpose as JavaScript functions, but work in
isolation and return HTML.

Components come in two types

- Class components
- Function components

#### Class Component

A class component must include the extends React.Component statement. This statement creates an inheritance to
React.Component, and gives your component access to React.Component's functions.

```javascript
class Car extends React.Component {
  render() {
    return <h2>Hi, I am a Car!</h2>;
  }
}
```

#### Function components

A Function component also returns HTML, and behaves much the same way as a Class component, but Function components can
be written using much less code, are easier to understand, and will be preferred in this tutorial.

```javascript
function Car() {
  return <h2>Hi, I am a Car!</h2>;
}
```

Rendering a React Components using

```javascript
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Car />);
```

### React Class

Follow Documents

- https://www.w3schools.com/REACT/react_class.asp

### React Props

React Props are like function arguments in JavaScript and attributes in HTML.

React Props are also how you pass data from one component to another, as parameters.

To send props into a component, use the same syntax as HTML attributes:

```javascript
const myElement = <Car brand="Ford" />;
```

The component receives the argument as a props object:

```javascript
function Car(props) {
  return <h2>I am a { props.brand }!</h2>;
}
```

> Note: React Props are read-only! You will get an error if you try to change their value.
>
Follow Documents

- https://www.w3schools.com/REACT/react_props.asp

### React Events

Just like HTML DOM events, React can perform actions based on user events.

React has the same events as HTML: click, change, mouseover etc.

Adding Events
React events are written in camelCase syntax:

`onClick` instead of `onclick`.

React event handlers are written inside curly braces:

`onClick={shoot} ` instead of `onClick="shoot()"`.

```javascript
# React
<button onClick={shoot}>Take the Shot!</button>

# HTML
<button onclick="shoot()">Take the Shot!</button>
```

**Example**

```javascript
function Football() {
  const shoot = () => {
    alert("Great Shot!");
  }

  return (
    <button onClick={shoot}>Take the shot!</button>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Football />);
```

Follow Documents

- https://www.w3schools.com/REACT/react_events.asp

### React Conditionals

Follow Documents

- https://www.w3schools.com/REACT/react_conditional_rendering.asp

### React Lists

In React, you will render lists with some type of loop.

The JavaScript map() array method is generally the preferred method.

#### Keys

Keys allow React to keep track of elements. This way, if an item is updated or removed, only that item will be
re-rendered instead of the entire list.

Keys need to be unique to each sibling. But they can be duplicated globally.

```javascript
function Car(props) {
  return <li>I am a { props.brand }</li>;
}

function Garage() {
  const cars = [
    {id: 1, brand: 'Ford'},
    {id: 2, brand: 'BMW'},
    {id: 3, brand: 'Audi'}
  ];
  return (
    <>
      <h1>Who lives in my garage?</h1>
      <ul>
        {cars.map((car) => <Car key={car.id} brand={car.brand} />)}
      </ul>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Garage />);
```

### React Forms

Follow Documents

- https://www.w3schools.com/REACT/react_forms.asp

### React Router
Create React App doesn't include page routing.

React Router is a lightweight, fully-featured routing library for the React JavaScript library. React Router runs everywhere that React runs; on the web, on the server (using node.js), and on React Native.
```javascript
npm install react-router-dom
```

React Router in application using in this way

```javascript
//Import it from your react index.js file
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

//Rap your app with BrowserRouter
<BrowserRouter>
	<App />  
</BrowserRouter>

//Define you Routes in your app and import it on the top
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/create" element={<Create />} />
  <Route path="/blogs/:id" element={<BlogDetails />} />
  <Route path="*" element={<NotFound />} />
</Routes>

//Now you are all set. You can use this with
<Link to="/create" element={Create}/>
```

Follow Documents

- https://www.w3schools.com/REACT/react_router.asp

### React Memo

Using memo will cause React to skip rendering a component if its props have not changed.
This can improve performance.

Follow Documents

- https://www.w3schools.com/REACT/react_memo.asp

## Hooks

React Hooks are simple JavaScript functions that we can use to isolate the reusable part from a functional component.
Hooks can be stateful and can manage side-effects. React provides a bunch of standard in-built hooks

Hooks let you use different React features from your components. You can either use the built-in Hooks or combine them
to build your own. This page lists all built-in Hooks in React.

There are 3 rules for hooks

- Hooks can only be called inside React function components.
- Hooks can only be called at the top level of a component.
- Hooks cannot be conditional

> Note: [More details about React Hooks Rules](https://devdocs.io/react/hooks-rules)


There are 15 built-in hooks available in React.

### State Hooks

State lets a component “remember” information like user input.

For example, a form component can use state to store the input value, while an image gallery component can use state to
store the selected image index.

To add state to a component, use one of these Hooks

#### 1. useState

The React `useState` Hook allows us to track state in a function component.

```javascript
const [state, setState] = useState(initialState);
```

**Import `useState`**

```javascript
import { useState } from "react";
```

**Initialize `useState`**

We initialize our state by calling useState in our function component.

`useState` accepts an initial state and returns two values:

The current state.
A function that updates the state.

```javascript
import { useState } from "react";

function FavoriteColor() {
  const [color, setColor] = useState("");
  const [cars,setCars] = useState([]);
}
```

**Read `useState`**

We can now include our state anywhere in our component.

```javascript
import { useState } from "react";
import ReactDOM from "react-dom/client";

function FavoriteColor() {
  const [color, setColor] = useState("red");

  return <h1>My favorite color is {color}!</h1>
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<FavoriteColor />);
```

**Update `useState`**
To update our state, we use our state updater function.

```javascript
import { useState } from "react";
import ReactDOM from "react-dom/client";

function FavoriteColor() {
  const [color, setColor] = useState("red");

  return (
    <>
      <h1>My favorite color is {color}!</h1>
      <button
        type="button"
        onClick={() => setColor("blue")}
      >Blue</button>
    </>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<FavoriteColor />);
```

#### 2. useReducer

Follow Documents

- https://www.w3schools.com/REACT/react_usereducer.asp
- https://devdocs.io/react/hooks-reference#usereducer
- https://react.dev/reference/react/useReducer

### Context Hooks

#### 3. useContext

React Context is a way to manage state globally.

It can be used together with the useState Hook to share state between deeply nested components more easily than with
useState alone.

Follow Documents

- https://www.w3schools.com/REACT/react_usecontext.asp
- https://devdocs.io/react/hooks-reference#usecontext

### Ref Hooks

#### 4. useRef

The useRef Hook allows you to persist values between renders.

It can be used to store a mutable value that does not cause a re-render when updated.

It can be used to access a DOM element directly.

Does Not Cause Re-renders
If we tried to count how many times our application renders using the useState Hook, we would be caught in an infinite
loop since this Hook itself causes a re-render.

To avoid this, we can use the useRef Hook.

```javascript
import { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom/client";

function App() {
  const [inputValue, setInputValue] = useState("");
  const count = useRef(0);

  useEffect(() => {
    count.current = count.current + 1;
  });

  return (
    <>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <h1>Render Count: {count.current}</h1>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

> useRef() only returns one item. It returns an Object called current.

> When we initialize useRef we set the initial value: useRef(0).


Follow Documents

- https://dmitripavlutin.com/react-useref/
- https://www.w3schools.com/REACT/react_useref.asp

#### 5. useImperativeHandle

Follow Documents

- https://devdocs.io/react/hooks-reference#useimperativehandle
- https://react.dev/reference/react/useImperativeHandle

### Effect Hooks

#### 6. useEffect

The `useEffect` Hook allows you to perform side effects in your components.

Mutations, subscriptions, timers, logging, and other side effects are not allowed inside the main body of a function
component (referred to as React’s render phase). Doing so will lead to confusing bugs and inconsistencies in the UI.

Some examples of side effects are:

- fetching data
- directly updating the DOM
- timers

useEffect accepts two arguments. The second argument is optional.

`
useEffect(<function>, <dependency>)
`

`useEffect` runs on every render. That means that when the count changes, a render happens, which then triggers another
effect.

This is not what we want. There are several ways to control when side effects run.

We should always include the second parameter which accepts an array. We can optionally pass dependencies to useEffect
in this array.

```javascript
useEffect(() => {
  //Runs on every render
});

useEffect(() => {
  //Runs only on the first render
}, []);

useEffect(() => {
  //Runs on the first render
  //And any time any dependency value changes
}, [prop, state]);


```

So, to fix this issue, let's only run this effect on the initial render.

```javascript
import { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    setTimeout(() => {
      setCount((count) => count + 1);
    }, 1000);
  }, []); // <- add empty brackets here

  return <h1>I've rendered {count} times!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Timer />);
```

Follow Documents

- https://www.w3schools.com/REACT/react_useeffect.asp
- https://devdocs.io/react/hooks-reference#useeffect

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

You can
also [define your own custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks#extracting-your-own-custom-hook-from-a-component)
as JavaScript functions.

# Interview Questions
Prepare for Interview [here](./interview/README.md).

# References

- https://react.dev/learn/start-a-new-react-project
- https://www.w3schools.com/REACT/react_es6_array_methods.asp
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- https://devdocs.io/react/hooks-intro
- https://react.dev/reference/react
- https://state-updates.vercel.app/
- https://jsx-notes.vercel.app/
  
