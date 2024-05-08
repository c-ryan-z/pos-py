from datetime import datetime

import psycopg2

from src.backend.database.query_executor import execute_query


def get_inventory():
    query = """
        SELECT name, price, category, stock, is_active
        FROM products
        ORDER BY name
    """
    return execute_query(query, (1,), fetch=True, fetchall=True)


def search_inventory(search):
    query = """
        SELECT name, price, category, stock, is_active
        FROM products
        WHERE name ILIKE %s
        ORDER BY name
    """
    return execute_query(query, (f"%{search}%",), fetch=True, fetchall=True)


def get_inventory_by_name(item_name):
    query = """
        SELECT name, price, category, stock, image, id
        FROM products
        WHERE name = %s
    """
    return execute_query(query, (item_name,), fetch=True)


def get_inventory_by_id(item_id):
    query = """
        SELECT name, price, category, stock, image, id
        FROM products
        WHERE id = %s
    """
    return execute_query(query, (item_id,), fetch=True)


def update_item_image(path, item_name):
    query = """
        UPDATE products
        SET image = %s
        WHERE name = %s
    """

    with open(path, 'rb') as file:
        image_data = file.read()

    return execute_query(query, (psycopg2.Binary(image_data), item_name), commit=True)


def get_img(name):
    query = """
        SELECT image
        FROM products
        WHERE name = %s
    """
    return execute_query(query, (name,), fetch=True)


def upsert_product(name, price, category, stock, cost=None, image=None):
    if cost is None:
        cost = price * 0.8

    if image is None:
        query = """
            INSERT INTO products (name, price, category, stock, cost)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (name)
            DO UPDATE SET price = %s, category = %s, stock = %s, cost = %s
        """
        return execute_query(query, (name, price, category, stock, cost, price, category, stock, cost), commit=True)
    else:
        query = """
            INSERT INTO products (name, price, category, stock, cost, image)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (name)
            DO UPDATE SET price = %s, category = %s, stock = %s, cost = %s, image = %s
        """

        with open(image, 'rb') as file:
            image_data = file.read()

        return execute_query(query, (
            name, price, category, stock, cost, psycopg2.Binary(image_data), price, category, stock, cost,
            psycopg2.Binary(image_data)), commit=True)


def delete_product(name):
    query = """
        UPDATE products
        SET is_active = FALSE
        WHERE name = %s
    """
    return execute_query(query, (name,), commit=True)


def log_delete(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "Inventory", details, session_id), commit=True)


def log_add_edit(user_id, activity_type, details, session_id):
    query = """
        INSERT INTO activity_logs (user_id, timestamp, activity_type, activity_category, details, session_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_query(query, (user_id, datetime.now(), activity_type, "Inventory", details, session_id), commit=True)
