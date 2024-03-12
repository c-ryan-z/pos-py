import os
import psycopg2


def connectionDB():
    db_username = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    try:
        connection = psycopg2.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
