#-------Quiz #3----------#
Integrantes1: "Wlliam Velez"
Integrante2: "Sergio Gómez"
#--------Punto 1 ---------#
#--------Entrada al codigo-----------#
class ElementosDigitales():
    def __init__(self, nombreEntrada, creadorEntrada,fechaEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fecha = fechaEntrada
    def mostrarAtributos(self):
        print(f'Mi nombre es {self.nombre}, mi creador se llama {self.creador} y sali el {self.fecha}')

class Usuario ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.nacionalidad= nacionalidadEntrada
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre},tengo {self.edad} años,soy de sexo {self.sexo} soy de nacionalidad {self.nacionalidad}''')
    def escucharCancion(self, cancionEntrada):
        print (f"  soy {self.nombre} y estoy escuchando {cancionEntrada}")


class Pagina():
    def __init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada):
        self.tipocontenido = tipocontenidoEntrada
        self.formato = formatoEntrada
        self.fecha = fechaEntrada
    def mostrarAtributos(self):
        print(f'en mi pagina se puede encontrar {self.tipocontenido}, mi formato es {self.formato} y sali el {self.fecha}')
#----------------- Punto 2 ---------------------#
listaFav = ['Sin tiempo', 'vete', 'perriando', 'decidete', 'ojala']
print(listaFav)
pregunta_n = '¿deseas eliminar alguna cancion?: '
class Cancion(ElementosDigitales):
    def __init__(self, nombreEntrada, creadorEntrada,fechaEntrada, generoEntrada, duracionEntrada):
        ElementosDigitales.__init__(self,nombreEntrada, creadorEntrada,fechaEntrada)
        self.genero = generoEntrada
        self.duracion = duracionEntrada
        print(f'La nueva cancion se llama {self.nombre} y se estreno el {self.fecha}')
    def reproducir(self, veces):
        for i in range (veces):
            print (f'{self.nombre} sonando {i+1} veces')

class Artista(Usuario):
    def __init__(self, generoEntrada, numerocancionesEntrada, albumsEntrada, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada,):
        Usuario.__init__(self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada,  )
        self.generomusical = generoEntrada
        self.numerocanciones = numerocancionesEntrada
        self.numeroDeAlbums = albumsEntrada
    def asistirConcierto(self, localidadEntrada):
        self.localidadconcert = localidadEntrada
        print (f" Hola, soy {self.nombre}, iré a un concierto en {self.localidadconcert} del genero {self.generomusical} que tiene {self.numeroDeAlbums} albums con {self.numerocanciones} canciones.")



class Favoritos(Pagina):
    def __init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada, fechaactEntrada):
        Pagina.__init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada)
        self.comunidad = listaFav
        self.fechaactualizacion = fechaactEntrada
    def agregarcancion(self, cancion, fechaactualizacion):
        listaFav.append(cancion)
        print(f'La fechaahora es {fechaactualizacion}')
    def eliminarcancion(self, n=int(input(pregunta_n))):
        print(listaFav)
        listaFav.pop(n-1)
        print(listaFav)


favorito1 = Favoritos('Canciones', 'MP3', '15 de febrero de 2003', '20 de junio de 2020')
favorito1.agregarcancion('fresco', '3 oct. 2019')
favorito1.eliminarcancion()

cancion1 = Cancion('canguro', 'wos', '8 ago. 2019', 'rap',240)
cancion1.reproducir(5)

Fabio = Artista ("rap ", "3", "32", "27", "Sergio", "hombre", "Colombiano")
Fabio.asistirConcierto("Argentina")
