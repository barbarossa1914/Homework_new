from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited[start] = 1

        for u in self.graph[start]:
            if visited[u] == 1:
                return 1
            if visited[u] == 0:
                if self.dfs(u, visited):
                    return 1

        visited[start] = 2

    def cycle(self):
        for vertex in self.vertices:
            visited = {vertex: 0 for vertex in self.vertices}
            if self.dfs(vertex, visited):
                return 'Yes'
        return 'No'


n = int(input())
graph_1 = Graph()
for i in range(n):
    v1, v2 = list(map(int, input().split()))
    graph_1.add_edge(v1, v2)
print(graph_1.cycle())

