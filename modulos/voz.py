import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def hablar(texto):
    print("AURELIO:", texto)

    engine.say(texto)
    engine.runAndWait()


if __name__ == "__main__":
    hablar("Hola, soy Aurelio. Sistema de asistencia iniciado.")