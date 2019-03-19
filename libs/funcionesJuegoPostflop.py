import os
from libs.Introduccion_cartas import *
from libs.equity import *
from libs.funcionesPostflop import *
import random
import pexpect.popen_spawn
from time import time, sleep
import re

def calculoApuesta(vector_acciones,bet):
	vectorAccionesSinAcumular=[]
	for i in range(len(vector_acciones)):

		if vector_acciones[i]=="c":
			vectorAccionesSinAcumular.append(vector_acciones[i])
		elif vector_acciones[i]=="f":
			vectorAccionesSinAcumular.append(vector_acciones[i])
		else:
			apuesta=vector_acciones[i]
			apuesta=apuesta.replace("b","")
			#bet=int(bet)+int(apuesta)
			vectorAccionesSinAcumular.append("b"+str(int(apuesta)-bet))
	return vectorAccionesSinAcumular

def AccionRecomendada(accion,bet):
	if accion=="c":
			recomendada=accion
	elif accion=="f":
			recomendada=accion
	else:
		apuesta=accion.replace("b","")
		recomendada="b"+str(int(apuesta)-bet)
	return recomendada


def leerAccion(bet,accion,accionAnterior):
	if accion=="c":
		accionActualizada=accion
		if accionAnterior!="c":
			bet=int(accionAnterior.replace("b",""))+bet

	elif accion=="f":
		accionActualizada=accion
	else:
		#if accionAnterior!="c":
		betActualizado=int(accion.replace("b",""))+bet
		accionActualizada="b"+str(betActualizado)
		print("bet actualizado: ",betActualizado,"accion Actualizada: ",accionActualizada)
		#else:
		#	accionActualizada=accion
	return bet, accionActualizada

def llamarPiosolver(name,child):
	while not os.path.isfile(name):
		sleep(0.2)	
	archivo=open(name,"r")
	lines=archivo.readlines()
	archivo.close()
	for i in range(len(lines)):
		lines[i]=lines[i].replace("\n","")
	for i in range(len(lines)):
		child.sendline(lines[i])
def esperarPiosolver(nombre):
	while not os.path.isfile(nombre):
		sleep(0.2)
	f = open(nombre, "r")
	salir = False
	comando = ""
	if nombre!="estrategia.txt":
		while not salir:
			#print("esperando que termine piosolver")
			linea = f.readline()
			if "END" in linea:
				salir = True
				f.close()
	else:
		cont=0
		while not salir:	
			linea = f.readline()
			if "END" in linea:
				if cont==0:
					cont=cont+1
				else:
					#print("archivo extrategia creado, numero de end: ",cont)
					salir = True
					f.close()

	#print("input creado")

def borrarArchivo(nombre):
	try:
		os.remove(nombre)

	except PermissionError:
		print("Pemiso denegado 1 ",nombre)
		sleep(1)
		os.remove(nombre)

def crearArbol(ciegas,tipoMesa,mesa,nodo):
	archivo=open("arbol_.txt","w")
	archivo.write(f"stdoutredi \"arbol.txt\"\nload_tree \"C:\\PioSOLVER\\HU GTO\\{ciegas}\\{tipoMesa}\\{mesa}.cfr\"\n"
		f"show_node {nodo}\nstdoutback")
	archivo.close()

def cargarJuego(nodo,child,nombreCarta):
	
	crearPosicion_(nodo)

	
	llamarPiosolver("posicion_.txt",child)
	esperarPiosolver("posicion.txt")
	borrarArchivo("posicion_.txt")


	Turno,nodo=buscaPosicion("posicion.txt",nodo,nombreCarta,child)
	borrarArchivo("posicion.txt")

	return Turno,nodo

def crearCodigo(nodo):
	archivo=open("codigo.txt","w")
	archivo.write(f"stdoutredi \"estrategia.txt\"\nshow_effective_stack\nshow_children {nodo}\nshow_strategy_pp {nodo}\nstdoutback")
	archivo.close()

def crearPosicion_(nodo):
	archivo=open("posicion_.txt","w")
	archivo.write(f"stdoutredi \"posicion.txt\"\nshow_node {nodo}\nstdoutback")
	archivo.close()

def crearTipo_nodo_(nodo):
	archivo=open("tipo_nodo_.txt","w")
	archivo.write(f"stdoutredi \"tipo_nodo.txt\"\nshow_node {nodo}\nstdoutback")
	archivo.close()

def crearInputFinalPostflop():
	archivo=open("C:/R&JF/libs/input.txt","w")
	archivo.write("Villano\nHero\nSplit")
	archivo.close()

