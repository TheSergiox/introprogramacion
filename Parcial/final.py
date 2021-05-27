from typing import final
import matplotlib.pyplot as plt
#---constantes---#
Saludo = "Hola profe este es mi examen final"
Soborno = "profe si gano el quiz nos vamos por unas polas"
despetida = "ahi esta su quiz, *se voltea indignado por la dificultad del quiz*"
#------Punto 1-----#
Pregunta_Comida = " Ingrese por favor sus Comidas favoritas : "
Pregunta_PrecioComida = "ingrese por favor el valor de la Comida: "
comidas = []
n=8
#---entrada al codigo---#
print(Saludo)
print(Soborno)
while (n>0):
    comida = input (Pregunta_Comida)
    comidas.append(comida)
    n=n-1

precios = []
n=8
while (n>0):
    precio = int(input(Pregunta_PrecioComida))
    precios.append(precio)
    n=n-1
plt.bar(comidas, precio, width=0.7, color='b')
#-----------------------
plt.title('Comida favorita y precio de esta')
plt.xlabel('Comida')
plt.ylabel('Valor del Comida')
plt.savefig('graficoBComida.png')
#-----------------------
plt.show()

#-------Punto 2--------
PreguntaPeso = "cual es tu peso en kg : "
PreguntaEstatura = "cual es tu estatura en m : "
Mensajefinal = "tu imc es..."

class Humano ():
    def _init_(self, nombreEntrada, edadEntrada,sexoEntrada):
        print('Hola soy un nuevo usuario')
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada

    def hablar(seld,mensaje):
        print(f'hola soy {self.nombre} tengo un mensaje que decir....',mensaje)

class Doctor(Humano):
    def _init_ (self,nombreEntrada, edadEntrada,sexoEntrada,areaEntrada):
        Humano. _init_(self,nombreEntrada,edadEntrada,sexoEntrada)
        self.area = areaEntrada

doctor1 = print( 'Hola, hoy sere tu doctor y calculare tu imc')
peso = float(input(PreguntaPeso))
estatura = float(input(PreguntaEstatura))
imc = peso/estatura**2
print(Mensajefinal, imc)
isobeso = imc>=20
print('el resultado del examen de obesidad es...',isobeso )
#------Punto 3------#
preguntaNombre = 'hola, cual es tu nombre : ' 
Preguntadolares = 'Por favor ingrese su nombre y la cantidad de dinero en dolares que quieres convertir : '
mensajeE = 'su dinero en en euros es..'
ValorEurosxDolar = 0.82
Nombre = input(preguntaNombre)
dolares = float(input(Preguntadolares))
multiplicar = dolares * ValorEurosxDolar
print (f"sus dolares en euros son {multiplicar}")