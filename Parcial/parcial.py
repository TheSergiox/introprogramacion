#----------------------------------------------------Parcial------------------------------------------------#
def lindesing(cantidad=10,simbolo="#"):
    print(simbolo *cantidad)
    return None 

#---------------------------------------Punto 1 --------------------------------------#
#----------Sumar tres numeros----------#
def sumar (a = 0,b = 0,c = 0 ):
    suma = a + b + c
    return suma
lindesing(30,"#")

#---------Restar tres nuemros--------#
def resta (a = 0, b = 0, c = 0):
    resta = a - b - c
    return resta
lindesing(30,"#")
#----------Multiplicar tres numeros----------#
def multiplicar (a = 0, b = 0, c = 0):
    multiplica = a * b * c
    return multiplica
lindesing(30,"#")
#---------dividir tres numeros----------#
def dividir (a = 0, b = 1, c = 1):
    dividi = a / b / c
    return dividi
lindesing(30,"#")
#-----------potenciar tres numeros----------#
def potenciar (base = 0, exponente = 1,exponente2 = 1):
    potencia = base ** exponente ** exponente2
    return potencia
lindesing(30,"#")

print(sumar(12,14,10))
print(resta(83,87,89))
print(multiplicar(83,87,37))
print(dividir(83,87,37))
print(potenciar(5,6,2))
#---------------------------------------Punto 2 --------------------------------------#
lista1 = [213,32,23123,321,321,233,1232,23]
lista2 = [564654,546,64543,2565,547,57865]
lista3 = [6473637,63673,8383,83838,6262]
def mostrarlista(listaEntrada,listaEntrada2,listaEntrada3):
    for elemento in listaEntrada:
        print(elemento)


    for elemento in listaEntrada2:
        print(elemento)


    for elemento in listaEntrada3:
        print(elemento)

mostrarlista(lista1,lista2,lista3)
#---------------------------------------Punto 3 --------------------------------------#
def areatriangulo (base = 0,altura = 0):
    areaTriangulo = base * altura /2
    return areaTriangulo

baseIngresada = int (input("ingrese el valor de la base del triangulo en cm: "))
alturaingresada = int (input("ingrese el valor de la altura del triangulo en cm: "))
print (f"El area del triangulo es {areatriangulo(baseIngresada,alturaingresada)} cm cuadrados ")
#---------------------------------------Punto 4 --------------------------------------#
numerosEnteros = [8,9,10,11,12]
def informalist (lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista :
        acumulador += elemento
    sizeList = len (lista)
    promedio = acumulador/sizeList
    print (f"El numero mayor de la lista es el {mayor}, el numero menor es el {menor} y el promedio es {promedio}")
informalist (numerosEnteros)
#---------------------------------------Punto 5 --------------------------------------#
def sucesion (n):
    a = 0
    b = 1
    for elemento in range (n):
        c = a + b
        a = b
        b = c
    return (b)
n = int(input("ingrese la posicion que quiere saber : "))
lugar = sucesion (n)
print (lugar)