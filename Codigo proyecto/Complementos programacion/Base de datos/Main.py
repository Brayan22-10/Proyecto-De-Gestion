import tkinter as tk
from PIL import Image, ImageTk
import registro
import busqueda
import modificaciones
import lista
import database

root = tk.Tk()
root.title("Base de datos Teach And Systems")

database.crear_tabla()

def crear_fondo_degradado():
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill='both', expand=True)

    for i in range(0, 256):
        color = f'#{i:02x}{i:02x}ff'  
        canvas.create_line(0, i, root.winfo_screenwidth(), i, fill=color)

def estilo_boton(boton):
    boton.config(
        bg='navy blue',        
        fg='white',         
        font=('Arial', 12), 
        padx=10,           
        pady=5,              
        relief='raised',  
        activebackground='darkblue',  
        activeforeground='white'       
    )

root.geometry("800x600")

crear_fondo_degradado()

frame = tk.Frame(root, bg='white', bd=2, relief='raised', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

boton_registrar = tk.Button(frame, text="Registrar nuevo objeto", command=lambda: registro.registrar_objeto(root))
estilo_boton(boton_registrar)
boton_registrar.pack(pady=10)

boton_buscar = tk.Button(frame, text="Buscar por ID", command=lambda: busqueda.buscar_por_etiqueta(root))
estilo_boton(boton_buscar)
boton_buscar.pack(pady=10)

boton_modificar = tk.Button(frame, text="Modificar por ID", command=lambda: modificaciones.realizar_cambios(root))
estilo_boton(boton_modificar)
boton_modificar.pack(pady=10)

boton_ver_lista = tk.Button(frame, text="Ver lista de objetos", command=lambda: lista.ver_lista_objetos(root))
estilo_boton(boton_ver_lista)
boton_ver_lista.pack(pady=10)

boton_salir = tk.Button(frame, text="Salir", command=root.quit)
estilo_boton(boton_salir)
boton_salir.pack(pady=10)

root.mainloop()
