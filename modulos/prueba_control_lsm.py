from control_lsm import ControlLSM


control = ControlLSM()


prueba = [
    "A",
    "A",
    "A",
    "A",
    "A"
]


for letra in prueba:

    resultado = control.estabilizador.filtrar(letra)

    print(
        "Detectado:",
        letra,
        "Aceptado:",
        resultado
    )