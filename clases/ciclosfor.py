
for iteracion in range (10) :
    print (iteracion)
print ( "#" *60)
for iteracion in range (10) :
    print (iteracion+1)
print ( "#" *60)
for iteracion in range (1,11) :
    print (iteracion)
print ( "#" *60)

for iteracion in range (1,14,2) :
    print(iteracion) 

residuo =5%4
print (residuo)
residuo = 4%4
print (residuo)
print ( "#" *60)
for iteracion in range (1,11) :
    if (iteracion % 2 == 0) :
        print(iteracion)

print ( "#" *60)
for iteracion in range (1,11) :
    if (iteracion % 2 != 0) :
        print(iteracion)
print ( "#" *60)
for iteracion in range (1,11) :
    if (iteracion % 2 == 0) :
        print(iteracion, "es un numero par")
    else :
        print(iteracion, "es un numero impar")
print ( "#" *60)
rango = int (input("ingrese el rango maximo : "))

opciones = int (input( """
    1- ver solo impares
    2- ver solo pares 
    3- ver los dos 
    4- cualquier numero paea mostrar nada 

"""))

if(opciones == 1):
    for iteracion in range (1,rango+1) :
        if (iteracion % 2 != 0) :
            print (iteracion)
elif(opciones == 2) :
    for iteracion in range (1,rango+1) :
        if (iteracion % 2 != 0) :
            print (iteracion)
elif(opciones == 3) :
    for iteracion in range (1,rango+1) :
        if (iteracion % 2 != 0) :
            print (iteracion, "es un numero par")
        else :
            print(iteracion, "es un numero impar")
else :
    print("mostrando nada")

