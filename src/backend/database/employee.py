import psycopg2.extras
from src.backend.database.connection import connectionDB


def uploadEmployeeImage(cashier_id, path):
    connection = connectionDB()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    with open(path, 'rb') as file:
        binary_data = file.read()

    cursor.execute("UPDATE employees SET employeeimage = %s WHERE id = %s",
                   (psycopg2.Binary(binary_data), cashier_id)
                   )
    connection.commit()
    cursor.close()
    connection.close()


def getEmployeeImage(employee_id):
    connection = connectionDB()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT employeeimage FROM employees WHERE id = %s", (employee_id,))
    image_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return image_data[0] if image_data else None
