import os

 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Ingresar Palabra")
	print ("\t2 - Mostrar  Palabra")
	print ("\t3 - Mostrar Palabra (Invertida)")
	print ("\t4 - salir")

def op1():
    n1 = int(input("¿cuantas letras tiene la palabra que decea ingresar?"))
    i=1
    n2=[]
    
    while i <= n1 :
        print("Digite letra ", i)
        b=input()
        n2.insert(i,b)
        i = i + 1 
           
    
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
	if opcionMenu=="1":
		op1()           

	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")