import psycopg2

def connectionDB():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="user10",
            host="localhost",
            port="5432",
            database="POS"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

def loginUser(username, password):
    connection = connectionDB()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT employees.id, employees.name, roles.name AS role_name
            FROM employees
            INNER JOIN roles ON employees.role_id = roles.id
            WHERE username = %s AND password = %s
        """, (username, password))
        user = cursor.fetchone()
        return user
    except (Exception, psycopg2.Error) as error:
        print("Error while querying data", error)
    finally:
        if connection:
            cursor.close()
            connection.close()