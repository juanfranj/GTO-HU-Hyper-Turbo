import os
from os import scandir
import random
import re
from time import time, sleep

def ls_dir(ruta = os.getcwd()):

    return [arch.name for arch in scandir(ruta) if arch.is_dir()]

def ls_files(ruta = os.getcwd()):

    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def buscarArchivo(Grupo_ciegas):

	os.chdir("C:/R&JF/utilidades")
	path=os.getcwd()
	path=path+"/"+"libs"+"/"+"Preflop"+"/"+Grupo_ciegas+"BB"
	os.chdir(path)
	
	return path

def accionesFinales(files,Preflop_cambiado):

	Acciones_porcentaje=[]
	for i in range(len(files)):
		archivo=files[i]
		porcentaje=accionesPorcentaje(archivo,Preflop_cambiado)
		Acciones_porcentaje.append(porcentaje)
	return Acciones_porcentaje

def accionesPorcentaje(file,Preflop_cambiado):
	
	f=open(file,"r")
	linea=f.readline()
	linea_=linea.split(",")
	f.close()
	posicion=[]
	encontrada=False
	for buscar in range(3):

		for i in range(len(linea_)):
			salir=re.match(Preflop_cambiado,linea_[i])
			if salir != None:
				posicion.append(i)
				#print(linea_[posicion[0]])
				mano_string=''.join(linea_[i])
				encontrada=True
				break
		if len(posicion)==0:
			Preflop_cambiado=Preflop_cambiado[0]+Preflop_cambiado[1]+"[^so]"
			#print(Preflop_cambiado)
		if buscar==1 and encontrada==False:
			Preflop_cambiado=Preflop_cambiado[0]+Preflop_cambiado[1]+"$"
			#print(Preflop_cambiado)
		if buscar==2 and encontrada==False:
			posicion.append(None)
			porcentaje=0
		if encontrada==True:
			break

	if posicion[0]!=None:
		buscar=re.search(":",linea_[posicion[0]])
		if buscar == None:
			porcentaje=1
		else:
			mano_=linea_[posicion[0]].split(":")
			porcentaje=mano_[1]

	return porcentaje

def escribirArchivo(acciones,Acciones_porcentaje,mano,path):
	total=0
	try:
		for i in range(len(Acciones_porcentaje)):
			total=total+float(Acciones_porcentaje[i])
		
		if (float(total)<1.0 and float(total)>0.0) or float(total)>1.0:
			
			try:
				f=open("C:/R&JF/utilidades/Errores.txt","a")
			except PermissionError:
				f=open("C:/R&JF/utilidades/Errores.txt","a")
				print("Error abriendo archivo Error: ")

			f.write(path+"\n")
			f.write(mano+": ")
			for i in range(len(acciones)):
				a=str(float(Acciones_porcentaje[i])*100)
				f.write(acciones[i]+":"+a+"%"+" ")
			f.write("TOTAL: "+str(float(total)*100)+"\n\n")
			f.close()

	except IndexError:
			print("error: Acciones porcentaje vacio")
			total=1.2

	#while not open("C:/R&JF/utilidades/Datos Porcentajes.txt","a"):
		#print("No existe el archivo")
		#sleep(1)
	
	try:
		#sleep(0.01)
		f=open("C:/R&JF/utilidades/Datos Porcentajes.txt","a")
	except PermissionError:
		f=open("C:/R&JF/utilidades/Datos Porcentajes.txt","a")
		print("error entrando en el archivo, permiso denegado:\n"+mano+"\n"+path)
		#mano="ERROR"

	f.write(mano+": ")
	for i in range(len(acciones)):
		try:
			a=str(float(Acciones_porcentaje[i])*100)
		except IndexError:
			print("error Acciones porcentaje 2",mano)
			a="ERROR"
			
		f.write(acciones[i]+":"+a+"%"+" ")
	f.write("TOTAL: "+str(float(total)*100)+"\n")
	f.close()
	
	
	

def rangoManos():

	f=open("C:/R&JF/utilidades/libs/manosPreflop.txt","r")
	linea=f.readline()
	manos=linea.split(",")
	f.close()
	manosPrueba=["AA","53o","K6o","76s"]
	return manos

