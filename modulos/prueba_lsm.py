import cv2

from camara import Camara
from mediapipe_detector import DetectorManos
from control_lsm import ControlLSM


# Inicializar módulos

camara = Camara()

detector = DetectorManos()

control = ControlLSM()


print("AURELIO LSM iniciado")
print("Presiona ESC para salir")


while True:

    frame = camara.leer()

    if frame is None:
        continue


    manos = detector.detectar(frame)


    letra = control.procesar(manos)


    if letra:

        print(
            "Seña aceptada:",
            letra
        )


    cv2.imshow(
        "AURELIO - LSM",
        frame
    )


    tecla = cv2.waitKey(1)


    if tecla == 27:
        break


camara.cerrar()

cv2.destroyAllWindows()