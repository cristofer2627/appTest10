num1 = 1
num2 =0
num3 = 0
print ("::::::::Sucesión Fibonacci::::::::")
print()
val = int(input("Digite la Cantidad de terminos de la serie FIBONACCI que desea mostrar "))
print ("serie  0 =",num1)
for i in range(0,val):
    num3=num2
    num2=num1
    num1= num3+num2
    print("Serie ",i+1, "=",num1)