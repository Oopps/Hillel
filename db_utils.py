import sqlite3


try:
    conn = sqlite3.connect('./db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER NOT NULL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails
    (id INTEGER NOT NULL PRIMARY KEY, email VARCHAR(50), user_id int);
    ''')

    conn.commit()
finally:
    conn.close()
