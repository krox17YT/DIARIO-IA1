from cola import enqueue, dequeue, peek, esta_vacia

def test_cola():
    c = []
    enqueue(c, 1)
    enqueue(c, 2)
    assert peek(c) == 1
    assert dequeue(c) == 1
    assert dequeue(c) == 2
    assert esta_vacia(c)