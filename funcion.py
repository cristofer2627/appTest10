#funcion 1:Multiplicar dos #s

#librerias
import os

#funcion

def Calc(a,b):
    add= a + b
    return add

#main 
os.system("cls")

n1= int(input("Digite numero 1: "))
n2= int(input("Digite numero 2: "))

Calc(n1,n2)
print("el resultado es: ",Calc(n1,n2))
