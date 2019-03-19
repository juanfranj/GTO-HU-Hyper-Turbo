def equity(Preflop,Hero,mesa,mesa_eq,nodo):

	import os
	import subprocess
	

	#Creo la mesa_fuerza para poder calcular la equity
	
	mesa_borrar=list(mesa_eq)
	mesa_fuerza=""

	for i in range(3):
		mesa_fuerza=mesa_fuerza+mesa_borrar[0]
		del mesa_borrar[0]
		mesa_fuerza=mesa_fuerza+mesa_borrar[0]
		del mesa_borrar[0]
		mesa_fuerza=mesa_fuerza+" "

	os.chdir("C:\PioSOLVER")
	#Creo los archivos de lectura de manos y de equity
	archivo=open("hands_.txt","w")
	archivo=archivo.write(f"load_tree \"C:\\PioSOLVER\\HU GTO\\25BB\\OR\\{mesa}.cfr\"\n"
	f"stdoutredi \"hands.txt\"\nshow_hand_order\nstdoutback\nexit")

	archivo=open("equity_.txt","w")
	archivo=archivo.write(f"load_tree \"C:\\PioSOLVER\\HU GTO\\25BB\\OR\\{mesa}.cfr\"\n"
	f"stdoutredi \"equity.txt\"\ncalc_eq_node {Hero} {nodo}\nstdoutback\nexit")

	archivo=open("categorias_.txt","w")
	archivo=archivo.write(f"load_tree \"C:\\PioSOLVER\\HU GTO\\25BB\\OR\\{mesa}.cfr\"\n"
	f"stdoutredi \"categorias.txt\"\nshow_category_names\nstdoutback\nexit")

	archivo=open("fuerza_.txt","w")
	archivo=archivo.write(f"load_tree \"C:\\PioSOLVER\\HU GTO\\25BB\\OR\\{mesa}.cfr\"\n"
	f"stdoutredi \"fuerza.txt\"\nshow_categories {mesa_fuerza}\nstdoutback\nexit")
	 
	#carga el archivo manos,equity,categorias
	#subprocess.run(["piosolver-pro.exe","hands_.txt","categorias_.txt"])
	#subprocess.run(["piosolver-pro.exe","categorias_.txt"])
	subprocess.run(["piosolver-pro.exe","fuerza_.txt"])
	subprocess.run(["piosolver-pro.exe","equity_.txt"])
	#leo el archivo hands y calculo la posicion de la mano
	archivo=open("hands.txt","r")
	lineas=archivo.readlines()
	lineas.remove(lineas[0])
	lineas=lineas[0]
	lineas=lineas.split()
	try: 
		a=lineas.index(Preflop)
	except ValueError:
		a=0
	if a==0:
		equity=0
		fuerza_mano=0
		draw_mano=0
		fuerza_=0
		draw_=0

	else:
		#leo equity para consultar la equity de la mano
		archivo=open("equity.txt","r")
		lineas=archivo.readlines()
		lineas.remove(lineas[0])
		lineas=lineas[0]
		lineas=lineas.split()
		equity=float(lineas[a])*100
		equity=round(equity,2)

		#creo el archivo donde estan todas las categorias
		archivo=open("categorias.txt","r")
		lineas=archivo.readlines()
		lineas.remove(lineas[0])
		fuerza=lineas[0]
		fuerza=fuerza.split()
		draw=lineas[1]
		draw=draw.split()
		#Busco la fuerza de la mano
		archivo=open("fuerza.txt","r")
		lineas=archivo.readlines()
		lineas.remove(lineas[0])
		fuerza_mano=lineas[0]
		fuerza_mano=fuerza_mano.split()
		fuerza_mano=fuerza_mano[a]
		fuerza_=fuerza_mano

		#fuerza_mano_=fuerza_mano #categoria de la fuerza
		fuerza_mano=fuerza[int(fuerza_mano)]
		draw_mano=lineas[1]
		draw_mano=draw_mano.split()
		draw_mano=draw_mano[a]
		draw_=draw_mano
		#draw_mano_=draw_mano #categoria del draw
		draw_mano=draw[int(draw_mano)]
		


	return equity, fuerza_mano, draw_mano, fuerza_, draw_