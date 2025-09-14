"""
promedio_temperaturas.py
Archivo para calcular el promedio de temperaturas por ciudad.
"""

def calcular_promedios(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad.

    Parámetros:
        temperaturas (dict): clave = ciudad, valor = lista de temperaturas (números)

    Retorna:
        dict: clave = ciudad, valor = promedio (float redondeado a 2 decimales)
    """
    promedios = {}
    for ciudad, valores in temperaturas.items():
        if not valores:  # si no hay datos
            promedios[ciudad] = None
            continue
        promedio = sum(valores) / len(valores)
        promedios[ciudad] = round(promedio, 2)
    return promedios


if __name__ == "__main__":
    # ==========================
    # EJEMPLO DE DATOS
    # ==========================
    temperaturas = {
        "Quito": [18, 20, 19, 17],
        "Guayaquil": [28, 30, 29, 31],
        "Cuenca": [15, 16, 14, 15]
    }

    resultado = calcular_promedios(temperaturas)

    print("Promedios de temperatura por ciudad:")
    for ciudad, prom in resultado.items():
        if prom is None:
            print(f"- {ciudad}: No hay datos")
        else:
            print(f"- {ciudad}: {prom} °C")
