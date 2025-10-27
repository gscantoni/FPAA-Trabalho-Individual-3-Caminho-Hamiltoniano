# main.py
"""
Implementação do algoritmo de Caminho Hamiltoniano (backtracking)
Autor: Guilherme Cantoni
Disciplina: Fundamentos de Projeto e Análise de Algoritmos
Professor: João Paulo Carneiro Aramuni
"""

def hamiltonian_path(graph):
    n = len(graph)
    path = []

    def backtrack(v, visited):
        path.append(v)
        visited.add(v)

        if len(path) == n:
            return True  # Caminho completo encontrado

        for u in graph[v]:
            if u not in visited:
                if backtrack(u, visited):
                    return True

        path.pop()
        visited.remove(v)
        return False

    for start_vertex in graph:
        path.clear()
        if backtrack(start_vertex, set()):
            return path

    return None


if __name__ == "__main__":
    # Exemplo de grafo representado como dicionário de adjacência
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    result = hamiltonian_path(graph)

    if result:
        print("Caminho Hamiltoniano encontrado:")
        print(" → ".join(result))
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")
