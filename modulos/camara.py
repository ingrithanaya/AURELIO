import cv2


def iniciar_camara():
    camara = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camara.isOpened():
        raise Exception("No se pudo abrir la cámara")

    return camara


def mostrar_camara():
    camara = iniciar_camara()

    while True:
        ret, frame = camara.read()

        if not ret:
            break

        cv2.imshow("AURELIO - Camara", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camara.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mostrar_camara()
