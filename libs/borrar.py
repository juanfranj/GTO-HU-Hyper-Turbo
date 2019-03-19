import re
def ciegasCalculo(Ciegas_reales):

	Grupo_ciegas=["25","22","19","16","13","10","8","6","0"]
	Ciegas_calculo=""
	
	for i in range(len(Grupo_ciegas)):

		if Ciegas_reales==Grupo_ciegas[i]:

			Ciegas_calculo=Ciegas_calculo+Grupo_ciegas[i]
			break
		
		elif int(Ciegas_reales)<int(Grupo_ciegas[i]) and int(Ciegas_reales)>int(Grupo_ciegas[i+1]):

			Ciegas_calculo=Ciegas_calculo+Grupo_ciegas[i]
			break

	return Ciegas_calculo


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

	if stack_Hero>stack_Villano:
		stackEfectivo=stack_Villano
	else:
		stackEfectivo=stack_Hero

	archivo=open("C:/R&JF/libs/contadorCiegas.txt","w")
	archivo.write(stack_Villano+"\n"+stack_Hero+"\n"+stackEfectivo+"\nEND")
	archivo.close()
	print(bote,stack_Villano,stack_Hero,stackEfectivo)

def calculoStackefectivoPreflop(Hero):

	archivo=open("C:/R&JF/libs/contadorCiegas.txt","r")
	lineas=archivo.readlines()
	stack_Villano=lineas[0]
	stack_Hero=lineas[1]
	stackEfectivo=lineas[2]
	#Hero="IP"
	boteIP=0
	boteOOP=0
	tipo_bote=['LIMP','RAISE','AI','FOLD']
	
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
			elif tipo_bote[i]=="CALL":
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
			elif tipo_bote[i]=="CALL":
				boteOOP=boteIP
			elif tipo_bote[i]=="AI":
				boteOOP=boteOOP+int(stackEfectivo)
			elif tipo_bote[i]=="OS":
				boteOOP=boteOOP+int(stackEfectivo)
			elif tipo_bote[i]=="3BAI":
				boteOOP=boteOOP+int(stackEfectivo)
	
	if boteIP>boteOOP:
		bote=boteOOP
	else:
		bote=boteIP
	
	print(boteIP,boteOOP)
	return bote

#calculoStackefectivoPreflop()
#calculoStackefectivoPostflop()

def CrearFlop():
	archivo=open("C:/R&JF/libs/1755Flops.txt","r")
	files=archivo.readlines()
	archivo.close()
	archivo=open("C:/R&JF/libs/Flops.txt","w")
	for i in range(len(files)):
		file=files[i].split(":")
		archivo.write(file[0]+"\n")
	archivo.close()
	archivo=open("C:/R&JF/libs/Flops.txt","r")
	files=archivo.readlines()
	archivo.close()
	print(f"El numero de Flops es {len(files)}")

#CrearFlop()

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
				print("mesa doblada")
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
	
	

def CrearFlopSin():
	archivo=open("C:/R&JF/libs/Flops.txt","r")
	files=archivo.readlines()
	archivo.close()
	archivo=open("C:/R&JF/libs/FlopsSin.txt","w")
	for i in range(len(files)):
		file=files[i].split("\n")
		file=file[0]
		if file[1]!="s" or (file[3]!="s" and file[3]!="d") or file[5]=="h":
			archivo.write(file+"\n")
	archivo.close()
	archivo=open("C:/R&JF/libs/FlopsSin.txt","r")
	files=archivo.readlines()
	archivo.close()
	print(f"El numero de Flops es {len(files)}")
	

Flop="AsTd6c"	
FlopTotal=flopSingulares(Flop)
print(FlopTotal)





		



