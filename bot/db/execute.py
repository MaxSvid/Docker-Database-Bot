from .connect import create_connection
from psycopg import OperationalError
from datetime import date

def insert_users(user_id: int, username: str, language: str):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            query = """
                INSERT INTO users (user_id, username, language, timestamp)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO NOTHING;
            """
            cur.execute(query, (user_id, username, language, date.today()))
        conn.commit()
        print("Execute file worked!")
    except OperationalError as e:
        print(f"Error with database: {e}")

def update_language_code(user_id: int, language_code: str):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            query = """
                UPDATE users
                SET language = %s
                WHERE user_id = %s;
            """
            cur.execute(query, (language_code, user_id))
            conn.commit()
            print("Language updated")
    except OperationalError as e:
        print(f"Error with database: {e}")

def user_ids():
    conn = create_connection()
    ids = []
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id FROM users;")
            ids = [row[0] for row in cur.fetchall()]
    except OperationalError as e:
        print(f"Error fetching user IDs: {e}")
    return ids

