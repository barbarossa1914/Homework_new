from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.vertices.add(u)
        self.vertices.add(v)

    def ford_bellman(self, start):
        dist = {vertex: 10 ** 9 for vertex in self.vertices}
        dist[start] = 0

        for i in range(0, len(self.vertices)):
            for vertex in self.vertices:
                for neighbor in self.graph[vertex]:
                    if dist[neighbor[0]] > dist[vertex] + neighbor[1]:
                        dist[neighbor[0]] = dist[vertex] + neighbor[1]


        for vertex in self.vertices:
            for neighbor in self.graph[vertex]:
                if dist[neighbor[0]] > dist[vertex] + neighbor[1]:
                    return 'возможно'

        return 'невозможно'


o = int(input())
ans = list()
for i in range(o):
    curr_graph = Graph()
    n, m = list(map(int, input().split()))
    for j in range(m):
        x, y, t = list(map(int, input().split()))
        curr_graph.add_edge(x, y, t)
    ans.append(curr_graph.ford_bellman(0))

print(*ans, sep='\n')
