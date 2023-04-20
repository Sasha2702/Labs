import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Функція для знаходження мінімального шляху в графі
def minimum_spanning_tree(graph, start):
    # Створюємо порожній список відвіданих вершин та додаємо початкову вершину
    visited_vertices = set([start])
    # Створюємо список ребер
    edges = [
        (cost, start, to)
        for to, cost in enumerate(graph[start])
        if cost > 0
    ]
    heapq.heapify(edges)
    # Записуємо ребра, які складають мінімальне дерево
    mst_edges = []
    # Проходимо по всіх ребрах графу
    while edges:
        cost, frm, to = heapq.heappop(edges)
        # Якщо вершина 'to' ще не відвідана, додаємо її до списку відвіданих та додаємо ребро до мінімального дерева
        if to not in visited_vertices:
            visited_vertices.add(to)
            mst_edges.append((frm, to, cost))
            # Додаємо усі ребра, які виходять з вершини 'to' до списку ребер
            for to_next, cost in enumerate(graph[to]):
                if cost > 0 and to_next not in visited_vertices:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst_edges


# Вхідна матриця
matrix = [
    [0, 0, 0, 0, 86, 94, 51, 82],
    [0, 0, 81, 0, 20, 87, 0, 0],
    [0, 81, 0, 83, 41, 0, 0, 0],
    [0, 0, 81, 0, 0, 0, 0, 0],
    [86, 20, 41, 8, 0, 40, 0, 54],
    [94, 87, 0, 0, 40, 0, 89, 0],
    [51, 0, 0, 0, 0, 89, 0, 18],
    [82, 0, 0, 0, 54, 0, 18, 0]
]

# Відображення графу
graph = {}
for i in range(len(matrix)):
    graph[i] = {}
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            graph[i][j] = matrix[i][j]

print("Graph:")

# Створення графу
G = nx.Graph()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            G.add_edge(i, j, weight=matrix[i][j])

# Відображення графу
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
