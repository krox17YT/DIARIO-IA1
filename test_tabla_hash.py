from tabla_hash import crear_tabla, insertar, buscar

def test_tabla_hash():
    t = crear_tabla(7)
    insertar(t, 10, "a")
    insertar(t, 17, "b")
    insertar(t, 45, "c")
    assert buscar(t, 10) == "a"
    assert buscar(t, 17) == "b"
    assert buscar(t, 45) == "c"
    assert buscar(t, 99) is None
    insertar(t, 17, "z")
    assert buscar(t, 17) == "z"
    