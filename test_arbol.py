from mini_ds.arbol import insertar, buscar, en_orden

def test_arbol():
    raiz = None
    for v in [5, 3, 8, 1, 4]:
        raiz = insertar(raiz, v)
    assert buscar(raiz, 4) is True
    assert buscar(raiz, 9) is False
    assert en_orden(raiz) == [1, 3, 4, 5, 8]
