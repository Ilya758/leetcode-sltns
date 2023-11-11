from collections import defaultdict
from heapq import *


class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = self.createGraph(edges)

    def createGraph(self, edges):
        graph = defaultdict(list)

        for u,v,w in edges:
            graph[u].append([v,w])
            graph[v] = graph.get(v, [])

        return graph


    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.graph[u].append([v, w])
        self.graph[v] = self.graph.get(v, [])

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = { node: float('inf') for node in self.graph }
        cameFrom = { node: None for node in self.graph }    
        distances[node1] = 0
        queue = [(0, node1)]

        while queue:
            dist, node = heappop(queue)

            if node == node2: return dist

            for nextNode, weight in self.graph[node]:
                nextDist = dist + weight
                
                if nextDist < distances[nextNode]:
                    distances[nextNode] = nextDist
                    cameFrom[nextNode] = node
                    heappush(queue,(nextDist, nextNode))
    
        return -1

    
n, edges = [4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]]


obj = Graph(n, edges)
obj.addEdge([1, 3, 4])
print(obj.shortestPath(3, 2))
