import tkinter as tk
from tkinter import messagebox
import database

def buscar_por_etiqueta(root):
    def realizar_busqueda():
        id_buscar = entry_id_buscar.get()
        objeto = database.buscar_objeto(id_buscar)
        
        if objeto:
            resultado = f'ID: {objeto[0]}\nNombre: {objeto[1]}\nAutor: {objeto[2]}\nCelular: {objeto[3]}\nCorreo: {objeto[4]}'
            messagebox.showinfo("Objeto encontrado", resultado)
        else:
            messagebox.showwarning("No encontrado", f"No hay ningún objeto con ID {id_buscar}")
        buscar_window.destroy()

    buscar_window = tk.Toplevel(root)
    buscar_window.title("Buscar por ID")
    
    tk.Label(buscar_window, text="Ingresar ID del Objeto:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_buscar = tk.Entry(buscar_window)
    entry_id_buscar.grid(row=0, column=1)
    
    tk.Button(buscar_window, text="Buscar", command=realizar_busqueda).grid(row=1, column=0, columnspan=2, pady=10)
