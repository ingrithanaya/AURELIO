import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import os


MODELO_MANOS = os.path.join(
    "modelos",
    "hand_landmarker.task"
)


class DetectorManos:

    def __init__(self):

        base_options = python.BaseOptions(
            model_asset_path=MODELO_MANOS
        )

        opciones = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=2
        )

        self.detector = vision.HandLandmarker.create_from_options(
            opciones
        )


    def detectar(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        imagen = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )


        resultado = self.detector.detect(
            imagen
        )


        manos_detectadas = []


        if resultado.hand_landmarks:


            for i, mano in enumerate(resultado.hand_landmarks):

                puntos = []


                for punto in mano:
                    puntos.append(punto)


                nombre_mano = "Desconocida"


                if resultado.handedness:


                    categoria = resultado.handedness[i][0]

                    nombre_mano = categoria.category_name



                # Dibujar puntos
                for punto in puntos:

                    x = int(
                        punto.x * frame.shape[1]
                    )

                    y = int(
                        punto.y * frame.shape[0]
                    )


                    cv2.circle(
                        frame,
                        (x,y),
                        5,
                        (0,255,0),
                        -1
                    )


                manos_detectadas.append(
                    {
                        "mano": nombre_mano,
                        "puntos": puntos
                    }
                )


        return manos_detectadas