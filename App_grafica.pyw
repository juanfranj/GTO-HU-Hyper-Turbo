from tkinter import *
from tkinter import messagebox
from libs.Introduccion_cartas import *
from libs.Preflop_grafica import *
from libs.postflopGrafica import *
from libs.funcionesPostflop import *
from libs.funcionesJuegoPostflop import *
from time import time, sleep
import _thread
import os




root=Tk()



#---------------Introduco el titulo y el logo del software-------------

root.iconbitmap("./imagenes/logo.ico")
root.title("R&JF Bomberos")

#---------------Introduzco el Frame-----------------------------------
#----------------Configuracion de Frames-----------------------------
#root.geometry("471x624")

miFrame3=Frame(root)
miFrame3.grid(row=0,column=0,sticky="nw")
miFrame3.config(bd=2)
miFrame3.config(relief="groove")


miFrame4=Frame(root)
miFrame4.grid(row=0,column=1,sticky="nw")
miFrame4.config(bd=2)
miFrame4.config(relief="groove")

miFrame=Frame(root)
miFrame.grid(row=1,column=0,columnspan=2,sticky="nw")
miFrame.config(bd=2)
miFrame.config(relief="groove")

miFrame2=Frame(root)
miFrame2.grid(row=2,column=0,columnspan=2,sticky="nw")
miFrame2.config(bd=2)
miFrame2.config(relief="groove")

miFrame5=Frame(root)#Ordenar flop y cambiar palos postflop
miFrame5.grid(row=0,column=3)
miFrame5.config(bd=2)
miFrame5.config(relief="groove")

miFrame6=Frame(root)#Calculo preflop
miFrame6.grid(row=2,column=3,sticky="w")
miFrame6.config(bd=2)
miFrame6.config(relief="groove")

miFrame7=Frame(root)#Calculo preflop
miFrame7.grid(row=1,column=3,sticky="w")
miFrame7.config(bd=2)
miFrame7.config(relief="groove")

#--------------Variables--------------------------------------------
Flop=StringVar()
Turn=StringVar()
River=StringVar()
PreFlop=StringVar()
Ciegas=StringVar()
Inicio_ciegas=StringVar()
varOpcion=IntVar()
varPosicion=IntVar()
Posicion_Hero=StringVar()
Flop_Calculo=StringVar()
Preflop_Calculo=StringVar()
Turn_Calculo=StringVar()
River_Calculo=StringVar()
accionPreflop_calculo=StringVar()
varFlop=IntVar()
varTurn=IntVar()
varRiver=IntVar()
varAccionPreflop=IntVar()
accion=StringVar()
tipoBote=StringVar()
turno=StringVar()
###############################Variables preflop##################
read=StringVar()
read1=StringVar()
read2=StringVar()
read3=StringVar()
read4=StringVar()
read5=StringVar()
read6=StringVar()
read7=StringVar()
read8=StringVar()



Botondesh=[]
Botonhab=""
cont=0
MesaFlop=""
MesaTurn=""
MesaRiver=""
MesaPreflop=""

#---------------------------Funciones-------------------------------

def introducirCartas(carta,boton):

	global MesaFlop
	global MesaTurn
	global MesaRiver
	global cont
	global Botondesh
	global MesaPreflop
	global varFlop

	Botondesh.append(boton)#Voy guardando los botones desactivados
	
	if cont<=6:

		if MesaPreflop !="" and cont<=1:

			boton.config(state="disabled")
			PreFlop.set(carta)
			MesaPreflop=""
			cont=cont+1

		elif MesaPreflop =="" and cont<=1:

			boton.config(state="disabled")
			PreFlop.set(PreFlop.get()+carta)
			if cont==1:
				botonPreflop.invoke()
			cont=cont+1


		elif MesaFlop !="" and cont> 1 and cont<=4:

			boton.config(state="disabled")
			Flop.set(carta)
			MesaFlop=""
			cont=cont+1

		elif MesaFlop =="" and cont> 1 and cont<=4:

			boton.config(state="disabled")
			Flop.set(Flop.get()+carta)
			if cont==4:
				check_flop.invoke()
				botonPostflop.invoke()
				#botonPreflop.config(state="disabled")
			cont=cont+1

		elif MesaTurn =="" and cont==5:

			boton.config(state="disabled")
			Turn.set(carta)
			MesaTurn=""
			check_turn.invoke()
			cont=cont+1

		elif MesaRiver =="" and cont==6:

			boton.config(state="disabled")
			River.set(carta)
			MesaRiver=""
			check_river.invoke()
			cont=cont+1

