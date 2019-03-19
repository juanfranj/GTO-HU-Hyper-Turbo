import re

def EncontrarFlop(Flop):
	archivo=open("C:/R&JF/libs/Flops.txt","r")
	lineas=archivo.readlines()
	archivo.close()
	buscar=False
	for i in range(len(lineas)):
		if re.search(Flop,lineas[i])!=None:
			buscar=True
			break

	return buscar

def excepcionesFlop(FlopTotal):
	
	for i in range(6):
		if i%2==0:
			doblado=re.findall(FlopTotal[i],FlopTotal)
			if len(doblado)>1:
				#print("mesa doblada")
				FlopTotal=list(FlopTotal)
				posicion=[]
				for i in range(6):
					if re.match(doblado[0],FlopTotal[i])!=None:
						posicion.append(i)
				
				cambio1=FlopTotal[int(posicion[0])+1]
				cambio2=FlopTotal[int(posicion[1])+1]
	
				FlopTotal[int(posicion[0])+1]=cambio2
				FlopTotal[int(posicion[1])+1]=cambio1
				FlopTotal=" ".join(FlopTotal)
				FlopTotal=FlopTotal.replace(" ","")
				break
	
	return FlopTotal

def flopSingulares(FlopTotal):
	FlopSingular=False
	FlopCambiar=FlopTotal
	archivo=open("C:/R&JF/libs/ExcepcionesFlop.txt","r")
	lineas=archivo.readlines()
	archivo.close()
	for i in range(len(lineas)):
		if re.search(FlopTotal,lineas[i])!=None:
			FlopCambiar=lineas[i].split(" ")
			FlopCambiar=FlopCambiar[0]
			FlopCambiar="".join(FlopCambiar)
			FlopSingular=True
			break
		#else:
			#print("No es flop singular")
	return FlopCambiar,FlopSingular	

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
	#print("Preflop:", cartas_preflop_ordenadas )
	return cartas_preflop_ordenadas


