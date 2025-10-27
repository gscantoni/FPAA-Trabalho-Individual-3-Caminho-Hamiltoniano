# view.py
"""
Visualização do Caminho Hamiltoniano usando NetworkX e Matplotlib.
Autor: Guilherme Cantoni
Disciplina: Fundamentos de Projeto e Análise de Algoritmos
Professor: João Paulo Carneiro Aramuni
"""

import networkx as nx
import matplotlib.pyplot as plt
from main import hamiltonian_path


def draw_graph(graph):
    # Criação do grafo com NetworkX
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Busca o Caminho Hamiltoniano
    path = hamiltonian_path(graph)

    pos = nx.spring_layout(G, seed=42)  # Layout consistente

    # Desenha o grafo base
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightgray",
        node_size=1800,
        font_size=12,
        font_weight="bold",
        width=2,
        edge_color="gray"
    )

    if path:
        # Constrói as arestas do caminho encontrado
        edges_in_path = list(zip(path, path[1:]))

        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges_in_path,
            width=4,
            edge_color="red",
            style="solid"
        )

        print("Caminho Hamiltoniano encontrado:")
        print(" → ".join(path))
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")

    # Salva imagem na pasta assets
    plt.title("Caminho Hamiltoniano", fontsize=14, fontweight="bold")
    plt.savefig("assets/graph.png", format="PNG", dpi=300)
    plt.show()


if __name__ == "__main__":
    # Mesmo grafo do main.py
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    draw_graph(graph)
