import os
from os import scandir
import time
import random
import re
from libs.funcionesJuegoPostflop import *
#from repartir_cartas import *
#from practicapreflop import *

#--------------------------------Funciones--------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

#Devuelve los directorios de la carpta, que basicamente son las acciones
def preflopcambiado(cartas,Palos_reales,Palos_cambiados):

	Preflop_calculo=""
	for i in range(4):	

		if i%2 ==0:
			Preflop_calculo=Preflop_calculo+cartas[i]
		else:
			Palo_Preflop=cartas[i]
			a=Palos_reales.index(Palo_Preflop)
			Palo_Preflop_Calculo=Palos_cambiados[a]
			Preflop_calculo=Preflop_calculo+Palo_Preflop_Calculo

	return Preflop_calculo


def ciegasCalculo(Ciegas_reales):

	Grupo_ciegas=["25","22","19","16","13","10","8","6","0"]
	Ciegas_calculo=""
	
	for i in range(len(Grupo_ciegas)):

		if int(Ciegas_reales)<=0:
			Ciegas_calculo="25"
			break

		elif Ciegas_reales==Grupo_ciegas[i]:

			Ciegas_calculo=Ciegas_calculo+Grupo_ciegas[i]
			break
		
		elif int(Ciegas_reales)<int(Grupo_ciegas[i]) and int(Ciegas_reales)>int(Grupo_ciegas[i+1]):

			Ciegas_calculo=Ciegas_calculo+Grupo_ciegas[i]
			break

	return Ciegas_calculo

#Busca los archivos y directorios que existen en el path
def ls_dir(ruta = os.getcwd()):

    return [arch.name for arch in scandir(ruta) if arch.is_dir()]

def ls_files(ruta = os.getcwd()):

    return [arch.name for arch in scandir(ruta) if arch.is_file()]


#Defino la funcion para realiar la accion.

def actuar_Hero_crear(acciones,Acciones_porcentaje):
	accion=""
	accion_recomendada=""
	print("Acciones a realizar: ", end="")
	for i in range(len(acciones)):
		a=float(Acciones_porcentaje[i])*100
		print(acciones[i]+":",int(a),"%", end=" ")
	#Calculo de la accion recomendada
	vector_acciones=""
	for i in range(len(acciones)):
		a=float(Acciones_porcentaje[i])*100	
		b=acciones[i]+" "
		vector=int(a)*b
		vector_acciones=vector_acciones+vector
	vector_acciones=vector_acciones.split()
	x=random.randrange(100)
	accion_recomendada=vector_acciones[x]

	crearArchivo(acciones,Acciones_porcentaje, accion_recomendada)
	esperarinput("C:/R&JF/libs/input.txt")
	#######################################################
	#print()
	#print("La accion recomendada es: ", accion_recomendada)
	#accion=input("La accion a realizar es: ")

def actuar_Hero(accion,fin):
	
	accion=leerAccion()
	if accion=="CALL" or accion=="FOLD" or accion=="CHECK":
		fin=True
	#print("El comando fin sera: ",fin)
	#print("La accion será: ", accion, len(accion), len("FOLD"))
	return accion,fin

def leerAccion():

	archivo=open("C:/R&JF/libs/output.txt","r")
	lineas=archivo.readlines()
	linea=lineas[0].split()
	archivo.close()
	accion=''.join(linea[0])
	archivo.close()
	os.remove("C:/R&JF/libs/output.txt")
	#print(accion, type(accion))
	return accion

def crearArchivo(acciones,Acciones_porcentaje,accion_recomendada):
	
	#print("\ncreando el archivo")
	archivo=open("C:/R&JF/libs/input.txt","w")

	for i in range(len(acciones)):
		a=int(float(Acciones_porcentaje[i])*100)
		a=str(a)
		archivo.write(acciones[i]+" "+a+"%\n")
		#archivo.write(int(a))

	archivo.write("\n\n\n\n\n"+accion_recomendada+",\nEND")

	archivo.close()

def crearArchivo_villano(acciones):
	#print("\ncreando el archivo villano")
	archivo=open("C:/R&JF/libs/input.txt","w")

	for i in range(len(acciones)):
		archivo.write(acciones[i]+"\n")
		#if i==len(acciones):
			#archivo.write(acciones[i]+" END")
		
	archivo.write("END")
	archivo.close()

