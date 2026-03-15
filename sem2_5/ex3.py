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


    def prim(self, start_edge):
        v1, v2, c = start_edge[0], start_edge[1], start_edge[2]
        queue = []
        visited = {vertex: False for vertex in self.vertices}
        visited[v1] = True
        visited[v2] = True
        weight = c

        for neighbor in self.graph[v1]:
            if not visited[neighbor[0]]:
                heapq.heappush(queue, (neighbor[1], v1, neighbor[0]))

        for neighbor in self.graph[v2]:
            if not visited[neighbor[0]]:
                heapq.heappush(queue, (neighbor[1], v2, neighbor[0]))

        while queue:
            w, u, v = heapq.heappop(queue)

            if visited[v]:
                continue

            visited[v] = True
            weight += w

            for neighbor in self.graph[v]:
                if not visited[neighbor[0]]:
                    heapq.heappush(queue, (neighbor[1], v, neighbor[0]))

        return weight

ans = []
edges = []
gr = Graph()
nn, m = list(map(int, input().split()))
for i in range(m):
    u1, u2, cost = list(map(int, input().split()))
    gr.add_edge(u1, u2, cost)
    string = (u1, u2, cost)
    edges.append(string)
for el in edges:
    ans.append(gr.prim(el))

print(*ans, sep='\n')

