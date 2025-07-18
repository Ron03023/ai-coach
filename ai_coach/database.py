import sqlite3

def init_db():
    conn = sqlite3.connect("coach.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY,
        date TEXT,
        exercise TEXT,
        sets INTEGER,
        reps INTEGER,
        weight INTEGER
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task TEXT,
        done INTEGER DEFAULT 0
    )''')

    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect("coach.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect("coach.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE done=0")
    tasks = c.fetchall()
    conn.close()
    return tasks
