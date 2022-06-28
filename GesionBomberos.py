from tkinter import *
from tkinter import ttk
import tkinter as tk

#Definir acciones menu
def Accion1():Programa.destroy
def AccionA():texto.configure(text="toti")
#Fin acciones menu

Programa=Tk()
Programa.geometry("1000x1000")
ventana=ttk.Frame(Programa, padding=10)
ventana.grid()

#ventana1=tk.Tk()
#ventana1.title("Toti")

texto=tk.Label(ventana,text="texto")
texto.place(x=200,y=200)


ttk.Label(ventana, text="Hello World").grid(column=0, row=0)
ttk.Button(ventana, text="Quit", command=Programa.destroy).grid(column=1,row=0)



Programa.mainloop()

