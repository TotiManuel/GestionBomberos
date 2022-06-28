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

def habilitarIncendio():
	checkbox1.state(["!disabled"]) and checkbox2.state(["!disabled"]) and checkbox3.state(["!disabled"]) and checkbox4.state(["!disabled"]) 
	checkbox5.state(["!disabled"]) and checkbox6.state(["!disabled"]) and checkbox7.state(["!disabled"]) and checkbox8.state(["!disabled"])  
	
def desabilitarIncendio():
	checkbox1.state(["disabled"]) and checkbox2.state(["disabled"]) and checkbox3.state(["disabled"]) and checkbox4.state(["disabled"]) 
	checkbox5.state(["disabled"]) and checkbox6.state(["disabled"]) and checkbox7.state(["disabled"]) and checkbox8.state(["disabled"])  

def habilitarAccidentes():
	checkbox9.state(["!disabled"]) and checkbox10.state(["!disabled"]) and checkbox11.state(["!disabled"]) and checkbox12.state(["!disabled"]) 
	checkbox13.state(["!disabled"]) and checkbox14.state(["!disabled"]) and checkbox15.state(["!disabled"]) and checkbox16.state(["!disabled"])  
	checkbox17.state(["!disabled"])
	
def desabilitarAccidentes():
	checkbox9.state(["disabled"]) and checkbox10.state(["disabled"]) and checkbox11.state(["disabled"]) and checkbox12.state(["disabled"]) 
	checkbox13.state(["disabled"]) and checkbox14.state(["disabled"]) and checkbox15.state(["disabled"]) and checkbox16.state(["disabled"])  
	checkbox17.state(["disabled"])

def habilitarRescate():
	checkbox18.state(["!disabled"]) and checkbox19.state(["!disabled"]) and checkbox20.state(["!disabled"]) and checkbox21.state(["!disabled"]) 
	checkbox22.state(["!disabled"]) and checkbox23.state(["!disabled"]) and checkbox24.state(["!disabled"]) and checkbox25.state(["!disabled"])  
	
def desabilitarRescate():
	checkbox18.state(["disabled"]) and checkbox19.state(["disabled"]) and checkbox20.state(["disabled"]) and checkbox21.state(["disabled"]) 
	checkbox22.state(["disabled"]) and checkbox23.state(["disabled"]) and checkbox24.state(["disabled"]) and checkbox25.state(["disabled"])  

def habilitarOtroServicio():
	checkbox26.state(["!disabled"]) and checkbox27.state(["!disabled"]) and checkbox28.state(["!disabled"]) and checkbox29.state(["!disabled"]) 
	checkbox30.state(["!disabled"]) and checkbox31.state(["!disabled"]) and checkbox32.state(["!disabled"]) and checkbox33.state(["!disabled"])
	checkbox34.state(["!disabled"]) and checkbox35.state(["!disabled"]) and checkbox36.state(["!disabled"]) 
	
def desabilitarOtroServicio():
	checkbox26.state(["disabled"]) and checkbox27.state(["disabled"]) and checkbox28.state(["disabled"]) and checkbox29.state(["disabled"]) 
	checkbox30.state(["disabled"]) and checkbox31.state(["disabled"]) and checkbox32.state(["disabled"]) and checkbox33.state(["disabled"])
	checkbox34.state(["disabled"]) and checkbox35.state(["disabled"]) and checkbox36.state(["disabled"])  

def habilitarFalsaAlarma():
	checkbox37.state(["!disabled"])  
	
def desabilitarFalsaAlarma():
	checkbox37.state(["disabled"])

def cb1():
	if(intcheck1.get()==1):
		mostrar()
	if(intcheck2.get()==1 or intcheck3.get()==1 or intcheck4.get()==1 or intcheck5.get()==1 or intcheck6.get()==1 or intcheck7.get()==1 or intcheck8.get()==1):
		intcheck1.set(1)
		desabilitarAccidentes()
		desabilitarRescate()
		desabilitarOtroServicio()
		desabilitarFalsaAlarma()
		mostrar()
	if(intcheck2.get()==0 and intcheck3.get()==0 and intcheck4.get()==0 and intcheck5.get()==0 and intcheck6.get()==0 and intcheck7.get()==0 and intcheck8.get()==0):
		intcheck1.set(0)
		habilitarAccidentes()
		habilitarRescate()
		habilitarOtroServicio()
		habilitarFalsaAlarma()

