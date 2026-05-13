# The Torchbearer

**Student Name:** Sean Tran
**Student ID:** 826491452
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  A single run from S only tells us the cheapest cost from the beginning node to the other nodes. 
  It cannot decide which relic chamber should be visited first, second, third, and so on.

- **What decision remains after all inter-location costs are known:**
  The decision remains is the order in which the relics should be collected before it reached the exit,

- **Why this requires a search over orders (one sentence):**
  This requires a search over orders because each possible relic visitation order can produce a different total fuel cost.

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
| Data structure name | nested dictionary 'dist_table' |
| What the keys represent | The outer keys are source nodes; inner keys are destination nodes |
| What the values represent | The shortest path fuel cost from the source node to the destination node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Python dictionaries use hash-table lookup for keys. |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** 'k+1'
- **Cost per run:** 'O(m log n)'
- **Total complexity:** 'O((k+1) m log n)'
- **Justification (one line):** The algorithm runs Dijkstra once from spawn node and once from each of the 'k' relic nodes

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  Once a node is finalized, the distance stored for it is the true minimum cost from the source. Algorithm will not need to improve that later.

- **For nodes not yet finalized (not in S):**
  The distances of the nodes are the best paths discovered so far using only already-finalized nodes as intermediate steps. The values may improve later on.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  At the start, the source has distance '0' and all other nodes have distance 'infinity'. No nodes are finalized yet, so the discovered distances are valid starting estimates.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The node with the smallest distance cannot be improved by going through another unfinished node because all edge weights are negative. Any alternate path through that node would at least be as large as the current minimum.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant gurantees that every reachable node has their own true shortest path distance from the source once the algorithm ends.
  Any unreachable nodes remain as 'infinity'

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Correct distances let the route planner compare relic orders using the real minimum travel cost between locations.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
