import tkinter as tk
import registro
import busqueda
import modificaciones
import lista
import database

root = tk.Tk()
root.title("Menú Principal")

database.crear_tabla()

tk.Button(root, text="Registrar nuevo objeto", command=lambda: registro.registrar_objeto(root)).pack(pady=10)
tk.Button(root, text="Buscar por ID", command=lambda: busqueda.buscar_por_etiqueta(root)).pack(pady=10)
tk.Button(root, text="Modificar por ID", command=lambda: modificaciones.realizar_cambios(root)).pack(pady=10)
tk.Button(root, text="Ver lista de objetos", command=lambda: lista.ver_lista_objetos(root)).pack(pady=10)
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()
