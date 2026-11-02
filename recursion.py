def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return -1                      # caso base: no está
    
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio                   # caso base: lo encontré
    
    if lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)
    
    return busqueda_binaria(lista, objetivo, inicio, medio - 1)

def invertir(lista):
    if len(lista) <= 1:
        return lista
    return invertir(lista[1:]) + [lista[0]]