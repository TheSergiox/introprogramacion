#---QUiZ 1---#
#---constantes---#
Saludo = "Hola profe este es mi quiz 1"
Soborno = "profe si gano el quiz nos vamos por unas polas"
despetida = "ahi esta su quiz, *se voltea indignado por la dificultad del quiz*"
optimo = "yeah bro estas mas sano que una papaya"
sobrelooptimo = "estas por encima de lo optimo pero no hay pedo"
Alto = "papi estas muy alto hay que bajar eso rapido"
Muyalto = " de que color quieres las rosas en tu funeral? "
#---preguntas---#
preguntaTrigliceridos = "ingrese cantidad de trigliceridos del paciente : "
preguntahomocisteina  = "ingrese cantidad de homocisteína del paciente : "
#---entrada al codigo---#
print(Saludo)
print(Soborno)
homocisteina  = float (input(preguntahomocisteina))
trigliceridos = float (input(preguntaTrigliceridos))
isoptimohomocisteina = homocisteina >= 2 and  homocisteina < 15
issobrelooptimohomocisteina = homocisteina >= 15 and homocisteina < 30
isAltohomocisteina = homocisteina >= 30 and homocisteina < 100 
isMuyaltohomocisteina = homocisteina >= 100 
#---homosisteina--#
resultado = ""
if (isoptimohomocisteina) :
    resultado = optimo
elif (issobrelooptimohomocisteina) :
    resultado = sobrelooptimo 
elif (isAltohomocisteina) :
    resultado = Alto
else: 
    resultado = Muyalto
print (resultado)

isoptimotrigliceridos = trigliceridos < 150 
issobrelooptimotrigliceridos = trigliceridos >= 150 and trigliceridos <= 199
isAltotrigliceridos = trigliceridos >= 200 and trigliceridos <= 499
isMuyaltotrigliceridos = trigliceridos > 500
#---trigliceridos---#
resultado = ""
if (isoptimotrigliceridos) :
    resultado = optimo
elif (issobrelooptimotrigliceridos) :
    resultado = sobrelooptimo
elif (isAltotrigliceridos) :
    resultado = Alto
else:
    resultado = Muyalto
print (resultado)|