from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def bfs(self, start):
        dist = {vertex: 10**9 for vertex in self.vertices}
        dist[start] = 0
        queue = []
        queue.append(start)

        while queue:
            current_vertex = queue.pop(0)
            for neighbor in self.graph[current_vertex]:
                if dist[neighbor] == 10**9:
                    dist[neighbor] = dist[current_vertex] + 1
                    queue.append(neighbor)

        return dist


n, m = list(map(int, input().split()))
graph_1 = Graph()

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    graph_1.add_edge(v1, v2)

dist = graph_1.bfs(0)

for i in range(n):
    print(dist[i])
