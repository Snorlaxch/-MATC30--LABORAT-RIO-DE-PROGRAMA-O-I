from exercicio_01 import resolver_labirinto

def testar_exercicio_01():
    print("📘 Exercício 01 – Labirinto do Sapo")
    n, m, k = 3, 6, 1
    maze = [
        "###*OO",
        "O#OA%O",
        "###*OO"
    ]
    tunnels = [(2, 3, 2, 1)]
    prob = resolver_labirinto(n, m, k, maze, tunnels)
    print(f"Probabilidade de fuga esperada: 0.25")
    print(f"Probabilidade de fuga obtida  : {prob:.6f}\n")


testar_exercicio_01()