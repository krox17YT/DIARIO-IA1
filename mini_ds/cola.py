def enqueue(cola, x):
    cola.append(x)

def dequeue(cola):
    return cola.pop(0)

def peek(cola):
    return cola[0]

def esta_vacia(cola):
    return len(cola) == 0