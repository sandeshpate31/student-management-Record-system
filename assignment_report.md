# ASSIGNMENT REPORT

## Mini Project –# Student Record Management System Application
## Mini Project-# Console Record-Management Application

### MCA Semester I

**Subject:** Python Programming & Relational Database

**Student Name:** Sandesh Suresh Pate

**Roll No:** 25

**Course:** MCA Semester I

**Assignment 1-** Mini Project:Console Record-Management Application
---

# 1. Introduction

The Student Record Management System Application is a Python-based mini project developed to demonstrate fundamental Python programming concepts and relational database connectivity.

The application provides a simple console-based interface through which users can manage student records.

The system supports adding, viewing, searching, updating, and deleting student records.

MySQL is used as the relational database and JSON File I/O is used to demonstrate persistent file handling.

---

# 2. Problem Statement

Managing student information manually can be time-consuming and may result in errors or loss of information.

The purpose of this project is to develop a simple computerized record-management application that can store and manage student information efficiently.

The application should provide a menu-driven interface and support basic CRUD operations.

---

# 3. Objectives

The main objectives of this project are:

1. To develop a menu-driven Python application.
2. To understand Python variables and data types.
3. To implement conditional statements and loops.
4. To use functions for modular programming.
5. To implement exception handling.
6. To understand File I/O.
7. To connect Python with MySQL.
8. To perform CRUD operations.
9. To store student records permanently.
10. To develop a clean and maintainable Python application.

---

# 4. Scope of the Project

The application can be used for basic student record management.

It can store information such as:

* Student ID
* Student Name
* Age
* Course
* Email

The project can be further extended with additional features such as:

* Login system
* Student attendance
* Marks management
* Search by name
* Multiple tables
* GUI interface
* Web-based interface

---

# 5. Technologies Used

## Python

Python is used as the primary programming language.

## MySQL

MySQL is used as the relational database management system.

## MySQL Connector/Python

The connector allows Python to communicate with MySQL.

## JSON

JSON is used for File I/O and maintaining a file-based copy of records.

## GitHub

GitHub is used for source-code submission and project version control.

---

# 6. Hardware Requirements

Minimum hardware requirements:

* Computer/Laptop
* 4 GB RAM or higher
* Basic storage space
* Keyboard
* Monitor

---

# 7. Software Requirements

* Windows / Linux / macOS
* Python 3.x
* MySQL Server
* MySQL Workbench
* VS Code or Python IDLE
* Git
* GitHub Account

---

# 8. System Design

The system follows a modular architecture.

```text
             USER
               |
               v
          main.py
               |
               v
      record_service.py
          /          \
         /            \
        v              v
   database.py    file_handler.py
        |              |
        v              v
      MySQL         records.json
```

---

# 9. Project Modules

## 9.1 main.py

The `main.py` file is responsible for:

* Starting the application
* Displaying the menu
* Accepting user choices
* Calling appropriate functions

---

## 9.2 database.py

The `database.py` file establishes a connection between Python and MySQL.

It contains the `create_connection()` function.

---

## 9.3 record_manager.py

This module contains the main record-management operations.

Functions include:

* `add_record()`
* `view_records()`
* `search_record()`
* `update_record()`
* `delete_record()`

---

## 9.4 file_handler.py

This module manages JSON File I/O.

It provides functions for:

* Loading records
* Saving records

The JSON file is located at:

```text
data/records.json
```

---

## 9.5 schema.sql

The `schema.sql` file contains SQL commands for creating the database and table.

---

# 10. Database Design

Database name:

```text
student_management
```

Table:

```text
students
```

Structure:

| Field  | Type         | Constraint                  |
| ------ | ------------ | --------------------------- |
| id     | INT          | Primary Key, Auto Increment |
| name   | VARCHAR(100) | NOT NULL                    |
| age    | INT          | NOT NULL                    |
| course | VARCHAR(100) | NOT NULL                    |
| email  | VARCHAR(100) | UNIQUE, NOT NULL            |

---

# 11. SQL Schema

```sql
CREATE DATABASE IF NOT EXISTS student_management;

USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

---

# 12. Python Data Types Used

The project uses several Python data types.

### String

Used for:

```python
name
course
email
```

### Integer

Used for:

```python
age
student_id
```

### List

Used to store multiple records loaded from JSON.

### Dictionary

Used to represent individual student records in JSON.

Example:

```python
{
    "id": 1,
    "name": "Sandesh",
    "age": 22,
    "course": "MCA",
    "email": "sandesh@gmail.com"
}
```

---

# 13. Conditional Statements

Conditional statements are used for menu selection.

Example:

```python
if choice == "1":
    add_record()

elif choice == "2":
    view_records()

else:
    print("Invalid choice.")
```

---

# 14. Loops

A `while` loop is used to continuously display the menu until the user selects Exit.

Example:

```python
while True:
    display_menu()
