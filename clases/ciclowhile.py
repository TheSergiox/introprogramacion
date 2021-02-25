#---mensajes---#
saludo  = "bienvenido, te ayudare ahorrando"
pregunta_cpu = " cuanto vale el pc? : "
pregunta_cuantotienes = "cuanto llevas ahorrado? :"
mensaje_ahorro = "llevas ahorrado ..."

#---entradas---#
print (saludo)
valor = float (input(pregunta_cpu))
ahorrado = float (input(pregunta_cuantotienes))

while (valor >= ahorrado) :
    print (mensaje_ahorro, ahorrado, "te faltan ....", valor - ahorrado)
    ahorrado = ahorrado +1000
print (valor == ahorrado)
