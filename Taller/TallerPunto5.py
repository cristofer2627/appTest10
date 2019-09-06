#Created by Cristofer Burbano, Robin Ruales
import os

n2 = []

 
def menu():
	
	os.system('cls')
	print ("Selecciona una opción")
	print ("\t1 - Ingresar Palabra")
	print ("\t2 - Mostrar  Palabra")
	print ("\t3 - Mostrar Palabra (Invertida)")
	print ("\t4 - salir")

def op1():
    n1 = int(input("¿cuantas letras tiene la palabra que desea ingresar?"))
    i=1
    global n2
    n2 = []
    
    
    while i <= n1 :
        print("Digite letra ", i)
        b=input()
        n2.insert(i,b)
        i = i + 1 
    print(n2)
    key = input("pulse ENTER para continuar")
           
def op2():
    global n2
    for letra in n2:
        print(letra)
    key = input("pulse ENTER para continuar")

def op3():
    global n2
    var1 = len(n2)
    
    while var1 > 0 :
        print(n2[var1 - 1])
        var1 = var1 - 1
    key = input("pulse ENTER para continuar")
    

  
while True:
	#menu
	menu()
 
	opcionMenu = input("inserta un numero valor >> ")
	if opcionMenu=="1":
		op1()           

	elif opcionMenu=="2":
		op2()
        
		
	elif opcionMenu=="3":
		op3()

	elif opcionMenu=="4":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")