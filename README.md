<div align="center">
    <img src="img/logo.png" height="320" width="830" alt="Tech Stacks">
    <h1>Tech Stacks</h1>
    <strong>A tech stack is the combination of technologies a company uses to build and run an application or project.</strong>
</div>


<!-- TOC -->

- [Stacks](#stacks)
    - [Message Queue](#message-queue)
        - [Kafka](#kafka)
        - [RabbitMQ](#rabbitmq)
    - [Management Methodology](#management-methodology)
        - [Scrum](#scrum)

<!-- /TOC -->


# Introduction
XPath can be used to navigate through elements and attributes in an XML document.
- XPath stands for XML Path Language
- XPath uses "path like" syntax to identify and navigate nodes in an XML document
- XPath contains over 200 built-in functions
- XPath is a major element in the XSLT standard
- XPath is a W3C recommendation
## XPath Path Expressions
XPath uses path expressions to select nodes or node-sets in an XML document.

## XPath Standard Functions
XPath includes over 200 built-in functions.

There are functions for string values, numeric values, booleans, date and time comparison, node manipulation, sequence manipulation, and much more.

## XPath is Used in XSLT
XPath is a major element in the XSLT standard.

With XPath knowledge you will be able to take great advantage of your XSLT knowledge.

# XPath Nodes
## XPath Terminology 

### Nodes
In XPATH there are 7 kinds of Nodes

1. Element
2. Attribute
3. Text
4. Namespace
5. Processing-instruction
6. Comment
7. Root Node

XML documents are treated as trees of nodes. The topmost element of the tree is called the root element.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
```

### Atomic values

Atomic values are nodes with no children or parent.

```xml
J K. Rowling

"en"
```
### Items
Items are atomic values or nodes.

## Relationship of Nodes
### Parent

Each element and attibute has one parent.

```xml
<!--book is the parent-->
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
> In the above example: the `book` element is the parent of the `title`, `author`, `year`, and `price`.

### Children
Element nodes may have zero, one or more children.

```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
> In the above example: the `title`, `author`, `year`, and `price` elements are all children of the book element:


### Siblings
Nodes that have the same parent.

```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
>  In the above example: the title, author, year, and price elements are all siblings

### Ancestors

A node's parent, parent's parent, etc.


```xml
<bookstore>
    <book>
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
    </book>
</bookstore>
```
> In the following example; the ancestors of the title element are the book element and the bookstore element:



### Descendants
A node's children, children's children, etc.



```xml
<bookstore>
    <book>
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
    </book>
</bookstore>
```
> In the following example; descendants of the bookstore element are the book, title, author, year, and price elements:

# XPath Syntax
```xml

<?xml version="1.0" encoding="UTF-8"?>

<bookstore>
    <book>
        <title lang="en">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="en">Learning XML</title>
        <price>39.95</price>
    </book>
</bookstore>
```

## Selecting Nodes

Expression  | Description
----------- | -------------
nodename    | Selects all nodes with the name "nodename"
/           | Selects from the root node
//          | Selects nodes in the document from the current node that match the selection no matter where they are
.           | Selects the current node
..          | Selects the parent of the current node
@           | Selects attributes





## Predicates


## Selecting Unknown Nodes

## Selecting Several Paths



# Axes


# Operators


# References
- https://www.w3schools.com/xml/xpath_intro.asp

