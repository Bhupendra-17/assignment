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

## MySQL Queries

- /users  : 
```bash
SELECT * FROM users
```

- /new_user  : 
```bash
INSERT INTO users (name, email, role) VALUES (%s, %s, %s)
```

- /users/<id>  : 
```bash
SELECT * FROM users WHERE id = %s", (user_id,)
```
