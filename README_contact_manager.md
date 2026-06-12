# Contact Management System

## Overview

The **Contact Management System** is a desktop-based application developed using **Python Tkinter** and **MySQL** for efficient contact management.

This project is an enhanced version of a basic contact manager application that originally used Python dictionaries and temporary memory storage. The system has been upgraded to include **persistent MySQL database storage**, a modern graphical interface, input validation, and improved contact handling features.

The application enables users to **add, search, update, delete, and manage contacts** through an interactive GUI while securely storing data in a MySQL database.

---

## Evolution of the Project

### Initial Version

The original implementation used:

* Python dictionary for storage
* `simpledialog` popup inputs
* Temporary in-memory data
* Basic CRUD functionality

Limitations:

* Data disappeared after closing application
* No database integration
* Basic interface with popup-heavy interaction
* Limited scalability

---

### Enhanced Version

The system was redesigned and improved with:

* **MySQL database integration**
* **Automatic database and table creation**
* **Persistent contact storage**
* **Improved Tkinter GUI**
* **Treeview table for contact display**
* **Search functionality**
* **Input validation**
* **Password-protected MySQL connection**
* **Better user experience**

---

## Features

### 1. Add Contact

Users can add new contacts with:

* Name
* Phone Number
* Email Address
* Address

Validation includes:

* Required fields check
* Phone number validation
* Email format validation
* Duplicate phone number prevention

---

### 2. View Contacts

All saved contacts are displayed in a structured table format using **Tkinter Treeview**.

Displayed fields:

* Contact ID
* Name
* Phone Number
* Email
* Address

---

### 3. Search Contact

Users can search contacts by:

* Name
* Phone Number

The system supports partial matching for easier search.

Example:

```text
Sa
```

can return:

```text
Sahil
Sashank
```

---

### 4. Update Contact

Users can select an existing contact and update:

* Name
* Phone Number
* Email
* Address

Changes are instantly updated in the MySQL database.

---

### 5. Delete Contact

Users can remove contacts with a confirmation dialog to prevent accidental deletion.

---

### 6. Persistent Database Storage

Unlike the original version, contacts are permanently stored in **MySQL** and remain available after restarting the application.

---

### 7. Automatic Database Setup

The application automatically:

* Connects to MySQL
* Creates database if it does not exist
* Creates table if it does not exist

No manual SQL setup is required.

---

## Technology Stack

### Programming Language

* Python

### GUI Framework

* Tkinter

### Database

* MySQL

### Python Libraries

* mysql-connector-python
* tkinter
* re (Regular Expressions)

---

## Database Structure

### Database Name

```text
contact_manager
```

### Table Name

```text
contacts
```

### Table Schema

| Column  | Data Type         |
| ------- | ----------------- |
| id      | INT (Primary Key) |
| name    | VARCHAR(100)      |
| phone   | VARCHAR(15)       |
| email   | VARCHAR(100)      |
| address | TEXT              |

---

## Project Structure

```text
contact-management-system/
│
├── contact_manager.py
├── README.md
└── requirements.txt
```

---

## Installation Guide

### Prerequisites

Install:

* Python 3.10+
* MySQL Server
* MySQL Workbench

---

### Step 1: Install Required Package

```bash
pip install mysql-connector-python
```

---

### Step 2: Ensure MySQL Server is Running

Start your local MySQL server.

Default configuration:

```text
Host: localhost
User: root
Port: 3306
```

---

### Step 3: Run Application

```bash
python contact_manager.py
```

---

### Step 4: Enter MySQL Password

When application starts, enter your MySQL password.

The system will automatically connect and configure the database.

---

## How It Works

1. User launches application
2. MySQL password prompt appears
3. Application connects to MySQL server
4. Database and table are automatically created if not present
5. User manages contacts using GUI
6. Data is permanently stored in MySQL

---

## Improvements Over Original Version

| Feature          | Original Version | Enhanced Version |
| ---------------- | ---------------- | ---------------- |
| Storage          | Dictionary       | MySQL Database   |
| Persistence      | Temporary        | Permanent        |
| Input            | Popup Dialogs    | GUI Form         |
| Contact Display  | Text Widget      | Table View       |
| Validation       | Minimal          | Improved         |
| Search           | Basic            | Enhanced         |
| Database Support | No               | Yes              |

---

## Future Enhancements

* Export contacts to CSV/Excel
* Dark mode interface
* Contact profile images
* Advanced filtering
* User authentication
* Backup & restore feature

---

## Developer Information

**Project Name:** Contact Management System
**Developed Using:** Python, Tkinter & MySQL
**Type:** Desktop CRUD Application
