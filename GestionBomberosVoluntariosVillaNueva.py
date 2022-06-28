# Importacion
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from datetime import datetime
import tkinter as tk
import sys
import os
from tkinter import messagebox as mb


#Definicion

def guardar():
        nombrearch=FileDialog.asksaveasfilename(initialdir = "/home/toti/Escritorio",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write("Aviso efectuado por: "+str(entry.get())+ "\n")
            archi1.write("Telefono: "+str(entry2.get())+"\n")
            archi1.write("DNI: "+str(entry3.get())+"\n")
            archi1.write("Fecha y Hora: "+str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)+" "+str(fecha.hour)+":"+str(fecha.minute)+":"+str(fecha.second)+"\n")
            archi1.write("Recepcionado por: "+str(recepcion_por.get())+"\n")
            archi1.write("Lugar del Siniestro: "+str(entry4.get())+"\n")
            archi1.write("Entre calles: "+str(entry5.get())+"\n")
            archi1.write("Localidad: "+str(cbx.get())+"\n")
            archi1.write("Tipo de Siniestro: "+str(checkbox1)+"\n")
            archi1.write("Magnitud: "+"\n")
            archi1.write("Toque de alarma: "+"\n")
            archi1.write("General: "+"\n")
            archi1.write("Resumen: "+"\n"+str(resumen.get("1.0", "end-1c"))+"\n")
            archi1.close()
            mb.showinfo(message="Emergencia Guardada con Exito!", title="Emergencia Guardada")

def buscar_archivo():
    fichero=FileDialog.askopenfilename(title="Abrir Fichero")
    print(fichero)

def elegir_color():
    color=ColorChooser.askcolor(title="Elegi un color")#Selecciona un color
    print(color)#imprime los datos del color
    fondo_pantalla=ColorChooser.askcolor(title="Elegi el color de fondo")#Selecciona un color
    Programa.configure(bg=fondo_pantalla[1])#Cambia fondo de pantalla, [0]es RGB y [1]es hexadecimal

def combobox():
    cbx.bind("<<ComboboxSelected>>", "changed")
    print(cbx.get())

def receptor():
    mostrarReceptor=recepcion_por.get()
    print("Eligio la opcion: ", mostrarReceptor)

Programa=Tk()
Programa.geometry("1366x768")
Programa.title("Bomberos Voluntarios Villa Nueva")
#Programa.config(bg="blue") cambia color de fondo cambia color de fondo  
#Programa.iconbitmap("hola.ico") añadirle icono al programa
ventana=ttk.Frame(Programa, padding=0)
ventana.place()

######################################################################
#Menu
######################################################################

#Colocacion del Menu en la interfaz
barra_menus=tk.Menu(Programa)
Programa.config(menu=barra_menus)

#Menus Definidos
menu=tk.Menu(barra_menus, tearoff=False)
menuArchivo=tk.Menu(barra_menus, tearoff=False)
menuSanciones=tk.Menu(barra_menus, tearoff=False)
menuCursos=tk.Menu(barra_menus, tearoff=False)
menuInventario=tk.Menu(barra_menus, tearoff=False)
menuBomberos=tk.Menu(barra_menus, tearoff=False)
menuEmergencias=tk.Menu(barra_menus, tearoff=False)
menuReparacion=tk.Menu(barra_menus, tearoff=False)
menuOpciones=tk.Menu(barra_menus, tearoff=False)
#SubMenus Definidos
submenu=tk.Menu(menu,tearoff=False)



#Opciones del Menu
barra_menus.add_cascade(label="Menu", menu=menu)
barra_menus.add_cascade(label="Archivo", menu=menuArchivo)
barra_menus.add_cascade(label="Sanciones", menu=menuSanciones)
barra_menus.add_cascade(label="Cursos", menu=menuCursos)
barra_menus.add_cascade(label="Inventario", menu=menuInventario)
barra_menus.add_cascade(label="Listado de Bomberos", menu=menuBomberos)
barra_menus.add_cascade(label="Listado de Emergencias", menu=menuEmergencias)
barra_menus.add_cascade(label="Elementos en Reparacion", menu=menuReparacion)
barra_menus.add_cascade(label="Opciones", menu=menuOpciones)

