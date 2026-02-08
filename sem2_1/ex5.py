n = int(input())
graph = dict()

graph_values = set()
for i in range(n):
    string = list(map(int, input().split()))
    graph_values.add(string[0])
    graph_values.add(string[1])
    if string[0] not in graph:
        graph[string[0]] = [(string[1], string[2])]
    else:
        graph[string[0]].append((string[1], string[2]))
start_node, end_node = list(map(int, input().split()))
graph_keys = set(graph.keys())


def dijkstra_wrapper(g, start, end):
    visited = []
    unvisited = [v for v in graph_values]
    distance = {v: 10**9 for v in graph_values}
    distance[start] = 0

    def dijkstra(g1, start1, end1):
        if not unvisited:
            return -1
        candidates = {vv: distance[vv] for vv in unvisited}
        v = min(candidates, key=candidates.get)
        if distance[v] == 10**9:
            return -1
        visited.append(v)
        unvisited.remove(v)
        if v not in graph_keys and v == end:
            return distance[v]
        elif v not in graph_keys and v != end:
            return dijkstra(g1, start1, end1)
        for el in g1[v]:
            if el[0] in unvisited:
                new_distance = el[1] + distance[v]
                if new_distance < distance[el[0]]:
                    distance[el[0]] = new_distance
        if end1 in visited:
            return distance[end1]
        else:
            return dijkstra(g1, start1, end1)
    return dijkstra(g, start, end)


print(dijkstra_wrapper(graph, start_node, end_node))
