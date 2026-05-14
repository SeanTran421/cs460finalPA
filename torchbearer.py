"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Sean Tran
Student ID:   826491452

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """

    return """
    A single run can only give us the cheapest cost from the start node to the other nodes.
    It won't give us the decision on which relic chamber will be visited in that order.
    After all inter-location costs are known, we only have the order of which relics should be collected before the exit is reached.
    This requires a search over orders because each possible relic visitation order can produce a different total fuel cost.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = [spawn]

    for relic in relics:
        if relic not in sources:
            sources.append(relic)

    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    dist = {}

    for node in graph:
        dist[node] = float('inf')
    
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, cost in graph[node]:
            new_dist = current_dist + cost

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = {}

    sources = select_sources(spawn, relics, exit_node)

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    Once a node is finalized, the distance stored for it is the true minimum cost from the source. Algorithm will not need to improve that later.

    The distances of the nodes are the best paths discovered so far using only already-finalized nodes as intermediate steps. The values may improve later on.

    At the start, the source has distance 0 and all other nodes have distance infinity. No nodes are finalized yet, so the discovered distances are valid starting estimates.

    The node with the smallest distance cannot be improved by going through another unfinished node because all edge weights are nonnegative. Any alternate path through that node would at least be as large as the current minimum.

    The invariant gurantees that every reachable node has their own true shortest path distance from the source once the algorithm ends.
    Any unreachable nodes remain as infinity.

    Correct distances let the route planner compare relic orders using the real minimum travel cost between locations.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """

    return """
    The failure mode: A greedy strategy may pick the closest node, but the local choice could potentially have us spend a lot more fuel.
    Counter-example setup: In the example, the important nodes are 'S', relics 'B', 'C', 'D', and exit 'T'.
    What greedy picks: Greedy could pick S to C because C has low immediate cost from 'S' and a series would be 'C -> B -> D -> T' for total cost of 5.
    What optimal picks: The optimal route would be S -> B -> D -> C -> T and the total cost would be 4.
    Why greedy loses: Greedy only considers the cheapest step first, while the optimal route depends on the full relic order affects the cost.

    The algorithm must explore different relic visitation **order** choices because the cheapest next relic may not give us the total cheaper cost in whole.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best = [float('inf'), []]

    relics_remaining = set(relics)

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        [],
        0,
        exit_node,
        best,
    )

    return (best[0], best[1])

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    #The pruning condition is safe because all weights are nonegative, so the continuing search would only increase the total cost.
    #If cost_so_far already exceeded the best solution found, the branch cannot become optimal.

    if cost_so_far >= best[0]:
        return

    #Base case
    if not relics_remaining:

        exit_cost = dist_table[current_loc][exit_node]

        if exit_cost != float('inf'):
            total_cost = cost_so_far + exit_cost

            if total_cost < best[0]:
                best[0] = total_cost
                best[1] = relics_visited_order.copy()

        return
    
    #Recursive case
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

        #Backtrack: undo the choice so the next branch starts with the original state
        relics_visited_order.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(
        graph,
        spawn,
        relics,
        exit_node
    )

    return find_optimal_route(
        dist_table,
        spawn,
        relics,
        exit_node
    )


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