#Opciones SubMenus Principal 
menu.add_command(label="Abrir", command=buscar_archivo)
menuArchivo.add_command(label="Opcion 2", command=elegir_color)
menuArchivo.add_command(label="Combobox", command=combobox)

menuArchivo.add_command(label="Guardar Emergencia", command=receptor)
menuArchivo.add_command(label="Recuperar Emergencia", command=receptor)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=Programa.quit)

 
#SubMenu Sanciones
menuSanciones.add_command(label="Ver Sanciones", command=receptor)
menuSanciones.add_command(label="Agregar Sancion", command=receptor)
menuSanciones.add_command(label="Editar Sancion", command=receptor)
menuSanciones.add_command(label="Eliminar Sancion", command=receptor)
        
#SubMenu Cursos
menuCursos.add_command(label="Ver Cursos", command=receptor)
menuCursos.add_command(label="Crear Curso", command=receptor)
menuCursos.add_command(label="Editar Curso", command=receptor)
menuCursos.add_command(label="Eliminar Curso", command=receptor)
        
        #SubMenu Inventario
menuInventario.add_command(label="Equipamentos", command=receptor)
menuInventario.add_command(label="Herramientas", command=receptor)
menuInventario.add_command(label="Vehiculos", command=receptor)
menuInventario.add_command(label="Uniformes", command=receptor)
menuInventario.add_command(label="Alimentos", command=receptor)
        
        #SubMenu Listado de Bomberos
menuBomberos.add_command(label="Ver Listado de Bomberos", command=receptor)
menuBomberos.add_command(label="Agregar Bombero", command=receptor)
menuBomberos.add_command(label="Editar Bombero", command=receptor)
menuBomberos.add_command(label="Eliminar Bombero", command=receptor)
        
        #SubMenu Listado de Emergencias
menuEmergencias.add_command(label="Ver Emergencias", command=receptor)
menuEmergencias.add_command(label="Editar Emergencia", command=receptor)
menuEmergencias.add_command(label="Eliminar Emergencia", command=receptor)

        #SubMenu Elementos en Reparacion
menuReparacion.add_command(label="Ver Elementos en Reparacion", command=receptor)
menuReparacion.add_command(label="Editar Elementos en Reparacion", command=receptor)
menuReparacion.add_command(label="Eliminar Elementos en Reparacion", command=receptor)
        
        #SubMenu Opciones
menuOpciones.add_command(label="Opciones1", command=receptor)
menuOpciones.add_command(label="Salir", command=receptor)

#Opciones SubMenus Secundario
menu.add_cascade(label="SubMenu1",menu=submenu)

#Opciones SubMenus Terciario
submenu.add_command(label="SubMenu 2", command=Programa.destroy)

menu.add_separator()
menu.add_command(label="Salir", command=Programa.quit)

#######################################################################
#Punto 1
#######################################################################

entry=Entry(Programa)
entry.place(x=155, y=10)
label=Label(Programa, text="Aviso efectuado por: ")
label.place(x=10, y=10)

entry2=Entry(Programa)
entry2.place(x=400, y=10)
entry2.config(show="*")
label2=Label(Programa, text="Telefono: ")
label2.place(x=330, y=10)

entry3=Entry(Programa)
entry3.place(x=610, y=10)
label3=Label(Programa, text="DNI: ")
label3.place(x=570, y=10)

Programa.add_separator=ttk.Separator(Programa, orient="vertical").place(relx=0.58, rely=0, relwidth=1, relheight=1)
Programa.add_separator=ttk.Separator(Programa, orient="horizontal").place(relx=0, rely=0.06, relwidth=1, relheight=1)

label4=Label(Programa, text="Recepcionado por: ")
label4.place(x=10, y=50)

