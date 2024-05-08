from src.backend.database.query_executor import execute_query


def get_all_activity_logs():
    query = """
        SELECT user_id, session_id, timestamp, activity_category, activity_type
        FROM activity_logs
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def get_activity_logs_by_user_id(user_id):
    query = """
        SELECT session_id, timestamp, activity_category, activity_type
        FROM activity_logs
        WHERE user_id = %s 
    """

    return execute_query(query, (user_id,), fetch=True, fetchall=True)
