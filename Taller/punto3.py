def Factorial():
    print()
    print ("::::::::Factorial de un Numero::::::::")
    print()
    num = int(input("Digite el numero a calcular: "))
    numero=num
    fac = 1
    for i in range(num):
        fac = fac * num
        num = num - 1
    print("El factorial del numero", numero, "es: ", fac)


Factorial()
