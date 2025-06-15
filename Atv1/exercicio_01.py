def resolver_labirinto(n, m, k, maze, tunnels):
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10000)

    # Representar túneis como dicionário bidirecional
    tunnel_map = {}
    for i1, j1, i2, j2 in tunnels:
        tunnel_map[(i1, j1)] = (i2, j2)
        tunnel_map[(i2, j2)] = (i1, j1)

    # Localizar posição inicial
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                start = (i, j)

    # Memoização
    memo = {}

    def dentro(i, j):
        return 0 <= i < n and 0 <= j < m

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        cell = maze[i][j]

        # Casos base
        if cell == '*':
            return 0.0
        if cell == '%':
            return 1.0

        # Verifica se há túnel
        if (i, j) in tunnel_map:
            i, j = tunnel_map[(i, j)]
            cell = maze[i][j]
            if cell == '*':
                return 0.0
            if cell == '%':
                return 1.0

        # Explorar vizinhos válidos
        vizinhos = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+dx, j+dy
            if dentro(ni, nj) and maze[ni][nj] != '#':
                vizinhos.append((ni, nj))

        if not vizinhos:
            return 0.0

        prob = 0.0
        for ni, nj in vizinhos:
            prob += dfs(ni, nj)
        prob /= len(vizinhos)

        memo[(i, j)] = prob
        return prob

    return dfs(*start)


if __name__ == "__main__":

    n = 3
    m = 6
    k = 1
    maze = [
        "###*OO",
        "O#OA%O",
        "###*OO"
    ]
    tunnels = [(2, 3, 2, 1)]

    resultado = resolver_labirinto(n, m, k, maze, tunnels)
    print(f"{resultado:.6f}")
