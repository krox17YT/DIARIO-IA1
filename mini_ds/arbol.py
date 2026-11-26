def insertar(raiz, valor):
    if raiz is None:
        return [valor, None, None]
    if valor < raiz[0]:
        raiz[1] = insertar(raiz[1], valor)
    elif valor > raiz[0]:
        raiz[2] = insertar(raiz[2], valor)
    return raiz

def buscar(raiz, valor):
    if raiz is None:
        return False
    if valor == raiz[0]:
        return True
    if valor < raiz[0]:
        return buscar(raiz[1], valor)
    return buscar(raiz[2], valor)

def en_orden(raiz):
    if raiz is None:
        return []
    return en_orden(raiz[1]) + [raiz[0]] + en_orden(raiz[2])