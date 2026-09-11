import cv2
import time

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos
from modulos.capturador_lsm import CapturadorLSM
from modulos.capturador_dinamico import CapturadorDinamicoLSM


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

FRAMES_DINAMICOS = 30

INTERVALO_DINAMICO = 0.05

INTERVALO_ESTATICO = 0.15


# ==========================================================
# SEÑAS ESTÁTICAS
# ==========================================================

SENAS_ESTATICAS = {
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "Y"
}


# ==========================================================
# SEÑAS DINÁMICAS
# ==========================================================

SENAS_DINAMICAS = {
    "J", "K", "LL", "Ñ", "RR", "X", "Z"
}


# ==========================================================
# INICIALIZAR
# ==========================================================

camara = iniciar_camara()

detector = DetectorManos()

capturador_estatico = CapturadorLSM()

capturador_dinamico = CapturadorDinamicoLSM()


# ==========================================================
# VARIABLES
# ==========================================================

sena_actual = None

ultimo_guardado = 0

contador = 0

capturando_dinamica = False

esperando_inicio = False

frame_dinamico = 0

secuencia_actual = 0


# ==========================================================
# TECLAS
# ==========================================================

teclas = {

    ord("a"): "A",
    ord("b"): "B",
    ord("c"): "C",
    ord("d"): "D",
    ord("e"): "E",
    ord("f"): "F",
    ord("g"): "G",
    ord("h"): "H",
    ord("i"): "I",
    ord("j"): "J",
    ord("k"): "K",
    ord("l"): "L",
    ord("m"): "M",
    ord("n"): "N",
    ord("o"): "O",
    ord("p"): "P",
    ord("q"): "Q",
    ord("r"): "R",
    ord("s"): "S",
    ord("t"): "T",
    ord("u"): "U",
    ord("v"): "V",
    ord("w"): "W",
    ord("x"): "X",
    ord("y"): "Y",
    ord("z"): "Z"
}


# ==========================================================
# TECLAS ESPECIALES
# ==========================================================

# LL
TECLA_LL = ord("1")

# Ñ
TECLA_ENE = ord("2")

# RR
TECLA_RR = ord("3")


# Z
TECLA_Z = ord("4")



# ==========================================================
# FUNCIÓN DE TEXTO
# ==========================================================

def texto(
    frame,
    mensaje,
    posicion,
    escala=0.7,
    color=(0, 255, 0),
    grosor=2
):

    cv2.putText(
        frame,
        mensaje,
        posicion,
        cv2.FONT_HERSHEY_SIMPLEX,
        escala,
        color,
        grosor
    )


# ==========================================================
# MENÚ
# ==========================================================

print()
print("==========================================")
print("        AURELIO - CAPTURA LSM")
print("==========================================")
print()

print("ESTÁTICAS:")
print("A B C D E F G H I L M N O P Q R")
print("S T U V W Y")
print()

print("DINÁMICAS:")
print("J K LL Ñ RR X Z")
print()

print("CONTROLES:")
print("A-Z  -> seleccionar letra")
print("1    -> LL")
print("2    -> Ñ")
print("3    -> RR")
print("ENTER -> iniciar dinámica")
print("ESC  -> cancelar / salir")
print()

print("==========================================")
print()


# ==========================================================
# LOOP
# ==========================================================

