from heap import insertar, minimo, extraer_min

def test_heap():
    h = []
    for v in [5, 3, 8, 1, 4]:
        insertar(h, v)
    assert minimo(h) == 1
    assert extraer_min(h) == 1
    assert extraer_min(h) == 3
    assert extraer_min(h) == 4
    assert extraer_min(h) == 5
    assert extraer_min(h) == 8
    assert h == []