def limpiaMesa():

	global Botondesh
	global cont
	global varFlop
	
	for i in range(len(Botondesh)):
		Botondesh[i].config(state=NORMAL)

	Preflop_Calculo.set("")
	Flop_Calculo.set("")
	Turn_Calculo.set("")
	River_Calculo.set("")
	PreFlop.set("")
	Flop.set("")
	Turn.set("")
	River.set("")

	check_flop.deselect()
	check_turn.deselect()
	check_river.deselect()
	
	cont=0

	read.set("")
	read1.set("")
	read2.set("")
	read3.set("")
	read4.set("")
	read5.set("")
	read6.set("")
	read7.set("")
	read8.set("")

	crearTipoBote()
	archivoTurno("Cartas Preflop")
	cambiaPosicion()
	crearArchivoAccion()

	if os.path.isfile("C:/R&JF/libs/input.txt"):
		os.remove("C:/R&JF/libs/input.txt")
		
	
	try:
		os.remove("C:/R&JF/libs/Datos_Calculo.txt")
		os.remove("C:/R&JF/Datos.txt")
		#os.remove("C:/R&JF/tipoBote.txt")
		

	except FileNotFoundError:
		pass

	
	

def salirAplicacion():

	#valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
	valor=messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
	if valor==True:
		root.destroy()

def numeroCiegas():

	if varOpcion.get()==25:

		Inicio_ciegas.set("25")

	elif varOpcion.get()==22:

		Inicio_ciegas.set("22")

	elif varOpcion.get()==19:

		Inicio_ciegas.set("19")

	elif varOpcion.get()==16:

		Inicio_ciegas.set("16")

	elif varOpcion.get()==13:

		Inicio_ciegas.set("13")

	elif varOpcion.get()==10:

		Inicio_ciegas.set("10")

	elif varOpcion.get()==8:

		Inicio_ciegas.set("8")

	elif varOpcion.get()==6:

		Inicio_ciegas.set("6")

def configurarCiegas():
	fin=False
	while not fin:
		archivo=open("C:/R&JF/libs/contadorCiegas.txt","r")
		files=archivo.readlines()
		ciegasArchivo=float(files[2].replace("\n",""))/10
		ciegas2=str(int(ciegasArchivo))
		ciegas=ciegasCalculo(ciegas2)
		Ciegas.set(ciegas)
		#print(ciegas)
		archivo.close()
		sleep(0.2)

def inicioContador(ciegas):
	archivo=open("C:/R&JF/libs/contadorCiegas.txt","w")
	ciegasEscritura=str(int(ciegas)*10)
	archivo.write(ciegasEscritura+"\n"+ciegasEscritura+"\n"+ciegasEscritura)
	archivo.close()

def cambiaPosicion():

	global varPosicion
	if varPosicion.get()==0:
		varPosicion.set(1)
		Posicion_Hero.set("OOP")

	else:
		varPosicion.set(0)
		Posicion_Hero.set("IP")



def Posicion():

	if varPosicion.get()==0:

		Posicion_Hero.set("IP")

	else:

		Posicion_Hero.set("OOP")

def labelAccion():
	
	fin=False
	while not fin:
		archivo=open("C:/R&JF/libs/accion.txt","r")
		linea=archivo.readline()
		accion.set(linea)
		archivo.close()
		sleep(0.2)

def labelTipoBote():	

	fin=False
	while not fin:
		archivo=open("C:/R&JF/libs/tipoBote.txt","r")
		linea=archivo.readline()
		tipoBote.set(linea)
		archivo.close()
		sleep(0.2)

def labelTurno():
	fin=False
	while not fin:
		archivo=open("C:/R&JF/libs/turno.txt","r")
		linea=archivo.readline()
		turno.set(linea)
		sleep(0.2)
		if linea=="Mano Finalizada":
			sleep(1)
			limpiaMesa()
		archivo.close()
 #-----------------------------Menu-----------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

#------------------------miFrame----------------------------------
#--------------Ventana de cartas=miFrame-------------------------------------

#--------------Label-------------------------------------------------

Label(miFrame, text="Elige Cartas: ").grid(row=0,column=0,sticky="w",columnspan=4,pady=10)

#-------------------Treboles----------------------------------------
Ac=PhotoImage(file="./imagenes/cartas/Ac.png")
botonAc=Button(miFrame, image=Ac,width=30,height=19, command=lambda:introducirCartas("Ac",botonAc))
botonAc.grid(row=1,column=0)
botonAc.config(cursor="hand2")

Kc=PhotoImage(file="./imagenes/cartas/Kc.png")
botonKc=Button(miFrame, image=Kc,width=30,height=19,command=lambda:introducirCartas("Kc",botonKc))
botonKc.grid(row=1,column=1)
botonKc.config(cursor="hand2")

Qc=PhotoImage(file="./imagenes/cartas/Qc.png")
botonQc=Button(miFrame, image=Qc,width=30,height=19,command=lambda:introducirCartas("Qc",botonQc))
botonQc.grid(row=1,column=2)
botonQc.config(cursor="hand2")

Jc=PhotoImage(file="./imagenes/cartas/Jc.png")
botonJc=Button(miFrame, image=Jc,width=30,height=19,command=lambda:introducirCartas("Jc",botonJc))
botonJc.grid(row=1,column=3)
botonJc.config(cursor="hand2")

