# The Torchbearer

**Student Name:** Sean Tran
**Student ID:** 826491452
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _A single run from S only tells us the cheapest cost from the beginning node to the other nodes._
  _It cannot decide which relic chamber should be visited first, second, third, and so on._

- **What decision remains after all inter-location costs are known:**
  _The decision remains is the order in which the relics should be collected before it reached the exit,_

- **Why this requires a search over orders (one sentence):**
  _This requires a search over orders because each possible relic visitation order can produce a different total fuel cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Start node | This is the entrance so we would need shortest distances from the start to the rest of the relics |
| Relic nodes | After collecting a relic, the route may go find another one or head to the exit|

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | nested dictionary `dist_table` |
| What the keys represent | The outer keys are source nodes; inner keys are destination nodes |
| What the values represent | The shortest path fuel cost from the source node to the destination node |
| Lookup time complexity | `O(1)` |
| Why O(1) lookup is possible | Python dictionaries use hash-table lookup for keys. |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** `k+1`
- **Cost per run:** `O(m log n)`
- **Total complexity:** `O((k+1) m log n)`
- **Justification (one line):** The algorithm runs Dijkstra once from spawn node and once from each of the 'k' relic nodes

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _Once a node is finalized, the distance stored for it is the true minimum cost from the source. Algorithm will not need to improve that later._

- **For nodes not yet finalized (not in S):**
  _The distances of the nodes are the best paths discovered so far using only already-finalized nodes as intermediate steps. The values may improve later on._

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _At the start, the source has distance 0 and all other nodes have distance infinity. No nodes are finalized yet, so the discovered distances are valid starting estimates._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _The node with the smallest distance cannot be improved by going through another unfinished node because all edge weights are nonnegative. Any alternate path through that node would at least be as large as the current minimum._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant gurantees that every reachable node has their own true shortest path distance from the source once the algorithm ends._
  _Any unreachable nodes remain as infinity_

### Part 3c: Why This Matters for the Route Planner

_Correct distances let the route planner compare relic orders using the real minimum travel cost between locations._

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** _A greedy strategy may pick the closest node, but the local choice could potentially have us spend a lot more fuel._
- **Counter-example setup:** _In the example, the important nodes are 'S', relics 'B', 'C', 'D', and exit 'T'._
- **What greedy picks:** _Greedy could pick S to C because C has low immediate cost from 'S' and a series would be 'C -> B -> D -> T' for total cost of 5._
- **What optimal picks:** _The optimal route would be S -> B -> D -> C -> T and the total cost would be 4._
- **Why greedy loses:** _Greedy only considers the cheapest step first, while the optimal route depends on the full relic order affects the cost._

### What the Algorithm Must Explore

- _The algorithm must explore different relic visitation **order** choices because the cheapest next relic may not give us the total cheaper cost in whole._

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | `current_loc` | node | The current and present node |
| Relics already collected | `relics_visited_order` | list[node] | The ordered list of relics collected so far |
| Fuel cost so far | `cost_so_far` | float/int | The total fuel used by the current partial route. |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Set `relics_remaining` |
| Operation: check if relic already collected | Time complexity: `O(1)` |
| Operation: mark a relic as collected | Time complexity: `O(1)` |
| Operation: unmark a relic (backtrack) | Time complexity: `O(1)` |
| Why this structure fits | A set supports fast membership checks, removal, and re-adding during backtracking. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _`k!`_
- **Why:** _With `k` relics, the algorithm may try every possible visitation orders._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** _The algorithm is tracking the lowest complete route cost found so far and the relic order that the route is with._
- **When it is used:** _It is checked during recursion._
- **What it allows the algorithm to skip:** _It allows the algorithm to skip partial costs where their costs are already greater than or equal to the best cost efficient route._

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** _The information that is avaialble is the `current_loc`, `relics_remaining`, `relics_visited_order`, `cost_so_far`, `exit_node`, and the current best route._
- **What the lower bound accounts for:** _The lower bound accounts for fuel already spent in the state._
- **Why it never overestimates:** _Since all edge weights are nonnegative, the final route cost can never be lower than `cost_so_far`_

### Part 6c: Pruning Correctness

- _If `cost_so_far` is already greater than or equal to the best route, continuing that branch cannot produce a better route._
- _Because all future travel costs are nonnegative, pruning this branch cannot remove the optimal solution._

---

## References

- _None beyond lecture notes_
