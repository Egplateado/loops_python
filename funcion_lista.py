from pickle import APPEND
lista = []

def crear():
    i = 1
    while(i<=5):
        num = int(input("Ingrese un numero\n"))
        lista.append(num)
        i+=1
print(lista)


def ordenar():
    lista.sort()
    par = []
    impar = []
    for i in lista:
        if i%2 == 0:
            par.append(i)
        else:
            impar.append(i)
    print(lista)
    print(par)
    print(impar)

crear()
ordenar()