Tc=PhotoImage(file="./imagenes/cartas/Tc.png")
botonTc=Button(miFrame, image=Tc,width=30,height=19,command=lambda:introducirCartas("Tc",botonTc))
botonTc.grid(row=1,column=4)
botonTc.config(cursor="hand2")

im9c=PhotoImage(file="./imagenes/cartas/9c.png")
boton9c=Button(miFrame, image=im9c,width=30,height=19,command=lambda:introducirCartas("9c",boton9c))
boton9c.grid(row=1,column=5)
boton9c.config(cursor="hand2")

im8c=PhotoImage(file="./imagenes/cartas/8c.png")
boton8c=Button(miFrame, image=im8c,width=30,height=19,command=lambda:introducirCartas("8c",boton8c))
boton8c.grid(row=1,column=6)
boton8c.config(cursor="hand2")

im7c=PhotoImage(file="./imagenes/cartas/7c.png")
boton7c=Button(miFrame, image=im7c,width=30,height=19,command=lambda:introducirCartas("7c",boton7c))
boton7c.grid(row=1,column=7)
boton7c.config(cursor="hand2")

im6c=PhotoImage(file="./imagenes/cartas/6c.png")
boton6c=Button(miFrame, image=im6c,width=30,height=19,command=lambda:introducirCartas("6c",boton6c))
boton6c.grid(row=1,column=8)
boton6c.config(cursor="hand2")

im5c=PhotoImage(file="./imagenes/cartas/5c.png")
boton5c=Button(miFrame, image=im5c,width=30,height=19,command=lambda:introducirCartas("5c",boton5c))
boton5c.grid(row=1,column=9)
boton5c.config(cursor="hand2")

im4c=PhotoImage(file="./imagenes/cartas/4c.png")
boton4c=Button(miFrame, image=im4c,width=30,height=19,command=lambda:introducirCartas("4c",boton4c))
boton4c.grid(row=1,column=10)
boton4c.config(cursor="hand2")

im3c=PhotoImage(file="./imagenes/cartas/3c.png")
boton3c=Button(miFrame, image=im3c,width=30,height=19,command=lambda:introducirCartas("3c",boton3c))
boton3c.grid(row=1,column=11)
boton3c.config(cursor="hand2")

im2c=PhotoImage(file="./imagenes/cartas/2c.png")
boton2c=Button(miFrame, image=im2c,width=30,height=19,command=lambda:introducirCartas("2c",boton2c))
boton2c.grid(row=1,column=12)
boton2c.config(cursor="hand2")

#------------------------------Diamantes-------------------------------

Ad =PhotoImage(file="./imagenes/cartas/Ad.png")
botonAd=Button(miFrame, image=Ad,width=30,height=19, command=lambda:introducirCartas("Ad",botonAd))
botonAd.grid(row=2,column=0)
botonAd.config(cursor="hand2")

Kd =PhotoImage(file="./imagenes/cartas/Kd.png")
botonKd=Button(miFrame, image=Kd,width=30,height=19,command=lambda:introducirCartas("Kd",botonKd))
botonKd.grid(row=2,column=1)
botonKd.config(cursor="hand2")

Qd=PhotoImage(file="./imagenes/cartas/Qd.png")
botonQd=Button(miFrame, image=Qd,width=30,height=19,command=lambda:introducirCartas("Qd",botonQd))
botonQd.grid(row=2,column=2)
botonQd.config(cursor="hand2")

Jd=PhotoImage(file="./imagenes/cartas/Jd.png")
botonJd=Button(miFrame, image=Jd,width=30,height=19,command=lambda:introducirCartas("Jd",botonJd))
botonJd.grid(row=2,column=3)
botonJd.config(cursor="hand2")

Td=PhotoImage(file="./imagenes/cartas/Td.png")
botonTd=Button(miFrame, image=Td,width=30,height=19,command=lambda:introducirCartas("Td",botonTd))
botonTd.grid(row=2,column=4)
botonTd.config(cursor="hand2")

im9d=PhotoImage(file="./imagenes/cartas/9d.png")
boton9d=Button(miFrame, image=im9d,width=30,height=19,command=lambda:introducirCartas("9d",boton9d))
boton9d.grid(row=2,column=5)
boton9d.config(cursor="hand2")

im8d=PhotoImage(file="./imagenes/cartas/8d.png")
boton8d=Button(miFrame, image=im8d,width=30,height=19,command=lambda:introducirCartas("8d",boton8d))
boton8d.grid(row=2,column=6)
boton8d.config(cursor="hand2")

im7d=PhotoImage(file="./imagenes/cartas/7d.png")
boton7d=Button(miFrame, image=im7d,width=30,height=19,command=lambda:introducirCartas("7d",boton7d))
boton7d.grid(row=2,column=7)
boton7d.config(cursor="hand2")

im6d=PhotoImage(file="./imagenes/cartas/6d.png")
boton6d=Button(miFrame, image=im6d,width=30,height=19,command=lambda:introducirCartas("6d",boton6d))
boton6d.grid(row=2,column=8)
boton6d.config(cursor="hand2")

