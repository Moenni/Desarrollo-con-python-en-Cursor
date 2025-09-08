#Importar Tkinter y modulos necesarios
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#Crear la ventana principal
ventana= tk.Tk()
ventana.title("Block de notas")
ventana.geometry("600x400")
#Esto crea la ventana con título y tamaño inicial

#Area de texto multi-linea
texto= tk.Text(ventana,wrap="word")
texto.pack(expand=True,fill="both")
# Text es el widget que permite escribir. wrap="word" evita que corte palabras al final de línea.

#Funciones para abrir y guardar archivos

def abrir_archivos():
    ruta=filedialog.askopenfilename(filetypes=[("Archivos de texto","*.txt")])
    if ruta:
        with open(ruta,"r",encoding="utf-8") as archivo:
            contenido= archivo.read()
            texto.delete("1.0",tk.END)
            texto.insert(tk.END,contenido)
def guardar_archivo():
    ruta= filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Archivos de texto", "*.txt") ])
    if ruta:
        with open(ruta ,"w", encoding="utf-8")as archivo:
            contenido=texto.get("1.0",tk.END)
            archivo.write(contenido)
        messagebox.showinfo("Guardado","Archivo guardado correctamente")

#Menu de opciones
menu= tk.Menu(ventana)
ventana.config(menu=menu)

archivo_menu= tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=abrir_archivos)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir",command=ventana.quit)
#Esto crea un menú superior con opciones para abrir, guardar y salir

#Ejecucion de la aplicacion
ventana.mainloop()