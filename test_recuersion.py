from recursion import factorial, potencia, fibonacci, busqueda_binaria, invertir

def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8

def test_busqueda_binaria():
    lista = [1, 3, 5, 7, 9, 11]
    assert busqueda_binaria(lista, 7) == 3
    assert busqueda_binaria(lista, 1) == 0
    assert busqueda_binaria(lista, 4) == -1
    assert busqueda_binaria(lista, 100) == -1

def test_invertir():
    assert invertir([1, 2, 3]) == [3, 2, 1]
    assert invertir([]) == []
    assert invertir([7]) == [7]