def crearInputFinal():
	archivo=open("C:/R&JF/libs/input.txt","w")
	archivo.write("END")
	archivo.close()


def archivoTipoBote(tipo_bote):
	archivo=open("C:/R&JF/libs/tipoBote.txt","a")
	archivo.write(tipo_bote+" POT")
	archivo.close()

def esperarinput(nombre):
	while not os.path.isfile(nombre):
		sleep(0.2)
	f = open(nombre, "r")
	salir = False
	comando = ""
	while not salir:
		#print("esperando input preflop")
		linea = f.readline()
		if "END" in linea:
			salir = True
			f.close()
	#print("input preflop creado")

#Manera de actuar del villano--------------------------------	

def actuar_villano(acciones,fin):
	nombre="C:/R&JF/libs/output.txt"
	accion=""
	print("Acciones a realizar: ")
	for i in range(len(acciones)):
		print(acciones[i]+" ", end="")
	print("La accion a realizar es:\n ")
	crearArchivo_villano(acciones)
	esperarinput("C:/R&JF/libs/input.txt")
	#print("archivo acciones creado")
	input_fichero(nombre)
	accion=leerAccion()

	if accion=="CALL" or accion=="FOLD" or accion=="CHECK":
		fin=True
	return accion,fin

#Buesca el archivo donde estoy para ver las acciones

def buscarArchivo(accion,Ciegas_calculo):

	if accion=="":

		os.chdir("C:/R&JF/")
		path=os.getcwd()
		path=path+"/"+"libs"+"/"+"Preflop"+"/"+Ciegas_calculo+"BB"
		os.chdir(path)
	
	else:

		
		path=os.getcwd()
		path=path+"/"+accion
		os.chdir(path)


	return path

def conversionPreflop(Preflop):
	Preflop=ordenaPreflop(Preflop)
	Preflop_cambiado=""
	if Preflop[0]==Preflop[2]:
		Preflop_cambiado=Preflop[0]+Preflop[2]
	elif Preflop[1]==Preflop[3]:
		Preflop_cambiado=Preflop[0]+Preflop[2]+"s"
	else:
		Preflop_cambiado=Preflop[0]+Preflop[2]+"o"

	return Preflop_cambiado

def ordenaPreflop(cartas):
	lista_cartas=[]
	cartas_ordenadas=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
	cartas_preflop_ordenadas=[]

	for i in range(len(cartas)):
		a=cartas[i]
		lista_cartas.append(a)

	if cartas_ordenadas.index(lista_cartas[0]) < cartas_ordenadas.index(lista_cartas[2]):
		cartas_preflop_ordenadas=lista_cartas

	else: 
		lista_cartas[0], lista_cartas[2] = lista_cartas[2], lista_cartas[0]
		lista_cartas[1], lista_cartas[3] = lista_cartas[3], lista_cartas[1]
		cartas_preflop_ordenadas=lista_cartas
	cartas_preflop_ordenadas = ''.join(cartas_preflop_ordenadas)
	return cartas_preflop_ordenadas

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
#-------------------------------------------------------------------
#-------------------------------------------------------------------
def input_fichero(nombre):

	while not os.path.isfile(nombre):
		#print("input_fichero no creado")
		sleep(0.2)
	f = open(nombre, "r")
	salir = False
	comando = ""
	while not salir:
		#print("fichero creado")
	
		linea = f.readline()
		#lineas = f.readlines()
		
		if "FIN" in linea:
			salir = True
						
	#print(comando,type(comando),len(comando))			
	#return comando

def datosPostflop(tipo_bote,ciegas,posicion,cartasPreflop):
	if tipo_bote=="RAISE":
		tipo_bote="ISO"
	archivo=open("C:/R&JF/libs/Datos.txt","w")
	archivo.write(tipo_bote+","+ciegas+","+posicion)
	archivo.close()
	return tipo_bote

def crearInputFinalPreflop():
	archivo=open("C:/R&JF/libs/input.txt","w")
	archivo.write("Villano\nHero\nSplit")
	archivo.close()