while True:

    ret, frame = camara.read()

    if not ret:

        print("No se pudo leer la cámara.")

        break


    manos = detector.detectar(frame)


    # ======================================================
    # DINÁMICA EN PROCESO
    # ======================================================

    if capturando_dinamica:

        texto(
            frame,
            "DINAMICA: " + sena_actual,
            (30, 45),
            0.9
        )

        texto(
            frame,
            f"Frame: {frame_dinamico}/{FRAMES_DINAMICOS}",
            (30, 85),
            0.75,
            (255, 255, 0)
        )

        texto(
            frame,
            "REALIZA EL MOVIMIENTO",
            (30, 125),
            0.7
        )

        texto(
            frame,
            "ESC = cancelar",
            (30, 160),
            0.6,
            (255, 255, 255)
        )


        if len(manos) > 0:

            ahora = time.time()

            if ahora - ultimo_guardado >= INTERVALO_DINAMICO:

                frame_dinamico += 1

                capturador_dinamico.guardar_frame(
                    manos,
                    sena_actual,
                    secuencia_actual,
                    frame_dinamico
                )

                ultimo_guardado = ahora


        # ==================================================
        # TERMINAR SECUENCIA
        # ==================================================

        if frame_dinamico >= FRAMES_DINAMICOS:

            print()
            print("------------------------------------------")
            print("SECUENCIA COMPLETADA")
            print("Seña:", sena_actual)
            print("Secuencia:", secuencia_actual)
            print("Frames:", frame_dinamico)
            print("------------------------------------------")
            print()

            capturando_dinamica = False

            esperando_inicio = False

            frame_dinamico = 0

            sena_actual = None

            contador += 1


    # ======================================================
    # ESPERANDO ENTER
    # ======================================================

    elif esperando_inicio:

        texto(
            frame,
            "DINAMICA: " + sena_actual,
            (30, 50),
            0.9
        )

        texto(
            frame,
            "Presiona ENTER para comenzar",
            (30, 90),
            0.7,
            (255, 255, 0)
        )

        texto(
            frame,
            "ESC = cancelar",
            (30, 125),
            0.6,
            (255, 255, 255)
        )


    # ======================================================
    # ESTÁTICA
    # ======================================================

    elif sena_actual in SENAS_ESTATICAS:

        texto(
            frame,
            "ESTATICA: " + sena_actual,
            (30, 50),
            0.9
        )

        texto(
            frame,
            "Muestras: " + str(contador),
            (30, 90),
            0.7,
            (255, 255, 0)
        )

        texto(
            frame,
            "ESC = salir",
            (30, 125),
            0.6,
            (255, 255, 255)
        )


        if len(manos) > 0:

            ahora = time.time()

            if ahora - ultimo_guardado >= INTERVALO_ESTATICO:

                capturador_estatico.guardar(
                    manos,
                    sena_actual
                )

                contador += 1

                ultimo_guardado = ahora


    # ======================================================
    # SIN SEÑA
    # ======================================================

    else:

        texto(
            frame,
            "Seleccione una sena",
            (30, 50),
            0.8
        )

        texto(
            frame,
            "A-Z = seleccionar",
            (30, 90),
            0.6
        )

        texto(
            frame,
            "1 = LL | 2 = Ñ | 3 = RR",
            (30, 120),
            0.6
        )


    # ======================================================
    # MOSTRAR CÁMARA
    # ======================================================

    cv2.imshow(
        "AURELIO CAPTURA LSM",
        frame
    )


    # ======================================================
    # TECLADO
    # ======================================================

    tecla = cv2.waitKey(1) & 0xFF


    # ======================================================
    # ESC
    # ======================================================

    if tecla == 27:

        if capturando_dinamica:

            print("Secuencia cancelada.")

            capturando_dinamica = False

            frame_dinamico = 0

            esperando_inicio = False

            sena_actual = None


        elif esperando_inicio:

            print("Selección cancelada.")

            esperando_inicio = False

            sena_actual = None


        else:

            print("Cerrando captura...")

            break


    # ======================================================
    # ENTER
    # ======================================================

    if tecla == 13:

        if (
            esperando_inicio
            and sena_actual in SENAS_DINAMICAS
        ):

            secuencia_actual += 1

            frame_dinamico = 0

            ultimo_guardado = 0

            capturando_dinamica = True

            esperando_inicio = False


            capturador_dinamico.nueva_secuencia(
                sena_actual,
                secuencia_actual
            )


    # ======================================================
    # LL
    # ======================================================

    if tecla == TECLA_LL:

        sena_actual = "LL"

        contador = 0

        esperando_inicio = True

        capturando_dinamica = False

        frame_dinamico = 0

        print("Seña seleccionada: LL")


    # ======================================================
    # Ñ
    # ======================================================

    if tecla == TECLA_ENE:

        sena_actual = "Ñ"

        contador = 0

        esperando_inicio = True

        capturando_dinamica = False

        frame_dinamico = 0

        print("Seña seleccionada: Ñ")


    # ======================================================
    # RR
    # ======================================================

    if tecla == TECLA_RR:

        sena_actual = "RR"

        contador = 0

        esperando_inicio = True

        capturando_dinamica = False

        frame_dinamico = 0

        print("Seña seleccionada: RR")


    # ======================================================
    # A-Z
    # ======================================================

    if tecla in teclas:

        sena_actual = teclas[tecla]

        contador = 0

        frame_dinamico = 0

        capturando_dinamica = False


        if sena_actual in SENAS_DINAMICAS:

            esperando_inicio = True

            print()
            print("------------------------------------------")
            print("Seña dinámica seleccionada:", sena_actual)
            print("Presiona ENTER para comenzar.")
            print("------------------------------------------")
            print()

        else:

            esperando_inicio = False

            print()
            print("------------------------------------------")
            print("Seña estática seleccionada:", sena_actual)
            print("Mantén la mano en posición.")
            print("------------------------------------------")
            print()


# ==========================================================
# CERRAR
# ==========================================================

camara.release()

cv2.destroyAllWindows()

print()
print("==========================================")
print("       CAPTURA FINALIZADA ingrith ")
print("==========================================")