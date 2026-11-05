def push(pila, x):
    pila.append(x)

def pop(pila):
    return pila.pop()

def peek(pila):
    return pila[-1]

def esta_vacia(pila):
    return len(pila) == 0