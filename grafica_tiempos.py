import time
import random
import matplotlib.pyplot as plt
from mini_ds.ordenamientos import selection_sort, bubble_sort, merge_sort

tamanos = [100, 500, 1000, 2000, 4000]
algoritmos = {
    "selection sort": selection_sort,
    "bubble sort": bubble_sort,
    "merge sort": merge_sort,
    "sorted de Python": sorted,
}

for nombre, funcion in algoritmos.items():
    tiempos = []
    for n in tamanos:
        lista = []
        for _ in range(n):
            lista.append(random.randint(0, 100000))
        inicio = time.perf_counter()
        funcion(lista)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    plt.plot(tamanos, tiempos, marker="o", label=nombre)

plt.xlabel("n (tamaño de la lista)")
plt.ylabel("tiempo (segundos)")
plt.title("Tiempo de los ordenamientos")
plt.legend()
plt.savefig("grafica_tiempos.png")