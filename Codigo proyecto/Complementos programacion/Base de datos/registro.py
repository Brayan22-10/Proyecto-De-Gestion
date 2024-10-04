import tkinter as tk
from tkinter import messagebox
import database

def registrar_objeto(root):
    def guardar_objeto():
        objeto_id = entry_id.get().strip()
        nombre = entry_nombre.get().strip()
        autor = entry_autor.get().strip()
        celular = entry_celular.get().strip()
        correo = entry_correo.get().strip()

        if not objeto_id or not nombre or not autor or not celular or not correo:
            messagebox.showwarning("Campo vacío", "Por favor, complete todos los campos.")
            return  

        try:
            database.insertar_objeto(objeto_id, nombre, autor, celular, correo)
            messagebox.showinfo("Registro", "El objeto ha sido registrado exitosamente.")
            reg_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "El ID ya existe. Por favor, ingrese un ID único.")

    reg_window = tk.Toplevel(root)
    reg_window.title("Registrar Objeto")

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

    tk.Button(reg_window, text="Guardar", command=guardar_objeto).grid(row=5, column=0, columnspan=2, pady=10)