def introduce_flop(FlopTotal):

	#print("Introduccion Flop")
	Palos_calculo=["x","x","x"]
	Palos_reales=["s","d","c","h"]
	Palos_cambiados=["s","d","c","h"]
		
	contador=0
	flop=[1,2,3]
	Palos=[1,2,3]
	#Generación del Flop
	for i in [0,2,4]:
		flop[contador]=FlopTotal[i]
		contador=contador+1
	
	#Combierte flop en numerico y lo orcena
	for i in range(3):
		
		if flop[i]==str("A"):
			flop[i]=14
		elif flop[i]==str("K"):
			flop[i]=13
		elif flop[i]==str("Q"):
			flop[i]=12
		elif flop[i]==str("J"):
			flop[i]=11
		elif flop[i]==str("T"):
			flop[i]=10
		elif flop[i]==str("2") or flop[i]==str("3") or flop[i]==str("4") or flop[i]==str("5") or flop[i]==str("6") or flop[i]==str("7") or flop[i]==str("8") or flop[i]==str("9"):
			flop[i]=int(flop[i])
	flop.sort(reverse=True)

	#Lo convierte en texto

	for i in range(3):
		
		if flop[i]==14:
			flop[i]=str("A")
		elif flop[i]==13:
			flop[i]=str("K")
		elif flop[i]==12:
			flop[i]=str("Q")
		elif flop[i]==11:
			flop[i]=str("J")
		elif flop[i]==10:
			flop[i]=str("T")
		elif flop[i]==2 or flop[i]==3 or flop[i]==4 or flop[i]==5 or flop[i]==6 or flop[i]==7 or flop[i]==8 or flop[i]==9:
			flop[i]=str(flop[i])

	#Ordenar palos

	FlopCambio=FlopTotal
	for i in range(3):

		for j in range(6):

			if flop[i]==FlopCambio[j]:
				Palos[i]=FlopCambio[(j+1)]
				FlopCambio=FlopCambio.replace(FlopTotal[j],"X",1)
				#print(f"{i}{j},{flop[0]}{flop[1]}{flop[2]},{FlopTotal},{FlopCambio}",Palos)
				break

	#Cambio primera carta del Flop
	#for i in range(3):
	#	Palos[i]=palos_texto[i]

	if Palos[0]!=str("s"):
		a=Palos_reales.index(Palos[0])
		Palos_cambiados[a]="s"
		Palos_cambiados[0]=Palos[0]
		Palos_calculo[0]="s"
	else:
		Palos_calculo[0]="s"

	#Cambio de la segunda carta del flop

	if Palos[0]==str("s") and Palos[1]==str("s"):
		Palos_calculo[1]="s"

	elif Palos[0]==str("s") and Palos[1]==str("d"):
		Palos_calculo[1]="d"

	elif Palos[0]==str("d") and Palos[1]==str("d"):
		Palos_calculo[1]="s"

	elif Palos[0]==str("s") and Palos[1]!=str("d") and Palos[1]!=str("s"):
		Palos_calculo[1]="d"
		a=Palos_reales.index("d")
		Palos_cambiados[a]=Palos[1]
		a=Palos_reales.index(Palos[1])
		Palos_cambiados[a]="d"

	elif Palos[0]!=str("s") and Palos[1]==str("s"):
		Palos_calculo[1]="d"

	elif Palos[0]!=str("s") and Palos[1]==str("d"):
		Palos_calculo[1]="d"

	elif Palos[0]!=str("s") and Palos[1]!=str("s") and Palos[1]!=str("d") and Palos[1]==Palos[0]:
		
		a=Palos_reales.index(Palos[1])
		Palos_calculo[1]=Palos_cambiados[a]

	elif Palos[0]!=str("s") and Palos[1]!=str("s") and Palos[1]!=str("d") and Palos[1]!=Palos[0]:
		
		Palos_calculo[1]="d"
		a=Palos_reales.index("d")
		Palos_cambiados[a]=Palos[1]
		a=Palos_reales.index(Palos[1])
		Palos_cambiados[a]="d"
	#s--s--x
	if Palos[0]==str("s") and Palos[1]==str("s") and Palos[2]==str("s"):
		Palos_calculo[2]="s"
		Palos_cambiados=["s","d","c","h"]
		#print("entra s s s")

	if Palos[0]==str("s") and Palos[1]==str("s") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","d","c","h"]
		#print("entra s s d")

	if Palos[0]==str("s") and Palos[1]==str("s") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","c","d","h"]
		#print("entra s s c")

	if Palos[0]==str("s") and Palos[1]==str("s") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","h","c","d"]
		#print("entra s s c")
	#s--d--x
	if Palos[0]==str("s") and Palos[1]==str("d") and Palos[2]==str("s"):
		Palos_calculo[2]="s"
		Palos_cambiados=["s","d","c","h"]
		#print("entra s d s")

	if Palos[0]==str("s") and Palos[1]==str("d") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","d","c","h"]
		#print("entra s d d")

	if Palos[0]==str("s") and Palos[1]==str("d") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","d","c","h"]
		#print("entra s d c")

	if Palos[0]==str("s") and Palos[1]==str("d") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","d","h","c"]
		#print("entra s d h")

	#s--c--x
	if Palos[0]==str("s") and Palos[1]==str("c") and Palos[2]==str("s"):
		Palos_calculo[2]="s"
		Palos_cambiados=["s","c","d","h"]
		#print("entra s c s")

	if Palos[0]==str("s") and Palos[1]==str("c") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","c","d","h"]
		#print("entra s c d")

	if Palos[0]==str("s") and Palos[1]==str("c") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","c","d","h"]
		#print("entra s c c")

	if Palos[0]==str("s") and Palos[1]==str("c") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","h","d","c"]
		#print("entra s c h")


	#s--h--x
	if Palos[0]==str("s") and Palos[1]==str("h") and Palos[2]==str("s"):
		Palos_calculo[2]="s"
		Palos_cambiados=["s","h","c","d"]
		#print("entra s h s")

	if Palos[0]==str("s") and Palos[1]==str("h") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","c","h","d"]
		#print("entra s h d")

	if Palos[0]==str("s") and Palos[1]==str("h") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["s","h","c","d"]
		#print("entra s h c")


	if Palos[0]==str("s") and Palos[1]==str("h") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["s","h","c","d"]
		#print("entra s h h")

	#!s--s--x

	if Palos[0]==str("c") and Palos[1]==str("s") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","c","s","h"]
		#print("entra en c s s")

	if Palos[0]==str("d") and Palos[1]==str("s") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","s","c","h"]
		#print("entra en d s s")

	if Palos[0]==str("h") and Palos[1]==str("s") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","h","c","s"]
		#print("entra en h s s")

	if Palos[0]==str("c") and Palos[1]==str("s") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","c","s","h"]

	if Palos[0]==str("d") and Palos[1]==str("s") and Palos[2]==str("d"):
		Palos_calculo[2]="s"
		Palos_cambiados=["d","s","c","h"]

	if Palos[0]==str("h") and Palos[1]==str("s") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","c","h","s"]

	if Palos[0]==str("c") and Palos[1]==str("s") and Palos[2]==str("c"):
		Palos_calculo[2]="s"
		Palos_cambiados=["d","c","s","h"]
			
	if Palos[0]==str("c") and Palos[1]==str("s") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","h","s","c"]

	if Palos[0]==str("d") and Palos[1]==str("s") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","s","c","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("s") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","s","h","c"]
			
	if Palos[0]==str("h") and Palos[1]==str("s") and Palos[2]==str("h"):
		Palos_calculo[2]="s"
		Palos_cambiados=["d","h","c","s"]
		print("entra en h s h")

	if Palos[0]==str("h") and Palos[1]==str("s") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["d","h","c","s"]

			
	##!s--d--x

	if Palos[0]==str("c") and Palos[1]==str("d") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","d","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("d") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","s","c","h"]
			
	if Palos[0]==str("h") and Palos[1]==str("d") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","d","h","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("d") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","d","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("d") and Palos[2]==str("d"):
		Palos_calculo[2]="s"
		Palos_cambiados=["d","s","c","h"]
			
	if Palos[0]==str("h") and Palos[1]==str("d") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","d","c","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("d") and Palos[2]==str("c"):
		Palos_calculo[2]="s"
		Palos_cambiados=["c","d","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("d") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","s","d","h"]
			
	if Palos[0]==str("h") and Palos[1]==str("d") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","d","c","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("d") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","d","s","c"]
		#print("dentro")
			
	if Palos[0]==str("d") and Palos[1]==str("d") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","s","c","d"]
			
	if Palos[0]==str("h") and Palos[1]==str("d") and Palos[2]==str("h"):
		Palos_calculo[2]="s"
		Palos_cambiados=["h","d","c","s"]
			
	##!s--c--x

	if Palos[0]==str("c") and Palos[1]==str("c") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","c","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("c") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","s","d","h"]
			
	if Palos[0]==str("h") and Palos[1]==str("c") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","h","d","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("c") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","d","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("c") and Palos[2]==str("d"):
		Palos_calculo[2]="s"
		Palos_cambiados=["c","s","d","h"]
			
	if Palos[0]==str("h") and Palos[1]==str("c") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","c","d","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("c") and Palos[2]==str("c"):
		Palos_calculo[2]="s"
		Palos_cambiados=["c","d","s","h"]
			
	if Palos[0]==str("d") and Palos[1]==str("c") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","s","d","h"]

	if Palos[0]==str("h") and Palos[1]==str("c") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","c","d","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("c") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","h","s","d"]
			
	if Palos[0]==str("d") and Palos[1]==str("c") and Palos[2]==str("h"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","s","d","c"]
			
	if Palos[0]==str("h") and Palos[1]==str("c") and Palos[2]==str("h"):
		Palos_calculo[2]="s"
		Palos_cambiados=["h","c","d","s"]

##!s--h--x
			
	if Palos[0]==str("c") and Palos[1]==str("h") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","h","s","d"]
			
	if Palos[0]==str("d") and Palos[1]==str("h") and Palos[2]==str("s"):
		Palos_calculo[2]="c"
		Palos_cambiados=["c","s","h","d"]
			
	if Palos[0]==str("h") and Palos[1]==str("h") and Palos[2]==str("s"):
		Palos_calculo[2]="d"
		Palos_cambiados=["d","h","c","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("h") and Palos[2]==str("d"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","c","s","d"]
			
	if Palos[0]==str("d") and Palos[1]==str("h") and Palos[2]==str("d"):
		Palos_calculo[2]="s"
		Palos_cambiados=["h","s","c","d"]
			
	if Palos[0]==str("h") and Palos[1]==str("h") and Palos[2]==str("d"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","d","c","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("h") and Palos[2]==str("c"):
		Palos_calculo[2]="s"
		Palos_cambiados=["c","h","s","d"]
			
	if Palos[0]==str("d") and Palos[1]==str("h") and Palos[2]==str("c"):
		Palos_calculo[2]="c"
		Palos_cambiados=["h","s","c","d"]
			
	if Palos[0]==str("h") and Palos[1]==str("h") and Palos[2]==str("c"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","c","d","s"]
			
	if Palos[0]==str("c") and Palos[1]==str("h") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["c","h","s","d"]
			
	if Palos[0]==str("d") and Palos[1]==str("h") and Palos[2]==str("h"):
		Palos_calculo[2]="d"
		Palos_cambiados=["h","s","c","d"]
			
	if Palos[0]==str("h") and Palos[1]==str("h") and Palos[2]==str("h"):
		Palos_calculo[2]="s"
		Palos_cambiados=["h","d","c","s"]
	
	#--------------------------------Mesa original---------------------
	Mesa_original=""
	for i in range(3):

		Mesa_original=Mesa_original+flop[i]+Palos[i]
		
	#------------------------------Mesa Calculo--------------------------
	Mesa_Calculo=""
	for i in range(3):

		Mesa_Calculo=Mesa_Calculo+flop[i]+Palos_calculo[i]	
	
	buscar=EncontrarFlop(Mesa_Calculo)

	if buscar==True:
		print("Flop Encontrado")
		return Mesa_Calculo, Palos_reales,Palos_cambiados
	else:
		print("Flop No Encontrado")
		Mesa_Calculo,FlopSingular=flopSingulares(Mesa_Calculo)
		
		if FlopSingular==False:
		
			FlopTotal=excepcionesFlop(FlopTotal)
			Mesa_Calculo, Palos_reales,Palos_cambiados=introduce_flop(FlopTotal)
		
		#buscar=EncontrarFlop(Mesa_Calculo)
		#if buscar==True:
		#	pass
			#print("Flop Encontrado")
			#return Mesa_Calculo, Palos_reales,Palos_cambiados
		#else:
		#	print("Flop No Encontrado")
			#if Mesa_Calculo=="JsJdTc":
				#Mesa_Calculo="JdJcTs"

		#return Mesa_Calculo, Palos_reales,Palos_cambiados

	#print(buscar, Mesa_Calculo)
	#print(f"Flop Original: {Mesa_original}\nFlop Calculo: {Mesa_Calculo}")
	#print(f"Palos reales:  {Palos_reales} Palos Cambiados: {Palos_cambiados}")
	#print(f"Palos :  {Palos} Palos Cambiados: {Palos_calculo}")
	return Mesa_Calculo, Palos_reales,Palos_cambiados

def introduce_carta(Carta_original,Palos_reales,Palos_cambiados):
	
	carta=""
	#Carta_original=input("Introduce carta: ")
	Turn_original=Carta_original[0]
	Palo_turn=Carta_original[1]
	a=Palos_reales.index(Palo_turn)
	Palo_turn_Calculo=Palos_cambiados[a]
	carta=Turn_original+Palo_turn_Calculo
	#print(carta,"Palo Original: ",Palo_turn,"Palo cambiado: ",Palo_turn_Calculo)
	return carta




