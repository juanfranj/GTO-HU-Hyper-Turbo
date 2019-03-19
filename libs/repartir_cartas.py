import random
#from Introduccion_cartas import *

def repartirCartas():
	#Abro el fichero con todas las cartas y las paso a una lista
	fichero=open("cartas.txt","r")
	lineas=fichero.readlines()
	cartas_baraja=lineas[0].split()
	fichero.close()
	#Se reparten las cartas preflop a los dos jugadores
	cont=52
	cartas_flop=""
	cartas_Hero=""
	cartas_Villano=""

	#Reparto las cartas Preflop a Hero y Villano
	for i in range(4):
	    
	    if i % 2 ==0:

		    x=random.randrange(cont)
		    cartas_Hero=cartas_Hero+cartas_baraja[x]
		    cartas_baraja.remove(cartas_baraja[x])
		    cont=cont-1

	    else:

	        
	        x=random.randrange(cont)
	        cartas_Villano=cartas_Villano+cartas_baraja[x]
	        cartas_baraja.remove(cartas_baraja[x])
	        cont=cont-1

	#print(" Cartas Hero:",cartas_Hero,"\n","Cartas Villano: ", cartas_Villano)

	#Ordeno las cartas Preflop
	#cartas_Hero=ordenaPreflop(cartas_Hero)
	#cartas_Villano=ordenaPreflop(cartas_Villano)

	#Solicito las cartas Flop

	Flop=""
	for i in range(3):
	    
		x=random.randrange(cont)
		Flop=Flop+cartas_baraja[x]
		cartas_baraja.remove(cartas_baraja[x])
		cont=cont-1

	return cartas_Hero, cartas_Villano, Flop

def CiegasPosicion():

	ciegas=str(random.randrange(1,26))
	posicion=["IP","OOP"]
	x=random.randrange(2)
	posicion=posicion[x]

	return ciegas,posicion


cartas_Hero,cartas_Villano,Flop=repartirCartas()
print(" Cartas Hero:",cartas_Hero,"\n","Cartas Villano: ", cartas_Villano, "\n","Flop: ",Flop)
ciegas,posicion=CiegasPosicion()
print("Ciegas: "+ciegas+" Posicion: "+posicion)


	