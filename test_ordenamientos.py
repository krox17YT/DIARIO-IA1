from ordenamientos import selection_sort, bubble_sort, merge_sort

def test_ordenamientos():
    lista = [5, 3, 1, 4, 2]
    esperado = [1, 2, 3, 4, 5]
    assert selection_sort(lista) == esperado
    assert bubble_sort(lista) == esperado
    assert merge_sort(lista) == esperado
    assert merge_sort([]) == []
    