from datetime import datetime

from src.backend.database.query_executor import execute_query


def get_monthly_sales():
    current_month = datetime.now().month
    current_year = datetime.now().year
    query = f"""
    SELECT SUM(total) as total
    from transactions
    WHERE EXTRACT(MONTH FROM date_time) = %s
    AND EXTRACT(YEAR FROM date_time) = %s
    """
    result = execute_query(query, (current_month, current_year), fetch=True)
    return str(result[0]) if result and result[0] is not None else '0'


def get_daily_sales():
    current_date = datetime.now().date()
    query = f"""
    SELECT SUM(total) as total
    from transactions
    WHERE DATE(date_time) = %s
    """
    result = execute_query(query, (current_date,), fetch=True)
    return str(result[0]) if result and result[0] is not None else '0'


def get_weekly_sales():
    current_date = datetime.now().date()
    query = f"""
    SELECT SUM(total) as total
    from transactions
    WHERE date_time >= %s - INTERVAL '1 week'
    """
    result = execute_query(query, (current_date,), fetch=True)
    return str(result[0]) if result and result[0] is not None else '0'


def get_annual_sales():
    current_year = datetime.now().year
    query = f"""
    SELECT SUM(total) as total
    from transactions
    WHERE EXTRACT(YEAR FROM date_time) = %s
    """
    result = execute_query(query, (current_year,), fetch=True)
    return str(result[0]) if result and result[0] is not None else '0'


def get_unique_years():
    query = """
        SELECT DISTINCT EXTRACT(YEAR FROM date_time) as year
        FROM transactions
        ORDER BY year DESC 
    """

    result = execute_query(query, (1,), fetch=True, fetchall=True)
    return [str(year[0]) for year in result]


def get_yearly_sum(year):
    query = f"""
    SELECT EXTRACT(MONTH FROM date_time) AS month, SUM(total) as total
    from transactions
    WHERE EXTRACT(YEAR FROM date_time) = %s
    GROUP BY month
    ORDER BY month
    """
    result = execute_query(query, (year,), fetch=True, fetchall=True)
    return [(float(res[0]) - 1, float(res[1])) for res in result]


def get_top_products():
    query = """
    SELECT p.name, SUM(ti.quantity) as total
    FROM transaction_items ti
    INNER JOIN products p ON ti.product_id = p.id
    GROUP BY p.name
    ORDER BY total DESC
    LIMIT 5
    """
    result = execute_query(query, (1,), fetch=True, fetchall=True)
    return [(res[0], float(res[1])) for res in result]
