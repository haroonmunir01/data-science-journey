# Student Record Manager

A simple command-line Student Record Manager built with Python.

## Why I Built This

This project was created as a practical way to refresh Python fundamentals by building something functional instead of studying individual concepts separately.

The goal was to practice writing Python code, handling user input, working with collections, and controlling program flow in a small real-world-style application.

## Features

* Add a new student
* View all student records
* Search for a student by name
* Add multiple students
* Navigate through a command-line menu
* Exit the application

## Concepts Practiced

* Variables
* User input and type conversion
* Lists
* Dictionaries
* for loops
* while loops
* Nested loops
* match/case
* break and continue
* Functions
* Function arguments
* Boolean flags
* Conditional statements
* f-strings
* Basic terminal control
* time.sleep()

## Data Structure

Student records are stored as dictionaries inside a list:

```python
students = [
    {
        "name": "Haroon",
        "age": 22,
        "course": "Computer Science"
    }
]
```

This structure allows multiple student records to be stored and accessed using dictionary keys.

## How It Works

The program provides a menu where the user can choose an action:

```text
====== Student Record Manager ======

1. Add Student
2. View Students
3. Search Student
0. Exit
```

Each option performs a specific operation on the student records.

## Project Type

**Command-Line Application**

**Language:** Python
