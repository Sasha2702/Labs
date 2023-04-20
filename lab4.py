import numpy as np


def ford_fulkerson(graph, source, sink):
    def bfs(graph, s, t, parent):
        visited = [False] * len(graph)
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    # ініціалізуємо максимальний потік нулями
    max_flow = 0

    # створюємо копію графа, щоб не змінювати вхідну матрицю
    r_graph = np.copy(graph)

    # список зберігає шлях від джерела до стоку
    parent = [-1] * len(graph)

    # поки є шлях від джерела до стоку, шукаємо мінімальний потік на шляху та оновлюємо максимальний потік
    while bfs(r_graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, r_graph[parent[s]][s])
        s = parent[s]

    max_flow += path_flow

    # оновлюємо вагу ребер на шляху
    v = sink
    while v != source:
        u = parent[v]
        r_graph[u][v] -= path_flow
        r_graph[v][u] += path_flow
        v = parent[v]

    return max_flow


graph = np.array([[0, 20, 20, 20, 0, 0, 0, 0],
                  [0, 0, 0, 0, 30, 0, 0, 0],
                  [0, 10, 0, 0, 0, 10, 20, 0],
                  [0, 0, 0, 0, 0, 15, 0, 0],
                  [0, 0, 10, 0, 0, 10, 0, 20],
                  [0, 0, 0, 0, 0, 0, 10, 20],
                  [0, 0, 0, 10, 0, 0, 0, 20],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

source = 0
sink = 7

print("Максимальний потік: ", ford_fulkerson(graph, source, sink))
