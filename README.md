# Student Study & Task Management System

## Project Overview

The Student Study & Task Management System is a Python-based command-line application designed to help students manage their academic tasks and study sessions.

The system allows students to add, view, complete, and delete tasks. It also allows students to record their study sessions and view statistics about their tasks and study time.

The project is developed as part of the Python Essentials course.

## Features

### 1. Task Management
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Store task information using JSON files

### 2. Study Management
- Add study sessions
- Record subject, topic, and study duration
- View previous study sessions
- Store study records using JSON files

### 3. Statistics & Reports
- Display total number of tasks
- Display completed tasks
- Display pending tasks
- Calculate total study time
- Display subject-wise study time

### 4. Input Validation
- Prevent empty task and subject names
- Validate study duration
- Handle invalid numeric input

### 5. Data Persistence
- Task and study data are stored in JSON files
- Data remains available after restarting the application

## Technologies Used

- Python
- JSON
- VS Code
- Git & GitHub

## Python Concepts Used

- Variables
- Data types
- Input and output
- Conditional statements
- For loops
- While loops
- Lists
- Dictionaries
- Functions
- File handling
- JSON
- Exception handling
- Modules
- Testing

## Project Structure

```text
StudentStudyManager/
│
├── main.py
├── task_manager.py
├── study_manager.py
├── statistics.py
├── file_handler.py
├── validation.py
│
├── data/
│   ├── tasks.json
│   └── study_records.json
│
├── tests/
│   └── test_project.py
│
├── README.md
└── statement.md

## Installation and Setup
Step 1: Install Python :
        Make sure Python is installed on your computer.
        By checking "python --version" in VS Code Terminal

Step 2: Open The Project :
        Open the "StudentStudyManager" Folder in VS Code.

Step 3: Run The Application :
        Open the VS Code Terminal and Run: "python main.py"

## How to Use This Student Study Manager App
After running the program, the main menu will appear like,
                  1. Add Task
                  2. View Tasks
                  3. Complete Task
                  4. Delete Task
                  5. Add Study Session
                  6. View Study Sessions
                  7. View Statistics
                  8. Exit
Enter the number corresponding to the operation you want to perform.

# Testing
The Project contains basic tests in: "tests/test_project.py"
Run the tests using: "python tests/test_project.py"
The Program should display: "ALL TESTS PASSED SUCCESSFULLY !"

# Data Storage
The applictaion stores data in JSON files: "data/tasks.json"
                                           "data/study_records.json"
This allow task and study information to ramain available when the application is restarted.


