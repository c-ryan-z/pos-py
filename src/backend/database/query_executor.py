from src.backend.database.connection import connectionDB
import psycopg2


def execute_query(query, params, commit=False, fetch=False, executemany=False, fetchall=False):
    connection = connectionDB()
    cursor = connection.cursor()

    try:
        if executemany:
            cursor.executemany(query, params)
        else:
            cursor.execute(query, params)
        if commit:
            connection.commit()
            if fetch:
                return cursor.fetchone()
        elif fetch:
            if fetchall:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        raise Exception(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
