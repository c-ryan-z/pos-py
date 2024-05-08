from datetime import datetime

from src.backend.database.query_executor import execute_query


def get_tax():
    query = """
        SELECT setting_value FROM system_settings WHERE setting_name = %s
    """
    return execute_query(query, ("tax_percentage",), fetch=True)


def update_tax(tax):
    query = """
        UPDATE system_settings SET setting_value = %s WHERE setting_name = %s
    """
    return execute_query(query, (tax, "tax_percentage"), commit=True)


def log_tax(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "System", details, session_id),
                         commit=True)
