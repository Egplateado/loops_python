numero = int(input("Ingrese el numero de la tabla de multiplicar que desee conocer\n")) 
i = 0
valor = 0

while(i<=10):
    valor = i*numero
    print("{} * {} = {}".format(i,numero,valor))
    i+=1
    