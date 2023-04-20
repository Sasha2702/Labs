import sys
import heapq


# Create a graph class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def primMST(self):
        # List to store minimum weight for each vertex
        key = [sys.maxsize] * self.V
        key[0] = 0  # Starting vertex is assigned a weight of 0
        mstSet = [False] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        parent[0] = -1  # Starting vertex is the root

        # Heap for extracting minimum weight
        minHeap = []
        heapq.heappush(minHeap, (0, 0))

        while minHeap:
            # Extract the minimum weight vertex
            minWeightVertex = heapq.heappop(minHeap)
            u = minWeightVertex[1]
            mstSet[u] = True

            # Update the minimum weight of adjacent vertices
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    heapq.heappush(minHeap, (key[v], v))
                    parent[v] = u

        self.printMST(parent)


# Driver code
if __name__ == "__main__":
    # Input matrix
    matrix = [
    [0, 3, 0, 0, 0, 34, 0, 80],
    [3, 0, 0, 1, 0, 0, 0, 68],
    [0, 0, 0, 0, 23, 0, 12, 0],
    [0, 1, 0, 0, 53, 0, 0, 39],
    [0, 0, 23, 53, 0, 0, 68, 14],
    [34, 0, 0, 0, 0, 0, 0, 25],
    [0, 0, 12, 0, 68, 0, 0, 99],
    [80, 68, 0, 39, 14, 25, 99, 0]
]

    # Create a graph object and run the algorithm
    g = Graph(8)
    g.graph = matrix
    g.primMST()
