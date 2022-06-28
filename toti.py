"""
Fecha:11/09/2022
Autor: Julian Manuel Mandaio
Desimantación: Gestion de Emergencias de los Bomberos de Villa Nueva
Función principal: Gestionar la Informacion de las Emergencias Ocurridas
Objetivo: Mejor Gestion de Emergencias
"""
#Librerias que utiliza
import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb

#Mensaje de Inicio(modificar askyesno)
mb.askyesno(message="Bienvenido Bombero!!", title="Bienvenido")


class Aplicacion:
    def __init__(self):
        #Configuracion de la ventana
        self.ventana1=tk.Tk()
        self.ventana1.geometry("1500x1000")
        #Configuracion del Menu
        self.agregar_menu()
        #Configuracion del Resumen
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=10, height=10, padx=150,pady=150, wrap=tk.WORD)
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=30, height=30, wrap=tk.WORD)
        #Configuracion de los Label
        ttk.Label(self.ventana1, text="Aviso efectuado por: ").grid(column=0, row=0)
        ttk.Label(self.ventana1, text="Hay Heridos?").place(x=850, y=90)
        ttk.Label(self.ventana1, text="Hay Obitos?").place(x=850, y=60)
        
        #Confirmacion de Combobox
        def mensaje(event): self.combo.get(), mb.askyesno(message="¿Desea continuar con: "+self.combo.get()+"?" , title="Título")
        
        #Configuracion del Combobox
        self.combo = ttk.Combobox(self.ventana1, state="readonly", values=["Incendio", "Choque", "Urgencia Medica", "Explosion"])
        self.combo.current()
        self.combo.set("Motivo")  
        self.combo.bind('<<ComboboxSelected>>', mensaje)
        self.combo.place(x=850, y=30)
        
        #Confirmacion de Combobox
        def mensaje2(event): self.combo2.get(), mb.askyesno(message="¿Desea continuar con: "+self.combo2.get()+"?" , title="Título")
        #Configuracion del Combobox
        self.combo2 = ttk.Combobox(self.ventana1, state="readonly", values=["Villa Nueva", "Villa Maria", "Urgencia Medica", "Explosion"])
        self.combo2.current()
        self.combo2.set("Ciudad")  
        self.combo2.bind('<<ComboboxSelected>>', mensaje2)
        self.combo2.place(x=1040, y=30)

	#Configuracion del titulo de la ventana
        self.ventana1.title("Gestion de Emergencias")
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10) 
        self.ventana1.mainloop()
        
       
    #Menu Desplegable
    def agregar_menu(self):
    
    #Menu Principal
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        
        #SubMenu Archivos
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar Emergencia", command=self.guardar)
        opciones1.add_command(label="Recuperar Emergencia", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)

        
        #SubMenu Sanciones
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Ver Sanciones", command=self.salir)
        opciones2.add_command(label="Agregar Sancion", command=self.salir)
        opciones2.add_command(label="Editar Sancion", command=self.salir)
        opciones2.add_command(label="Eliminar Sancion", command=self.salir)
        
        #SubMenu Cursos
        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones3.add_command(label="Ver Cursos", command=self.salir)
        opciones3.add_command(label="Crear Curso", command=self.v2)
        opciones3.add_command(label="Editar Curso", command=self.salir)
        opciones3.add_command(label="Eliminar Curso", command=self.salir)
        
        #SubMenu Inventario
        opciones4 = tk.Menu(menubar1, tearoff=0)
        opciones4.add_command(label="Equipamentos", command=self.salir)
        opciones4.add_command(label="Herramientas", command=self.salir)
        opciones4.add_command(label="Vehiculos", command=self.salir)
        opciones4.add_command(label="Uniformes", command=self.salir)
        opciones4.add_command(label="Alimentos", command=self.salir)
        
        #SubMenu Listado de Bomberos
        opciones5 = tk.Menu(menubar1, tearoff=0)
        opciones5.add_command(label="Ver Listado de Bomberos", command=self.salir)
        opciones5.add_command(label="Agregar Bombero", command=self.salir)
        opciones5.add_command(label="Editar Bombero", command=self.salir)
        opciones5.add_command(label="Eliminar Bombero", command=self.salir)
        
        #SubMenu Listado de Emergencias
        opciones6 = tk.Menu(menubar1, tearoff=0)
        opciones6.add_command(label="Ver Emergencias", command=self.salir)
        opciones6.add_command(label="Editar Emergencia", command=self.salir)
        opciones6.add_command(label="Eliminar Emergencia", command=self.salir)
        
        #SubMenu Elementos en Reparacion
        opciones7 = tk.Menu(menubar1, tearoff=0)
        opciones7.add_command(label="Ver Elementos en Reparacion", command=self.salir)
        opciones7.add_command(label="Editar Elementos en Reparacion", command=self.salir)
        opciones7.add_command(label="Eliminar Elementos en Reparacion", command=self.salir)
        
        #SubMenu Opciones
        opciones8 = tk.Menu(menubar1, tearoff=0)
        opciones8.add_command(label="Opciones1", command=self.salir)
        opciones8.add_command(label="Salir", command=self.salir)

	
	#Menu Archivo
        menubar1.add_cascade(label="Archivo", menu=opciones1)  
        
        #Menu Sanciones
        menubar1.add_cascade(label="Sanciones", menu=opciones2) 
        
        #Menu Cursos
        menubar1.add_cascade(label="Cursos", menu=opciones3)
        
        #Menu Inventario
        menubar1.add_cascade(label="Inventario", menu=opciones4)
        
        #Menu Listado de Bomberos
        menubar1.add_cascade(label="Listado de Bomberos", menu=opciones5)
        
        #Menu Listado de Emergencias
        menubar1.add_cascade(label="Listado de Emergencias", menu=opciones6)
        
        #Menu Elementos en Reparacion
        menubar1.add_cascade(label="Elementos en Reparacion", menu=opciones7)
        
        #Menu Opciones
        menubar1.add_cascade(label="Opciones", menu=opciones8)

    
    
	#Funcion del Menu Salir
    def salir(self):
        sys.exit()
 #Abrir nueva ventana
    def v2(event):ventana2=tk.Tk(),ventana2.title("Julian"),ventana2.geometry("500x500")

	#Funcion del Menu Guardar
    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write("Tipo de Incidente: "+self.combo.get()+"\n")
            archi1.write("Lugar del Incidente: "+self.combo2.get()+"\n")
            archi1.write("Resumen: "+self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

	#Funcion del Menu Recuperar
    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)
                    

aplicacion1=Aplicacion() 
### #Confirmacion de CheckBox
#        def mensaje3(event): self.check2.get(), mb.askyesno(message="¿Desea continuar con: "+self.check2.get()+"?" , title="Título")
 #       #Configuracion del CheckBox
  #      self.check2 = ttk.Checkbox(self.ventana1, state="readonly", values=["Villa Nueva", "Villa Maria", "Urgencia Medica", "Explosion"])
   #     self.check2.current()
    #    self.check2.set("Ciudad")  
     #   self.check2.bind('<<CheckboxSelected>>', mensaje3)
#        self.check2.place(x=1040, y=30)
