from src.backend.database.query_executor import execute_query


def cashier_transactions():
    query = """
        SELECT id, cashier_id,date_time, is_successful, total, amount_paid FROM transactions
        ORDER BY id
    """
    return query


def retrieve_admin_transaction(transaction_id):
    query = """
        SELECT id, cashier_id, date_time, is_successful, total, amount_paid FROM transactions
        WHERE CAST(id AS TEXT) LIKE %s
        ORDER BY id
        LIMIT 20
    """
    return execute_query(query, (f"%{transaction_id}%",), fetch=True, fetchall=True)