im5d=PhotoImage(file="./imagenes/cartas/5d.png")
boton5d=Button(miFrame, image=im5d,width=30,height=19,command=lambda:introducirCartas("5d",boton5d))
boton5d.grid(row=2,column=9)
boton5d.config(cursor="hand2")

im4d=PhotoImage(file="./imagenes/cartas/4d.png")
boton4d=Button(miFrame, image=im4d,width=30,height=19,command=lambda:introducirCartas("4d",boton4d))
boton4d.grid(row=2,column=10)
boton4d.config(cursor="hand2")

im3d=PhotoImage(file="./imagenes/cartas/3d.png")
boton3d=Button(miFrame, image=im3d,width=30,height=19,command=lambda:introducirCartas("3d",boton3d))
boton3d.grid(row=2,column=11)
boton3d.config(cursor="hand2")

im2d=PhotoImage(file="./imagenes/cartas/2d.png")
boton2d=Button(miFrame, image=im2d,width=30,height=19,command=lambda:introducirCartas("2d",boton2d))
boton2d.grid(row=2,column=12)
boton2d.config(cursor="hand2")

#---------------------------------Corazones---------------------------------------

Ah=PhotoImage(file="./imagenes/cartas/Ah.png")
botonAh=Button(miFrame, image=Ah,width=30,height=19, command=lambda:introducirCartas("Ah",botonAh))
botonAh.grid(row=3,column=0)
botonAh.config(cursor="hand2")

Kh=PhotoImage(file="./imagenes/cartas/Kh.png")
botonKh=Button(miFrame, image=Kh,width=30,height=19,command=lambda:introducirCartas("Kh",botonKh))
botonKh.grid(row=3,column=1)
botonKh.config(cursor="hand2")

Qh=PhotoImage(file="./imagenes/cartas/Qh.png")
botonQh=Button(miFrame, image=Qh,width=30,height=19,command=lambda:introducirCartas("Qh",botonQh))
botonQh.grid(row=3,column=2)
botonQh.config(cursor="hand2")

Jh=PhotoImage(file="./imagenes/cartas/Jh.png")
botonJh=Button(miFrame, image=Jh,width=30,height=19,command=lambda:introducirCartas("Jh",botonJh))
botonJh.grid(row=3,column=3)
botonJh.config(cursor="hand2")

Th=PhotoImage(file="./imagenes/cartas/Th.png")
botonTh=Button(miFrame, image=Th,width=30,height=19,command=lambda:introducirCartas("Th",botonTh))
botonTh.grid(row=3,column=4)
botonTh.config(cursor="hand2")

im9h=PhotoImage(file="./imagenes/cartas/9h.png")
boton9h=Button(miFrame, image=im9h,width=30,height=19,command=lambda:introducirCartas("9h",boton9h))
boton9h.grid(row=3,column=5)
boton9h.config(cursor="hand2")

im8h=PhotoImage(file="./imagenes/cartas/8h.png")
boton8h=Button(miFrame, image=im8h,width=30,height=19,command=lambda:introducirCartas("8h",boton8h))
boton8h.grid(row=3,column=6)
boton8h.config(cursor="hand2")

im7h=PhotoImage(file="./imagenes/cartas/7h.png")
boton7h=Button(miFrame, image=im7h,width=30,height=19,command=lambda:introducirCartas("7h",boton7h))
boton7h.grid(row=3,column=7)
boton7h.config(cursor="hand2")

im6h=PhotoImage(file="./imagenes/cartas/6h.png")
boton6h=Button(miFrame, image=im6h,width=30,height=19,command=lambda:introducirCartas("6h",boton6h))
boton6h.grid(row=3,column=8)
boton6h.config(cursor="hand2")

im5h=PhotoImage(file="./imagenes/cartas/5h.png")
boton5h=Button(miFrame, image=im5h,width=30,height=19,command=lambda:introducirCartas("5h",boton5h))
boton5h.grid(row=3,column=9)
boton5h.config(cursor="hand2")

im4h=PhotoImage(file="./imagenes/cartas/4h.png")
boton4h=Button(miFrame, image=im4h,width=30,height=19,command=lambda:introducirCartas("4h",boton4h))
boton4h.grid(row=3,column=10)
boton4h.config(cursor="hand2")

im3h=PhotoImage(file="./imagenes/cartas/3h.png")
boton3h=Button(miFrame, image=im3h,width=30,height=19,command=lambda:introducirCartas("3h",boton3h))
boton3h.grid(row=3,column=11)
boton3h.config(cursor="hand2")

im2h=PhotoImage(file="./imagenes/cartas/2h.png")
boton2h=Button(miFrame, image=im2h,width=30,height=19,command=lambda:introducirCartas("2h",boton2h))
boton2h.grid(row=3,column=12)
boton2h.config(cursor="hand2")

#-------------------------------Picas----------------------------------------

