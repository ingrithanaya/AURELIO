from lsm_reconocedor import ReconocedorLSM
from estabilizador import EstabilizadorLSM


class ControlLSM:

    def __init__(self):

        self.reconocedor = ReconocedorLSM()

        self.estabilizador = EstabilizadorLSM(
            repeticiones=5
        )


    def procesar(self, manos):

        # Reconocimiento normal
        letra = self.reconocedor.reconocer(manos)


        # Pasar por estabilizador
        letra_estable = self.estabilizador.filtrar(letra)


        return letra_estable