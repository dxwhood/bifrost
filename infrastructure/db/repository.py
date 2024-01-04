import psycopg2
from psycopg2 import sql

def create_connection():
    # Replace with your database connection details
    return psycopg2.connect(
            host="localhost",
            port="5432",
            database="bifrost_zero",
            user="postgres",
            password="batman"
    )

def create_user(name, email, location):
    query = sql.SQL("INSERT INTO users (name, email, location) VALUES (%s, %s, %s)")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, email, location))

def get_user(name):
    query = "SELECT user_id FROM users WHERE name = %s"
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            return result

def update_user(user_id, name=None, email=None, location=None):
    query = sql.SQL("UPDATE users SET name = %s, email = %s, location = %s WHERE user_id = %s")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, email, location, user_id))

def add_user_knowledge(user_id, category, key, value, additional_info=None):
    query = sql.SQL("INSERT INTO user_knowledge (user_id, category, key, value, additional_info) VALUES (%s, %s, %s, %s, %s)")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, category, key, value, additional_info))

def get_user_knowledge(user_id, category, key):
    query = sql.SQL("SELECT value, additional_info FROM user_knowledge WHERE user_id = %s AND category = %s AND key = %s")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id, category, key))
            return cursor.fetchone()

def delete_user_knowledge(knowledge_id):
    query = sql.SQL("DELETE FROM user_knowledge WHERE knowledge_id = %s")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (knowledge_id,))

def update_user_knowledge(knowledge_id, value, additional_info=None):
    query = sql.SQL("UPDATE user_knowledge SET value = %s, additional_info = %s WHERE knowledge_id = %s")
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (value, additional_info, knowledge_id))
