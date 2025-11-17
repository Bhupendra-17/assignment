# Flask User Mgmt

A simple Flask web application for managing users with MySQL database.

## Features

- View all users in a table
- Add new users through a form
- View individual user details
- Error handling for missing resources

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd assignment
```

2. Install Requirements.txt:
```bash
pip install -r requirements.txt
```
3. Setup the .env file with these
```bash
DB_HOST=localhost
DB_NAME=users
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_PORT=3306
```
### Run the server 

```bash
python app.py

```
or
```bash
python app
```

# Database Schema & Application Overview

## 📌 Database Schema

### **Users Table Structure**

| Field | Type | Attributes |
|-------|--------|------------------------------|
| **id** | INT | Primary Key, Auto Increment |
| **name** | VARCHAR(100) | NOT NULL |
| **email** | VARCHAR(100) | UNIQUE, NOT NULL |
| **role** | VARCHAR(50) | NOT NULL |

---

### **Sample Data Population**

Run the provided SQL `INSERT` commands to populate the database with initial sample records.
```sql
INSERT INTO users (name, email, role) VALUES 
('John Doe', 'john.doe@example.com', 'Admin'),
('Jane Smith', 'jane.smith@example.com', 'User'),
('Mike Johnson', 'mike.johnson@example.com', 'Editor');
```
---

## 📌 Application Routes & SQL Queries

## MySQL Queries

- /users  : 
```sql
SELECT * FROM users
```

- /new_user  : 
```sql
INSERT INTO users (name, email, role) VALUES (%s, %s, %s)
```

- /users/<id>  : 
```sql
SELECT * FROM users WHERE id = %s"
```

## Git Workflow
### Branching Strategy
- Main Branch: Production-ready code

- Assignment Branch: Feature development branch

### Contribution Process
1. Fork the repository or clone directly if you have access

2. Create a feature branch from the main branch:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit with descriptive messages:
```bash
git add .
git commit -m "Add: description of changes"
```

4. Push to remote repository:

```bash
git push origin feature/your-feature-name
```
5. Create a Pull Request from your feature branch to the main branch

6. Code review and address any feedback

7. Merge after approval