As=PhotoImage(file="./imagenes/cartas/As.png")
botonAs=Button(miFrame, image=As,width=30,height=19, command=lambda:introducirCartas("As",botonAs))
botonAs.grid(row=4,column=0)
botonAs.config(cursor="hand2")

Ks=PhotoImage(file="./imagenes/cartas/Ks.png")
botonKs=Button(miFrame, image=Ks,width=30,height=19,command=lambda:introducirCartas("Ks",botonKs))
botonKs.grid(row=4,column=1)
botonKs.config(cursor="hand2")

Qs=PhotoImage(file="./imagenes/cartas/Qs.png")
botonQs=Button(miFrame, image=Qs,width=30,height=19,command=lambda:introducirCartas("Qs",botonQs))
botonQs.grid(row=4,column=2)
botonQs.config(cursor="hand2")

Js=PhotoImage(file="./imagenes/cartas/Js.png")
botonJs=Button(miFrame, image=Js,width=30,height=19,command=lambda:introducirCartas("Js",botonJs))
botonJs.grid(row=4,column=3)
botonJs.config(cursor="hand2")

Ts=PhotoImage(file="./imagenes/cartas/Ts.png")
botonTs=Button(miFrame, image=Ts,width=30,height=19,command=lambda:introducirCartas("Ts",botonTs))
botonTs.grid(row=4,column=4)
botonTs.config(cursor="hand2")

im9s=PhotoImage(file="./imagenes/cartas/9s.png")
boton9s=Button(miFrame, image=im9s,width=30,height=19,command=lambda:introducirCartas("9s",boton9s))
boton9s.grid(row=4,column=5)
boton9s.config(cursor="hand2")

im8s=PhotoImage(file="./imagenes/cartas/8s.png")
boton8s=Button(miFrame, image=im8s,width=30,height=19,command=lambda:introducirCartas("8s",boton8s))
boton8s.grid(row=4,column=6)
boton8s.config(cursor="hand2")

im7s=PhotoImage(file="./imagenes/cartas/7s.png")
boton7s=Button(miFrame, image=im7s,width=30,height=19,command=lambda:introducirCartas("7s",boton7s))
boton7s.grid(row=4,column=7)
boton7s.config(cursor="hand2")

im6s=PhotoImage(file="./imagenes/cartas/6s.png")
boton6s=Button(miFrame, image=im6s,width=30,height=19,command=lambda:introducirCartas("6s",boton6s))
boton6s.grid(row=4,column=8)
boton6s.config(cursor="hand2")

im5s=PhotoImage(file="./imagenes/cartas/5s.png")
boton5s=Button(miFrame, image=im5s,width=30,height=19,command=lambda:introducirCartas("5s",boton5s))
boton5s.grid(row=4,column=9)
boton5s.config(cursor="hand2")

im4s=PhotoImage(file="./imagenes/cartas/4s.png")
boton4s=Button(miFrame, image=im4s,width=30,height=19,command=lambda:introducirCartas("4s",boton4s))
boton4s.grid(row=4,column=10)
boton4s.config(cursor="hand2")

im3s=PhotoImage(file="./imagenes/cartas/3s.png")
boton3s=Button(miFrame, image=im3s,width=30,height=19,command=lambda:introducirCartas("3s",boton3s))
boton3s.grid(row=4,column=11)
boton3s.config(cursor="hand2")

im2s=PhotoImage(file="./imagenes/cartas/2s.png")
boton2s=Button(miFrame, image=im2s,width=30,height=19,command=lambda:introducirCartas("2s",boton2s))
boton2s.grid(row=4,column=12)
boton2s.config(cursor="hand2")

#-----------------------------Boton Clear---------------------------------

botonClear=Button(miFrame, text="Clear", command=lambda:limpiaMesa())
botonClear.grid(row=5,column=0, sticky="w",columnspan=3, pady=10)
botonClear.config(width=15)
botonClear.config(cursor="hand2")

#-----------------------------miFrame2-----------------------------------
#----------------------------Preflop-------------------------------------

nombrePreflop=Label(miFrame2, text="PreFlop:")
nombrePreflop.grid(row=0,column=0,sticky="w",pady=10)
cuadroPreflop=Entry(miFrame2, textvariable=PreFlop)
cuadroPreflop.grid(row=0,column=1)

#-----------------------------Flop,Turn,River=miFrame2----------------------------------

nombreFlop=Label(miFrame2, text="Flop:")
nombreFlop.grid(row=1,column=0,sticky="w",pady=10)
cuadroFlop=Entry(miFrame2, textvariable=Flop)
cuadroFlop.grid(row=1,column=1)

nombreTurn=Label(miFrame2, text="Turn:")
nombreTurn.grid(row=1,column=2,sticky="w")
cuadroTurn=Entry(miFrame2, textvariable=Turn)
cuadroTurn.grid(row=1,column=3)

nombreRiver=Label(miFrame2, text="River:")
nombreRiver.grid(row=1,column=4,sticky="w")
cuadroTurn=Entry(miFrame2, textvariable=River)
cuadroTurn.grid(row=1,column=5)


