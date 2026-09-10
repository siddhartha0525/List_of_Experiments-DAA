# Prim's Algorithm - Minimum Spanning Tree

INF = 999999

# Graph represented using adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

n = len(graph)

selected = [False] * n
selected[0] = True

print("Edges in Minimum Spanning Tree:")

total_cost = 0

for _ in range(n - 1):
    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", graph[x][y])

    total_cost += graph[x][y]
    selected[y] = True

print("Minimum cost:", total_cost)
