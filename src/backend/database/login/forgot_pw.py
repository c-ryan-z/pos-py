from src.backend.database.query_executor import execute_query
from datetime import datetime
from src.backend.Utilities import reset_info


def verify_email(email):
    query = """
        SELECT id, username
        FROM employees
        WHERE email = %s
    """
    return execute_query(query, (email,), fetch=True)


def rate_limit(email):
    query = """
        SELECT COUNT(*)
        FROM auth_codes
        WHERE user_id = (SELECT id FROM employees WHERE email = %s) AND timestamp > now() - interval '1 minutes'
    """
    return execute_query(query, (email,), fetch=True)


def insert_reset_code(auth_code, user_id, auth_type):
    query = """
        INSERT INTO auth_codes (auth_code, timestamp, user_id, auth_type)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (auth_code, datetime.now(), user_id, auth_type), commit=True)


def check_code(auth_code, user_id, auth_type):
    query = """
        SELECT wrong_attempts FROM auth_codes
        WHERE auth_code = %s AND user_id = %s AND auth_type = %s  AND timestamp > now() - interval '5 minutes'
        ORDER BY timestamp DESC
        LIMIT 1
    """
    return execute_query(query, (auth_code, user_id, auth_type), fetch=True)


def verify_code(user_id, code):
    query = """
        SELECT auth_code, timestamp, id
        FROM auth_codes
        WHERE id = (
            SELECT id FROM auth_codes
            WHERE user_id = %s AND auth_type = 'RESET'
            ORDER BY timestamp DESC
            LIMIT 1
        ) AND auth_code = %s
    """
    return execute_query(query, (user_id, code), fetch=True)


def increment_code_attempts(user_id, auth_type):
    query = """
        UPDATE auth_codes
        SET wrong_attempts = wrong_attempts + 1
        WHERE user_id = %s AND auth_type = %s AND timestamp > now() - interval '5 minutes'
    """
    execute_query(query, (user_id, auth_type), commit=True)


def change_password(user_id, password):
    query = """
        UPDATE employees
        SET password = %s
        WHERE id = %s
    """
    execute_query(query, (password, user_id), commit=True)


def record_successful_reset(user_id, ):
    ip, location, os_info, mac_address = reset_info()
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details)
        VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(query, (user_id, datetime.now(), 'Password Reset', 'Account',
                          f'Password reset successful at ({ip}, {location}, {os_info}, {mac_address})'), commit=True)
