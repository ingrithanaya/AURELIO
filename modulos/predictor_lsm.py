import joblib
import pandas as pd

class PredictorLSM:

    def __init__(self):
        self.modelo = joblib.load("modelos/modelo_lsm.pkl")

        print("========================================")
        print("MODELO LSM CARGADO")
        print("========================================")

        if not hasattr(self.modelo, "predict_proba"):
            raise RuntimeError("El modelo no permite obtener compatibilidad.")

    def reconocer(self, manos):

        if len(manos) == 0:
            return "Sin mano", 0.0

        puntos = manos[0]["puntos"]

        if len(puntos) != 21:
            return "Desconocido", 0.0

        datos = {}

        for i in range(21):
            datos[f"x{i}"] = puntos[i].x

        for i in range(21):
            datos[f"y{i}"] = puntos[i].y

        for i in range(21):
            datos[f"z{i}"] = puntos[i].z

        columnas = []

        for eje in ["x", "y", "z"]:
            for i in range(21):
                columnas.append(f"{eje}{i}")

        entrada = pd.DataFrame([datos])
        entrada = entrada[columnas]

        probabilidades = self.modelo.predict_proba(entrada)[0]
        clases = self.modelo.classes_

        indice = probabilidades.argmax()

        sena = clases[indice]
        compatibilidad = probabilidades[indice] * 100

        return sena, compatibilidad