recepcion_por=StringVar(Programa, "100")
Radiobutton(Programa, text="100", variable=recepcion_por, value="100").place(x=135, y=50)
Radiobutton(Programa, text="Tel: 4913388", variable=recepcion_por, value="Tel: 4913388").place(x=190, y=50)
Radiobutton(Programa, text="Tel: 4911716", variable=recepcion_por, value="Tel: 4911716").place(x=310, y=50)
Radiobutton(Programa, text="Cel: 3534138833", variable=recepcion_por, value="Cel: 3534138833").place(x=440, y=50)
Radiobutton(Programa, text="Cuartel", variable=recepcion_por, value="Cuartel").place(x=590, y=50)

#######################################################################
#Punto 2
#######################################################################

entry4=Entry(Programa)
entry4.place(x=145, y=80)
label5=Label(Programa, text="Lugar del Siniestro: ")
label5.place(x=10, y=80)

entry5=Entry(Programa)
entry5.place(x=410, y=80)
label6=Label(Programa, text="Entre Calles: ")
label6.place(x=315, y=80)

label8=Label(Programa, text="Localidad: ")
label8.place(x=580, y=80)

cbx=ttk.Combobox(values=["Villa Nueva", "Villa Maria", "Oncativo"])
cbx.set("Villa Nueva")
cbx.configure(width=25)
cbx.place(x=660, y=80)

Programa.add_separator=ttk.Separator(Programa, orient="horizontal").place(relx=0, rely=0.17, relwidth=1, relheight=1)

#######################################################################
#Punto 3
#######################################################################


checkbox1=ttk.Checkbutton(Programa, text="INCENDIO")
checkbox1.place(x=20, y=120)
checkbox=ttk.Checkbutton(Programa, text="Vivienda")
checkbox.place(x=30, y=140)
checkbox=ttk.Checkbutton(Programa, text="Comercio")
checkbox.place(x=30, y=160)
checkbox=ttk.Checkbutton(Programa, text="Industria")
checkbox.place(x=30, y=180)
checkbox=ttk.Checkbutton(Programa, text="Vehiculo")
checkbox.place(x=30, y=200)
checkbox=ttk.Checkbutton(Programa, text="Campos")
checkbox.place(x=30, y=220)
checkbox=ttk.Checkbutton(Programa, text="Rollos")
checkbox.place(x=30, y=240)
checkbox=ttk.Checkbutton(Programa, text="Otros")
checkbox.place(x=30, y=260)
checkbox=ttk.Checkbutton(Programa, text="ACCIDENTE")
checkbox.place(x=150, y=120)
checkbox=ttk.Checkbutton(Programa, text="Urbano")
checkbox.place(x=160, y=140)
checkbox=ttk.Checkbutton(Programa, text="Rural")
checkbox.place(x=160, y=160)
checkbox=ttk.Checkbutton(Programa, text="Automovil")
checkbox.place(x=160, y=180)
checkbox=ttk.Checkbutton(Programa, text="Colectivo")
checkbox.place(x=160, y=200)
checkbox=ttk.Checkbutton(Programa, text="Moto")
checkbox.place(x=160, y=220)
checkbox=ttk.Checkbutton(Programa, text="Tren")
checkbox.place(x=160, y=240)
checkbox=ttk.Checkbutton(Programa, text="Animal")
checkbox.place(x=160, y=260)
checkbox=ttk.Checkbutton(Programa, text="Otro")
checkbox.place(x=160, y=280)
checkbox=ttk.Checkbutton(Programa, text="RESCATE")
checkbox.place(x=280, y=120)
checkbox=ttk.Checkbutton(Programa, text="Persona")
checkbox.place(x=290, y=140)
checkbox=ttk.Checkbutton(Programa, text="Animal")
checkbox.place(x=290, y=160)
checkbox=ttk.Checkbutton(Programa, text="Vivo")
checkbox.place(x=290, y=180)
checkbox=ttk.Checkbutton(Programa, text="Muerto")
checkbox.place(x=290, y=200)
checkbox=ttk.Checkbutton(Programa, text="Libre")
checkbox.place(x=290, y=220)
checkbox=ttk.Checkbutton(Programa, text="Atrapado")
checkbox.place(x=290, y=240)
checkbox=ttk.Checkbutton(Programa, text="Ahogado")
checkbox.place(x=290, y=260)
checkbox=ttk.Checkbutton(Programa, text="OTRO SERVICIO")
checkbox.place(x=410, y=120)
checkbox=ttk.Checkbutton(Programa, text="Prevencion")
checkbox.place(x=420, y=140)
checkbox=ttk.Checkbutton(Programa, text="Traslado")
checkbox.place(x=420, y=160)
checkbox=ttk.Checkbutton(Programa, text="Arbol Caido")
checkbox.place(x=420, y=180)
checkbox=ttk.Checkbutton(Programa, text="Cable Colgado")
checkbox.place(x=420, y=200)
checkbox=ttk.Checkbutton(Programa, text="Derrumbe")
checkbox.place(x=420, y=220)
checkbox=ttk.Checkbutton(Programa, text="Escape de Gas")
checkbox.place(x=420, y=240)
checkbox=ttk.Checkbutton(Programa, text="Mat-Pel")
checkbox.place(x=420, y=260)
checkbox=ttk.Checkbutton(Programa, text="Abejas/Avispas")
checkbox.place(x=420, y=280)
checkbox=ttk.Checkbutton(Programa, text="Derrame de Combustible")
checkbox.place(x=420, y=300)
checkbox=ttk.Checkbutton(Programa, text="Otro")
checkbox.place(x=420, y=320)
checkbox=ttk.Checkbutton(Programa, text="FALSA ALARMA")
checkbox.place(x=610, y=120)

