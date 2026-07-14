import joblib
import pandas as pd


class PredictorLSM:

    def __init__(self):

        self.modelo = joblib.load(
            "modelos/modelo_lsm.pkl"
        )

        print("Modelo LSM cargado correctamente")


    def reconocer(self, manos):

        if len(manos) == 0:
            return "Sin mano"


        # Usamos la primera mano detectada
        puntos = manos[0]["puntos"]


        datos = {}


        # Coordenadas X
        for i in range(21):
            datos[f"x{i}"] = puntos[i].x


        # Coordenadas Y
        for i in range(21):
            datos[f"y{i}"] = puntos[i].y


        # Coordenadas Z
        for i in range(21):
            datos[f"z{i}"] = puntos[i].z



        columnas = []


        for eje in ["x","y","z"]:
            for i in range(21):
                columnas.append(
                    f"{eje}{i}"
                )



        entrada = pd.DataFrame(
            [datos]
        )


        entrada = entrada[columnas]



        prediccion = self.modelo.predict(
            entrada
        )


        return prediccion[0]