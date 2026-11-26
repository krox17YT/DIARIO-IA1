def push(pila: list, x) -> None:
    pila.append(x)

def pop(pila: list):
    return pila.pop()

def peek(pila: list):
    return pila[-1]

def esta_vacia(pila: list) -> bool:
    return len(pila) == 0