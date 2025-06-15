from exercicio_05 import similar_pair

def testar_exercicio_05():
    print("📘 Exercício 05 – Pares Similares em Árvore")
    casos = [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)], 4),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)], 7),
        (4, 1, [(1, 2), (2, 3), (3, 4)], 3),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)], 9),
        (3, 0, [(1, 2), (2, 3)], 0),
    ]
    for i, (n, k, edges, esperado) in enumerate(casos, 1):
        resultado = similar_pair(n, k, edges)
        print(f"Teste {i} ➜ Esperado: {esperado}, Obtido: {resultado}")
    print()

testar_exercicio_05()