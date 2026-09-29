# Algoritmo básico de prueba: calcula el copago según el nivel del afiliado
def calcular_copago(valor_servicio, nivel):
    porcentajes = {1: 0.11, 2: 0.17, 3: 0.23}
    if nivel not in porcentajes:
        return "Nivel no válido"
    return round(valor_servicio * porcentajes[nivel], 2)

print(calcular_copago(100000, 1))
print(calcular_copago(100000, 3))
print(calcular_copago(100000, 9))
