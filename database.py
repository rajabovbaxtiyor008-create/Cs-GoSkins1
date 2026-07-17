import sqlite3

DATABASE_NAME = "cs2_shop.db"


def connect():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Пользователи
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 1000,
        cases_opened INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Инвентарь
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        skin_name TEXT,
        rarity TEXT,
        price INTEGER,
        wear TEXT,
        obtained_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Кейсы пользователя
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        case_name TEXT,
        amount INTEGER DEFAULT 1
    )
    """)

    # История продаж
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item_name TEXT,
        sell_price INTEGER,
        sold_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def register_user(user_id, username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id, username) VALUES (?, ?)",
        (user_id, username)
    )

    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return 0


def add_balance(user_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id=?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def remove_balance(user_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET balance = balance - ? WHERE user_id=?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def add_item(user_id, skin_name, rarity, price, wear):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventory
        (user_id, skin_name, rarity, price, wear)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        skin_name,
        rarity,
        price,
        wear
    ))

    conn.commit()
    conn.close()


def get_inventory(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, skin_name, rarity, price, wear
        FROM inventory
        WHERE user_id=?
    """, (user_id,))

    items = cursor.fetchall()

    conn.close()

    return items


def sell_item(item_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, skin_name, price
        FROM inventory
        WHERE id=?
    """, (item_id,))

    item = cursor.fetchone()

    if item is None:
        conn.close()
        return False

    user_id, skin_name, price = item

    sell_price = int(price * 0.9)

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id=?",
        (sell_price, user_id)
    )

    cursor.execute(
        "DELETE FROM inventory WHERE id=?",
        (item_id,)
    )

    cursor.execute("""
        INSERT INTO sales
        (user_id, item_name, sell_price)
        VALUES (?, ?, ?)
    """, (
        user_id,
        skin_name,
        sell_price
    ))

    conn.commit()
    conn.close()

    return True
