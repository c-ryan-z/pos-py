from datetime import datetime

from src.backend.database.query_executor import execute_query


def retrieve_product(product_id):
    query = """
        SELECT * FROM products
        WHERE id = %s
    """
    return execute_query(query, (product_id,), fetch=True)


def record_transaction(cashier_id, subtotal, tax, discount, total, amount_paid, change_due):
    query = """
        INSERT INTO transactions (cashier_id, sub_total, tax, discount, total, amount_paid, change_due, date_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        RETURNING id
    """
    return execute_query(query, (cashier_id, subtotal, tax, discount, total, amount_paid, change_due), fetch=True,
                         commit=True)


def record_transaction_items(transaction_id, items):
    query = """
        INSERT INTO transaction_items (transaction_id, product_id, quantity)
        VALUES (%s, %s, %s)
    """
    params = [(transaction_id, product_id, quantity) for product_id, quantity in items]
    return execute_query(query, params, commit=True, executemany=True)


def transaction_checkout(cashier_id, subtotal, tax, discount, total, amount_paid, change_due, items, session_id):
    transaction = record_transaction(cashier_id, subtotal, tax, discount, total, amount_paid, change_due)
    transaction_id = transaction[0]

    record_transaction_items(transaction_id, items)
    log_transaction(cashier_id, "Transaction", f"Transaction ID: {transaction_id}", str(session_id))


def log_transaction(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "Sales", details, session_id),
                         commit=True)


def transactions_query():
    query = """
        SELECT id, date_time, is_successful, total, amount_paid FROM transactions
        WHERE cashier_id = %s
        ORDER BY id
    """
    return query


def retrieve_transaction(transaction_id):
    query = """
        SELECT id, date_time, is_successful, total, amount_paid FROM transactions
        WHERE CAST(id AS TEXT) LIKE %s
        ORDER BY id
        LIMIT 20
    """
    return execute_query(query, (f"{transaction_id}%",), fetch=True, fetchall=True)