def cb2():
	if(intcheck9.get()==1):
		mostrar()
	if(intcheck10.get()==1 or intcheck11.get()==1 or intcheck12.get()==1 or intcheck13.get()==1 or intcheck14.get()==1 or intcheck15.get()==1 or intcheck16.get()==1 or intcheck17.get()==1):
		intcheck9.set(1)
		desabilitarIncendio()
		desabilitarRescate()
		desabilitarOtroServicio()
		desabilitarFalsaAlarma()
		mostrar()
	if(intcheck10.get()==0 and intcheck11.get()==0 and intcheck12.get()==0 and intcheck13.get()==0 and intcheck14.get()==0 and intcheck15.get()==0 and intcheck16.get()==0 and intcheck17.get()==0):
		intcheck9.set(0)
		habilitarIncendio()
		habilitarRescate()
		habilitarOtroServicio()
		habilitarFalsaAlarma()

def cb3():
	if(intcheck18.get()==1):
		mostrar()
	if(intcheck19.get()==1 or intcheck20.get()==1 or intcheck21.get()==1 or intcheck22.get()==1 or intcheck23.get()==1 or intcheck24.get()==1 or intcheck25.get()==1):
		intcheck18.set(1)
		desabilitarAccidentes()
		desabilitarIncendio()
		desabilitarOtroServicio()
		desabilitarFalsaAlarma()
		mostrar()
	if(intcheck19.get()==0 and intcheck20.get()==0 and intcheck21.get()==0 and intcheck22.get()==0 and intcheck23.get()==0 and intcheck24.get()==0 and intcheck25.get()==0):
		intcheck18.set(0)
		habilitarAccidentes()
		habilitarIncendio()
		habilitarOtroServicio()
		habilitarFalsaAlarma()

def cb4():
	if(intcheck26.get()==1):
		mostrar()
	if(intcheck27.get()==1 or intcheck28.get()==1 or intcheck29.get()==1 or intcheck30.get()==1 or intcheck31.get()==1 or intcheck32.get()==1 or intcheck33.get()==1 or intcheck34.get()==1 or intcheck35.get()==1 or intcheck36.get()==1):
		intcheck26.set(1)
		desabilitarAccidentes()
		desabilitarRescate()
		desabilitarIncendio()
		desabilitarFalsaAlarma()
		mostrar()
	if(intcheck27.get()==0 and intcheck28.get()==0 and intcheck29.get()==0 and intcheck30.get()==0 and intcheck31.get()==0 and intcheck32.get()==0 and intcheck33.get()==0 and intcheck34.get()==0 and intcheck35.get()==0 and intcheck36.get()==0):
		intcheck26.set(0)
		habilitarAccidentes()
		habilitarRescate()
		habilitarIncendio()
		habilitarFalsaAlarma()

def cb5():
	if(intcheck37.get()==1):
		desabilitarAccidentes()
		desabilitarRescate()
		desabilitarOtroServicio()
		desabilitarIncendio()
		mostrar()
	if(intcheck37.get()==0):
		habilitarAccidentes()
		habilitarRescate()
		habilitarOtroServicio()
		habilitarIncendio()
