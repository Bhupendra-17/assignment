from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'database': 'users',
    'user': 'root',  # Replace with your MySQL username
    'password': ''   # Replace with your MySQL password
}

def get_db_connection():
    """Create and return database connection"""
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/hello')
def hello():
    """Route that returns Hello World"""
    return "Hello World!"

@app.route('/users')
def get_users():
    """Route to retrieve all users from database"""
    connection = get_db_connection()
    if connection is None:
        return "Database connection failed", 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return render_template('users.html', users=users)
    except Error as e:
        return f"Error retrieving users: {e}", 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

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
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                (name, email, role)
            )
            connection.commit()
            return redirect(url_for('get_users'))
        except Error as e:
            return f"Error adding user: {e}", 500
        finally:
            if connection.is_connected():
                cursor.close()
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
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        
        if user:
            return render_template('user_detail.html', user=user)
        else:
            return "User not found", 404
    except Error as e:
        return f"Error retrieving user: {e}", 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.errorhandler(404)
def not_found(error):
    return "Resource not found", 404

@app.errorhandler(500)
def internal_error(error):
    return "Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)