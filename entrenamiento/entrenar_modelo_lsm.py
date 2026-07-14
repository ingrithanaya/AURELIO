import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


print("=" * 50)
print("ENTRENAMIENTO DEL MODELO LSM - AURELIO")
print("=" * 50)


ruta_dataset = "capturas/dataset_lsm.csv"


datos = pd.read_csv(ruta_dataset)


print("\nMuestras cargadas:", len(datos))


columnas = []

for eje in ["x", "y", "z"]:
    for i in range(21):
        columnas.append(f"{eje}{i}")


X = datos[columnas]

y = datos["sena"]


print("\nClases encontradas:")
print(y.value_counts())


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


modelo = RandomForestClassifier(
    n_estimators=500,
    random_state=42
)


print("\nEntrenando modelo...")


modelo.fit(
    X_train,
    y_train
)


predicciones = modelo.predict(X_test)


accuracy = accuracy_score(
    y_test,
    predicciones
)


print("\n==============================")
print("Accuracy:", accuracy)
print("==============================")


print("\nReporte:")
print(classification_report(y_test, predicciones))


print("\nMatriz:")
print(confusion_matrix(y_test, predicciones))


os.makedirs(
    "modelos",
    exist_ok=True
)


joblib.dump(
    modelo,
    "modelos/modelo_lsm.pkl"
)


print("\nModelo guardado correctamente")