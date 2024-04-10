from src.backend.database.query_executor import execute_query


def retrieve_product(product_id):
    query = """
        SELECT * FROM products
        WHERE id = %s
    """
    return execute_query(query, (product_id,), fetch=True)
