# Algoritmo básico de prueba: valida si un afiliado está activo
afiliados = {"1001": "activo", "1002": "suspendido", "1003": "activo"}

def validar_afiliado(documento):
    estado = afiliados.get(documento)
    if estado is None:
        return "Afiliado no encontrado"
    return f"Afiliado {documento}: {estado}"

print(validar_afiliado("1001"))
print(validar_afiliado("1002"))
print(validar_afiliado("9999"))
