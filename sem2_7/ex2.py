from collections import defaultdict, deque
import heapq


class Graph:
    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v, cost):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append((v, cost))

    def dijkstra(self, start):
        distances = {vertex: 10 ** 9 for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            dist, cur_vertex = heapq.heappop(pq)
            if dist > distances[cur_vertex]:
                continue
            for neighbor, cost in self.graph[cur_vertex]:
                new_dist = dist + cost
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return distances

class FlowNetwork:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        self.graph[u].append([v, cap, cost, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, len(self.graph[u]) - 1])

    def min_flow(self, s, t, flow_limit=10 ** 9):
        n = self.n
        prev_v = [0] * n
        prev_e = [0] * n
        pot = [0] * n

        flow = 0
        cost = 0
        while flow < flow_limit:
            dist = [10 ** 9] * n
            dist[s] = 0
            in_queue = [False] * n
            q = deque([s])
            in_queue[s] = True

            while q:
                u = q.popleft()
                in_queue[u] = False
                for i, (to, cap, c, rev) in enumerate(self.graph[u]):
                    if cap > 0 and dist[to] > dist[u] + c + pot[u] - pot[to]:
                        dist[to] = dist[u] + c + pot[u] - pot[to]
                        prev_v[to] = u
                        prev_e[to] = i
                        if not in_queue[to]:
                            q.append(to)
                            in_queue[to] = True

            if dist[t] == 10 ** 9:
                break

            for i in range(n):
                if dist[i] < 10 ** 9:
                    pot[i] += dist[i]

            aug_flow = flow_limit - flow
            v = t
            while v != s:
                u = prev_v[v]
                e_index = prev_e[v]
                aug_flow = min(aug_flow, self.graph[u][e_index][1])
                v = u

            v = t
            while v != s:
                u = prev_v[v]
                e_index = prev_e[v]
                rev_index = self.graph[u][e_index][3]
                self.graph[u][e_index][1] -= aug_flow
                self.graph[v][rev_index][1] += aug_flow
                v = u

            flow += aug_flow
            cost += aug_flow * pot[t]

        return flow, cost

def task():
    cards = []
    n = int(input())
    for _ in range(n):
        cards.append(int(input()))

    req_cards = set(range(1, n + 1)) - set(cards)
    repl = int(input())

    gr = Graph()
    extra_cards = {
        card: cards.count(card) - 1
        for card in set(cards)
        if cards.count(card) > 1
    }

    for _ in range(repl):
        a, b = map(int, input().split())
        gr.add_edge(a, b, 1)

    min_paths = defaultdict(dict)
    for extra_card in extra_cards.keys():
        distances = gr.dijkstra(extra_card)
        for req_card in req_cards:
            min_paths[extra_card][req_card] = distances.get(req_card, 10 ** 9)

    extra_list = []
    for card, count in extra_cards.items():
        extra_list.extend([card] * count)

    missing_list = list(req_cards)
    M = len(extra_list)
    K = len(missing_list)

    S = 0
    T = M + K + 1
    min_flow_graph = FlowNetwork(T + 1)

    for i in range(M):
        min_flow_graph.add_edge(S, i + 1, 1, 0)

    for i, extra_card in enumerate(extra_list):
        for j, missing_card in enumerate(missing_list):
            cost = min_paths[extra_card][missing_card]
            if cost < 10 ** 9:
                min_flow_graph.add_edge(i + 1, M + 1 + j, 1, cost)

    for j in range(K):
        min_flow_graph.add_edge(M + 1 + j, T, 1, 0)

    flow, total_cost = min_flow_graph.min_flow(S, T)

    return total_cost

t = int(input())
ans = []
for i in range(t):
    ans.append(task())
print(ans)