def crearArchivoAccion():
	archivo=open("C:/R&JF/libs/accion.txt","w")
	archivo.close()
	
def crearTipoBote():
	archivo=open("C:/R&JF/libs/tipoBote.txt","w")
	archivo.close()


def buscaPosicion(name,nodo,nombreCarta,child):
	while not os.path.isfile(name):
		sleep(0.2)	

	archivo=open(name,"r")
	lineas=archivo.readlines()
	archivo.close()
	
	posicion=lineas[2]
	if posicion[0]=="O":
		Turno="OOP"
		return Turno,nodo
	elif posicion[0]=="S": #Split pot, y tiene q pedir carta
		borrarArchivo("posicion.txt")
		print("Introduce carta: ")
		archivoTurno("Introduce carta")
		input_fichero(nombreCarta)
		carta=introduceCarta()
		escribirCarta(carta)
		print("La carta introducida es: ",carta)
		nodo=nodo+":"+carta
		crearPosicion_(nodo)	
		llamarPiosolver("posicion_.txt",child)
		esperarPiosolver("posicion.txt")
		borrarArchivo("posicion_.txt")
		archivo=open("posicion.txt","r")
		lineas=archivo.readlines()
		archivo.close()
		#borrarArchivo("posicion.txt")
		posicion=lineas[2]

		if posicion[0]=="O":
			Turno="OOP"
			return Turno,nodo
		else:
			Turno="IP"
			return Turno,nodo	
		
	else:
		Turno="IP"
		return Turno,nodo

def crearEstrategia(Preflop,name,vector_acciones):
	while not os.path.isfile(name):
		sleep(0.2)
	archivo=open(name,"r")
	lineas=archivo.readlines()
	archivo.close()
	#borrarArchivo(name)
	vec_est=[]

	for i in range(len(lineas)):
		if re.match(Preflop,lineas[i])!=None:
			vec_est.append(lineas[i])
#Cnd son parejas, cambia los palos de posicion si no lo encuentra.
	if len(vec_est)==0 and Preflop[0]==Preflop[2]:
		Preflop_=[]
		for i in Preflop:
			Preflop_.append(i)
		a=Preflop_[1]
		b=Preflop_[3]
		Preflop_[1]=b
		Preflop_[3]=a
		Preflop=''.join(Preflop_)
		print("Preflop cambiado",Preflop)
		for i in range(len(lineas)):
			if re.match(Preflop,lineas[i])!=None:
				vec_est.append(lineas[i])

	vec_est[0]=vec_est[0].replace("\n","")
	vec_est=vec_est[0].split()
	vec_est.remove(vec_est[0])
	vector_estrategia=vec_est

	for i in range(len(vector_estrategia)):
		vector_estrategia[i]=round(float(vector_estrategia[i]),2)*100
	#Introduzco la variable fold
	if len(vector_acciones)!=len(vector_estrategia):
		total=sum(vector_estrategia)
		if total>=100:
			f=0
			f=round(f,2)
		else:
			f=100-total
			f=round(f,2)
		vector_estrategia.append(f)
	return vector_estrategia

def archivoAccion(accion):
	archivo=open("C:/R&JF/libs/accion.txt","a")
	archivo.write("|"+accion)
	archivo.close()

def escribirCarta(carta):
	archivo=open("C:/R&JF/libs/accion.txt","a")
	archivo.write("||_"+carta+"_|")
	archivo.close()

def archivoTurno(escribe):
	archivo=open("C:/R&JF/libs/turno.txt","w")
	archivo.write(escribe)
	archivo.close()

def crearGanador(nombre):
	#Espero el archivo output=nombre y lo borro
	input_fichero(nombre)
	archivo=open(nombre,"r")
	ganador=archivo.readline()
	archivo.close()
	os.remove(nombre)
	#creo el archivo ganador y el input con el end para que salga del bucle
	archivo=open("C:/R&JF/libs/ganador.txt","w")
	archivo.write(ganador)
	archivo.close()
	archivo=open("C:/R&JF/libs/input.txt","w")
	archivo.write("END")


