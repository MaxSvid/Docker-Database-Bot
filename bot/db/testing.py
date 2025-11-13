from psycopg import OperationalError
from .execute import insert_users

def main():
    try:
        insert_users()
        print("Database works...")
    except OperationalError as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    main()