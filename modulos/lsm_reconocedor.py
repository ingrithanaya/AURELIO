import math


class ReconocedorLSM:


    def reconocer(self, puntos):

        dedos = self.contar_dedos(puntos)


        if dedos == 0:
            return "A"


        elif dedos == 5:
            return "B"


        elif dedos == 3:
            return "C"


        elif dedos == 1:
            return "HOLA"


        return "Desconocido"



    def contar_dedos(self, puntos):

        abiertos = 0


        # Pulgar
        if puntos[4].x < puntos[3].x:
            abiertos += 1


        # Índice
        if puntos[8].y < puntos[6].y:
            abiertos += 1


        # Medio
        if puntos[12].y < puntos[10].y:
            abiertos += 1


        # Anular
        if puntos[16].y < puntos[14].y:
            abiertos += 1


        # Meñique
        if puntos[20].y < puntos[18].y:
            abiertos += 1


        return abiertos