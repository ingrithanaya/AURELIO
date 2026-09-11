import cv2
import pandas as pd
import numpy as np

RUTA_DATASET = "capturas/dataset_lsm.csv"

datos = pd.read_csv(RUTA_DATASET)

columnas_x = [f"x{i}" for i in range(21)]
columnas_y = [f"y{i}" for i in range(21)]
columnas_z = [f"z{i}" for i in range(21)]

print("=" * 50)
print("AURELIO - VISOR DE MUESTREO LSM")
print("=" * 50)

print("\nSeñas disponibles:")
print(sorted(datos["sena"].unique()))

sena = input("\nEscribe la letra que quieres revisar: ").strip().upper()

if sena not in datos["sena"].values:
    print(f"\nLa seña '{sena}' no existe en el dataset.")
    exit()

muestras = datos[datos["sena"] == sena].reset_index(drop=True)

print(f"\nSeña seleccionada: {sena}")
print(f"Muestras disponibles: {len(muestras)}")

indice = 0

while True:

    muestra = muestras.iloc[indice]

    imagen = np.zeros((700, 900, 3), dtype=np.uint8)

    puntos = []

    for i in range(21):
        x = float(muestra[f"x{i}"])
        y = float(muestra[f"y{i}"])

        px = int(x * 700)
        py = int(y * 600) + 50

        puntos.append((px, py))

    # Dibujar conexiones de la mano
    conexiones = [
        (0,1),(1,2),(2,3),(3,4),
        (0,5),(5,6),(6,7),(7,8),
        (5,9),(9,10),(10,11),(11,12),
        (9,13),(13,14),(14,15),(15,16),
        (13,17),(17,18),(18,19),(19,20),
        (0,17)
    ]

    for a, b in conexiones:
        cv2.line(
            imagen,
            puntos[a],
            puntos[b],
            (100, 100, 100),
            2
        )

    # Dibujar puntos
    for i, (x, y) in enumerate(puntos):

        cv2.circle(
            imagen,
            (x, y),
            7,
            (0, 255, 0),
            -1
        )

        cv2.putText(
            imagen,
            str(i),
            (x + 8, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255),
            1
        )

    # Información
    cv2.putText(
        imagen,
        f"SENA: {sena}",
        (30, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.putText(
        imagen,
        f"Muestra: {indice + 1} / {len(muestras)}",
        (600, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        imagen,
        "A/D: anterior/siguiente    Q: salir",
        (30, 680),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        1
    )

    cv2.imshow("AURELIO - Visor de Muestreo", imagen)

    tecla = cv2.waitKey(0) & 0xFF

    if tecla == ord("q"):
        break

    elif tecla == ord("d"):
        indice += 1

        if indice >= len(muestras):
            indice = 0

    elif tecla == ord("a"):
        indice -= 1

        if indice < 0:
            indice = len(muestras) - 1

cv2.destroyAllWindows()