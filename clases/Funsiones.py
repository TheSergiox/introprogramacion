def lindesing(cantidad=10,simbolo="#"):
    print(simbolo *cantidad)
    return None 

lindesing(30,"#")
lindesing(10,"#")
lindesing(100,"#")
lindesing()

#-----------Muestre la lista-----------#
def mostrarlista(listaEntrada):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista= [213,32,23123,321,321,233,1232,23]
lista2 = [564654,546,64543,2565,547,57865]
lindesing(30,"#")
mostrarlista(lista)
lindesing(30,"*")
mostrarlista(lista)

#----------Sumar dos numeros----------#
def sumar (a= 0,b = 0):
    suma = a + b
    return suma
lindesing(30,"!")
resultado= sumar()
print(resultado)
print(sumar(12,14))
round (12.234897,2)
#---------Restar dos nuemros--------#
def resta (a = 0, b = 0):
    resta = a - b
    return resta
#----------Multiplicar dos numeros----------#
def multiplicar (a = 0, b = 0):
    multiplica = a * b
    return multiplica
#---------dividir dos numeros----------#
def dividir (a = 0, b = 1):
    dividi = a / b
    return dividi

print(resta(83,87))
print(multiplicar(83,87))
print(dividir(83,87))