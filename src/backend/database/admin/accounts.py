from src.backend.database.query_executor import execute_query


def get_user_accounts():
    query = """
        SELECT employees.id, employees.name, username, email, r.name
        FROM employees
        JOIN  roles r ON employees.role_id = r.id
        ORDER BY username
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def get_user_info(user_id):
    query = """
        SELECT employees.id, employees.name, r.name, employees.employeeimage
        FROM employees
        JOIN  roles r ON employees.role_id = r.id
        WHERE employees.id = %s
    """
    return execute_query(query, (user_id,), fetch=True)