def crearAcciones(name,nodo):
	while not os.path.isfile(name):
		sleep(0.2)
	vector_acciones_=[]
	vector_acciones=[]

	archivo=open("estrategia.txt","r")
	lineas=archivo.readlines()
	archivo.close()
		
	#borrarArchivo("estrategia.txt")

	for i in range(len(lineas)):
		if re.match("r:0",lineas[i])!=None:
			vector_acciones_.append(lineas[i])
		if re.match("END",lineas[i])!=None:
			break
	for i in range(len(vector_acciones_)):
		vector_acciones_[i]=vector_acciones_[i].replace("\n","")
		b=vector_acciones_[i]
		a=""
		for j in range(1,10):
				
			if b[-j]!=":":
				a=a+b[-j]
			else:
				a=a[::-1]
				vector_acciones.append(a)
				break

	if vector_acciones[-1]!="f":#Introduzco el fold en las acciones si no existe
		vector_acciones.append("f")
	return vector_acciones

def juegoVillano(vector_acciones,accionAnterior,bet,nombre,nodo):
	

	vectorAccionesSinAcumular=calculoApuesta(vector_acciones,bet)
	print()
	for i in range(len(vector_acciones)):
		print(vectorAccionesSinAcumular[i])
#----------------------------Creo el archivo para que lo lea la app------------------------------
	crearArchivoPostflopVill(vectorAccionesSinAcumular)
#---------------------------Espero a que lea el archivo de la GUI---------------------
	input_fichero(nombre)
	accion=leerArchivoVill()
	accionAnterior.append(accion)
	bet, accion=leerAccion(bet,accion,accionAnterior[-2])
	nodo=nodo+":"+accion

	return bet, accion, accionAnterior, nodo

def juegoHero(vector_acciones,vector_estrategia,accionAnterior,bet,nombre,nodo):
#---------------------Calcula el vector de acciones restando bet
	vectorAccionesSinAcumular=calculoApuesta(vector_acciones,bet)
	print("Las acciones a seguir son:")			
	for i in range(len(vector_acciones)):
		print(vectorAccionesSinAcumular[i],"=",vector_estrategia[i],"%")

#---------------------Calcula la accion con timer------------------------
	b=[" "]
	for i in range(len(vector_acciones)):
		for j in range(int(vector_estrategia[i])):
			if j==0 and len(b)==1:
				b[j]=vector_acciones[i]
			else:
				b.append(vector_acciones[i])       
#---------Si solo se hace fold, se saca el vector fold entero de 100 unidades
	if len(b)<10:
		for i in range(100):
			if i==0:
				b[i]="f"
			else:
				b.append("f")
	aleatorio=random.randrange(100)
	accion_final=b[aleatorio]
	accion_final=AccionRecomendada(accion_final,bet)
#----------------------------Creo el archivo para que lo lea la app------------------------------
	crearArchivoPostflopHero(vectorAccionesSinAcumular,vector_estrategia,accion_final)

	print(f"La accion a realizar es: \n {accion_final}")
#-------------------------Espero a que lea el archivo de la GUI---------------------
	input_fichero(nombre)
	accion=leerArchivoHero()
	accionAnterior.append(accion)
#lee la accion introducidad y debe de sumar el bet existente y actualizar la accion sumando el bet
	bet, accion=leerAccion(bet,accion,accionAnterior[-2])
	nodo=nodo+":"+accion

	return bet, accion, accionAnterior, nodo


def finalMano(nodo,child,accion):
	bote_final=""
	crearTipo_nodo_(nodo)
	llamarPiosolver("tipo_nodo_.txt",child)
	esperarPiosolver("tipo_nodo.txt")
	borrarArchivo("tipo_nodo_.txt")
	archivo=open("tipo_nodo.txt","r")
	lineas=archivo.readlines()
	archivo.close()
	borrarArchivo("tipo_nodo.txt")
	if re.match("END",lineas[2])!=None or accion=="f":
		Mano_finalizada=True
		bote_final=lineas[4]
		bote_final=bote_final.split(" ")
		#print("Detecta final de nodo")
		#input("consultar lineas")
		print("Mano Finalizada")
		return Mano_finalizada, bote_final
	else:
		Mano_finalizada=False
		return Mano_finalizada,bote_final

def esperarInputPostFlop(nombre):
	while not os.path.isfile(nombre):
		sleep(0.2)
	f = open(nombre, "r")
	salir = False
	comando = ""
	while not salir:
		#print("esperando input postflop")
		linea = f.readline()
		if "END" in linea:
			salir = True
			f.close()
	#print("input postflop creado")


def leerganador(Hero):
		
	archivo=open("C:/R&JF/libs/ganador.txt","r")
	ganadorNombre=archivo.readlines()
	ganadorNombre=ganadorNombre[0].replace("\n","")
	archivo.close()

	return ganadorNombre

