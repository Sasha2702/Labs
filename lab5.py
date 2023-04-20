import networkx as nx
import matplotlib.pyplot as plt

# граф G1
G1 = nx.Graph()
G1.add_nodes_from([1, 2, 3, 4, 5])
G1.add_edges_from([(1, 2), (1, 4), (2, 3), (2, 5), (3, 5), (4, 5)])

# граф G2
G2 = nx.Graph()
G2.add_nodes_from([6, 7, 8, 9, 10])
G2.add_edges_from([(6, 7), (6, 9), (7, 8), (7, 10), (8, 10), (9, 10)])

# візуалізація графів
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

nx.draw(G1, with_labels=True, font_weight='bold', ax=ax1)
ax1.set_title('G1')

nx.draw(G2, with_labels=True, font_weight='bold', ax=ax2)
ax2.set_title('G2')

plt.show()
