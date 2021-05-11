import matplotlib.pyplot as plt
#--------Punto 1-------#
#---constantes---#
Saludo = "Hola profe este es mi quiz 4"
Soborno = "profe si gano el quiz nos vamos por unas polas"
despetida = "ahi esta su quiz, *se voltea indignado por la dificultad del quiz*"
Pregunta_snacks = " Ingrese por favor sus snacks favoritos : "
Pregunta_PrecioSnack = "ingrese por favor el valor del snack : "
snacks = []
n=5
#---entrada al codigo---#
print(Saludo)
print(Soborno)
while (n>0):
    snack = input (Pregunta_snacks)
    snacks.append(snack)
    n=n-1

precios = []
n=5
while (n>0):
    precio = int(input(Pregunta_PrecioSnack))
    precios.append(precio)
    n=n-1
plt.bar(snacks,precio, width=0.7, color='b')
#-----------------------
plt.title('Snacks favoritos y precio de estos mismos')
plt.xlabel('Snacks')
plt.ylabel('Valor del snack')
plt.savefig('graficoBSanack.png')
#-----------------------
plt.show()
#-----------Punto 2----------#
Pregunta_Ciudad = "ingrese una ciudad de colombia :"
Pregunta_poblacion = "ingrese la poblacion de esa cidad : "
ciudades = []
n=5
while (n>0):
    ciudad = input(Pregunta_Ciudad)
    ciudades.append(ciudad)
    n=n-1

sizes = []
n=5
while (n>0):
    poblacion = int(input(Pregunta_poblacion))
    sizes.append(poblacion)
    n=n-1

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador +=elemento

    for i in range (len(labels)):
        ciudades[i] += indicador+str(round(sizes[i]/acumulador*100,2)) + "%"

etiquetarElementosPorcentuales(sizes,ciudades,'-')
plt.pie(sizes,labels=ciudades,shadow=1,counterclock=1)
plt.title("ciudades favoritas" )
plt.savefig("CiudadesTorta.png")
#---------#
maximo = max(sizes)
ubicacion = sizes.index(maximo)
print(ubicacion)
plt.show()
#--------punto3---------#
print ('Punto 3 --- Grafico curvas')

print ('ecg = Un electrocardiograma ECG es un examen que registra la actividad eléctrica del corazón.')
print ('ppg = Es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano')

import pandas as pd

ppgData = pd.read_csv ('ppg.csv', encoding = 'UT8', header = 0, delimiter = ';').to_dict ()
muestras = list (ppgData ['muestra'].values ())
valores = list (ppgData ['valor'].values ())
plt.plot (muestras, valores)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Fotopletismografia')
plt.savefig ('Grafico ppg.png')
##
ecgData = pd.read_csv ('ecg.csv', encoding = 'UT8', header = 0, delimiter = ';').to_dict ()
muestra1 = list (ecgData ['muestra'].values ())
voltaje = list (ecgData ['valor'].values ())
plt.plot (muestra1, voltaje)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Electrocardiograma')
plt.savefig ('Grafico ecg.png')
plt.show ()