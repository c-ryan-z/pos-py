from datetime import datetime

import psycopg2

from src.backend.database.query_executor import execute_query


def get_user_accounts():
    query = """
        SELECT employees.id, employees.name, username, email, r.name
        FROM employees
        JOIN  roles r ON employees.role_id = r.id
        WHERE employees.active = TRUE
        ORDER BY id
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def get_user_info(user_id):
    query = """
        SELECT employees.id, employees.name, r.name, employees.employeeimage
        FROM employees
        JOIN  roles r ON employees.role_id = r.id
        WHERE employees.id = %s
    """
    return execute_query(query, (user_id,), fetch=True)


def get_max_user_id():
    query = """
        SELECT MAX(id)
        FROM employees
    """
    result = execute_query(query, (1,), fetch=True)
    return result[0] if result else None


def add_user(name, phone, email, username, password, role_id, twofactorauthentication):
    query = """
        INSERT INTO employees (name, phone, email, username, password, role_id, twofactorauthentication)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """
    return execute_query(query, (name, phone, email, username, password, role_id, twofactorauthentication),
                         fetch=True, commit=True)


def set_user_image(user_id, image):
    query = """
        UPDATE employees
        SET employeeimage = %s
        WHERE id = %s
    """

    with open(image, 'rb') as file:
        image_data = file.read()

    return execute_query(query, (psycopg2.Binary(image_data), user_id), commit=True)


def edit_initial_data(user_id):
    query = """
        SELECT name, phone, email, username, role_id, twofactorauthentication, employeeimage
        FROM employees
        WHERE id = %s
    """
    return execute_query(query, (user_id,), fetch=True)


def edit_user(fields, user_id):
    query_parts = []

    for field in fields:
        query_parts.append(f"{field} = %s")

    set_clause = ", ".join(query_parts)

    query = f"""
        UPDATE employees
        SET {set_clause}
        WHERE id = %s
    """
    print(query)
    values = tuple(fields.values()) + (user_id,)
    return execute_query(query, values, commit=True)


def deactivate_user(user_id):
    query = """
        UPDATE employees
        SET active = FALSE
        WHERE id = %s
    """
    return execute_query(query, (user_id,), commit=True)


def log_accounts(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "Accounts", details, session_id),
                         commit=True)
