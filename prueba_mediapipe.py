import cv2

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos


# ================================
# INICIO
# ================================

camara = iniciar_camara()

detector = DetectorManos()


# ================================
# LOOP PRINCIPAL
# ================================

while True:

    ret, frame = camara.read()

    if not ret:
        break


    manos = detector.detectar(frame)


    cantidad = len(manos)


    print("----------------")
    print("Manos detectadas:", cantidad)


    for mano in manos:
        print(
            "Mano:",
            mano["mano"]
        )


    cv2.putText(
        frame,
        f"Manos detectadas: {cantidad}",
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )


    cv2.imshow(
        "AURELIO - Dos manos MediaPipe",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



camara.release()

cv2.destroyAllWindows()