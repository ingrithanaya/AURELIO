class ConstructorPalabras:

    def __init__(self):
        self.palabra = ""
        self.ultima_letra = ""


    def agregar_letra(self, letra):

        if letra != self.ultima_letra:

            self.palabra += letra
            self.ultima_letra = letra

        return self.palabra


    def limpiar(self):

        self.palabra = ""
        self.ultima_letra = ""


    def obtener(self):

        return self.palabra