from pila import push, pop, peek, esta_vacia

def test_pila():
    p = []
    push(p, 1)
    push(p, 2)
    assert peek(p) == 2
    assert pop(p) == 2
    assert pop(p) == 1
    assert esta_vacia(p)