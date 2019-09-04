#Cristofer Burbano - Robin Ruales
from random import randint,uniform,random

#nump = (int(input("digite el número de jugadores: ")))

#menu
import os
def basico():
    pl1 =0
    pl2 = 0
    pl3 = 0
    pl4 = 0
    
    d1 = 0
    d2 = 0
    while pl1 <= 20 :
        d1 = randint(1,6)
        d2 = randint(1,6)
        pl1 = d1 + d2
        print("posición actual", pl1)    
        key = input("press any key to continue")
        d1 = randint(1,6)
        d2 = randint(1,6)
        pl2 = d1 + d2
        print("posición actual", pl2)    
        key = input("press any key to continue")
        d1 = randint(1,6)
        d2 = randint(1,6)
        pl3 = d1 + d2
        print("posición actual", pl3)    
        key = input("press any key to continue")
   
 
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') 
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")