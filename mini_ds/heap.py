def insertar(heap, valor):
    heap.append(valor)
    i = len(heap) - 1
    while i > 0:
        padre = (i - 1) // 2
        if heap[i] < heap[padre]:
            heap[i], heap[padre] = heap[padre], heap[i]
            i = padre
        else:
            break

def minimo(heap):
    return heap[0]

def extraer_min(heap):
    menor = heap[0]
    ultimo = heap.pop()
    if heap:
        heap[0] = ultimo
        i = 0
        n = len(heap)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            menor_idx = i
            if izq < n and heap[izq] < heap[menor_idx]:
                menor_idx = izq
            if der < n and heap[der] < heap[menor_idx]:
                menor_idx = der
            if menor_idx == i:
                break
            heap[i], heap[menor_idx] = heap[menor_idx], heap[i]
            i = menor_idx
    return menor