from flask import Flask, render_template, request, redirect, url_for
import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database configuration from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'users'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Rahul@17'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    """Create and return database connection"""
    print("Connecting to database with PyMySQL...")
    
    try:
        connection = pymysql.connect(**db_config)
        print("✅ Database connection successful!")
        return connection
    except Exception as e:
        print(f"❌ Error connecting to MySQL: {e}")
        return None

@app.route('/hello')
def hello():
    """Route that returns Hello World"""
    return "Hello World!"

@app.route('/users')
def get_users():
    """Route to retrieve all users from database"""
    print("🔍 Attempting to fetch users from database...")
    
    connection = get_db_connection()
    if connection is None:
        return "Database connection failed", 500
    
    try:
        with connection.cursor() as cursor:
            print("✅ Database cursor created")
            
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            print(f"✅ Found {len(users)} users")
            
            return render_template('users.html', users=users)
            
    except Exception as e:
        print(f"❌ Error retrieving users: {e}")
        return f"Error retrieving users: {e}", 500
    finally:
        connection.close()
        print("✅ Connection closed")

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    """Route to add new user (form and processing)"""
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        
        connection = get_db_connection()
        if connection is None:
            return "Database connection failed", 500
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                    (name, email, role)
                )
                connection.commit()
                print("✅ New user added successfully")
                return redirect('/users')
        except Exception as e:
            print(f"❌ Error adding user: {e}")
            return f"Error adding user: {e}", 500
        finally:
            connection.close()
    
    # GET request - show the form
    return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def get_user(user_id):
    """Route to retrieve specific user by ID"""
    connection = get_db_connection()
    if connection is None:
        return "Database connection failed", 500
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            
            if user:
                print(f"✅ Found user: {user['name']}")
                return render_template('user_detail.html', user=user)
            else:
                print(f"❌ User with ID {user_id} not found")
                return "User not found", 404
    except Exception as e:
        print(f"❌ Error retrieving user: {e}")
        return f"Error retrieving user: {e}", 500
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)