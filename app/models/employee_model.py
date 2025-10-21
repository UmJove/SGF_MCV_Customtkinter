import sqlite3

class EmployeeModel:
    def __init__(self, db):
        self.db = db

    # Função para cadastro de novo funcionário (CREATE)
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

    # Função para pegar todos os dados do banco (READ)
        # Função de consulta (read) não precisa de commit pois estamos pegando do banco, não mudando nada no banco (colocar em notas, depois)
    def get_all_employees(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM") ##### ACHO QUE ANOTEI ERRADO CONFERIR
        return cursor.fetchall()
    
    # Função para pegar funcionário por ID (READ (ONE))
    def get_employee_by_id(self, employee_id):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id))
        return cursor.fetchone()

    # Função para atualizar dados (UPDATE)
    def update_employee(self, code: str, name: str, nickname: str, gender: str, age: int, salary: float, temp_work: str):
        cursor = self.db.conn.cursor()

        cursor.execute(
            """
            UPDATE employees SET
                code = ?, 
                name = ?, 
                nickname = ?, 
                gender = ?, 
                age = ?, 
                salary = ?, 
                temp_work = ?
            WHERE id = ?
            """,
            (code, name, nickname, gender, age, salary, temp_work),
        )

        self.db.commit()

    # Função para deletar funcionário (DELETE)
    def delete_employee(self, employee_id: int):
        cursor = self.db.conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id))
        self.db.conn.commit()
...
