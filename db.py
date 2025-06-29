import sqlite3

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada")
