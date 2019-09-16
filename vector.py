from random import randint,uniform,random

fruits =["apple", "banana", "orange"]
print("primer valor", fruits[0])
print("Ultimo valor", fruits[2])


   

n=[]
i = 1
naleatorio= int(input("Cuantos numeros aleatorios desea generar?"))

while i<= naleatorio :
    a = randint (0,100)
    i= i+1

i=0
while i< naleatorio: 
    print("El valor en la pocicion ", i, "es: ", a[i])
    i= i+1