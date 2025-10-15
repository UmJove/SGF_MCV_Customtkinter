import sqlite3

class DataBase:
    def __init__(self, db_name='app.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Tabela de usuários do sistema
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
                )
        """)

        # Tabela de funcionários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                nickname TEXT,
                gender TEXT,
                age INTEGER,
                salary REAL,
                temp_work TEXT
                )
        """)

        self.conn.commit()