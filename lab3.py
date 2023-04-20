import sys

import networkx as nx
from matplotlib import pyplot as plt


def tsp_algorithm(graph):
    n = len(graph)
    # Передбачаємо, що вершина 0 є початковою та кінцевою точкою
    start_vertex = 0
    # Використовуємо метод гілки та межі, щоб знайти найкоротший цикл комівояжера
    # Починаємо з першої вершини
    visited = [False] * n
    visited[start_vertex] = True
    path = [start_vertex]
    total_cost = 0
    # Цикл для вибору наступної вершини для відвідування
    for i in range(n - 1):
        min_cost = sys.maxsize
        next_vertex = None
        current_vertex = path[-1]
        # Знаходимо наступну вершину, яка ще не відвідана та має найменший ваговий коефіцієнт
        for j in range(n):
            if not visited[j] and graph[current_vertex][j] < min_cost:
                next_vertex = j
                min_cost = graph[current_vertex][j]
        # Додаємо наступну вершину в шлях та відзначаємо її як відвідану
        path.append(next_vertex)
        visited[next_vertex] = True
        total_cost += min_cost
    # Додаємо повернення до початкової вершини
    path.append(start_vertex)
    total_cost += graph[path[-2]][start_vertex]
    return path, total_cost


def prim_algorithm(graph):
    n = len(graph)
    # Починаємо з першої вершини
    start_vertex = 0
    # Ініціалізуємо масив відвіданих вершин та масив ребер мінімального остовного дерева
    visited = [False] * n
    mst = []
    # Відзначаємо початкову вершину як відвідану
    visited[start_vertex] = True
    # Цикл, який обирає n-1 ребер
    for i in range(n - 1):
        min_cost = sys.maxsize
        source_vertex = None
        dest_vertex = None
        # Знаходимо ребро з найменшою вагою, що з'єднує відвідану вершину

        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if not visited[k] and graph[j][k] < min_cost:
                        source_vertex = j
    dest_vertex = k
    min_cost = graph[j][k]
    # Додаємо ребро в мінімальне остовне дерево та відзначаємо наступну вершину як відвідану
    mst.append((source_vertex, dest_vertex))
    visited[dest_vertex] = True
    return mst


graph = [[0, 0, 69, 60, 10, 20],
         [0, 0, 0, 31, 39, 2],
         [69, 0, 0, 0, 59, 0],
         [60, 31, 0, 0, 0, 36],
         [10, 39, 59, 0, 0, 79],
         [20, 2, 0, 36, 79, 0]]

mst = prim_algorithm(graph)
path, total_cost = tsp_algorithm(graph)

print("Мінімальне остовне дерево:")
for edge in mst:
    print(edge[0], "-", edge[1])
print("Найкоротший цикл комівояжера:")
print(" -> ".join([str(x) for x in path]))
print("Вага циклу:", total_cost)

G = nx.Graph()

for i in range(len(graph)):
    for j in range(i+1, len(graph)):
        if graph[i][j] != 0:
            G.add_edge(i, j, weight=graph[i][j])

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
path_colors = ['gray' if edge in path_edges else 'gray' for edge in G.edges()]

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=path_colors, width=2)
plt.axis('off')
plt.show()