def crearGanador():
	#Espero el archivo output=nombre y lo borro
	nombre="C:/R&JF/libs/output.txt"
	input_fichero(nombre)
	archivo=open(nombre,"r")
	ganador=archivo.readline()
	archivo.close()
	os.remove(nombre)
	#creo el archivo ganador y el input con el end para que salga del bucle
	archivo=open("C:/R&JF/libs/ganador.txt","w")
	archivo.write(ganador+"END")
	archivo.close()
	archivo=open("C:/R&JF/libs/input.txt","w")
	archivo.write("END")
	
def analizarTipoBote(tipo_bote,boteOOP,boteIP,posicion):
	archivo=open("C:/R&JF/libs/contadorCiegas.txt","r")
	lineas=archivo.readlines()
	stack_Villano=lineas[0].replace("\n","")
	stack_Hero=lineas[1].replace("\n","")
	archivo.close()

	if tipo_bote=="AI" or tipo_bote=="OS" or tipo_bote=="3BAI" or tipo_bote=="FOLD":
		if boteOOP==0:
			boteOOP="10"
		if boteIP==0:
			boteIP="5"

		archivoTurno("El ganador es:")
		crearInputFinalPreflop()
		crearGanador()
		esperarinput("C:/R&JF/libs/ganador.txt")
		archivo=open("C:/R&JF/libs/ganador.txt","r")
		files=archivo.readlines()
		ganador=files[0].replace("\n","")

		if int(boteIP)>int(boteOOP):
			bote=boteOOP
		else:
			bote=boteIP

		if ganador=="Hero":
			stack_Hero=str(int(stack_Hero)+int(bote))
			stack_Villano=str(int(stack_Villano)-int(bote))
		elif ganador=="Split":
			stack_Hero=str(int(stack_Hero))
			stack_Villano=str(int(stack_Villano))
		else:
			stack_Hero=str(int(stack_Hero)-int(bote))
			stack_Villano=str(int(stack_Villano)+int(bote))

		if int(stack_Hero)>int(stack_Villano):
			stackEfectivo=stack_Villano
		else:
			stackEfectivo=stack_Hero

		archivo=open("C:/R&JF/libs/contadorCiegas.txt","w")
		archivo.write(stack_Villano+"\n"+stack_Hero+"\n"+stackEfectivo+"\nEND")
		archivo.close()	


		return "Mano Finalizada"
	else:
		if posicion=="IP":
			stack_Hero=str(int(stack_Hero)-int(boteIP))
			stack_Villano=str(int(stack_Villano)-int(boteOOP))
		elif posicion=="OOP":
			stack_Hero=str(int(stack_Hero)-int(boteOOP))
			stack_Villano=str(int(stack_Villano)-int(boteIP))
		
		if int(stack_Hero)>int(stack_Villano):
			stackEfectivo=stack_Villano
		else:
			stackEfectivo=stack_Hero

		archivo=open("C:/R&JF/libs/contadorCiegas.txt","w")
		archivo.write(stack_Villano+"\n"+stack_Hero+"\n"+stackEfectivo+"\nEND")
		archivo.close()
		crearInputFinal()

		return "Introduce Flop"

def calculoStackefectivoPreflop(posicion,tipo_bote):

	archivo=open("C:/R&JF/libs/contadorCiegas.txt","r")
	lineas=archivo.readlines()
	stack_Villano=lineas[0]
	stack_Hero=lineas[1]
	stackEfectivo=lineas[2]
	#Hero="IP"
	boteIP=0
	boteOOP=0
	#tipo_bote=['LIMP','RAISE','AI','FOLD']
	
	for i in range(len(tipo_bote)):
		if i%2 == 0:
			if tipo_bote[i]=="OR":
				boteIP=boteIP+20
			elif tipo_bote[i]=="LIMP":
				boteIP=boteIP+10
			elif tipo_bote[i]=="RAISE":
				boteIP=boteIP+30
			elif tipo_bote[i]=="3BNAI":
				boteIP=boteIP+50
			elif tipo_bote[i]=="CALL" or tipo_bote[i]=="CHECK":
				boteIP=boteOOP
			elif tipo_bote[i]=="AI":
				boteIP=boteIP+int(stackEfectivo)
			elif tipo_bote[i]=="OS":
				boteIP=boteIP+int(stackEfectivo)
			elif tipo_bote[i]=="3BAI":
				boteIP=boteIP+int(stackEfectivo)

		else:
			if tipo_bote[i]=="OR":
				boteOOP=boteOOP+20
			elif tipo_bote[i]=="LIMP":
				boteOOP=boteOOP+10
			elif tipo_bote[i]=="RAISE":
				boteOOP=boteOOP+30
			elif tipo_bote[i]=="3BNAI":
				boteOOP=boteOOP+50
			elif tipo_bote[i]=="CALL" or tipo_bote[i]=="CHECK":
				boteOOP=boteIP
			elif tipo_bote[i]=="AI":
				boteOOP=boteOOP+int(stackEfectivo)
			elif tipo_bote[i]=="OS":
				boteOOP=boteOOP+int(stackEfectivo)
			elif tipo_bote[i]=="3BAI":
				boteOOP=boteOOP+int(stackEfectivo)
	
	if posicion=="IP":
		bote=boteOOP
	else:
		bote=boteIP
	
	#print(boteOOP,boteIP)
	return boteOOP,boteIP


