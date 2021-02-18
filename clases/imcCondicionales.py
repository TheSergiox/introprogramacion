#----constantes----#
Pregunta_peso = "cuanto pesas en Kg? : "
Pregunta_estatura = "cuanto mides en M? : "
Mensaje_debienvenida = "hola voy a calcular ti IMC"
Mensaje_dedespedida = "tu IMC es.."
Mensaje_bajopeso = "no te estas comiendo toda la sopita"
Mensaje_normal = "estas bien fachero mi pana"
Mensaje_sobrepeso = " estas gordidito pero no hay pedo"
Meensaje_obeso = "papi estas peor que ibai"

#----entrada de codigo----#
print(Mensaje_debienvenida)
peso = float (input(Pregunta_peso))
estatura = float (input(Pregunta_estatura))
IMC = peso/(estatura**2)
isBajopeso = IMC < 18.5
isNormal = IMC >= 18.5 and IMC < 25
isSobrepeso = IMC >= 25 and IMC < 30
resultado = ""
if (isBajopeso) :
    resultado = Mensaje_bajopeso
elif (isNormal) :
    resultado = Mensaje_normal
elif ( isSobrepeso) :
    resultado = Mensaje_sobrepeso
else:
    resultado = Meensaje_obeso
print( Mensaje_dedespedida, IMC)
print (resultado)
