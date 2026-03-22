from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def matching(self):
        n = len(self.vertices)
        c = 1
        while n > 0:
            c *= n - 1
            n -= 2

        return c


N = int(input())
gr = Graph()
for i in range(1, N+1):
    gr.vertices.add(i)
print(gr.matching())
