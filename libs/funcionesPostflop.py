import os
import time

def cargarMesa():
	
	#archivo=open("./libs/Datos.txt","r")
	archivo=open("C:/R&JF/libs/Datos.txt","r")
	linea=archivo.readline()
	archivo.close()
	linea=linea.split(",") 
	tipoMesa=linea[0]
	ciegas=linea[1]+"BB"
	posicion=linea[2]
	#archivo=open("./libs/Datos_Calculo.txt","r")
	archivo=open("C:/R&JF/libs/Datos_Calculo.txt","r")
	linea=archivo.readline()
	archivo.close()
	linea=linea.split(",")
	preflopCalculo=linea[0]
	flopCalculo=linea[1]

	return tipoMesa,ciegas,posicion,preflopCalculo,flopCalculo

def introduceCarta():
	archivo=open("C:/R&JF/libs/IntroduceCarta.txt","r")
	linea=archivo.readline()
	archivo.close()
	os.remove("C:/R&JF/libs/IntroduceCarta.txt")
	linea=linea.split(",")
	carta=linea[0]

	return carta

def crearArchivoPostflopHero(vectorAccionesSinAcumular,vector_estrategia,accion_final):

	archivo=open("C:/R&JF/libs/input.txt","w")
	for i in range(len(vectorAccionesSinAcumular)):
		archivo.write(str(vectorAccionesSinAcumular[i])+"="+str(vector_estrategia[i])+"%"+"\n")
	archivo.write("\n\n\n\n\n\n\n")
	archivo.write(accion_final+",\nEND")
	archivo.close()
	
	
def crearArchivoPostflopVill(vectorAccionesSinAcumular):

	archivo=open("C:/R&JF/libs/input.txt","w")
	for i in range(len(vectorAccionesSinAcumular)):
		archivo.write(str(vectorAccionesSinAcumular[i])+"\n")
	archivo.write("END")
	archivo.close()
	

def input_fichero(nombre):

	while not os.path.isfile(nombre):
		time.sleep(0.2)
	f = open(nombre, "r")
	salir = False
	comando = ""
	while not salir:
		linea = f.readline()
		if "FIN" in linea:
			salir = True
			f.close()
		#else:
			#comando=comando+linea
			#comando.rstrip('\n')


def leerArchivoVill():
	archivo=open("C:/R&JF/libs/output.txt","r")
	linea=archivo.readline()
	linea=linea.split("\n")
	archivo.close()
	os.remove("C:/R&JF/libs/output.txt")
	return linea[0]

def leerArchivoHero():
	archivo=open("C:/R&JF/libs/output.txt","r")
	linea=archivo.readline()
	linea=linea.split("=")
	linea=linea[0].split("\n")
	archivo.close()
	os.remove("C:/R&JF/libs/output.txt")
	return linea[0]


#tipoMesa,ciegas,posicion,preflopCalculo,flopCalculo=cargarMesa()
#print("Tipo mesa: "+tipoMesa+"\nCiegas: "+ciegas+"\nPosicion: "+posicion
#	+"\nPreflop: "+preflopCalculo+"\nFlop Calculo: "+flopCalculo)
