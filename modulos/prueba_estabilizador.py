from estabilizador import EstabilizadorLSM


estabilizador = EstabilizadorLSM(repeticiones=5)


pruebas = [
    "A",
    "A",
    "A",
    "A",
    "A",

    "B",
    "B",
    "C",
    "B",
    "B",

    "H",
    "H",
    "H",
    "H",
    "H"
]


for letra in pruebas:

    resultado = estabilizador.filtrar(letra)

    print(
        "Entrada:",
        letra,
        " | Resultado:",
        resultado
    )