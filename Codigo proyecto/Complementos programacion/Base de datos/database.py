import sqlite3

conn = sqlite3.connect('objetos.db')
c = conn.cursor()

def crear_tabla():
    c.execute('''CREATE TABLE IF NOT EXISTS objetos (
                    id TEXT PRIMARY KEY,
                    nombre TEXT,
                    autor TEXT,
                    celular TEXT,
                    correo TEXT
                )''')
    conn.commit()

def insertar_objeto(id, nombre, autor, celular, correo):
    try:
        c.execute("INSERT INTO objetos (id, nombre, autor, celular, correo) VALUES (?, ?, ?, ?, ?)",
                  (id, nombre, autor, celular, correo))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("ID duplicado")

def buscar_objeto(id):
    c.execute("SELECT * FROM objetos WHERE id = ?", (id,))
    return c.fetchone()

def actualizar_objeto(id, nombre, autor, celular, correo):
    c.execute("UPDATE objetos SET nombre = ?, autor = ?, celular = ?, correo = ? WHERE id = ?",
              (nombre, autor, celular, correo, id))
    conn.commit()

def obtener_todos_los_objetos():
    c.execute("SELECT * FROM objetos")
    return c.fetchall()

def cerrar_conexion():
    conn.close()
