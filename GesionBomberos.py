from tkinter import *
from tkinter import ttk
import tkinter as tk

def accionUno():
        Programa.destroy

Programa=Tk()
Programa.geometry("500x500")
Programa.title("Bomberos Voluntarios Villa Nueva")
ventana=ttk.Frame(Programa, padding=0)
ventana.grid()

#Colocacion del Menu en la interfaz
barra_menus=tk.Menu(Programa)
Programa.config(menu=barra_menus)

#Menus Definidos
menu=tk.Menu(barra_menus, tearoff=False)
menuArchivo=tk.Menu(barra_menus, tearoff=False)
#SubMenus Definidos
submenu=tk.Menu(menu,tearoff=False)

#Opciones del Menu
barra_menus.add_cascade(label="Menu", menu=menu)
barra_menus.add_cascade(label="Archivo", menu=menuArchivo)

#Opciones SubMenus Principal 
menu.add_command(label="Opcion 1", command=Programa.destroy)
menuArchivo.add_command(label="Opcion 2", command=Programa.destroy)

#Opciones SubMenus Secundario
menu.add_cascade(label="SubMenu1",menu=submenu)

#Opciones SubMenus Terciario
submenu.add_command(label="SubMenu 2", command=Programa.destroy)

Programa.mainloop()