def mostrar():
	tipoSiniestro=""
	if(intcheck1.get()==1):
		tipoSiniestro=tipoSiniestro+"INCENDIO: "
	if(intcheck2.get()==1):
		tipoSiniestro=tipoSiniestro+", Vivienda"
	if(intcheck3.get()==1):
		tipoSiniestro=tipoSiniestro+", Comercio"
	if(intcheck4.get()==1):
		tipoSiniestro=tipoSiniestro+", Industria"
	if(intcheck5.get()==1):
		tipoSiniestro=tipoSiniestro+", Vehiculo"
	if(intcheck6.get()==1):
		tipoSiniestro=tipoSiniestro+", Campos"
	if(intcheck7.get()==1):
		tipoSiniestro=tipoSiniestro+", Rollos"
	if(intcheck8.get()==1):
		tipoSiniestro=tipoSiniestro+", Otros"
	if(intcheck9.get()==1):
		tipoSiniestro=tipoSiniestro+"ACCIDENTE: "
	if(intcheck10.get()==1):
		tipoSiniestro=tipoSiniestro+", Urbano"
	if(intcheck11.get()==1):
		tipoSiniestro=tipoSiniestro+", Rural"
	if(intcheck12.get()==1):
		tipoSiniestro=tipoSiniestro+", Automovil"
	if(intcheck13.get()==1):
		tipoSiniestro=tipoSiniestro+", Colectivo"
	if(intcheck14.get()==1):
		tipoSiniestro=tipoSiniestro+", Moto"
	if(intcheck15.get()==1):
		tipoSiniestro=tipoSiniestro+", Tren"
	if(intcheck16.get()==1):
		tipoSiniestro=tipoSiniestro+", Animal"
	if(intcheck17.get()==1):
		tipoSiniestro=tipoSiniestro+", Otro"
	if(intcheck18.get()==1):
		tipoSiniestro=tipoSiniestro+"RESCATE: "
	if(intcheck19.get()==1):
		tipoSiniestro=tipoSiniestro+", Persona"
	if(intcheck20.get()==1):
		tipoSiniestro=tipoSiniestro+", Animal"
	if(intcheck21.get()==1):
		tipoSiniestro=tipoSiniestro+", Vivo"
	if(intcheck22.get()==1):
		tipoSiniestro=tipoSiniestro+", Muerto"
	if(intcheck23.get()==1):
		tipoSiniestro=tipoSiniestro+", Libre"
	if(intcheck24.get()==1):
		tipoSiniestro=tipoSiniestro+", Atrapado"
	if(intcheck25.get()==1):
		tipoSiniestro=tipoSiniestro+", Ahogado"
	if(intcheck26.get()==1):
		tipoSiniestro=tipoSiniestro+"OTRO SERVICIO: "
	if(intcheck27.get()==1):
		tipoSiniestro=tipoSiniestro+", Prevencion"
	if(intcheck28.get()==1):
		tipoSiniestro=tipoSiniestro+", Traslado"
	if(intcheck29.get()==1):
		tipoSiniestro=tipoSiniestro+", Arbol Caido"
	if(intcheck30.get()==1):
		tipoSiniestro=tipoSiniestro+", Cable Colgado"
	if(intcheck31.get()==1):
		tipoSiniestro=tipoSiniestro+", Derrumbe"
	if(intcheck32.get()==1):
		tipoSiniestro=tipoSiniestro+", Escape de Gas"
	if(intcheck33.get()==1):
		tipoSiniestro=tipoSiniestro+", Mat-Pel"
	if(intcheck34.get()==1):
		tipoSiniestro=tipoSiniestro+", Abejas/Avispas"
	if(intcheck35.get()==1):
		tipoSiniestro=tipoSiniestro+", Derrame de Combustible"
	if(intcheck36.get()==1):
		tipoSiniestro=tipoSiniestro+", Otro"
	if(intcheck37.get()==1):
		tipoSiniestro=tipoSiniestro+"Falsa Alarma"
	else:
		print(tipoSiniestro)
		return tipoSiniestro

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
            archi1.write("Tipo de Siniestro:"+mostrar()+ "\n")
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
intcheck1=tk.IntVar()
intcheck2=tk.IntVar()
intcheck3=tk.IntVar()
intcheck4=tk.IntVar()
intcheck5=tk.IntVar()
intcheck6=tk.IntVar()
intcheck7=tk.IntVar()
intcheck8=tk.IntVar()
intcheck9=tk.IntVar()
intcheck10=tk.IntVar()
intcheck11=tk.IntVar()
intcheck12=tk.IntVar()
intcheck13=tk.IntVar()
intcheck14=tk.IntVar()
intcheck15=tk.IntVar()
intcheck16=tk.IntVar()
intcheck17=tk.IntVar()
intcheck18=tk.IntVar()
intcheck19=tk.IntVar()
intcheck20=tk.IntVar()
intcheck21=tk.IntVar()
intcheck22=tk.IntVar()
intcheck23=tk.IntVar()
intcheck24=tk.IntVar()
intcheck25=tk.IntVar()
intcheck26=tk.IntVar()
intcheck27=tk.IntVar()
intcheck28=tk.IntVar()
intcheck29=tk.IntVar()
intcheck30=tk.IntVar()
intcheck31=tk.IntVar()
intcheck32=tk.IntVar()
intcheck33=tk.IntVar()
intcheck34=tk.IntVar()
intcheck35=tk.IntVar()
intcheck36=tk.IntVar()
intcheck37=tk.IntVar()

#######################################################################
#Punto 3.1
#######################################################################

