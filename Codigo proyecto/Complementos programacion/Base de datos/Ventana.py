import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('objetos.db')
c = conn.cursor()

# Crear la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS objetos (
                id TEXT PRIMARY KEY,
                nombre TEXT,
                autor TEXT,
                celular TEXT,
                correo TEXT
            )''')
conn.commit()

# Función para registrar un nuevo objeto
def registrar_objeto():
    def guardar_objeto():
        # Obtener datos del formulario
        objeto_id = entry_id.get()
        nombre = entry_nombre.get()
        autor = entry_autor.get()
        celular = entry_celular.get()
        correo = entry_correo.get()

        # Insertar datos en la base de datos
        try:
            c.execute("INSERT INTO objetos (id, nombre, autor, celular, correo) VALUES (?, ?, ?, ?, ?)",
                      (objeto_id, nombre, autor, celular, correo))
            conn.commit()
            messagebox.showinfo("Registro", "El objeto ha sido registrado exitosamente.")
            reg_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El ID ya existe. Por favor, ingrese un ID único.")

    # Crear ventana para el registro
    reg_window = tk.Toplevel(root)
    reg_window.title("Registrar Objeto")

    # Etiquetas y campos de entrada
    tk.Label(reg_window, text="Número de ID").grid(row=0, column=0, padx=10, pady=10)
    entry_id = tk.Entry(reg_window)
    entry_id.grid(row=0, column=1)

    tk.Label(reg_window, text="Nombre del Objeto").grid(row=1, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(reg_window)
    entry_nombre.grid(row=1, column=1)

    tk.Label(reg_window, text="Autor").grid(row=2, column=0, padx=10, pady=10)
    entry_autor = tk.Entry(reg_window)
    entry_autor.grid(row=2, column=1)

    tk.Label(reg_window, text="Celular").grid(row=3, column=0, padx=10, pady=10)
    entry_celular = tk.Entry(reg_window)
    entry_celular.grid(row=3, column=1)

    tk.Label(reg_window, text="Correo").grid(row=4, column=0, padx=10, pady=10)
    entry_correo = tk.Entry(reg_window)
    entry_correo.grid(row=4, column=1)

    # Botón para guardar el objeto
    tk.Button(reg_window, text="Guardar", command=guardar_objeto).grid(row=5, column=0, columnspan=2, pady=10)

# Función para buscar por número de ID
def buscar_por_etiqueta():
    def realizar_busqueda():
        id_buscar = entry_id_buscar.get()
        c.execute("SELECT * FROM objetos WHERE id = ?", (id_buscar,))
        objeto = c.fetchone()
        
        if objeto:
            resultado = f'ID: {objeto[0]}\nNombre: {objeto[1]}\nAutor: {objeto[2]}\nCelular: {objeto[3]}\nCorreo: {objeto[4]}'
            messagebox.showinfo("Objeto encontrado", resultado)
        else:
            messagebox.showwarning("No encontrado", f"No hay ningún objeto con ID {id_buscar}")
        buscar_window.destroy()

    # Crear ventana para buscar por ID
    buscar_window = tk.Toplevel(root)
    buscar_window.title("Buscar por ID")
    
    tk.Label(buscar_window, text="Ingresar ID del Objeto:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_buscar = tk.Entry(buscar_window)
    entry_id_buscar.grid(row=0, column=1)
    
    tk.Button(buscar_window, text="Buscar", command=realizar_busqueda).grid(row=1, column=0, columnspan=2, pady=10)

# Función para realizar cambios por ID
def realizar_cambios():
    def buscar_y_cambiar():
        id_cambiar = entry_id_cambiar.get()
        c.execute("SELECT * FROM objetos WHERE id = ?", (id_cambiar,))
        objeto = c.fetchone()
        
        if objeto:
            def guardar_cambios():
                nuevo_nombre = entry_nombre.get()
                nuevo_autor = entry_autor.get()
                nuevo_celular = entry_celular.get()
                nuevo_correo = entry_correo.get()
                
                c.execute("UPDATE objetos SET nombre = ?, autor = ?, celular = ?, correo = ? WHERE id = ?",
                          (nuevo_nombre, nuevo_autor, nuevo_celular, nuevo_correo, id_cambiar))
                conn.commit()
                messagebox.showinfo("Cambios realizados", "Los cambios se han guardado exitosamente.")
                cambios_window.destroy()

            # Crear ventana para modificar los datos
            cambios_window = tk.Toplevel(root)
            cambios_window.title("Modificar Objeto")

            tk.Label(cambios_window, text="Número de ID (no modificable)").grid(row=0, column=0, padx=10, pady=10)
            tk.Label(cambios_window, text=id_cambiar).grid(row=0, column=1)

            tk.Label(cambios_window, text="Nombre del Objeto").grid(row=1, column=0, padx=10, pady=10)
            entry_nombre = tk.Entry(cambios_window)
            entry_nombre.insert(0, objeto[1])
            entry_nombre.grid(row=1, column=1)

            tk.Label(cambios_window, text="Autor").grid(row=2, column=0, padx=10, pady=10)
            entry_autor = tk.Entry(cambios_window)
            entry_autor.insert(0, objeto[2])
            entry_autor.grid(row=2, column=1)

            tk.Label(cambios_window, text="Celular").grid(row=3, column=0, padx=10, pady=10)
            entry_celular = tk.Entry(cambios_window)
            entry_celular.insert(0, objeto[3])
            entry_celular.grid(row=3, column=1)

            tk.Label(cambios_window, text="Correo").grid(row=4, column=0, padx=10, pady=10)
            entry_correo = tk.Entry(cambios_window)
            entry_correo.insert(0, objeto[4])
            entry_correo.grid(row=4, column=1)

            tk.Button(cambios_window, text="Guardar Cambios", command=guardar_cambios).grid(row=5, column=0, columnspan=2, pady=10)
            modificar_window.destroy()
        else:
            messagebox.showwarning("No encontrado", f"No hay ningún objeto con ID {id_cambiar}")

    # Crear ventana para buscar por ID y realizar cambios
    modificar_window = tk.Toplevel(root)
    modificar_window.title("Modificar por ID")

    tk.Label(modificar_window, text="Ingresar ID del Objeto a modificar:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_cambiar = tk.Entry(modificar_window)
    entry_id_cambiar.grid(row=0, column=1)

    tk.Button(modificar_window, text="Buscar y Modificar", command=buscar_y_cambiar).grid(row=1, column=0, columnspan=2, pady=10)

# Función para salir de la aplicación
def salir():
    conn.close()  # Cerrar la conexión a la base de datos
    root.destroy()

# Ventana principal
root = tk.Tk()
root.title("Gestión de Objetos")

# Botones en la ventana principal
btn_registrar = tk.Button(root, text="Registrar", command=registrar_objeto)
btn_registrar.grid(row=0, column=0, padx=20, pady=20)

btn_buscar = tk.Button(root, text="Buscar por Etiqueta (ID)", command=buscar_por_etiqueta)
btn_buscar.grid(row=0, column=1, padx=20, pady=20)

btn_cambios = tk.Button(root, text="Realizar Cambios por ID", command=realizar_cambios)
btn_cambios.grid(row=1, column=0, padx=20, pady=20)

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.grid(row=1, column=1, padx=20, pady=20)

# Iniciar la aplicación
root.mainloop()
