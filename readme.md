# Personal Expense Tracker

## Project Overview

Personal Expense Tracker is a Python-based application that helps users track and manage their daily expenses. Users can add, view, delete, and analyze their expenses easily. The project uses SQLite as the database for storing data permanently, Pandas for data analysis, and Matplotlib for data visualization.

---

## Features

* Add new expense with date, category, amount, and description
* View all stored expenses in a structured format
* Delete expense by ID
* Undo delete functionality using backup system
* Category-wise expense analysis
* Total expense calculation
* Persistent data storage using SQLite database

---

## Technologies Used

* Python
* SQLite3
* Pandas
* Matplotlib

---

## Project Structure

Personal Expense Tracker/
│
├── main.py # Main menu-driven program
├── database.py # Database connection and table creation
├── operations.py # Add, view, delete, undo operations
├── reports.py # Data analysis using Pandas
├── graphs.py # Data visualization using Matplotlib
└── README.md


---

## Database Fields

* ID (Auto Increment Primary Key)
* Date
* Category
* Amount
* Description

---

## Graphical Representation

* Pie Chart is used to show category-wise expense distribution using Matplotlib

---

## How to Run

### 1. Install required dependencies

```bash
pip install pandas matplotlib

2. Run the project
   python main.py

3. Use the menu
   Add Expense
   View Expenses
   Delete Expense
   Undo Delete
   View Reports
   View Pie Chart

   Learning Outcomes

This project helps to understand:

  Python programming basics
  Conditional statements and loops
  Functions and modular coding
  SQLite database handling
  SQL queries (INSERT, SELECT, DELETE)
  Data analysis using Pandas
  Data visualization using Matplotlib
  Real-world project structure

Author:
Krapali Dwivedi