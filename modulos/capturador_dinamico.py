import csv
import os
from datetime import datetime


CARPETA = "capturas"

ARCHIVO = os.path.join(
    CARPETA,
    "dataset_lsm_dinamico.csv"
)


class CapturadorDinamicoLSM:

    def __init__(self):

        os.makedirs(
            CARPETA,
            exist_ok=True
        )

        if not os.path.exists(ARCHIVO):

            with open(
                ARCHIVO,
                "w",
                newline="",
                encoding="utf-8"
            ) as archivo:

                escritor = csv.writer(archivo)

                escritor.writerow(
                    [
                        "fecha",
                        "sena",
                        "secuencia",
                        "frame",
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


    def guardar_frame(
        self,
        manos,
        sena,
        secuencia,
        frame_num
    ):

        if not manos:
            return


        with open(
            ARCHIVO,
            "a",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(
                archivo
            )


            for mano in manos:

                puntos = mano["puntos"]


                if len(puntos) != 21:
                    continue


                fila = [

                    datetime.now().isoformat(),

                    sena,

                    secuencia,

                    frame_num,

                    mano["mano"]

                ]


                # Coordenadas X

                for p in puntos:
                    fila.append(p.x)


                # Coordenadas Y

                for p in puntos:
                    fila.append(p.y)


                # Coordenadas Z

                for p in puntos:
                    fila.append(p.z)


                escritor.writerow(
                    fila
                )


    def nueva_secuencia(
        self,
        sena,
        secuencia
    ):

        print(
            "================================"
        )

        print(
            "Nueva secuencia:",
            secuencia
        )

        print(
            "Seña:",
            sena
        )

        print(
            "================================"
        )