#--------------------------------------miFrame3------------------------
#-------------------------------------Numero de ciegas-----------------

Label(miFrame3, text="Numero de ciegas").grid(row=0,column=0,sticky="w",columnspan=2,pady=10)
botonciegas=Button(miFrame3, text="Accion",command=_thread.start_new_thread(configurarCiegas,()))
Numero_ciegas=Entry(miFrame3, textvariable=Ciegas)
Numero_ciegas.grid(row=0,column=2,columnspan=3)
#Ciegas.set("25")





#--------------------------------Radiobutton-----------------------------

Radiobutton(miFrame3, text="25BB",variable=varOpcion, value=25, command=numeroCiegas).grid(row=1,column=0)
Radiobutton(miFrame3, text="22BB",variable=varOpcion, value=22, command=numeroCiegas).grid(row=1,column=1)
Radiobutton(miFrame3, text="19BB",variable=varOpcion, value=19, command=numeroCiegas).grid(row=1,column=2)
Radiobutton(miFrame3, text="16BB",variable=varOpcion, value=16, command=numeroCiegas).grid(row=1,column=3)
Radiobutton(miFrame3, text="13BB",variable=varOpcion, value=13, command=numeroCiegas).grid(row=2,column=0)
Radiobutton(miFrame3, text="10BB",variable=varOpcion, value=10, command=numeroCiegas).grid(row=2,column=1)
Radiobutton(miFrame3, text="8BB",variable=varOpcion, value=8, command=numeroCiegas).grid(row=2,column=2)
Radiobutton(miFrame3, text="6BB",variable=varOpcion, value=6, command=numeroCiegas).grid(row=2,column=3)

#--------------------------------------miFrame4------------------------
#-------------------------------------Posicion-----------------

Label(miFrame4, text="Posicion").grid(row=0,column=0,sticky="w",columnspan=2,pady=10,padx=10)

cuadroPosicion=Entry(miFrame4, textvariable=Posicion_Hero)
cuadroPosicion.grid(row=0,column=2,columnspan=1)
Posicion_Hero.set("IP")

Label(miFrame4, text="Inicio Ciegas").grid(row=2,column=0,sticky="w",columnspan=2,pady=10)
InicioCiegas=Entry(miFrame4, textvariable=Inicio_ciegas)
InicioCiegas.grid(row=2,column=2,columnspan=1)
botonciegas=Button(miFrame4, text="Ciegas",command=lambda:inicioContador(Inicio_ciegas.get()))
botonciegas.grid(row=1,column=2,columnspan=1)
#--------------------------------Radiobutton-----------------------------

Radiobutton(miFrame4, text="IP",variable=varPosicion, value=0, command=Posicion).grid(row=1,column=0)
Radiobutton(miFrame4, text="OOP",variable=varPosicion, value=1, command=Posicion).grid(row=1,column=1)

botonAccion=Button(miFrame5, text="Accion",command=_thread.start_new_thread(labelAccion,()))
textoAccion=Label(miFrame5, textvariable=accion,width="10",height="2")
textoAccion.grid(row=1,column=0,columnspan=8)
textoAccion.config(anchor="w",justify="left",width="16",height="2",fg="black",
	font=("helvetica", "10", "bold"))

botonTipoBote=Button(miFrame5, text="bote",command=_thread.start_new_thread(labelTipoBote,()))
textoTipoBote=Label(miFrame5, textvariable=tipoBote)
textoTipoBote.grid(row=0,column=0,columnspan=10)
textoTipoBote.config(anchor="center",justify="center",width="16",height="2",fg="black",
	font=("helvetica", "11", "bold"))

botonTurno=Button(miFrame5, text="bote",command=_thread.start_new_thread(labelTurno,()))
textoTurno=Label(miFrame5, textvariable=turno)
textoTurno.grid(row=2,column=0,columnspan=10)
textoTurno.config(anchor="center",justify="center",width="16",height="2",fg="black",
	font=("helvetica", "11", "bold"))

#--------------------------------miFrame 5-------------------------------

#Label(miFrame5, text="Flop Calculo:").grid(row=0,column=0,sticky="nw")
#Flop_Calculo_cuadro=Entry(miFrame5, textvariable=Flop_Calculo)
#Flop_Calculo_cuadro.grid(row=0,column=1,columnspan=3)

