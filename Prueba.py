from tkinter import *
from tkinter import ttk
import tkinter as tk

def Accion1():texto.configure(text="TotiManuel")
def AccionA():texto.configure(text="toti")
Programa=Tk()
Programa.geometry("500x500")
ventana=ttk.Frame(Programa, padding=10)
ventana.grid()

#ventana1=tk.Tk()
#ventana1.title("Toti")



barra_menus=tk.Menu(Programa)
Programa.config(menu=barra_menus)
menu=tk.Menu(barra_menus, tearoff=False)
menu.add_command(label="Opcion1", command=Accion1)
menu.add_command(label="Opcion1", command=Programa.destroy)
submenu=tk.Menu(menu, tearoff=False)
submenu.add_command(label="OpcionA", command=AccionA)
barra_menus.add_cascade(label="Menu", menu=menu)
menu.add_cascade(label="submenu", menu=submenu)

texto=tk.Label(ventana,text="texto")
texto.place(x=200,y=200)


ttk.Label(ventana, text="Hello World").grid(column=0, row=0)
ttk.Button(ventana, text="Quit", command=Programa.destroy).grid(column=1,row=0)



Programa.mainloop()

