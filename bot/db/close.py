"""
python -m db.close
from /bot folder import same level file .connect py
This file is part of database connection idae, make sure to use global connection variable for working with the same file from connect.py
"""

from .connect import create_connection 
from psycopg import OperationalError

connection = create_connection()

def close_connection():
    try:
        if connection and not connection.closed:
            connection.close()
            print("Connection to PostgreSQL DB closed")
        else:
            print("No active connection to close")
    except OperationalError as e:
        print(f"Error closing the DB connection: {e}")

if __name__ == "__main__":
    close_connection()
