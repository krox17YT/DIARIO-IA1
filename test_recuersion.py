from recursion import factorial, potencia, fibonacci

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
    