def buscarManos(manos,files,acciones,path):

	os.chdir(path)

	for j in range(len(manos)):
			
		Acciones_porcentaje=accionesFinales(files,manos[j])
		escribirArchivo(acciones,Acciones_porcentaje,manos[j],path)

def abriArchivo():
	#sleep(.30)
	try:
		f=open("C:/R&JF/utilidades/Datos Porcentajes.txt","a")
	except PermissionError:
		f=open("C:/R&JF/utilidades/Datos Porcentajes.txt","a")

	return f

def comprobarPreflop():
	f=open("C:/R&JF/utilidades/Errores.txt","w")
	f.close()
	f=open("C:/R&JF/utilidades/Datos Porcentajes.txt","w")
	f.close()
	Grupo_ciegas=["25","22","19","16","13","10","8","6"]
	manos=rangoManos()

	for i in range(len(Grupo_ciegas)):
		
		f=abriArchivo()
		f.write("\n---------------------------"+Grupo_ciegas[i]+"BB--------------------------------------------------------------------\n\n")
		path=buscarArchivo(Grupo_ciegas[i])
		acciones=ls_dir(path)
		files=ls_files(path)
		f.write(path+"\n\n")
		f.close()
		buscarManos(manos,files,acciones,path)

		f=abriArchivo()		
		pathLimp=path+"/"+"LIMP"
		f.write("\n\n"+pathLimp+"\n\n")
		acciones=ls_dir(pathLimp)
		files=ls_files(pathLimp)
		f.close()
		buscarManos(manos,files,acciones,pathLimp)

		f=abriArchivo()		
		pathLimpAI=pathLimp+"/"+"AI"
		f.write("\n\n"+pathLimpAI+"\n\n")
		acciones=ls_dir(pathLimpAI)
		files=ls_files(pathLimpAI)
		f.close()
		buscarManos(manos,files,acciones,pathLimpAI)

		f=abriArchivo()		
		pathLimpRaise=pathLimp+"/"+"RAISE"
		f.write("\n\n"+pathLimpRaise+"\n\n")
		acciones=ls_dir(pathLimpRaise)
		files=ls_files(pathLimpRaise)
		f.close()
		buscarManos(manos,files,acciones,pathLimpRaise)

		f=abriArchivo()		
		pathLimpRaiseAI=pathLimpRaise+"/"+"AI"
		f.write("\n\n"+pathLimpRaiseAI+"\n\n")
		acciones=ls_dir(pathLimpRaiseAI)
		files=ls_files(pathLimpRaiseAI)
		f.close()
		buscarManos(manos,files,acciones,pathLimpRaiseAI)

		f=abriArchivo()		
		pathOR=path+"/"+"OR"
		f.write("\n\n"+pathOR+"\n\n")
		acciones=ls_dir(pathOR)
		files=ls_files(pathOR)
		f.close()
		buscarManos(manos,files,acciones,pathOR)

		f=abriArchivo()		
		pathOR3BAI=pathOR+"/"+"3BAI"
		f.write("\n\n"+pathOR3BAI+"\n\n")
		acciones=ls_dir(pathOR3BAI)
		files=ls_files(pathOR3BAI)
		f.close()
		buscarManos(manos,files,acciones,pathOR3BAI)

		f=abriArchivo()		
		pathOR3BNAI=pathOR+"/"+"3BNAI"
		f.write("\n\n"+pathOR3BNAI+"\n\n")
		acciones=ls_dir(pathOR3BNAI)
		files=ls_files(pathOR3BNAI)
		f.close()
		buscarManos(manos,files,acciones,pathOR3BNAI)

		f=abriArchivo()		
		pathOR3BNAIAI=pathOR3BNAI+"/"+"AI"
		f.write("\n\n"+pathOR3BNAIAI+"\n\n")
		acciones=ls_dir(pathOR3BNAIAI)
		files=ls_files(pathOR3BNAIAI)
		f.close()
		buscarManos(manos,files,acciones,pathOR3BNAIAI)

		f=abriArchivo()		
		pathOS=path+"/"+"OS"
		f.write("\n\n"+pathOS+"\n\n")
		acciones=ls_dir(pathOS)
		files=ls_files(pathOS)
		f.close()
		buscarManos(manos,files,acciones,pathOS)

comprobarPreflop()
