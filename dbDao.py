from db import get_db
def create_taskDao(task):
    db = get_db()
    create_table()
    query = "INSERT INTO task_table (task) VALUES (?)"
    db.execute(query,(task,))
    db.commit()

def create_table():
    db = get_db()
    query = """CREATE TABLE IF NOT EXISTS task_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    );"""
    cur = db.execute(query)
    cur.close()

def getAllTask_taskDao():
    db = get_db()
    query = "SELECT * FROM task_table"
    cur = db.execute(query)
    return cur.fetchall()

def delete_taskDao(id):
    db = get_db()
    query = "DELETE from task_table where id = ?"
    db.execute(query,(id,))
    db.commit()
