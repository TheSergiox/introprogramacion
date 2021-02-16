#----constantes----#
Pregunta_peso = "cuanto pesas en Kg? : "
Pregunta_estatura = "cuanto mides en M? : "
Mensaje_debienvenida = "hola voy a calcular ti IMC"
Mensaje_dedespedida = "tu IMC es.."

#----entrada de codigo----#
print(Mensaje_debienvenida)
peso = float (input(Pregunta_peso))
estatura = float (input(Pregunta_estatura))
IMC = peso/(estatura**2)
print(Mensaje_dedespedida, IMC)
isObeso = IMC >= 30
print ("El resultado de la prueba de obesidad es ...", isObeso)

