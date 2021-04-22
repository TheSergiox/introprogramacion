#---Quiz2---#

#---datos iniciales---#
temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
#---saludo---#
saludo = "bienvenido al quiz 3"
#---Pregunta---#

PreguntaMenu = """por favor ingrese alguna de las siguientes opciones : 
        1-convertidor
        2-Clasificaion de Temperatura
        3-Temperatura maxima y minima
        4-salir
: """
#---conversion---#

Preguntaconversion = """Por favor ingrese la unidad en que quiere saber su temperatura
        C-Temperatura el celsius
        K-Tempereatura en Kelcin
        F-Temperatura en  Fahrenheit
: """
mensajeC= "la conversion no es necesaria"
mensajeF = "su temperatura en fahrenheit es.."
mensajeK = "su temperatura en kelvin es ..."
MensajeH = "hipotermia"
MensajeFiebre = "fiebre"
MensajeN = "Normal"
MensajeMAX = "la temperatura maxima es.."
MensajeMIN= "la temperatura minima es ..."
MensajeError = "seleccione una opcion valida"
mensajeTomada = "la temperatura se tomaba cada... "
MensajeDespedida = "Adios"
#---codigo---#
listafahrenheit  =[]
for elemento in temperatura_Corporal:
    fahrenheit = round((elemento*1.8) + 32,2)
    listafahrenheit.append (fahrenheit)
listakelvin = []
for elemento in temperatura_Corporal:
    kelvin = round (elemento + 273.15,2)
    listakelvin.append (kelvin)
opcion = int(input(PreguntaMenu))
while (opcion != 4):
    if(opcion ==1):
        print("Escogiste la opcion 1")
        opcionGrados = input(Preguntaconversion)
        if(opcionGrados=="C"):
            print (mensajeC)
            print (temperatura_Corporal)
        elif (opcionGrados == "F"):
            print (mensajeF)
            print(listafahrenheit)
        elif (opcionGrados == "K"):
            print (mensajeK)
            print (listakelvin)
        else:
            print (MensajeError)
    elif (opcion == 2):
        print ("Escogiste la opcion 2")
        for posicion in temperatura_Corporal:
            if (posicion<36):
                print(posicion, "----->", MensajeH)
            elif (posicion>=36 and posicion<=37.5):
                print(posicion, "---->",MensajeN)
            else:
                print(posicion, "--->",MensajeFiebre)
    elif(opcion == 3):
        print("Escogiste la opcion 2")
        print(MensajeMAX, max(temperatura_Corporal))
        print (MensajeMIN, min(temperatura_Corporal))
        print(mensajeTomada, len(temperatura_Corporal)/24*60,"minutos")
    else:
        print(MensajeError)
    opcion=int(input(PreguntaMenu))
print(MensajeDespedida)
