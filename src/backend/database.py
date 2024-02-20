import psycopg2
import psycopg2.extras


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


def uploadCashierImage(cashier_id, path):
    connection = connectionDB()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    with open(path, 'rb') as file:
        binary_data = file.read()

    cursor.execute("UPDATE employees SET cashierimage = %s WHERE id = %s",
                   (psycopg2.Binary(binary_data), cashier_id)
                   )
    connection.commit()
    cursor.close()
    connection.close()


def getCashierImage(cashier_id):
    connection = connectionDB()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT cashierimage FROM employees WHERE id = %s", (cashier_id,))
    image_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return image_data[0] if image_data else None
