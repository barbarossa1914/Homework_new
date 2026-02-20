from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)


graph_1 = Graph()

n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

meets = [(start[i], end[i]) for i in range(n)]
meets = list(sorted(meets, key=lambda x: x[1]))

c = 1
current = 0
for i in range(1, n):
    if meets[i][0] > meets[current][1]:
        c += 1
        current = i

print(c)
