from grafo import bfs, dfs

GRAFO = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C"],
    "E": ["C"],
}

def test_bfs():
    assert bfs(GRAFO, "A") == ["A", "B", "C", "D", "E"]

def test_dfs():
    assert dfs(GRAFO, "A") == ["A", "B", "D", "C", "E"]