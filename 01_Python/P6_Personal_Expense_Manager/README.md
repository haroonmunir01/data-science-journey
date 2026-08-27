# Project 06 – Personal Expense Manager

## Overview

Personal Expense Manager is a command-line Python application that allows users to record, view, search, and delete personal expenses.

The project focuses on practicing **file handling, CSV data storage, Python modules, functions, input validation, and basic data processing**.

Expense records are stored persistently in a CSV file so that data remains available after the program is closed.

## Features

* Add expenses
* View all expenses
* Search expenses by ID
* Delete expenses by ID
* Automatic expense ID generation
* Expense categories
* CSV-based data storage
* Input validation
* Empty-input validation
* Numeric amount validation
* Category selection validation
* Modular project structure
* Command-line menu

## Expense Categories

The project uses the following categories:

* Food
* Transport
* Shopping
* Bills
* Entertainment
* Health
* Education
* Rent
* Utilities
* Travel
* Subscriptions
* Other

## Technologies & Concepts Used

* Python
* CSV files
* `csv` module
* `csv.reader()`
* `csv.writer()`
* `csv.DictReader()`
* `open()`
* File modes
* `with` statement
* Lists
* Dictionaries
* List comprehensions
* Functions
* Python modules
* `import`
* `os` module
* `try/except`
* `FileNotFoundError`
* `ValueError`
* `enumerate()`
* `next()`
* `max()`
* Input validation
* Menu-driven program flow

## Project Structure

```text
P6_Personal_Expense_Manager/
│
├── main.py
├── expense_manager.py
├── csv_handling.py
├── expenses.csv
└── README.md
```

## How It Works

1. The program starts with a command-line menu.
2. The user selects an operation.
3. When adding an expense, the user enters the amount, category, and description.
4. The program generates the next available expense ID.
5. The expense is saved as a new row in `expenses.csv`.
6. Existing expenses can be loaded using `csv.DictReader()`.
7. Expenses can be displayed or searched by ID.
8. When an expense is deleted, the remaining records are written back to the CSV file.
9. The program continues running until the user selects the exit option.

## CSV Data Format

Expense data is stored using the following columns:

```text
id,amount,category,description
```

Example:

```text
1,500.0,Food,Lunch
2,350.0,Transport,Uber
3,1200.0,Entertainment,Movie
```

## Purpose

This project was created to practice **persistent data storage and file handling in Python** through a small practical application.

It introduced CSV-based data management, reading and writing structured data, modular Python files, and basic input validation.

The project also provided practice working with lists of dictionaries and Python's CSV tools.

