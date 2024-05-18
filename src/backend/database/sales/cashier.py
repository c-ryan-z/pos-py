from datetime import datetime

from src.backend.database.query_executor import execute_query


def initialize_tax():
    query = """
        SELECT setting_value FROM system_settings
        WHERE id = %s
    """
    result = execute_query(query, (1,), fetch=True)
    return result[0] if result else None


def retrieve_product(product_id):
    query = """
        SELECT * FROM products
        WHERE id = %s AND is_active = TRUE
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
    for product_id, quantity in items:
        existing_item = retrieve_transaction_item(transaction_id, product_id)
        if existing_item:
            update_transaction_item(transaction_id, product_id, quantity)
        else:
            insert_transaction_item(transaction_id, product_id, quantity)


def retrieve_transaction_item(transaction_id, product_id):
    query = """
        SELECT * FROM transaction_items
        WHERE transaction_id = %s AND product_id = %s
    """
    return execute_query(query, (transaction_id, product_id), fetch=True)


def update_transaction_item(transaction_id, product_id, quantity):
    query = """
        UPDATE transaction_items
        SET quantity = quantity + %s
        WHERE transaction_id = %s AND product_id = %s
    """
    return execute_query(query, (quantity, transaction_id, product_id), commit=True)


def insert_transaction_item(transaction_id, product_id, quantity):
    query = """
        INSERT INTO transaction_items (transaction_id, product_id, quantity)
        VALUES (%s, %s, %s)
    """
    return execute_query(query, (transaction_id, product_id, quantity), commit=True)


def transaction_checkout(cashier_id, subtotal, tax, discount, total, amount_paid, change_due, items, session_id):
    transaction = record_transaction(cashier_id, subtotal, tax, discount, total, amount_paid, change_due)
    transaction_id = transaction[0]

    record_transaction_items(transaction_id, items)
    log_transaction(cashier_id, "Transaction", f"Transaction ID: {transaction_id}", str(session_id))
    return transaction_id


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


def retrieve_transaction(transaction_id, cashier_id):
    query = """
        SELECT id, date_time, is_successful, total, amount_paid FROM transactions
        WHERE CAST(id AS TEXT) LIKE %s AND cashier_id = %s
        ORDER BY id
        LIMIT 20
    """
    return execute_query(query, (f"%{transaction_id}%", cashier_id), fetch=True, fetchall=True)


def void_transaction(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "Sales", details, session_id),
                         commit=True)


def interleave_transaction(cashier_id, subtotal, tax, discount, total):
    query = """
        INSERT INTO transactions (cashier_id, sub_total, tax, discount, total,
         date_time, is_successful)
        VALUES (%s, %s, %s, %s, %s, NOW(), FALSE)
        RETURNING id
    """
    return execute_query(query, (cashier_id, subtotal, tax, discount, total), commit=True, fetch=True)


def retrieve_interleaved_transactions():
    query = """
        SELECT id FROM transactions
        WHERE is_successful = FALSE
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def retrieve_transaction_items(transaction_id):
    query = """
        SELECT product_id, quantity FROM transaction_items
        WHERE transaction_id = %s
    """
    return execute_query(query, (transaction_id,), fetch=True, fetchall=True)


def update_transaction(transaction_id, subtotal, tax, discount, total, amount_paid, change_due):
    query = """
        UPDATE transactions
        SET sub_total = %s, tax = %s, discount = %s, total = %s, amount_paid = %s, change_due = %s, is_successful = TRUE
        WHERE id = %s;
    """
    execute_query(query, (subtotal, tax, discount, total, amount_paid, change_due, transaction_id), commit=True)
    return transaction_id
