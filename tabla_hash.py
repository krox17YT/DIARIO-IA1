def crear_tabla(tamano=7):
    tabla = []
    for i in range(tamano):
        tabla.append([])
    return tabla

def insertar(tabla, clave, valor):
    pos = clave % len(tabla)
    for par in tabla[pos]:
        if par[0] == clave:
            par[1] = valor
            return
    tabla[pos].append([clave, valor])

def buscar(tabla, clave):
    pos = clave % len(tabla)
    for par in tabla[pos]:
        if par[0] == clave:
            return par[1]
    return None