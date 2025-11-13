"""
from /bot folder python -m db.connect
This file is used to make a connection to database, file close.py need it in case you need to fix some issues and stop db 
"""

# Configuration file with classes "DatabaseSettings" from config.py for database connection

# https://www.geeksforgeeks.org/python/python-psycopg-connection-class/

# from db.connect import create_connection

from psycopg import connect, OperationalError
from config import databaseSettings

def create_connection():
    try:
        connection = connect(
            dbname=databaseSettings.POSTGRES_DB,
            user=databaseSettings.POSTGRES_USER,    
            password=databaseSettings.POSTGRES_PASSWORD,
            host=databaseSettings.POSTGRES_HOST,
            port=databaseSettings.POSTGRES_PORT_NUMBER)
        return connection
    except OperationalError as e:
            print(f"Can't connect to PostgreSQL server: {e}")
            return None

if __name__ == "__main__":
    connection = create_connection()
