import cv2
import time

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos
from modulos.lsm_reconocedor import ReconocedorLSM
from modulos.voz import hablar


# ================================
# INICIALIZAR AURELIO
# ================================

camara = iniciar_camara()

detector = DetectorManos()

reconocedor = ReconocedorLSM()


ultima_sena = ""

tiempo_ultima_respuesta = 0


# ================================
# LOOP PRINCIPAL
# ================================

while True:

    ret, frame = camara.read()

    if not ret:
        break


    manos = detector.detectar(frame)


    sena = reconocedor.reconocer(manos)


    cv2.putText(
        frame,
        sena,
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )


    tiempo_actual = time.time()


    if sena != ultima_sena and sena not in ["Desconocido", "Sin mano"]:

        if tiempo_actual - tiempo_ultima_respuesta > 2:

            print("Seña detectada:", sena)

            hablar(sena)

            ultima_sena = sena

            tiempo_ultima_respuesta = tiempo_actual



    cv2.imshow(
        "AURELIO LSM",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



camara.release()

cv2.destroyAllWindows()