import cv2
import time

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos
from modulos.capturador_lsm import CapturadorLSM


# ===============================
# INICIALIZAR AURELIO
# ===============================

camara = iniciar_camara()

detector = DetectorManos()

capturador = CapturadorLSM()


sena_actual = None

ultimo_guardado = 0

contador = 0


print("==============================")
print("     AURELIO - CAPTURA LSM")
print("==============================")
print("")
print("Teclas:")
print("A -> capturar A")
print("B -> capturar B")
print("C -> capturar C")
print("H -> capturar HOLA")
print("G -> capturar GRACIAS")
print("Q -> salir")
print("")


# ===============================
# LOOP PRINCIPAL
# ===============================

while True:


    ret, frame = camara.read()


    if not ret:
        break



    manos = detector.detectar(frame)



    # Mostrar estado

    if sena_actual:

        texto = "CAPTURANDO: " + sena_actual

    else:

        texto = "Seleccione una sena"



    cv2.putText(
        frame,
        texto,
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )



    # ===============================
    # GUARDAR DATOS
    # ===============================


    if len(manos) > 0 and sena_actual:


        ahora = time.time()


        # Guarda cada 150 milisegundos

        if ahora - ultimo_guardado > 0.15:


            capturador.guardar(
                manos,
                sena_actual
            )


            contador += 1


            ultimo_guardado = ahora



    # Mostrar contador

    cv2.putText(
        frame,
        "Muestras: " + str(contador),
        (30,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,0),
        2
    )



    cv2.imshow(
        "AURELIO CAPTURA LSM",
        frame
    )



    # ===============================
    # TECLAS
    # ===============================


    tecla = cv2.waitKey(1) & 0xFF



    if tecla == ord("a"):

        sena_actual = "A"

        print("Capturando A")



    elif tecla == ord("b"):

        sena_actual = "B"

        print("Capturando B")



    elif tecla == ord("c"):

        sena_actual = "C"

        print("Capturando C")



    elif tecla == ord("h"):

        sena_actual = "HOLA"

        print("Capturando HOLA")



    elif tecla == ord("g"):

        sena_actual = "GRACIAS"

        print("Capturando GRACIAS")



    elif tecla == ord("q"):

        break



# ===============================
# CERRAR
# ===============================

camara.release()

cv2.destroyAllWindows()