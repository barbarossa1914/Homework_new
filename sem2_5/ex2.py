import random
import time
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

    def prim(self, start=None):
        if not self.vertices:
            return 0, []

        if start is None:
            start = min(self.vertices)

        visited = set()
        pq = []
        heapq.heappush(pq, (0, start, -1))

        total_weight = 0
        edges = []

        while pq:
            weight, node, parent = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            total_weight += weight
            if parent != -1:
                edges.append((parent, node, weight))

            for neighbor, w in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (w, neighbor, node))

        return total_weight, edges

    def get_edges(self):
        edges = []
        for u in self.graph:
            for v, cost in self.graph[u]:
                if u < v:
                    edges.append((u, v, cost))
        return edges

    def kruskal(self):
        edges = self.get_edges()
        edges.sort(key=lambda x: x[2])

        dsu = DSU(self.vertices)

        mst_edges = []
        total_weight = 0

        for u, v, cost in edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, cost))
                total_weight += cost

        return total_weight, mst_edges


class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True


def generate_test(n, m):
    edges = []
    for i in range(1, n):
        u = i
        v = random.randint(0, i - 1)
        w = random.randint(1, 100)
        edges.append((u, v, w))

    additional = m - (n - 1)
    for _ in range(additional):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            w = random.randint(1, 100)
            edges.append((u, v, w))

    return edges, n


def create_graph(edges, n):
    g = Graph()
    for i in range(n):
        g.vertices.add(i)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g


tests = [
    (5, 8), (5, 10), (7, 15),
    (20, 50), (20, 100), (30, 150),
    (50, 60), (100, 120), (200, 250),
    (30, 200), (40, 400), (50, 600),
    (30, 400), (40, 700), (50, 1000)
]

linear1 = [(i, i + 1, random.randint(1, 50)) for i in range(99)]
linear2 = [(i, i + 1, random.randint(1, 50)) for i in range(199)]

dense1 = []
n1 = 40
for i in range(n1):
    for j in range(i + 1, n1):
        if random.random() < 0.8:
            dense1.append((i, j, random.randint(1, 50)))

dense2 = []
n2 = 50
for i in range(n2):
    for j in range(i + 1, n2):
        if random.random() < 0.7:
            dense2.append((i, j, random.randint(1, 50)))

complete = []
n3 = 30
for i in range(n3):
    for j in range(i + 1, n3):
        complete.append((i, j, random.randint(1, 50)))

special_tests = [
    (linear1, 100, 99, "linear_100"),
    (linear2, 200, 199, "linear_200"),
    (dense1, 40, len(dense1), "dense_40"),
    (dense2, 50, len(dense2), "dense_50"),
    (complete, 30, len(complete), "complete_30")
]

print("Test, Vertices, Edges, Prim(s), Kruskal(s), MST_Weight")
print("-" * 70)

for i, (n, m) in enumerate(tests, 1):
    edges, _ = generate_test(n, m)
    g = create_graph(edges, n)

    start = time.time()
    pw, pe = g.prim()
    pt = time.time() - start

    start = time.time()
    kw, ke = g.kruskal()
    kt = time.time() - start

    print(f"Test{i}, {n}, {m}, {pt:.6f}, {kt:.6f}, {pw}")

for edges, n, m, name in special_tests:
    g = create_graph(edges, n)

    start = time.time()
    pw, pe = g.prim()
    pt = time.time() - start

    start = time.time()
    kw, ke = g.kruskal()
    kt = time.time() - start

    print(f"{name}, {n}, {m}, {pt:.6f}, {kt:.6f}, {pw}")