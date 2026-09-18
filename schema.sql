CREATE DATABASE IF NOT EXISTS student_management;

USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO students (id, name, age, course, email)
VALUES
(101, 'Sandesh Pate', 20, 'MCA', 'sandesh@gmail.com'),
(102, 'Ritanshu Mahajn', 20, 'BCA', 'ritanshu@gmail.com'),
(103, 'Bhushan Kumbhar', 22, 'BCA', 'bhushan@gmail.com'),
(104, 'Sharavani Pataskar', 25, 'MCA', 'sharvani@gmail.com'),
(105, 'Shiv Sarode', 26, 'MCA', 'shiv@gmail.com');