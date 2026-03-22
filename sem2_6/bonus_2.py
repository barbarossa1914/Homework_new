import networkx as nx

G = nx.Graph()
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=3)
G.add_edge(12, 13, weight=3)
for i in range(4, 11):
    G.add_edge(i, i - 1, weight=i ** 2)
    G.add_edge(i, i - 2, weight=i ** 2)
    G.add_edge(i, i - 3, weight=i ** 2)

C = nx.complete_graph(5)

print(nx.number_connected_components(G))
print(nx.density(G))
print(list(nx.all_simple_paths(C, 2, 4)))
print(nx.dfs_predecessors(G, source=1))