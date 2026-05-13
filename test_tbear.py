from torchbearer import (
    select_sources,
    run_dijkstra,
    precompute_distances,
    solve
)

graph = {
    'S': [('A', 10), ('B', 1)],
    'A': [('B', 1), ('T', 1)],
    'B': [('A', 1), ('T', 100)],
    'T': []
}

cost, order = solve(graph, 'S', ['A', 'B'], 'T')
print(cost, order)

graph = {
    'S': [('R', 1)],
    'R': [],
    'T': []
}

cost, order = solve(graph, 'S', ['R'], 'T')
print(cost, order)