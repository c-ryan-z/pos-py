from datetime import datetime, timedelta

import psycopg2.extras

from src.backend.database.connection import connectionDB


def get_latest_attempt(cursor, user_id):
    cursor.execute("""
        SELECT timestamp, wrong_pw_attempts, id FROM loginattempts
        WHERE user_id = %s AND initial_login = %s
        ORDER BY timestamp DESC
        LIMIT 1
    """, (user_id, False))
    return cursor.fetchone()


def insert_attempt(cursor, user_id, success, ip_add, wrong_pw_attempts):
    cursor.execute("""
        INSERT INTO loginattempts (user_id, initial_login, ip_address, timestamp, wrong_pw_attempts)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (user_id, success, ip_add, datetime.now(), wrong_pw_attempts))
    return cursor.fetchone()[0]


def update_attempt(cursor, user_id, initial_login, attempt_id, wrong_pw_attempts=None):
    if wrong_pw_attempts is not None:
        cursor.execute("""
            UPDATE loginattempts
            SET wrong_pw_attempts = %s
            WHERE user_id = %s AND initial_login = %s AND id = %s
        """, (wrong_pw_attempts, user_id, initial_login, attempt_id))
    else:
        cursor.execute("""
            UPDATE loginattempts
            SET initial_login = %s
            WHERE user_id = %s AND initial_login = %s AND id = %s
        """, (True, user_id, initial_login, attempt_id))


def record_login_attempt(user_id, success, ip_add):
    attempt_id = None
    try:
        with connectionDB() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                attempt = get_latest_attempt(cursor, user_id)
                if not success:
                    if attempt is None or attempt[0] < datetime.now() - timedelta(minutes=15):
                        attempt_id = insert_attempt(cursor, user_id, success, ip_add, 1)
                    else:
                        update_attempt(cursor, user_id, False, attempt[2], attempt[1] + 1)
                else:
                    if attempt is not None:
                        update_attempt(cursor, user_id, False, attempt[2])
                    else:
                        attempt_id = insert_attempt(cursor, user_id, success, ip_add, 0)
                connection.commit()
    except Exception as e:
        print(f"Error recording login attempt: {e}")
    return attempt_id


def record_session(session_id, user_id, login_id):
    connection = connectionDB()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions (session_id, user_id, login_id)
        VALUES (%s, %s, %s)
    """, (str(session_id), user_id, login_id))
    connection.commit()
    cursor.close()
    connection.close()


def activity_log(user_id, activity_type, activity_category, details, session_id):
    connection = connectionDB()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, datetime.now(), activity_type, activity_category, details, str(session_id)))
    connection.commit()
    cursor.close()
    connection.close()
