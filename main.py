#192521344(nandhini V)                            
def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    total_weight = 0

    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j

        print(f"{x} - {y} : {graph[x][y]}")
        total_weight += graph[x][y]
        selected[y] = True

    print("Total weight =", total_weight)

graph = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]

prim_mst(graph)
