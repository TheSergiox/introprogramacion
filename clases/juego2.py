
import random
#---Entradas---#
mensaje_saludar = """
    bienvenido
        a este juego
    !!!juguemos!!!"""
pregunta_numero = """
        En este juego deber asertar un numero entero
        que va desde 1 a 10, la idea es que 
        lo puedas intentarlo hasta que se acaben
        las vidas, si pierdes todas las vidas se 
        reiniciara y tendras otro numero oculto
        Mucha suerte 
"""
Pregunta_fallida = "ahhhhh! fallaste :v ingresa otro numero : "
mensaje_ganaste = "felicidades has ganado"
Mensaje_perdiste = "perdiste D: vuelve a intentarlo!!"
#---Mensaje del codigo---#f
numeroOculto = random.randint(1,10)
vidas = 3
numeroingresado = int(input(pregunta_numero))
while (numeroingresado != numeroOculto and vidas>1):
    vidas -=1
    print (f"te quedan {vidas} vidas")
    numeroingresado = int(input(Pregunta_fallida))
if(vidas>=0 and numeroingresado == numeroOculto):
    print(mensaje_ganaste)
else:
        print(Mensaje_perdiste, "el numero era el", numeroOculto)