def calculoStackefectivoPostflop(Hero,bote_final):
	
	#Hero="IP"
	#bote_final=["50","14","20"]
	bote_IP=bote_final[1]
	bote_OOP=bote_final[0]
	archivo=open("C:/R&JF/libs/contadorCiegas.txt","r")
	files=archivo.readlines()
	archivo.close()
	stack_Hero=files[1]
	stack_Villano=files[0]

	ganador=leerganador(Hero)

	if int(bote_IP)>int(bote_OOP):
		bote=bote_OOP
	else:
		bote=bote_IP

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
	print(bote,stack_Villano,stack_Hero,stackEfectivo)

def actuar(accion,nodo,vector_acciones,child):
	if accion=="f":
		print("Fin")
		return nodo
	elif accion=="c":
		nodo=nodo+":"+accion ###Actualizo el nodo
		crearTipo_nodo_(nodo)
		llamarPiosolver("tipo_nodo_.txt",child)
		nodo=buscaNodo("tipo_nodo.txt",nodo)#Busca si es split pot
		return nodo
	else:
		accion=accion.replace("b","")
		accion=int(accion)
		tamaño_apuestas=[0]#desde aqui pegue
		apuesta=0
		contador=1
		for i in range(len(vector_acciones)):
			a=len(vector_acciones[i])
			if a>1:
				b=vector_acciones[i]
				b=b.replace("b","")
				if contador==1:
					tamaño_apuestas[i]=int(b)
					contador=contador+1
				else:
					tamaño_apuestas.append(int(b))
					contador=contador+1
		tamaño_apuestas.sort()
#----------------------------Calculo el stack efectivo para juego raro------
		archivo=open("estrategia.txt","r")
		linea=archivo.readlines()
		archivo.close()
		stack_efectivo=int(linea[1])
		bote=linea[6]
		bote=bote.split(" ")
		bote.remove(bote[0])
		bote.remove(bote[len(bote)-1])
		bote_efectivo=int(bote[0])+int(bote[1])

		for i in range(len(tamaño_apuestas)):

			if len(tamaño_apuestas)>1:

				if i==0:

					if accion>=tamaño_apuestas[i]/2 and accion<=(tamaño_apuestas[i]+tamaño_apuestas[i+1])/2:
						apuesta=tamaño_apuestas[i]
						apuesta="b"+str(apuesta)
						nodo=nodo+":"+apuesta
						break

				elif  i>0 and i<len(tamaño_apuestas)-1:

					if accion>=(tamaño_apuestas[i]+tamaño_apuestas[i-1])/2 and accion<=(tamaño_apuestas[i]+tamaño_apuestas[i+1])/2:
						apuesta=tamaño_apuestas[i]
						apuesta="b"+str(apuesta)
						nodo=nodo+":"+apuesta
						break

				elif i==len(tamaño_apuestas)-1:

					if accion>=(tamaño_apuestas[i]+tamaño_apuestas[i-1])/2 and accion<=tamaño_apuestas[i]*1.5:
						apuesta=tamaño_apuestas[i]
						apuesta="b"+str(apuesta)
						nodo=nodo+":"+apuesta
						break
			if len(tamaño_apuestas)==1:

				if accion>=tamaño_apuestas[i]/2 and accion<=tamaño_apuestas[i]*1.5:
					apuesta=tamaño_apuestas[i]
					apuesta="b"+str(apuesta)
					nodo=nodo+":"+apuesta
					break
		if apuesta==0:

			apuesta=str(tamaño_apuestas[len(tamaño_apuestas)-1])
			finaliza=False
			nodo=nodo+":"+"b"+apuesta
			eq, fuerza_mano, draw_mano, fuerza, draw=equity(Preflop,Hero,mesa,mesa_eq,nodo)
			
			if accion>=stack_efectivo/3 and accion<=stack_efectivo-10:

				if int(eq)<65:
					accion_hero="f"
				if int(eq)>65:
					accion_hero="b"+str(stack_efectivo)
					finaliza=True

			elif accion==stack_efectivo:

				if int(eq)<65:
					accion_hero="f"
				if int(eq)>65:
					accion_hero="c"
					finaliza=True

			elif int(eq)<=50:
				accion_hero="f"

			elif int(eq)>50 and int(eq)<70:
				accion_hero="c"

			elif int(eq)>70:
				accion_hero="b"+str(stack_efectivo)
				finaliza=True		
			print(f"La acción recomendada es: {accion_hero}\nIntroduce la acción: ")
			accion=input("La acción es: ")
			nodo=nodo+":"+accion
			return nodo
					
			print("In your own")