#Cristofer Burbano - Robin Ruales
from random import randint,uniform,random
import os
#menu
nump = 0

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') 
	print ("......CARRERA NUMERICA.......♫♫♫♫♫")
	print ("Selecciona una opción")
	print ("\t1 - Nivel Básico (tablero de 20 Posiciones)")
	print ("\t2 - Nivel Intermedio (tablero de 30 Posiciones)")
	print ("\t3 - Nivel Avanzado (tablero de 50 Posiciones)")
	print ("\t9 - salir")

def pedir():
	global nump
	nump = (int(input("digite el número de jugadores entre 2-4: ")))
	if (nump < 2) :
		print("en numero minimo de jugadores es 2")
		pedir()
	elif (nump > 4) :
		print("en numero maximo  de jugadores  es 4")
		pedir()
	else :
		return nump
	
def basico():

	input("El juego va a iniciar pulse ENTER para continuar")
	pl1 = 0
	pl2 = 0
	
	if (nump == 2):
		acum1 = 0
		acum2 = 0
		#pares = 0
		while ((acum1 or acum2) <= 20) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>19):
				print ("el jugador 1 es el ganador")
				break
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>19):
				print ("el jugador 2 es el ganador")
				break
	elif(nump==3):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		
		while ((acum1 or acum2 or acum3) <= 20) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>19):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>19):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>19):
				print("el jugador 3 es el ganador")
				break

	elif(nump==4):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		acum4 = 0
		
		while ((acum1 or acum2 or acum3 or acum4) <= 20) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>19):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>19):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>19):
				print("el jugador 3 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 4:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl4 = d1 + d2 # 7
			acum4= pl4 + acum4 # 7
			print("::::posición actual del jugador 4::::::", acum4)    
			key = input("pulse una tecla para continuar")
			if (acum4>19):
				print("el jugador 4 es el ganador")
				break

def Intermedio():
	input("El juego va a iniciar pulse ENTER para continuar")
	pl1 = 0
	pl2 = 0
	
	if (nump == 2):
		acum1 = 0
		acum2 = 0
		#pares = 0
		while ((acum1 or acum2) <= 30) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>29):
				print ("el jugador 1 es el ganador")
				break
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>29):
				print ("el jugador 2 es el ganador")
				break
	elif(nump==3):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		
		while ((acum1 or acum2 or acum3) <= 30) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>29):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>29):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>29):
				print("el jugador 3 es el ganador")
				break

	elif(nump==4):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		acum4 = 0
		
		while ((acum1 or acum2 or acum3 or acum4) <= 30) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>29):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>29):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>29):
				print("el jugador 3 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 4:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl4 = d1 + d2 # 7
			acum4= pl4 + acum4 # 7
			print("::::posición actual del jugador 4::::::", acum4)    
			key = input("pulse una tecla para continuar")
			if (acum4>29):
				print("el jugador 4 es el ganador")
				break

def Avanzado():
	input("El juego va a iniciar pulse ENTER para continuar")
	pl1 = 0
	pl2 = 0
	
	if (nump == 2):
		acum1 = 0
		acum2 = 0
		#pares = 0
		while ((acum1 or acum2) <= 50) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>49):
				print ("el jugador 1 es el ganador")
				break
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>49):
				print ("el jugador 2 es el ganador")
				break
	elif(nump==3):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		
		while ((acum1 or acum2 or acum3) <= 50) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>49):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>49):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>49):
				print("el jugador 3 es el ganador")
				break

	elif(nump==4):
		acum1 = 0
		acum2 = 0
		acum3 = 0
		acum4 = 0
		
		while ((acum1 or acum2 or acum3 or acum4) <= 50) :
			d1 = randint(1,6) #5
			print("::::Turno del jugador 1:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl1 = d1 + d2 # 7
			acum1= pl1 + acum1 # 7
			print("::::posición actual del jugador 1::::::", acum1)    
			key = input("pulse una tecla para continuar")
			if (acum1>49):
				print("el jugador 1 es el ganador")
				break
			
			d1 = randint(1,6)
			print("::::Turno del jugador 2:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6)
			print("el valor del segundo dado es" , d2)
			pl2 = d1 + d2
			acum2 = pl2 + acum2
			print(":::::posición actual del jugador 2::::::", acum2)    
			key = input("pulse una tecla para continuar")
			if (acum2>49):
				print("el jugador 2 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 3:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl3 = d1 + d2 # 7
			acum3= pl3 + acum3 # 7
			print("::::posición actual del jugador 3::::::", acum3)    
			key = input("pulse una tecla para continuar")
			if (acum3>49):
				print("el jugador 3 es el ganador")
				break
			
			d1 = randint(1,6) #5
			print("::::Turno del jugador 4:::::")
			print("el valor del primer dado es" , d1)
			d2 = randint(1,6) #2
			print("el valor del segundo dado es" , d2)
			pl4 = d1 + d2 # 7
			acum4= pl4 + acum4 # 7
			print("::::posición actual del jugador 4::::::", acum4)    
			key = input("pulse una tecla para continuar")
			if (acum4>49):
				print("el jugador 4 es el ganador")
				break

	
	

			
	
print ("......CARRERA NUMERICA.......♫♫♫♫♫")
 
while True:
	# Mostramos el menu
	pedir()
	menu()
	 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has ingresado al nivel Basico.....")
		basico()
		input("pulsa una tecla para continuar....")


	elif opcionMenu=="2":
		print ("")
		input("Has ingresado al nivel Intermedio...")
		Intermedio()
		input("pulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has ingresado al nivel Avanzado...")
		Avanzado()
		input("pulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
		