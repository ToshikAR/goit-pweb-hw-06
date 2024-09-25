import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    """create a database connection to a SQLite database"""
    try:
        conn = psycopg2.connect(
            host="localhost", database="module6base", user="admin", password="567890"
        )
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")
