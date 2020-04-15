import os
from libs.Introduccion_cartas import *
from libs.equity import *
from libs.funcionesPostflop import *
import random
import pexpect.popen_spawn
from time import time, sleep
from libs.funcionesJuegoPostflop import *
import re


def juegoPostflop():

	os.chdir("C:/PioSOLVER")
	nombre="C:/R&JF/libs/output.txt"
	nombreCarta="C:/R&JF/libs/IntroduceCarta.txt"
	
#----------------------------------variables----------------------------------------------------
	tipoMesa,ciegas,Hero,Preflop,mesa=cargarMesa()
	print("Tipo Mesa: ",tipoMesa,"\nciegas: ",ciegas,"\nPosicion: ",Hero,"\nPreflop: ",Preflop,"\nFlop: ",mesa)
	Turno=""
	mesa_eq=mesa
	Mano_finalizada=False
	nodo="r:0"
	bet=0
	accionAnterior=["0"]
	child=pexpect.popen_spawn.PopenSpawn('c:/piosolver/piosolver-pro.exe')
#----------------------------------Creo el arbol y lo ejecuto------------------------------
	crearArbol(ciegas,tipoMesa,mesa,nodo)
	llamarPiosolver("arbol_.txt",child)
	esperarPiosolver("arbol.txt")
	borrarArchivo("arbol_.txt")
	borrarArchivo("arbol.txt")
	crearArchivoAccion()		
#----------------------------------Juego postflop------------------------------------------------
	while Mano_finalizada==False:
		Turno,nodo=cargarJuego(nodo,child,nombreCarta)
		if Hero==Turno:
			if os.path.isfile("estrategia.txt"):
				borrarArchivo("estrategia.txt")
				#sleep(0.2)
			#print(nodo,accionAnterior)
			print("Hero tiene que actuar")
			archivoTurno("Turno Hero")
			crearCodigo(nodo)
			llamarPiosolver("codigo.txt",child)
			esperarPiosolver("estrategia.txt")
			borrarArchivo("codigo.txt")
			vector_acciones=crearAcciones("estrategia.txt",nodo)
			vector_estrategia=crearEstrategia(Preflop,"estrategia.txt",vector_acciones)
			bet,accion,accionAnterior,nodo=juegoHero(vector_acciones,vector_estrategia,accionAnterior,bet,nombre,nodo)
			archivoAccion(accion)		
		else:
			if os.path.isfile("estrategia.txt"):
				borrarArchivo("estrategia.txt")
			print("Villano tiene que actuar")
			archivoTurno("Turno Villano")
			crearCodigo(nodo)
			llamarPiosolver("codigo.txt",child)
			esperarPiosolver("estrategia.txt")
			borrarArchivo("codigo.txt")
			vector_acciones=crearAcciones("estrategia.txt",nodo)
			bet,accion,accionAnterior,nodo=juegoVillano(vector_acciones,accionAnterior,bet,nombre,nodo)
			archivoAccion(accion)

		Mano_finalizada,bote_final=finalMano(nodo,child,accion)
	
	crearInputFinalPostflop()
	archivoTurno("El ganador es:")
	crearGanador(nombre)
	crearArchivoAccion()
	crearTipoBote()
	calculoStackefectivoPostflop(Hero,bote_final)
	archivoTurno("Mano Finalizada")
	llamarPiosolver("exit.txt",child)

