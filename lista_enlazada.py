def insertar_inicio(cabeza, valor):
    return [valor, cabeza]

def recorrer(cabeza):
    resultado = []
    actual = cabeza
    while actual is not None:
        resultado.append(actual[0])
        actual = actual[1]
    return resultado

def buscar(cabeza, valor):
    actual = cabeza
    while actual is not None:
        if actual[0] == valor:
            return True
        actual = actual[1]
    return False