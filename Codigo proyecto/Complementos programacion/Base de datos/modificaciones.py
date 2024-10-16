import tkinter as tk
from tkinter import messagebox
import database

def realizar_cambios(root):
    def buscar_y_cambiar():
        id_cambiar = entry_id_cambiar.get().strip()  

        if not id_cambiar:
            messagebox.showwarning("Campo vacío", "Por favor, ingrese un ID.")
            return  

        objeto = database.buscar_objeto(id_cambiar)

        if objeto:
            def guardar_cambios():
                nuevo_nombre = entry_nombre.get().strip()
                nuevo_autor = entry_autor.get().strip()
                nuevo_celular = entry_celular.get().strip()

                if not nuevo_nombre or not nuevo_autor or not nuevo_celular:
                    messagebox.showwarning("Campo vacío", "Por favor, complete todos los campos.")
                    return

                database.actualizar_objeto(id_cambiar, nuevo_nombre, nuevo_autor, nuevo_celular)
                messagebox.showinfo("Cambios realizados", "Los cambios se han guardado exitosamente.")
                cambios_window.destroy()

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

            tk.Button(cambios_window, text="Guardar Cambios", command=guardar_cambios).grid(row=4, column=0, columnspan=2, pady=10)
        else:
            messagebox.showwarning("No encontrado", f"No hay ningún objeto con ID {id_cambiar}")

    modificar_window = tk.Toplevel(root)
    modificar_window.title("Modificar por ID")

    tk.Label(modificar_window, text="Ingresar ID del Objeto a modificar:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_cambiar = tk.Entry(modificar_window)
    entry_id_cambiar.grid(row=0, column=1)

    tk.Button(modificar_window, text="Buscar y Modificar", command=buscar_y_cambiar).grid(row=1, column=0, columnspan=2, pady=10)
