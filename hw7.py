import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} IN CREATE_CONNECTION function')
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} IN CREATE_TABLE function')


def insert_products(connection, product):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN INSERT_PRODUCTS function')


def update_quantity(connection, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN UPDATE_QUANTITY function')


def update_price(connection, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN UPDATE_PRICE function')


def delete_by_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN DELETE_BY_ID function')


def select_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_ALL function')


def select_by_price_and_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_BY_PRICE_AND_QUANTITY function')


def select_by_name(connection):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE '%Chocolate%' '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_BY_NAME function')


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection('hw.db')

if my_connection:
    print('Connected successfully!')
    create_table(my_connection, sql_to_create_products_table)

    products = [
        ('Classic Milk Chocolate', 120.50, 7),
        ('Dark Chocolate 70%', 150.00, 5),
        ('White Chocolate with Almonds', 130.75, 10),
        ('Ruby Chocolate', 180.90, 4),
        ('Hazelnut Milk Chocolate', 145.00, 6),
        ('Caramel Filled Chocolate', 160.50, 8),
        ('Mint Dark Chocolate', 140.00, 9),
        ('Orange Zest Milk Chocolate', 135.50, 5),
        ('Salted Caramel Chocolate', 170.25, 3),
        ('Strawberry White Chocolate', 125.00, 7),
        ('Coffee Infused Dark Chocolate', 155.50, 6),
        ('Peanut Butter Chocolate', 110.00, 10),
        ('Coconut Milk Chocolate', 130.00, 8),
        ('Chili Spiced Chocolate', 140.50, 5),
        ('Gingerbread Dark Chocolate', 150.00, 6)
    ]

    for product in products:
        insert_products(my_connection, product)

    update_price(my_connection, (150.0, 1))
    update_quantity(my_connection, (20, 5))
    delete_by_id(my_connection, 7)

    select_all(my_connection)
    select_by_price_and_quantity(my_connection, (100, 5))
    select_by_name(my_connection)
