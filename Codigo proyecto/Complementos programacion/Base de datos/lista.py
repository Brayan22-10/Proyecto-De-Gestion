import tkinter as tk
import database

def ver_lista_objetos(root):
    lista_window = tk.Toplevel(root)
    lista_window.title("Lista de Objetos")

    def mostrar_detalle(id_objeto):
        objeto = database.buscar_objeto(id_objeto)
        detalle = f"ID: {objeto[0]}\nNombre: {objeto[1]}\nAutor: {objeto[2]}\nCelular: {objeto[3]}\nCorreo: {objeto[4]}"
        detalle_label.config(text=detalle)

    objetos = database.obtener_todos_los_objetos()  

    tk.Label(lista_window, text="Objetos Registrados", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)

    if objetos:
        for index, objeto in enumerate(sorted(objetos, key=lambda x: x[0])):  # Ordenar por ID
            tk.Button(lista_window, text=f"ID: {objeto[0]} - {objeto[1]}", command=lambda id=objeto[0]: mostrar_detalle(id)).grid(row=index+1, column=0, padx=10, pady=5)
    else:
        tk.Label(lista_window, text="No hay objetos registrados.", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)

    detalle_label = tk.Label(lista_window, text="", font=("Arial", 12))
    detalle_label.grid(row=len(objetos)+1, column=0, padx=10, pady=10)

    tk.Button(lista_window, text="Salir", command=lista_window.destroy).grid(row=len(objetos)+2, column=0, pady=10)