def flopcalculo():

	

	
	if varFlop.get()==1:

		archivo=open("C:/R&JF/libs/Datos_Calculo.txt","w")
		Flop_Calculo_=introduce_flop(Flop.get())
		Flop_Calculo.set(Flop_Calculo_[0])
				
		Preflop_Calculo_=ordenaPreflop(PreFlop.get())
		Preflop_Calculo__=preflopcambiado(Preflop_Calculo_,Flop_Calculo_[1],Flop_Calculo_[2])
		Preflop_Calculo.set(Preflop_Calculo__)
		archivo.write(Preflop_Calculo__+","+Flop_Calculo_[0])
		archivo.close()


	if varTurn.get()==1:

		archivo=open("C:/R&JF/libs/IntroduceCarta.txt","w")
		Turn_Calculo_=introduce_carta(Turn.get(),Flop_Calculo_[1],Flop_Calculo_[2])
		Turn_Calculo.set(Turn_Calculo_)
		archivo.write(Turn_Calculo_+",")
		archivo.write("\n\nFIN")
		archivo.close()

	if varRiver.get()==1:

		archivo=open("C:/R&JF/libs/IntroduceCarta.txt","w")
		River_Calculo_=introduce_carta(River.get(),Flop_Calculo_[1],Flop_Calculo_[2])
		River_Calculo.set(River_Calculo_)
		archivo.write(River_Calculo_+",")
		archivo.write("\n\nFIN")
		archivo.close()

	

#Label(miFrame5, text="Calculos:").grid(row=0,column=0,sticky="w",padx=10,pady=10)
#Incluyo los checkbox
check_preflop=Checkbutton(miFrame5, text="PreFlop Calculo",variable=varFlop, onvalue=1, offvalue=0,command=flopcalculo)
#check_preflop.grid(row=1,column=0)

check_flop=Checkbutton(miFrame5, text="Flop Calculo",variable=varFlop, onvalue=1, offvalue=0,command=flopcalculo)
#check_flop.grid(row=2,column=0,sticky="w")

check_turn=Checkbutton(miFrame5, text="Turn Calculo",variable=varTurn, onvalue=1, offvalue=0,command=flopcalculo)
#check_turn.grid(row=3,column=0,sticky="w")

check_river=Checkbutton(miFrame5, text="River Calculo",variable=varRiver, onvalue=1, offvalue=0,command=flopcalculo)
#check_river.grid(row=4,column=0,sticky="w")


#a,b,c=flopcalculo()

Flop_Calculo_cuadro=Entry(miFrame5, textvariable=Flop_Calculo)
#Flop_Calculo_cuadro.grid(row=2,column=1,columnspan=3,sticky="w")

Prelop_Calculo_cuadro=Entry(miFrame5, textvariable=Preflop_Calculo)
#Prelop_Calculo_cuadro.grid(row=1,column=1,columnspan=3,sticky="w")

Turn_Calculo_cuadro=Entry(miFrame5, textvariable=Turn_Calculo)
#Turn_Calculo_cuadro.grid(row=3,column=1,columnspan=3,sticky="w")

River_Calculo_cuadro=Entry(miFrame5, textvariable=River_Calculo)
#River_Calculo_cuadro.grid(row=4,column=1,columnspan=3,sticky="w")

##########################miFrame6 Preflop######################
##################Funciones preflop

def accionrealizada():#read,read1,read2,read3
	
	fin=False
	read5.set(read.get())
	crearOutput()
	clear()
def accionrealizada1():#read,read1,read2,read3
	
	fin=False
	read5.set(read1.get())
	crearOutput()
	clear()
def accionrealizada2():#read,read1,read2,read3
	
	fin=False
	read5.set(read2.get())
	crearOutput()
	clear()
def accionrealizada3():#read,read1,read2,read3
	
	fin=False
	read5.set(read3.get())
	crearOutput()
	clear()	

def accionrealizada4():#read,read1,read2,read3
	
	fin=False
	read5.set(read4.get())
	crearOutput()
	clear()	

def accionrealizada7():
	read5.set(read7.get())
	crearOutput()
	clear()

def accionrealizada8():
	read5.set(read8.get())
	crearOutput()
	clear()


def sizeApuesta(ciegas,accion):
	
	size=""
	if accion=="RAISE":
		if int(ciegas)>19:
			size="3,5bb"
		elif int(ciegas)>13:
			size="3bb"
		elif int(ciegas)>10:
			size="2.7bb"
		elif int(ciegas)>6:
			size="2.5bb"
		else:
			size="2bb"
	if accion=="3BNAI":
		if int(ciegas)>19:
			size="5bb"
		elif int(ciegas)>13:
			size="4,5bb"

	return size
	
	
def abrirArchivo():
	sleep(0.2)
	while not os.path.isfile("C:/R&JF/libs/input.txt"):
		#print("Esperando Archivo input.txt")
		sleep(0.2)
	try:
		#esperarInput("C:/R&JF/libs/input.txt")
		archivo=open("C:/R&JF/libs/input.txt","r")
	except FileNotFoundError:
		sleep(0.5)
		archivo=open("C:/R&JF/libs/input.txt","r")
	except PermissionError:
		sleep(0.5)
		archivo=open("C:/R&JF/libs/input.txt","r")
	files=archivo.readlines()
	#os.remove("C:/Users/juanf/Desktop/prueba_preflop/Preflop_input.txt")
	archivo.close()
	try:
		pass
		os.remove("C:/R&JF/libs/input.txt")
	except PermissionError:
		sleep(0.5)
		os.remove("C:/R&JF/libs/input.txt")
	return files

