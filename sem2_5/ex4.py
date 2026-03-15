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
        self.graph[v].append((u, cost))

    def min_distance_to_centers(self, centers):
        dist = {v: 10 ** 9 for v in self.vertices}
        queue = []

        for c in centers:
            if c in self.vertices:
                dist[c] = 0
                heapq.heappush(queue, (0, c))

        while queue:
            d, u = heapq.heappop(queue)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(queue, (nd, v))

        return sum(d for d in dist.values() if d < 10 ** 9)


fl = input().split()
n = int(fl[0])
m = int(fl[1])
centers = [int(x) for x in fl[2:]]

g = Graph()

for _ in range(m):
    u, v, cost = map(int, input().split())
    g.add_edge(u, v, cost)

print(g.min_distance_to_centers(centers))