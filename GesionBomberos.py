from tkinter import *
from tkinter import ttk
import tkinter as tk

#Definir acciones menu
def Accion1():texto.configure(text="TotiManuel")
def AccionA():texto.configure(text="toti")
#Fin acciones menu

Programa=Tk()
Programa.geometry("1000x1000")
ventana=ttk.Frame(Programa, padding=10)
ventana.grid()

#ventana1=tk.Tk()
#ventana1.title("Toti")


#Configuracion Menu
barra_menus=tk.Menu(Programa)
Programa.config(menu=barra_menus)

menu=tk.Menu(barra_menus, tearoff=False)
barra_menus.add_cascade(label="Archivo", menu=menu)
barra_menus.add_cascade(label="Sanciones", menu=menu)
barra_menus.add_cascade(label="Cursos", menu=menu)
barra_menus.add_cascade(label="Inventario", menu=menu)
barra_menus.add_cascade(label="Listado de Bomberos", menu=menu)
barra_menus.add_cascade(label="Listado de Emergencias", menu=menu)
barra_menus.add_cascade(label="Elementos en Reparacion", menu=menu)
barra_menus.add_cascade(label="Opciones", menu=menu)

submenu=tk.Menu(menu, tearoff=False)

barra_menus.add_cascade(label="Menu", menu=menu)
menu.add_cascade(label="submenu", menu=submenu)
#Fin menu

texto=tk.Label(ventana,text="texto")
texto.place(x=200,y=200)


ttk.Label(ventana, text="Hello World").grid(column=0, row=0)
ttk.Button(ventana, text="Quit", command=Programa.destroy).grid(column=1,row=0)



Programa.mainloop()

