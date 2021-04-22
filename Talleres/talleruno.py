print("punto 1")

class ElementosDigitales ():
    def __init__ (self, nombreEntrada, creadorEntrada, fechapublicacionEntrada ):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fechapublic = fechapublicacionEntrada
    def mostrarAtributos(self):
        print (f'''El nombre de la cancion es {self.nombre}, el creador es {self.creador}, la fecha de publicacion es {self.fechapublic}''')

elemento = ElementosDigitales('la tusa','william',2019)
elemento.mostrarAtributos()

class Usuario ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada,cancionEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada
        self.cancion = cancionEntrada
    def mostrarAtributos (self):
        print (f''' mi nombre es {self.nombre}, tengo {self.edad} años, soy de sexo {self.sexo}, soy de nacionalidad {self.nacionalidad}, y estoy escuchando {self.cancion}''')

Usuario1 = Usuario (29,'sergio', 'Masculino','colombiana','la tusa')
Usuario1.mostrarAtributos ()

class Pagina ():
    def __init__ (self,tipodecontenidoEntrada,formatoEntrada,fechapublicacionEntrada):
        self.tipocontenido = tipodecontenidoEntrada
        self.formato = formatoEntrada
        self.fechapublicacion = fechapublicacionEntrada
    def mostrarAtributos (self):
        print (f''' En esta pagina se puede publicar {self.tipocontenido}, en el formato {self.formato} y la fecha de publicacion es {self.fechapublicacion} ''')

pagina1 = Pagina ('musica', 'mp3', 2020,)
pagina1.mostrarAtributos ()