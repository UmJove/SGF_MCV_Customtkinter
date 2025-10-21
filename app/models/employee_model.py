import sqlite3

class EmployeeModel:
    def __init__(self, db):
        self.db = db

    # Função para cadastro de novo funcionário
    def create_employee(self, code: str, name: str, nickname: str, gender: str, age: int, salary: float, temp_work: str):
        
        cursor = self.db.conn.cursor()
        
        try:
            cursor.execute(
                """
                INSERT INTO employees (code, name, nickname, gender, age, salary, temp_work) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (code, name, nickname, gender, age, salary, temp_work)
            )
            self.db.conn.commit()

        except sqlite3.IntegrityError:
            raise ValueError("Funcionário com este código já existe")
