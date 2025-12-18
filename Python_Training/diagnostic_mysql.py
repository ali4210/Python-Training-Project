import mysql.connector
import socket
from mysql.connector import Error


def test_mysql_connection():
    host = "192.168.0.150"
    port = 3306

    print("Testing connection to MySQL server...")
    print(f"Host: {host}")
    print(f"Port: {port}")

    # Test 1: Basic network connectivity
    try:
        print("\n1. Testing network connectivity...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            print("✓ Network connection successful - Port 3306 is open")
        else:
            print(f"✗ Network connection failed - Port 3306 is closed (Error: {result})")
            print("This means the server is not accessible at the network level")
            return False
    except Exception as e:
        print(f"✗ Network error: {e}")
        return False

    # Test 2: MySQL connection
    try:
        print("\n2. Testing MySQL connection...")
        connection = mysql.connector.connect(
            host=host,
            user="mysql_user",
            password="test123",
            database="alnafi",
            connection_timeout=5
        )

        if connection.is_connected():
            print("✓ MySQL connection successful!")

            # Test query
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION()")
            db_version = cursor.fetchone()
            print(f"✓ MySQL Version: {db_version[0]}")

            cursor.close()
            connection.close()
            return True

    except Error as e:
        print(f"✗ MySQL connection error: {e}")
        return False


if __name__ == "__main__":
    test_mysql_connection()