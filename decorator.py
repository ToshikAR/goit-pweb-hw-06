"""
Decorator psycopg2
"""

import logging
from functools import wraps
from connect import create_connection
from psycopg2 import DatabaseError


def decorator_sql_query(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            with create_connection() as conn:
                if conn is not None:
                    cur = conn.cursor()
                    try:
                        result = func(cur, *args, **kwargs)
                        # result = cur.fetchone()
                        result = cur.fetchall()
                        conn.commit()
                        return result
                    except DatabaseError as err:
                        logging.error(f"DatabaseError: => {err}")
                        conn.rollback()
                    finally:
                        cur.close()
                else:
                    print("Error: can't create the database connection")
        except RuntimeError as err:
            logging.error(f"RuntimeError: => {err}")

    return wrapper


def decorator_sql_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            with create_connection() as conn:
                if conn is not None:
                    cur = conn.cursor()
                    try:
                        result = func(cur, *args, **kwargs)
                        conn.commit()
                        return result
                    except DatabaseError as err:
                        logging.error(f"DatabaseError: => {err}")
                        conn.rollback()
                    finally:
                        cur.close()
                else:
                    print("Error: can't create the database connection")
        except RuntimeError as err:
            logging.error(f"RuntimeError: => {err}")

    return wrapper
