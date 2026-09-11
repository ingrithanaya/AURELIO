import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


print("=" * 60)
print("DIAGNOSTICO DEL MODELO LSM - AURELIO")
print("=" * 60)


# ============================================================
# 1. CARGAR DATASET
# ============================================================

ruta_dataset = "capturas/dataset_lsm.csv"

datos = pd.read_csv(ruta_dataset)

print("\nMuestras cargadas:", len(datos))


# ============================================================
# 2. CREAR COLUMNAS
# ============================================================

columnas = []

for eje in ["x", "y", "z"]:

    for i in range(21):

        columnas.append(f"{eje}{i}")


X = datos[columnas]

y = datos["sena"]


# ============================================================
# 3. MOSTRAR CANTIDAD POR LETRA
# ============================================================

print("\n========================================")
print("MUESTRAS POR LETRA")
print("========================================")

print(
    y.value_counts().sort_index()
)


# ============================================================
# 4. DIVIDIR DATASET
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("\nEntrenamiento:", len(X_train))
print("Prueba:", len(X_test))


# ============================================================
# 5. CREAR MODELO
# ============================================================

print("\n========================================")
print("ENTRENANDO RANDOM FOREST")
print("========================================")


modelo = RandomForestClassifier(

    n_estimators=500,

    random_state=42,

    n_jobs=-1
)


modelo.fit(
    X_train,
    y_train
)


# ============================================================
# 6. PREDICCIONES
# ============================================================

predicciones = modelo.predict(
    X_test
)


# ============================================================
# 7. ACCURACY GENERAL
# ============================================================

accuracy = accuracy_score(

    y_test,

    predicciones
)


print("\n========================================")
print("RESULTADO GENERAL")
print("========================================")

print(
    f"Accuracy: {accuracy:.4f}"
)


# ============================================================
# 8. REPORTE POR LETRA
# ============================================================

print("\n========================================")
print("PRECISION POR LETRA")
print("========================================")

reporte = classification_report(

    y_test,

    predicciones,

    digits=4
)

print(reporte)


# ============================================================
# 9. MATRIZ DE CONFUSION
# ============================================================

print("\n========================================")
print("MATRIZ DE CONFUSION")
print("========================================")

clases = sorted(
    y.unique()
)

matriz = confusion_matrix(

    y_test,

    predicciones,

    labels=clases
)


print("\nOrden de letras:")

print(
    clases
)

print("\nMatriz:")

print(
    matriz
)


# ============================================================
# 10. GUARDAR DIAGNOSTICO
# ============================================================

print("\n========================================")
print("DIAGNOSTICO TERMINADO")
print("========================================")

print(
    "\nIMPORTANTE: NO SE MODIFICO modelo_lsm.pkl"
)