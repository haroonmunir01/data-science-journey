# Project 05 – Library Management System

## Overview

Library Management System is a command-line Python application built using **Object-Oriented Programming (OOP)**.

The system manages books and library members. Users can add, view, search, and remove books, manage members, and handle book borrowing and returning.

The project is divided into multiple Python modules, with separate classes for books, members, and the library.

## Features

* Add books to the library
* View all books
* Search for books using Book ID
* Remove books from the library
* Add library members
* View all members
* Search for members using Member ID
* Borrow books
* Return books
* Automatically assign Book IDs
* Automatically assign Member IDs
* Track book availability
* Track borrowed books for each member
* Menu-driven command-line interface

## Project Structure

### Book

The `Book` class represents a book in the library.

Each Book object contains:

* Book ID
* Title
* Author
* Availability status

### Member

The `Member` class represents a library member.

Each Member object contains:

* Member ID
* Name
* List of borrowed books

### Library

The `Library` class manages the books and members.

It contains methods for:

* Adding books
* Viewing books
* Searching books
* Removing books
* Adding members
* Viewing members
* Searching members
* Borrowing books
* Returning books

## OOP Concepts Used

* Classes and objects
* `__init__()` constructors
* `self`
* Instance attributes
* Instance methods
* Object creation
* Objects stored inside lists
* Classes interacting with objects of other classes
* Object relationships
* Importing classes from separate modules
* Multiple Python modules
* Passing objects as method arguments

## How It Works

1. The user starts the program.
2. The main menu provides options for managing books and members.
3. When a book is added, a Book object is created with a unique Book ID.
4. The Book object is added to the Library's book collection.
5. Members can be created with automatically assigned Member IDs.
6. The Member object is added to the Library's member collection.
7. Books can be searched or removed using their Book IDs.
8. Members can be searched using their Member IDs.
9. A member can borrow an available book.
10. The borrowed Book object is stored in the member's `borrowed_books` list.
11. The book's availability changes to unavailable.
12. When the book is returned, it is removed from the member's borrowed books and becomes available again.


## Technologies & Concepts Used

* Python
* Object-Oriented Programming
* Classes
* Objects
* Constructors
* Instance attributes
* Instance methods
* Lists
* Dictionaries
* `for` loops
* `while` loops
* Conditional statements
* `match/case`
* `import`
* Python modules
* Object relationships
* Command-line menu flow

## Purpose

This project was created to transition from procedural Python programming into **Object-Oriented Programming**.

It introduced the practical use of classes, objects, constructors, instance attributes, methods, object relationships, and multi-file Python projects.

This project marks the completion of the **Python OOP mini-project phase** before moving on to the next stage of the learning track: **SQL**.

## Project Status

**Completed** — Python OOP Library Management System.
