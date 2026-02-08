n = int(input())
graph = dict()

for i in range(n):
    string = list(map(int, input().split()))
    if string[0] not in graph:
        graph[string[0]] = [string[1]]
    else:
        graph[string[0]].append(string[1])
start_node, end_node = list(map(int, input().split()))
graph_values = set(graph.keys())


def bfs(g, start):
    queue = []
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        if node in graph.keys():
            for neighbor in g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        else:
            visited.add(node)
    if end_node in visited:
        return True
    else:
        return False


print(bfs(graph, start_node))
