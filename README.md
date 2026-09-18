# Student Record Management System Application

## 1. Project Title

**student Record Management  system Application**

## 2. Student Details

**Name:** Sandesh Pate
**Course:** MCA Semester I
**Subject:** Python Programming & Relational Database
**Project Type:** Mini Project – Assignment 1

---

## 3. Project Description

The Console Record Management Application is a Python-based menu-driven application developed for managing student records.

The application allows the user to:

* Add student records
* View all student records
* Search for a student record
* Update existing records
* Delete records
* Store records permanently using MySQL
* Maintain records using JSON File I/O
* Handle invalid inputs and runtime errors

The project demonstrates basic Python programming concepts along with relational database connectivity using MySQL.

---

## 4. Features

### Add Record

Allows the user to enter a student's name, age, course, and email.

### View Records

Displays all student records stored in the MySQL database.

### Search Record

Searches for a student using the student ID.

### Update Record

Allows the user to modify an existing student's details.

### Delete Record

Deletes a student record using the student ID.

### File Storage

A JSON file is used to maintain a file-based copy of the records.

### MySQL Database

MySQL is used as the main relational database for storing student records.

### Exception Handling

The application handles invalid numeric input, database errors, and file-related errors.

---

## 5. Technologies Used

* Python 3
* MySQL
* MySQL Connector/Python
* JSON
* VS Code / Python IDLE
* GitHub

---

## 6. Python Concepts Used

The project demonstrates:

* Variables
* Data Types
* Lists
* Dictionaries
* Conditional Statements
* Loops
* Functions
* Exception Handling
* File I/O
* Modules
* SQL Queries
* Database Connectivity
* CRUD Operations
* Menu-driven Programming

---

## 7. Project Structure

```text
console_record_management/
│
├── main.py
├── database.py
├── record_manager.py
├── file_handler.py
├── schema.sql
├── requirements.txt
├── README.md
├── assignment_report.md
│
├── data/
│   └── records.json
│
└── screenshots/
    ├── menu.png
    ├── add_record.png
    ├── view_records.png
    ├── search_record.png
    ├── update_record.png
    ├── delete_record.png
    └── mysql_database.png
```

---

## 8. Database Structure

Database name:

```text
student_management
```

Table name:

```text
students
```

Table columns:

| Column | Data Type    | Description   |
| ------ | ------------ | ------------- |
| id     | INT          | Primary Key   |
| name   | VARCHAR(100) | Student name  |
| age    | INT          | Student age   |
| course | VARCHAR(100) | Course name   |
| email  | VARCHAR(100) | Student email |

---

## 9. How to Install

Install Python 3 on your computer.

Then open the terminal inside the project folder.

Run:

```bash
pip install mysql-connector-python
```

---

## 10. MySQL Setup

Open MySQL Workbench.

Open `schema.sql`.

Execute the SQL commands to create the database and table.

Update the MySQL password in `database.py`.

Example:

```python
password="YOUR_MYSQL_PASSWORD"
```

Replace `YOUR_MYSQL_PASSWORD` with your MySQL password.

---

## 11. How to Run

Open the terminal in the project folder.

Run:

```bash
python main.py
```

The application will display the main menu.

---

## 12. Sample Menu

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
Enter your choice:
```

---

## 13. Sample Add Record

```text
Enter your choice: 1

--- Add Student ---

Enter name: Sandesh
Enter age: 22
Enter course: MCA
Enter email: sandesh@gmail.com

Record added successfully!
Student ID: 1
```

---

## 14. Sample View Record

```text
Enter your choice: 2

--- Student Records ---

--------------------------------
ID: 1
Name: Sandesh
Age: 22
Course: MCA
Email: sandesh@gmail.com
```

---

## 15. Sample Search

```text
Enter your choice: 3

Enter student ID: 1

Record Found
ID: 1
Name: Sandesh
Age: 22
Course: MCA
Email: sandesh@gmail.com
```

---

## 16. Sample Update

```text
Enter your choice: 4

Enter student ID: 1
Enter new name: Sandesh Pate
Enter new age: 23
Enter new course: MCA
Enter new email: sandeshpate@gmail.com

Record updated successfully!
```

---

## 17. Sample Delete

```text
Enter your choice: 5

Enter student ID: 1

Record deleted successfully!
```

---

## 18. Error Handling

The application handles:

* Invalid menu choices
* Invalid age input
* Invalid student ID input
* Database connection errors
* File reading errors
* File writing errors
* Empty records

---

## 19. File I/O

The application uses:

```text
data/records.json
```

The JSON file stores a copy of student records.

Example:

```json
[
    {
        "id": 1,
        "name": "Sandesh",
        "age": 22,
        "course": "MCA",
        "email": "sandesh@gmail.com"
    }
]
```

---

## 20. Conclusion

The Console Record Management Application successfully demonstrates Python programming concepts, file handling, exception handling, menu-driven programming, CRUD operations, and MySQL database connectivity.

The project provides a simple and practical solution for managing student records through a console interface.

---

## 21. Author

**Sandesh Pate**
MCA Semester I
Python Programming & Relational Database
