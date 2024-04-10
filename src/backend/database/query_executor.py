from src.backend.database.connection import connectionDB
import psycopg2


def execute_query(query, params, commit=False, fetch=False):
    connection = connectionDB()
    cursor = connection.cursor()

    try:
        cursor.execute(query, params)
        if commit:
            connection.commit()
            if fetch:
                return cursor.fetchone()
        elif fetch:
            return cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        raise Exception(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
