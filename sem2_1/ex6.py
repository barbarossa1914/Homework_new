n = int(input())

graph = dict()
letter_deg = dict()
for i in range(n):
    string = str(input())
    start_letter = string[0]
    end_letter = string[-1]
    if start_letter in letter_deg:
        letter_deg[start_letter] += 1
    else:
        letter_deg[start_letter] = 1
    if end_letter in letter_deg:
        letter_deg[end_letter] -= 1
    else:
        letter_deg[end_letter] = -1
    if start_letter not in graph:
        graph[start_letter] = [end_letter]
    else:
        graph[start_letter].append(end_letter)
    if end_letter not in graph:
        graph[end_letter] = [start_letter]
    else:
        graph[end_letter].append(start_letter)
graph_values = set(graph.keys())


def bfs(g, start):
    queue = []
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for neighbor in g[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    if visited == graph_values:
        return 1
    else:
        return 0


state1 = True
for key in graph.keys():
    if bfs(graph, key) == 0:
        state1 = False
        break
state2 = True
for key in letter_deg.keys():
    if letter_deg[key] != 0:
        state2 = False
        break


print(state1 & state2)
