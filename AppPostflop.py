from tkinter import *
from time import time, sleep
from libs.postflopGrafica import *
import _thread
import os

root=Tk()

#---------------Introduco el titulo y el logo del software-------------

#root.iconbitmap("./imagenes/logo.ico")
root.title("R&JF Bomberos")

#---------------------------------Miframe------------------------------

miFrame7=Frame(root)
miFrame7.grid(row=0,column=0,sticky="w")
miFrame7.config(bd=2)
miFrame7.config(relief="groove")

#----------------------------------Variables---------------------------

read=StringVar()
read1=StringVar()
read2=StringVar()
read3=StringVar()
read4=StringVar()
read5=StringVar()
read6=StringVar()
read7=StringVar()
read8=StringVar()

#----------------------------------Funciones---------------------------
def accionrealizada():
	read5.set(read.get())
	crearOutput()
	clear()
def accionrealizada1():
	read5.set(read1.get())
	crearOutput()
	clear()
def accionrealizada2():
	read5.set(read2.get())
	crearOutput()
	clear()
def accionrealizada3():
	read5.set(read3.get())
	crearOutput()
	clear()
def accionrealizada4():
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


def abrirArchivo():
	while not os.path.isfile("C:/R&JF/libs/input.txt"):
		sleep(0.2)
	archivo=open("C:/R&JF/libs/input.txt","r")
	files=archivo.readlines()
	archivo.close()
	os.remove("C:/R&JF/libs/input.txt")
	return files

def crearOutput():
	linea=str(read5.get())
	archivo=open("C:/R&JF/libs/output.txt","w")
	archivo.write(linea+"\nFIN")
	archivo.close()

def seleccionaAccion(files):
	
	try:

		if len(files[0])!=0:
			read.set(files[0])
		if len(files[1])!=0:	
			read1.set(files[1])
		if len(files[2])!=0:
			read2.set(files[2])
		if len(files[3])!=0:
			read3.set(files[3])
		if len(files[4])!=0:
			read7.set(files[4])
		if len(files[5])!=0:
			read8.set(files[5])

		if len(files[-1])!=0 and len(files[-2])==1:
			read4.set(files[-1])
				
				
	except IndexError:
		pass 

def jugarPostflop():
	_thread.start_new_thread(juegoPostflop,())

	while not os.path.isfile("C:/R&JF/libs/input.txt"):
		sleep(0.2)
	fin=False
	while not fin:	
		files=abrirArchivo()
		seleccionaAccion(files)
		#fin=True

def comenzarPostflop():
	_thread.start_new_thread(jugarPostflop,())

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

#---------------------------------Botones------------------------------

botonA=Button(miFrame7, textvariable=read, command =accionrealizada)
botonA.grid(row=2,column=0)
botonA.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonB=Button(miFrame7, textvariable=read1, command =accionrealizada1)
botonB.grid(row=2,column=1)
botonB.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonC=Button(miFrame7, textvariable=read2, command =accionrealizada2)
botonC.grid(row=3,column=0)
botonC.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))


botonD=Button(miFrame7, textvariable=read3, command =accionrealizada3)
botonD.grid(row=3,column=1)
botonD.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonE=Button(miFrame7, textvariable=read7, command =accionrealizada7)
botonE.grid(row=4,column=0)
botonE.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))

botonF=Button(miFrame7, textvariable=read8, command =accionrealizada8)
botonF.grid(row=4,column=1)
botonF.config(background="#F1948A",justify="center",width="10",height="2",fg="black",
	cursor="hand2",font=("helvetica", "11", "bold"))



boton_recomendad=Button(miFrame7, textvariable=read4, command =accionrealizada4)
boton_recomendad.grid(row=1,column=0,columnspan=2)
boton_recomendad.config(background="#45B39D",justify="center",width="16",height="2",fg="black",
	cursor="hand2",font=("helvetica", "14", "bold"))


botonPostflop=Button(miFrame7, text ="Postflop", command =comenzarPostflop)
botonPostflop.grid(row=5,column=0,sticky="w",padx=10,pady=10)
botonClear=Button(miFrame7, text ="Clear", command = clear)
botonClear.grid(row=5,column=1,sticky="w",padx=10,pady=10)


root.mainloop()