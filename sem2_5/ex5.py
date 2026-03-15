from collections import defaultdict
import heapq


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v, cost):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append((v, cost))


    def prim(self, start=0):
        visited = {vertex: False for vertex in self.vertices}
        pq = []
        heapq.heappush(pq, (0, start, -1))

        total_weight = 0
        edges = []

        while pq:
            weight, node, parent = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            total_weight += weight
            if parent != -1:
                edges.append((parent, node, weight))

            for neighbor, w in self.graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(pq, (w, neighbor, node))

        return total_weight


n = int(input())
gr = Graph()
dots = []

for i in range(n):
    x, y = list(map(int, input().split()))
    dots.append((x, y))

for i in range(n):
    for j in range(n):
        if i != j:
            cost = ((dots[i][0] - dots[j][0])**2 + (dots[i][1] - dots[j][1])**2)**0.5
            gr.add_edge(dots[i], dots[j], cost)

print(gr.prim(dots[0]))

