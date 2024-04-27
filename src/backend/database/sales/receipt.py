from src.backend.database.query_executor import execute_query


def retrieve_receipt(transaction_id):
    query = """SELECT 
        date_time,
        transactions.id,
        e.name,
        cashier_id,
        transactions.sub_total,
        transactions.tax,
        transactions.discount,
        transactions.total,
        transactions.amount_paid,
        transactions.change_due
    FROM transactions
    INNER JOIN employees e on e.id = transactions.cashier_id
    WHERE transactions.id = %s
    """

    return execute_query(query, (transaction_id,), fetch=True)


def retrieve_items(transaction_id):
    query = """
    SELECT 
    quantity,
    p.name,
    p.price
     FROM transaction_items
    INNER JOIN products p on p.id = transaction_items.product_id
    WHERE transaction_id = %s
    """
    return execute_query(query, (transaction_id,), fetch=True, fetchall=True)
