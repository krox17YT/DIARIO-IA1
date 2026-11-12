from lista_enlazada import insertar_inicio, recorrer, buscar

def test_lista():
    cabeza = None
    cabeza = insertar_inicio(cabeza, 3)
    cabeza = insertar_inicio(cabeza, 2)
    cabeza = insertar_inicio(cabeza, 1)
    assert recorrer(cabeza) == [1, 2, 3]
    assert buscar(cabeza, 2) is True
    assert buscar(cabeza, 9) is False