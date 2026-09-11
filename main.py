import cv2

from modulos.camara import iniciar_camara
from modulos.mediapipe_detector import DetectorManos
from modulos.predictor_lsm import PredictorLSM


# ==========================================
# CONFIGURACIÓN
# ==========================================

camara = iniciar_camara()
detector = DetectorManos()
reconocedor = PredictorLSM()


# ==========================================
# FUNCIÓN PARA OBTENER COLOR
# ==========================================

def obtener_color(compatibilidad):

    if compatibilidad >= 80:
        return "ALTA", (0, 255, 0)       # Verde

    elif compatibilidad >= 60:
        return "MEDIA", (0, 255, 255)     # Amarillo

    elif compatibilidad >= 40:
        return "BAJA", (0, 165, 255)      # Naranja

    else:
        return "MUY BAJA", (0, 0, 255)    # Rojo


# ==========================================
# BUCLE PRINCIPAL
# ==========================================

while True:

    ret, frame = camara.read()

    if not ret:
        print("No se pudo leer la cámara.")
        break


    # ==========================================
    # DETECTAR MANOS
    # ==========================================

    manos = detector.detectar(frame)


    # ==========================================
    # RECONOCER SEÑA
    # ==========================================

    sena, compatibilidad = reconocedor.reconocer(manos)


    # Evitar valores fuera del rango
    compatibilidad = max(0, min(100, compatibilidad))


    # ==========================================
    # ESTADO Y COLOR
    # ==========================================

    estado, color = obtener_color(compatibilidad)


    # ==========================================
    # INFORMACIÓN DE LA SEÑA
    # ==========================================

    cv2.putText(
        frame,
        f"SENA: {sena}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.putText(
        frame,
        f"Compatibilidad: {compatibilidad:.2f}%",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.putText(
        frame,
        f"Estado: {estado}",
        (30, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )


    # ==========================================
    # BARRA DE COMPATIBILIDAD
    # ==========================================

    # Posición
    x1 = 30
    y1 = 160

    ancho = 400
    alto = 30

    # Fondo de la barra
    cv2.rectangle(
        frame,
        (x1, y1),
        (x1 + ancho, y1 + alto),
        (60, 60, 60),
        -1
    )

    # Ancho proporcional al porcentaje
    ancho_barra = int(
        (compatibilidad / 100) * ancho
    )

    # Barra de progreso
    if ancho_barra > 0:

        cv2.rectangle(
            frame,
            (x1, y1),
            (x1 + ancho_barra, y1 + alto),
            color,
            -1
        )


    # Borde de la barra
    cv2.rectangle(
        frame,
        (x1, y1),
        (x1 + ancho, y1 + alto),
        (255, 255, 255),
        2
    )


    # ==========================================
    # PORCENTAJE SOBRE LA BARRA
    # ==========================================

    texto_porcentaje = f"{compatibilidad:.1f}%"

    tamaño_texto = cv2.getTextSize(
        texto_porcentaje,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        2
    )[0]

    texto_x = x1 + (ancho - tamaño_texto[0]) // 2
    texto_y = y1 + 22

    cv2.putText(
        frame,
        texto_porcentaje,
        (texto_x, texto_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # ==========================================
    # MOSTRAR CÁMARA
    # ==========================================

    cv2.imshow(
        "AURELIO - Diagnostico LSM",
        frame
    )


    # ==========================================
    # SALIR
    # ==========================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================
# CERRAR
# ==========================================

camara.release()
cv2.destroyAllWindows()