def jugarPostflop():
	if os.path.isfile("C:/R&JF/libs/input.txt"):
		os.remove("C:/R&JF/libs/input.txt")
	_thread.start_new_thread(juegoPostflop,())

	while not os.path.isfile("C:/R&JF/libs/input.txt"):
		sleep(0.2)
	fin=False
	while not fin:	
		#esperarinput("C:/R&JF/libs/input.txt")
		files=abrirArchivo()
		#esperarinput("C:/R&JF/libs/input.txt")
		seleccionaAccion(files)
		try:
			if files[0]=="END":
				fin=True
		except IndexError:
			pass
	print("Fin Postflop")

def comenzarPostflop():
	_thread.start_new_thread(jugarPostflop,())


def seleccionaAccion(files):

	try:

		if len(files[0])!=0:
			if files[0]!="END":
				read.set(files[0])
				
		if len(files[1])!=0:
			if files[1]!="END":
				read1.set(files[1])
				
		if len(files[2])!=0:
			if files[2]!="END":
				read2.set(files[2])
				
		if len(files[3])!=0:
			if files[3]!="END":
				read3.set(files[3])
				
		if len(files[4])!=0:
			if files[4]!="END":
				read7.set(files[4])
				
		if len(files[5])!=0:
			if files[5]!="END":
				read8.set(files[5])
				
#--------------------------------Incluir el postflop aqui--------------
		if len(files[-2])!=0 and len(files[-3])==1:
			file=files[-2].split(",")
			size=""
			size=sizeApuesta(Ciegas.get(),file[0])
			#print("Resube :"+size)
			if size !="":
				read4.set(file[0])
				read4.set(read4.get()+" "+size)
			else:
				read4.set(file[0])

			#size=sizeApuesta(Ciegas.get(),files[-1])
			#print("Resube :"+size)
			#read4.set(files[-1])
			#read4.set(read4.get()+" "+size)

			
	except IndexError:
		pass
	

def jugar():

	if os.path.isfile("C:/R&JF/libs/input.txt"):
		os.remove("C:/R&JF/libs/input.txt")
		
	
	_thread.start_new_thread(juegoPreflop,(Ciegas.get(),Posicion_Hero.get(),PreFlop.get()))
	
	while not os.path.isfile("C:/R&JF/libs/input.txt"):
		sleep(0.25)
	fin=False
	while not fin:	
		files=abrirArchivo()
		seleccionaAccion(files)
		try:
			if files[0]=="END":
				fin=True
		except IndexError:
			pass
		sleep(0.3)
	print("Fin Preflop")
	#os.remove("C:/R&JF/libs/input.txt")
		
def crearOutput():
	linea=str(read5.get())
	print("la accion elegida es: ",linea)
	#print(len(linea))
	archivo=open("C:/R&JF/libs/output.txt","w")
	archivo.write(linea+"\nFIN")
	archivo.close()

	
	
def clear():
	read.set("")
	read1.set("")
	read2.set("")
	read3.set("")
	read4.set("")
	read5.set("")
	read6.set("")
	read7.set("")
	read8.set("")

def comenzarPreflop():
	_thread.start_new_thread(jugar,())


#------------------------------------Botones aciones------------
botonA=Button(miFrame7, textvariable=read, command =accionrealizada)
botonA.grid(row=2,column=0)
botonA.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonB=Button(miFrame7, textvariable=read1, command =accionrealizada1)
botonB.grid(row=2,column=1)
botonB.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonC=Button(miFrame7, textvariable=read2, command =accionrealizada2)
botonC.grid(row=3,column=0)
botonC.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))


botonD=Button(miFrame7, textvariable=read3, command =accionrealizada3)
botonD.grid(row=3,column=1)
botonD.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonE=Button(miFrame7, textvariable=read7, command =accionrealizada7)
botonE.grid(row=4,column=0)
botonE.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonF=Button(miFrame7, textvariable=read8, command =accionrealizada8)
botonF.grid(row=4,column=1)
botonF.config(anchor="center",background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))


boton_recomendad=Button(miFrame7, textvariable=read4, command =accionrealizada4)
boton_recomendad.grid(row=1,column=0,columnspan=2)
boton_recomendad.config(anchor="center",background="#45B39D",justify="center",width="16",height="2",fg="black",
	cursor="hand2",font=("helvetica", "14", "bold"))




#Label(miframe8, text="Preflop").grid(row=0,column=0)

botonPreflop=Button(miFrame6, text ="Preflop", command =comenzarPreflop)
#botonPreflop.grid(row=1,column=0,sticky="w",padx=10,pady=10)
botonPostflop=Button(miFrame6, text ="Postflop", command =comenzarPostflop)
#botonPostflop.grid(row=1,column=1,sticky="w",padx=10,pady=10)
botonClear=Button(miFrame6, text ="Clear", command = clear)
#botonClear.grid(row=1,column=2,sticky="w",padx=10,pady=10)


#-------------------------------------------------MiFrame8-----------------------------------------------------

















root.mainloop()