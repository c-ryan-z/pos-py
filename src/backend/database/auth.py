import psycopg2.extras
from datetime import datetime
from src.backend.database.connection import connectionDB


def execute_query(query, params, commit=False, fetch=False):
    connection = connectionDB()
    cursor = connection.cursor()

    try:
        cursor.execute(query, params)
        if commit:
            connection.commit()
            if fetch:
                return cursor.fetchone()
        elif fetch:
            return cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        print("Error while executing query", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def login_user(username, password):
    query = """
        SELECT employees.id, employees.name, roles.name AS role_name, 
        employees.twofactorauthentication, employees.email
        FROM employees
        INNER JOIN roles ON employees.role_id = roles.id
        WHERE username = %s AND password = %s
    """
    return execute_query(query, (username, password), fetch=True)


def login_attempt(user_id):
    query = """
        SELECT timestamp, wrong_pw_attempts, id FROM loginattempts
        WHERE user_id = %s AND initial_login = %s AND timestamp > now() - interval '1 hour'
        ORDER BY timestamp DESC
        LIMIT 1
    """
    return execute_query(query, (user_id, False), fetch=True)


def check_db_for_user(username):
    query = """
        SELECT id, username
        FROM employees
        WHERE username = %s
    """
    return execute_query(query, (username,), fetch=True)


def otp_attempts(user_id):
    query = """
        SELECT COUNT(*) FROM loginattempts
        WHERE user_id = %s AND otp_success = FALSE AND timestamp > now() - interval '1 hour'
    """
    return execute_query(query, (user_id,), fetch=True)[0]


def create_codes(auth_code, user_id, code_type):
    query = """
        INSERT INTO auth_codes (auth_code, timestamp, user_id, auth_type)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (auth_code, datetime.now(), user_id, code_type), commit=True)


def check_user_otp(user_id):
    query = """
        SELECT wrong_otp_attempts FROM auth_codes
        WHERE user_id = %s AND auth_type = 'OTP' AND timestamp > now() - interval '5 minutes'
        ORDER BY timestamp DESC
        LIMIT 1
    """
    return execute_query(query, (user_id,), fetch=True)


def increment_otp_attempts(user_id):
    query = """
        UPDATE auth_codes
        SET wrong_otp_attempts = wrong_otp_attempts + 1
        WHERE user_id = %s AND auth_type = 'OTP' AND timestamp > now() - interval '5 minutes'
    """
    execute_query(query, (user_id,), commit=True)


def verifyLoginOtp(user_id, otp):
    query = """
        SELECT auth_code, timestamp, id FROM auth_codes
        WHERE id = (
            SELECT id FROM auth_codes
            WHERE user_id = %s AND auth_type = 'OTP'
            ORDER BY timestamp DESC
            LIMIT 1
        ) AND auth_code = %s
        LIMIT 1
    """
    return execute_query(query, (user_id, otp), fetch=True)


def setOtpAttempt(user_id):
    query = """
    UPDATE loginattempts 
    SET otp_success = TRUE
    WHERE id = (
        SELECT id FROM loginattempts
        WHERE user_id = %s AND initial_login = TRUE
        ORDER BY timestamp DESC
        LIMIT 1
    )
    RETURNING id
    """
    return execute_query(query, (user_id,), commit=True, fetch=True)
