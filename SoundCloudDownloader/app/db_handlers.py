import sqlite3

# Подключение к базе данных SQLite
def get_db_connection():
    connection = sqlite3.connect("users.db")
    return connection

# Инициализация базы данных и создание таблицы
def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY
        )
    """)
    connection.commit()
    connection.close()

# Регистрация пользователя в базе данных
def register_user(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        connection.commit()
        print(f"User {user_id} registered successfully.")
    except sqlite3.IntegrityError:
        print(f"User {user_id} already exists.")

    connection.close()

# Проверка, зарегистрирован ли пользователь
def is_user_registered(user_id: int) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    connection.close()

    return user is not None

def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    connection.close()

    # Возвращаем список user_id
    return [user[0] for user in users]