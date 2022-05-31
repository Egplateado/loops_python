from os import system

num_1 = int(input("Ingrese el numero menor\n"))
system("cls")
num_2 =int(input("Ingrese el numero mayorn\n"))
system("cls")

for i in range (num_1 , num_2):
    if i%2 == 0:
        continue
    print(i)


