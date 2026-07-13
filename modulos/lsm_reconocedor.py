class ReconocedorLSM:


    def reconocer(self, manos):

        if len(manos) == 0:
            return "Sin mano"


        # Si solo hay una mano
        if len(manos) == 1:

            puntos = manos[0]["puntos"]

            dedos = self.contar_dedos(puntos)


            if dedos == 0:
                return "A"

            elif dedos == 5:
                return "B"

            elif dedos == 3:
                return "C"

            elif dedos == 1:
                return "HOLA"


        # Dos manos detectadas
        elif len(manos) == 2:

            izquierda = manos[0]
            derecha = manos[1]


            dedos_izq = self.contar_dedos(
                izquierda["puntos"]
            )

            dedos_der = self.contar_dedos(
                derecha["puntos"]
            )


            # Ejemplo de seña con dos manos abiertas
            if dedos_izq == 5 and dedos_der == 5:
                return "GRACIAS"


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