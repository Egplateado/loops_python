from os import system
def factorial():
    num = int(input("Ingrese un numero entero y mayor a cero\n"))
    system("cls")
    if num >0:
        factorial = 1
        for i in range(1 , num +1):
            factorial*=i
            print(factorial)
    else:
        print("El numero es negativo y no podemos proceder ( \n")

factorial()