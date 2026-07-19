class EstabilizadorLSM:

    def __init__(self, repeticiones=5):

        self.repeticiones = repeticiones

        self.historial = []


    def filtrar(self, letra):

        # Ignorar cuando no hay mano o la predicción es desconocida
        if letra in ["Sin mano", "Desconocido"]:
            self.historial.clear()
            return None

        # Agregar la letra al historial
        self.historial.append(letra)

        # Mantener solo las últimas N predicciones
        if len(self.historial) > self.repeticiones:
            self.historial.pop(0)

        # Aún no hay suficientes muestras
        if len(self.historial) < self.repeticiones:
            return None

        # Si todas las predicciones son iguales, aceptar la letra
        if len(set(self.historial)) == 1:
            letra_estable = self.historial[0]
            self.historial.clear()
            return letra_estable

        return None