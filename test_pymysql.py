import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

print("🔍 Testing PyMySQL connection...")

db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'users'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Rahul@17'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    print("1. Attempting to connect with PyMySQL...")
    connection = pymysql.connect(**db_config)
    print("✅ PyMySQL connected successfully!")
    
    print("2. Creating cursor...")
    with connection.cursor() as cursor:
        print("3. Executing query...")
        cursor.execute("SELECT * FROM users")
        
        print("4. Fetching results...")
        users = cursor.fetchall()
        print(f"✅ Found {len(users)} users")
        
        for user in users:
            print(f"   - ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Role: {user['role']}")
    
    print("5. Closing connection...")
    connection.close()
    
    print("🎉 All PyMySQL operations completed successfully!")
    
except Exception as e:
    print(f"❌ PyMySQL Error: {e}")
    print(f"🔍 Full traceback:")
    print(traceback.format_exc())