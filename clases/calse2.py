pruebaV = True
pruebaf = False
print (pruebaf)
print(pruebaV)
pruebaV = pruebaf
print (pruebaV)
edad = 17
estatura = 1.70
peso = 50
NOMBRE = "Sergio Gomez Valencia"
print("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print("#"*15,"Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# calculando si el peso es difenteren a 84
print("#"*15,"Peso diferente 84", "#"*15)
isPesoDiferente = peso != 84
print (isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "Herrera"
isApellido= apellido in NOMBRE
print("#"*15,"Esta apellido en el nombre?", "#"*15)
print (isApellido)
