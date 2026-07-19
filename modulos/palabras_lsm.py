import time


class ConstructorPalabras:

    def __init__(self):

        self.palabra = ""

        self.ultima_letra = ""

        self.tiempo_ultima = time.time()

        self.diccionario = {

            "BEBE": "Bebe",

        }


    def agregar_letra(self, letra):

        ahora = time.time()


        if letra != self.ultima_letra:

            self.palabra += letra

            self.ultima_letra = letra

            self.tiempo_ultima = ahora


        return self.palabra


    def verificar_palabra(self):

        if self.palabra in self.diccionario:

            palabra = self.diccionario[self.palabra]

            self.limpiar()

            return palabra

        return None


    def limpiar(self):

        self.palabra = ""

        self.ultima_letra = ""

        self.tiempo_ultima = time.time()