checkbox1=ttk.Checkbutton(Programa, text="INCENDIO", variable=intcheck1)
checkbox1.place(x=20, y=120)
checkbox2=ttk.Checkbutton(Programa, text="Vivienda", variable=intcheck2, command=cb1)
checkbox2.place(x=30, y=140)
checkbox3=ttk.Checkbutton(Programa, text="Comercio", variable=intcheck3, command=cb1)
checkbox3.place(x=30, y=160)
checkbox4=ttk.Checkbutton(Programa, text="Industria", variable=intcheck4, command=cb1)
checkbox4.place(x=30, y=180)
checkbox5=ttk.Checkbutton(Programa, text="Vehiculo", variable=intcheck5, command=cb1)
checkbox5.place(x=30, y=200)
checkbox6=ttk.Checkbutton(Programa, text="Campos", variable=intcheck6, command=cb1)
checkbox6.place(x=30, y=220)
checkbox7=ttk.Checkbutton(Programa, text="Rollos", variable=intcheck7, command=cb1)
checkbox7.place(x=30, y=240)
checkbox8=ttk.Checkbutton(Programa, text="Otros", variable=intcheck8, command=cb1)
checkbox8.place(x=30, y=260)
checkbox9=ttk.Checkbutton(Programa, text="ACCIDENTE", variable=intcheck9)
checkbox9.place(x=150, y=120)
checkbox10=ttk.Checkbutton(Programa, text="Urbano", variable=intcheck10, command=cb2)
checkbox10.place(x=160, y=140)
checkbox11=ttk.Checkbutton(Programa, text="Rural", variable=intcheck11, command=cb2)
checkbox11.place(x=160, y=160)
checkbox12=ttk.Checkbutton(Programa, text="Automovil", variable=intcheck12, command=cb2)
checkbox12.place(x=160, y=180)
checkbox13=ttk.Checkbutton(Programa, text="Colectivo", variable=intcheck13, command=cb2)
checkbox13.place(x=160, y=200)
checkbox14=ttk.Checkbutton(Programa, text="Moto", variable=intcheck14, command=cb2)
checkbox14.place(x=160, y=220)
checkbox15=ttk.Checkbutton(Programa, text="Tren", variable=intcheck15, command=cb2)
checkbox15.place(x=160, y=240)
checkbox16=ttk.Checkbutton(Programa, text="Animal", variable=intcheck16, command=cb2)
checkbox16.place(x=160, y=260)
checkbox17=ttk.Checkbutton(Programa, text="Otro", variable=intcheck17, command=cb2)
checkbox17.place(x=160, y=280)
checkbox18=ttk.Checkbutton(Programa, text="RESCATE", variable=intcheck18)
checkbox18.place(x=280, y=120)
checkbox19=ttk.Checkbutton(Programa, text="Persona", variable=intcheck19, command=cb3)
checkbox19.place(x=290, y=140)
checkbox20=ttk.Checkbutton(Programa, text="Animal", variable=intcheck20, command=cb3)
checkbox20.place(x=290, y=160)
checkbox21=ttk.Checkbutton(Programa, text="Vivo", variable=intcheck21, command=cb3)
checkbox21.place(x=290, y=180)
checkbox22=ttk.Checkbutton(Programa, text="Muerto", variable=intcheck22, command=cb3)
checkbox22.place(x=290, y=200)
checkbox23=ttk.Checkbutton(Programa, text="Libre", variable=intcheck23, command=cb3)
checkbox23.place(x=290, y=220)
checkbox24=ttk.Checkbutton(Programa, text="Atrapado", variable=intcheck24, command=cb3)
checkbox24.place(x=290, y=240)
checkbox25=ttk.Checkbutton(Programa, text="Ahogado", variable=intcheck25, command=cb3)
checkbox25.place(x=290, y=260)
checkbox26=ttk.Checkbutton(Programa, text="OTRO SERVICIO", variable=intcheck26)
checkbox26.place(x=410, y=120)
checkbox27=ttk.Checkbutton(Programa, text="Prevencion", variable=intcheck27, command=cb4)
checkbox27.place(x=420, y=140)
checkbox28=ttk.Checkbutton(Programa, text="Traslado", variable=intcheck28, command=cb4)
checkbox28.place(x=420, y=160)
checkbox29=ttk.Checkbutton(Programa, text="Arbol Caido", variable=intcheck29, command=cb4)
checkbox29.place(x=420, y=180)
checkbox30=ttk.Checkbutton(Programa, text="Cable Colgado", variable=intcheck30, command=cb4)
checkbox30.place(x=420, y=200)
checkbox31=ttk.Checkbutton(Programa, text="Derrumbe", variable=intcheck31, command=cb4)
checkbox31.place(x=420, y=220)
checkbox32=ttk.Checkbutton(Programa, text="Escape de Gas", variable=intcheck32, command=cb4)
checkbox32.place(x=420, y=240)
checkbox33=ttk.Checkbutton(Programa, text="Mat-Pel", variable=intcheck33, command=cb4)
checkbox33.place(x=420, y=260)
checkbox34=ttk.Checkbutton(Programa, text="Abejas/Avispas", variable=intcheck34, command=cb4)
checkbox34.place(x=420, y=280)
checkbox35=ttk.Checkbutton(Programa, text="Derrame de Combustible", variable=intcheck35, command=cb4)
checkbox35.place(x=420, y=300)
checkbox36=ttk.Checkbutton(Programa, text="Otro", variable=intcheck36, command=cb4)
checkbox36.place(x=420, y=320)
checkbox37=ttk.Checkbutton(Programa, text="FALSA ALARMA", variable=intcheck37, command=cb5)
checkbox37.place(x=610, y=120)


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
