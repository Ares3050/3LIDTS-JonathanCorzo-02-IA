import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Practica 02 py")
ventana.geometry("520x480")

# Etiqueta para pedir nombre
label_nombre = tk.Label(ventana, text="Ingrese nombre:")
label_nombre.place(x=120, y=100)

# Caja de texto para ingresar nombre
entrada_nombre = tk.Entry(ventana)
entrada_nombre.place(x=220, y=100, width=200)

# Función para botón Aceptar
def aceptar():
    nombre = entrada_nombre.get().strip()
    if nombre == "":
        messagebox.showwarning("Aviso", "Por favor, ingrese un nombre")
    else:
        messagebox.showinfo("Saludo", f"Hola, {nombre}!")

# Función para botón Cancelar (limpiar)
def cancelar():
    entrada_nombre.delete(0, tk.END)

# Botón Aceptar
btn_aceptar = tk.Button(ventana, text="Aceptar", command=aceptar)
btn_aceptar.place(x=120, y=140)

# Botón Cancelar
btn_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar)
btn_cancelar.place(x=280, y=140)

ventana.mainloop()

