n = int(input())
graph = dict()

for i in range(n):
    string = list(map(str, input().split()))
    if string[1] not in graph:
        graph[string[1]] = string[0]
    else:
        graph[string[1]].append(string[0])
graph_keys = set(graph.keys())
graph_values = set(graph.values())
end_node = ((graph_values ^ graph_keys) & graph_keys).pop()


def bfs(g, start):
    queue = []
    visited = []

    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)
        if node in graph.keys():
            for neighbor in g[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        else:
            continue
    return visited[::-1]


print(bfs(graph, end_node))