Programa.add_separator=ttk.Separator(Programa, orient="horizontal").place(relx=0, rely=0.52, relwidth=1, relheight=1)
Programa.add_separator=ttk.Separator(Programa, orient="vertical").place(relx=0.58, rely=0.18, relwidth=1, relheight=0.34)
#######################################################################
#Punto 4
#######################################################################

label_magnitud=Label(Programa, text="Magnitud: ")
label_magnitud.place(x=800, y=130)

magnitud=IntVar()
Radiobutton(Programa, text="1", variable=magnitud, value=1, command=receptor).place(x=870, y=130)
Radiobutton(Programa, text="2", variable=magnitud, value=2, command=receptor).place(x=920, y=130)
Radiobutton(Programa, text="3", variable=magnitud, value=3, command=receptor).place(x=970, y=130)

label_toque_alarma=Label(Programa, text="Toque de Alarma: ")
label_toque_alarma.place(x=800, y=160)

toque_alarma=IntVar()
Radiobutton(Programa, text="Si", variable=toque_alarma, value=1, command=receptor).place(x=920, y=160)
Radiobutton(Programa, text="No", variable=toque_alarma, value=2, command=receptor).place(x=970, y=160)

label_general=Label(Programa, text="General: ")
label_general.place(x=800, y=190)

general=IntVar()
Radiobutton(Programa, text="Si", variable=general, value=1, command=receptor).place(x=860, y=190)
Radiobutton(Programa, text="No", variable=general, value=2, command=receptor).place(x=910, y=190)

#######################################################################
#Punto 5
#######################################################################

boton1=Button(Programa, text="Guardar Emergencia", command=guardar, background="#b4b4b4")
boton1.config(bd=8, relief=RAISED)
boton1.place(x=10, y=400, width=200, height=100)

boton2=Button(Programa, text="Reiniciar", command=guardar, background="#b4b4b4")
boton2.config(bd=8, relief=RAISED)
boton2.place(x=250, y=400, width=200, height=100)

boton3=Button(Programa, text="Salir", command=Programa.quit, background="#b4b4b4")
boton3.config(bd=8, relief=RAISED)
boton3.place(x=500, y=400, width=200, height=100)

resumen=Text(Programa)
resumen.place(x=500, y=500, width=200, height=100)

#######################################################################
#Punto 6
#######################################################################

fecha=datetime.now()
fecha_ordenada="Hoy", "es:",  fecha.day, "/", fecha.month, "/", fecha.year

label7=Label(Programa, text=fecha_ordenada)
label7.place(x=800, y=10)




Programa.mainloop()
