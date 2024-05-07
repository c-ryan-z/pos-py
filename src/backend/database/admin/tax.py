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
