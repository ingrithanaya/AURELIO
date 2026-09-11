import cv2
import time

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos
from modulos.predictor_lsm import PredictorLSM
from modulos.voz import hablar
from modulos.palabras_lsm import ConstructorPalabras
from modulos.estabilizador import EstabilizadorLSM


# ================================
# INICIALIZAR AURELIO
# ================================

camara = iniciar_camara()

detector = DetectorManos()

reconocedor = PredictorLSM()

constructor = ConstructorPalabras()

# NUEVO: estabilizador
estabilizador = EstabilizadorLSM(repeticiones=5)

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

    # Predicción del modelo
    sena = reconocedor.reconocer(manos)

    # Filtrar la predicción para evitar falsos positivos
    sena = estabilizador.filtrar(sena)

    # Mostrar texto en pantalla
    texto = sena if sena else ""
    cv2.putText(
        frame,
        texto,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    tiempo_actual = time.time()

    if sena is not None:

        if sena != ultima_sena:

            if tiempo_actual - tiempo_ultima_respuesta > 1:

                palabra = constructor.agregar_letra(sena)

                print("Seña detectada:", sena)
                print("Palabra actual:", palabra)

                palabra_detectada = constructor.verificar_palabra()

                if palabra_detectada:

                    print("AURELIO dice:", palabra_detectada)

                    hablar(palabra_detectada)

                ultima_sena = sena
                tiempo_ultima_respuesta = tiempo_actual

    cv2.imshow(
        "AURELIO LSM mapachitos",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camara.release()

cv2.destroyAllWindows()