def juegoPreflop(ciegas,posicion,cartasPreflop):
	nombre="C:/R&JF/libs/output.txt"
	nombre_input="C:/R&JF/libs/input.txt"
	
	try:
		os.remove(nombre)
		os.remove(nombre_input)

	except FileNotFoundError:
		pass
	

	Ciegas_reales=ciegas
	posicion_hero=posicion
	accion=""
	tipo_bote=[]
	Preflop=cartasPreflop
	fin=False
	#Establezco el numero de ciegas que debo buscar
	Ciegas_calculo=ciegasCalculo(Ciegas_reales)
	#Busco la carpeta donde tengo que empezar la accion
	path=buscarArchivo(accion,Ciegas_calculo)
	#Convierto mi carta preflop para buscarla , ya sea suit, off o pareja
	Preflop_cambiado=conversionPreflop(Preflop)
	#Empieza el juego Preflop#########################################
	if posicion_hero =="IP":

		while fin == False:

			acciones=ls_dir(path)
			files=ls_files(path)
			
			Acciones_porcentaje=accionesFinales(files,Preflop_cambiado)
			actuar_Hero_crear(acciones,Acciones_porcentaje)
			archivoTurno("Turno Hero")
			input_fichero(nombre)
			#la GUI lee el fichero, mientras esta esperando
			#codigo para continuar.
			accion,fin=actuar_Hero(accion,fin)
			tipo_bote.append(accion)
			if fin==True:
				break
			path=buscarArchivo(accion,Ciegas_calculo)
			
			acciones=ls_dir(path)
			archivoTurno("Turno Villano")
			accion,fin=actuar_villano(acciones,fin)
			tipo_bote.append(accion)
			if fin==True:
				break
			path=buscarArchivo(accion,Ciegas_calculo)
			
			
	else:

		while fin == False:

			acciones=ls_dir(path)
			archivoTurno("Turno Villano")
			accion,fin=actuar_villano(acciones,fin)
			tipo_bote.append(accion)
			if fin==True:
				break
			path=buscarArchivo(accion,Ciegas_calculo)
			acciones=ls_dir(path)
			files=ls_files(path)
			Acciones_porcentaje=accionesFinales(files,Preflop_cambiado)
			actuar_Hero_crear(acciones,Acciones_porcentaje)
			archivoTurno("Turno Hero")
			input_fichero(nombre)
			accion,fin=actuar_Hero(acciones,fin)
			tipo_bote.append(accion)
			if fin==True:
				break
			path=buscarArchivo(accion,Ciegas_calculo)	
	##################################################################
	#print(tipo_bote)
	#crearInputFinal()
	if len(tipo_bote)==1:
		tipo_bote.append("FOLD")

	#if tipo_bote[-1]=="FOLD" and len(tipo_bote)<=2:
		#tipo_bote=tipo_bote[::-1]
	boteOOP,boteIP=calculoStackefectivoPreflop(posicion,tipo_bote)

	if tipo_bote[-1]=="FOLD":
		tipo_bote[-2]="FOLD"
	
	print(tipo_bote, boteOOP, boteIP)
	tipo_bote=datosPostflop(tipo_bote[-2],ciegas,posicion_hero,Preflop)
	archivoTipoBote(tipo_bote)
	texto=analizarTipoBote(tipo_bote,boteOOP,boteIP,posicion)
	archivoTurno(texto)


	#print("Mano Finalizada\n El tipo de bote es: ",tipo_bote)		#break
		
	#return tipo_bote

#juegoPreflop("25","IP")





