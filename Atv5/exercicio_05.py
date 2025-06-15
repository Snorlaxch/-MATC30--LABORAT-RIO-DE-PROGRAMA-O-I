from collections import defaultdict

def similar_pair(n, k, edges):
    tree = defaultdict(list)
    children = set()

    # construir grafo
    for pai, filho in edges:
        tree[pai].append(filho)
        children.add(filho)

    # raiz é o nó que não é filho de ninguém
    all_nodes = set(range(1, n + 1))
    raiz = list(all_nodes - children)[0]

    contador = 0
    caminho = []

    def dfs(no):
        nonlocal contador
        for ancestral in caminho:
            if abs(ancestral - no) <= k:
                contador += 1
        caminho.append(no)
        for vizinho in tree[no]:
            dfs(vizinho)
        caminho.pop()

    dfs(raiz)
    return contador

if __name__ == "__main__":

    # Exemplo do enunciado
    n = 5
    k = 2
    edges = [(3, 2), (3, 1), (1, 4), (1, 5)]

    print(similar_pair(n, k, edges))  # Esperado: 4


    casos = [
    (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),       # → 4
    (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),# → 7
    (4, 1, [(1, 2), (2, 3), (3, 4)]),               # → 3
    (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]), # → 9
    (3, 0, [(1, 2), (2, 3)])                        # → 0
    ]

    for i, (n, k, edges) in enumerate(casos, 1):
        print(f"Teste {i} ➡ {similar_pair(n, k, edges)}")
