from torchbearer import (
    select_sources,
    run_dijkstra,
    precompute_distances,
)

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2)],
    'C': []
}

print(run_dijkstra(graph, 'A'))

print(select_sources('S', ['A', 'B'], 'T'))

graph = {
    'S':[('R', 2)],
    'R':[('T', 3)],
    'T':[]
}

print(precompute_distances(graph,'S', ['R'], 'T'))