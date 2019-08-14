#randint = Numeros aleatorios
#uniform =  Numeros flotantes aleatorios
from random import randint,uniform,random

def Z():
    a = randint (0,100)
    return a

def R():
    b= uniform(0,100)
    return b
print ("Numero Z =", Z())
print ("Numero R =", Z())