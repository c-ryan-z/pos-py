from src.backend.database.query_executor import execute_query


def get_all_activity_logs():
    query = """
        SELECT id, user_id, session_id, timestamp, activity_category, activity_type
        FROM activity_logs
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def get_activity_logs_by_user_id(user_id):
    query = """
        SELECT id, session_id, timestamp, activity_category, activity_type
        FROM activity_logs
        WHERE user_id = %s 
    """

    return execute_query(query, (user_id,), fetch=True, fetchall=True)


def search_activity_logs_by_user_id(user_id):
    query = """
        SELECT id, user_id, session_id, timestamp, activity_category, activity_type
        FROM activity_logs
        WHERE CAST(user_id AS TEXT) LIKE %s
        ORDER BY user_id
        LIMIT 50
    """

    return execute_query(query, (f"%{user_id}%",), fetch=True, fetchall=True)


def search_activity_logs_by_activity_type(activity_type):
    query = """
        SELECT id, session_id, timestamp, activity_category, activity_type
        FROM activity_logs
        WHERE activity_type LIKE %s
        ORDER BY user_id
        LIMIT 50
    """

    return execute_query(query, (f"%{activity_type}%",), fetch=True, fetchall=True)


def get_row_info(activity_id):
    query = """
        SELECT * FROM activity_logs
        WHERE id = %s
    """

    return execute_query(query, (activity_id,), fetch=True)