```

A `for` loop is used to process records.

---

# 15. Functions

Functions are used to divide the application into smaller logical units.

Examples:

```python
add_record()
view_records()
search_record()
update_record()
delete_record()
```

This improves readability, reusability, and maintainability.

---

# 16. Exception Handling

Exception handling is implemented using `try` and `except`.

Example:

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number.")
```

This prevents the application from crashing when the user enters invalid input.

---

# 17. File I/O

The application uses JSON File I/O.

The following functions are used:

```python
load_records()
save_records()
```

Python's:

```python
open()
```

function is used to read and write the JSON file.

---

# 18. CRUD Operations

CRUD stands for:

```text
Create
Read
Update
Delete
```

The application implements:

| Operation | Application Feature |
| --------- | ------------------- |
| Create    | Add Record          |
| Read      | View/Search Record  |
| Update    | Update Record       |
| Delete    | Delete Record       |

---

# 19. Menu-Driven Interface

The application displays the following menu:

```text
==============================
 STUDENT RECORD MANAGEMENT
==============================
1. Add Record
2. View Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
==============================
```

The user selects an option and the corresponding function is executed.

---

# 20. Application Workflow

```text
Start
  |
  v
Display Menu
  |
  v
User Selects Option
  |
  +---- Add ------> MySQL + JSON
  |
  +---- View -----> MySQL
  |
  +---- Search ---> MySQL
  |
  +---- Update ---> MySQL
  |
  +---- Delete ---> MySQL
  |
  +---- Exit -----> End
```

---

# 21. Sample Input and Output

## Adding a Record

```text
Enter your choice: 1

Enter name: Sandesh
Enter age: 22
Enter course: MCA
Enter email: sandesh@gmail.com

Record added successfully!
Student ID: 1
```

## Viewing Records

```text
Enter your choice: 2

ID: 1
Name: Sandesh
Age: 22
Course: MCA
Email: sandesh@gmail.com
```

---

# 22. Testing

The application was tested using different inputs.

| Test Case    | Input          | Expected Result        |
| ------------ | -------------- | ---------------------- |
| Add record   | Valid details  | Record added           |
| View records | Option 2       | Records displayed      |
| Search       | Valid ID       | Record displayed       |
| Search       | Invalid ID     | Record not found       |
| Update       | Valid ID       | Record updated         |
| Delete       | Valid ID       | Record deleted         |
| Age          | Text input     | Error message          |
| Menu         | Invalid option | Invalid choice message |

---

# 23. Advantages

* Simple console interface
* Easy to understand
* Modular code structure
* Persistent database storage
* JSON File I/O
* Exception handling
* CRUD functionality
* Easy to extend

---

# 24. Limitations

* Console-based interface only
* No user authentication
* Basic validation
* Designed for basic record management
* No graphical user interface

---

# 25. Future Enhancements

The project can be enhanced by adding:

1. Login authentication
2. GUI using Tkinter
3. Web interface using Django/Flask
4. Advanced search
5. Sorting and filtering
6. Student attendance
7. Marks management
8. Export to CSV/PDF
9. Multiple database tables
10. Role-based access

---

# 26. Screenshots



The following screenshots should be included in the final report:


1. Add record
2. View records
3. Search record
4. Update record
5. Delete record
6. MySQL students table

    
1] ADD RECORD:

<img width="800" height="450" alt="add_Record" src="https://github.com/user-attachments/assets/07277089-0d4e-4aa9-9275-da1eb23d46b9" />

2] VIEW RECORD:

<img width="800" height="450" alt="View_record" src="https://github.com/user-attachments/assets/0ecc70b6-7fb0-4dad-b9d7-abaf56f1121d" />

3] SEARCH RECORD:

<img width="800" height="450" alt="Search_record" src="https://github.com/user-attachments/assets/b3bcf57d-e290-44f0-88df-878ee2697cd5" />

4] UPDATE RECORD:

<img width="800" height="450" alt="update_record" src="https://github.com/user-attachments/assets/d71e50ba-a491-48f2-89ae-79bcd5d03398" />

5] DELETE RECORD:

<img width="800" height="450" alt="Delete_record" src="https://github.com/user-attachments/assets/9d14a183-0ed0-49dd-916d-6ee4901f084f" />

6] MYSQL STUDENT STABLE:

<img width="800" height="450" alt="SQL_DATABASE" src="https://github.com/user-attachments/assets/3bcbc1df-a637-4fa3-9843-e7f6ef3429b8" />



---

# 27. Conclusion

The Console Record Management Application successfully demonstrates the use of fundamental Python programming concepts and relational database connectivity.

The project implements a menu-driven interface with CRUD operations, exception handling, File I/O, and MySQL connectivity.

The modular structure makes the application easy to understand, maintain, and extend.

This project helped in understanding how Python can be integrated with a relational database to create a practical record-management application.

---

# 28. References

* Python Documentation
* MySQL Documentation
* MySQL Connector/Python Documentation
* GitHub Documentation
