def bfs(grafo, inicio):
    visitados = [inicio]
    cola = [inicio]
    while cola:
        actual = cola.pop(0)
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)
    return visitados

def dfs(grafo, inicio):
    visitados = []
    pila = [inicio]
    while pila:
        actual = pila.pop()
        if actual in visitados:
            continue
        visitados.append(actual)
        pila.extend(reversed(grafo.get(actual, [])))
    return visitados