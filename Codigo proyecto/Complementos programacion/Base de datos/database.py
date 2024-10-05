import sqlite3

conn = sqlite3.connect('objetos.db')
c = conn.cursor()

def crear_tabla():
    c.execute('''CREATE TABLE IF NOT EXISTS objetos (
                    id TEXT PRIMARY KEY,
                    nombre TEXT,
                    autor TEXT,
                    celular TEXT,
                    verificado INTEGER DEFAULT 0  -- 0: Pendiente, 1: Verificado
                )''')
    conn.commit()

def insertar_objeto(id, nombre, autor, celular):
    try:
        c.execute("INSERT INTO objetos (id, nombre, autor, celular) VALUES (?, ?, ?, ?) ",
                  (id, nombre, autor, celular))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("ID duplicado")

def buscar_objeto(id):
    c.execute("SELECT * FROM objetos WHERE id = ?", (id,))
    return c.fetchone()

def actualizar_objeto(id, nombre, autor, celular):
    c.execute("UPDATE objetos SET nombre = ?, autor = ?, celular = ? WHERE id = ?",
              (nombre, autor, celular, id))
    conn.commit()

def obtener_todos_los_objetos():
    c.execute("SELECT * FROM objetos")
    return c.fetchall()

def cerrar_conexion():
    conn.close()

def obtener_objetos_ordenados():
    c.execute("SELECT * FROM objetos ORDER BY id")
    return c.fetchall()

def obtener_pendientes():
    c.execute("SELECT * FROM objetos WHERE verificado = 0")
    return c.fetchall()

def marcar_como_verificado(objeto_id):
    c.execute("UPDATE objetos SET verificado = 1 WHERE id = ?", (objeto_id,))
    conn.commit()
