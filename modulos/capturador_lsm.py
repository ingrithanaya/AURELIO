import csv
import os
import time

from datetime import datetime


CARPETA = "capturas"

ARCHIVO = os.path.join(
    CARPETA,
    "dataset_lsm.csv"
)


class CapturadorLSM:


    def __init__(self):

        os.makedirs(
            CARPETA,
            exist_ok=True
        )


        if not os.path.exists(ARCHIVO):

            with open(
                ARCHIVO,
                "w",
                newline=""
            ) as archivo:

                escritor = csv.writer(
                    archivo
                )

                escritor.writerow(
                    [
                        "fecha",
                        "sena",
                        "mano",
                        *[
                            f"x{i}"
                            for i in range(21)
                        ],
                        *[
                            f"y{i}"
                            for i in range(21)
                        ],
                        *[
                            f"z{i}"
                            for i in range(21)
                        ]
                    ]
                )


    def guardar(
        self,
        manos,
        sena
    ):


        with open(
            ARCHIVO,
            "a",
            newline=""
        ) as archivo:


            escritor = csv.writer(
                archivo
            )


            for mano in manos:


                puntos = mano["puntos"]


                fila = [

                    datetime.now(),

                    sena,

                    mano["mano"]

                ]


                for p in puntos:
                    fila.append(p.x)

                for p in puntos:
                    fila.append(p.y)

                for p in puntos:
                    fila.append(p.z)


                escritor.writerow(
                    fila
                )


        print(
            "Guardado:",
            sena
        )
