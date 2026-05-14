# Development Log – The Torchbearer

**Student Name:** Sean Tran
**Student ID:** 826491452

---

## Entry 1 – [May 12, 2026]: Initial Plan

The plan is straight. Forward. Such. We first implement Dijkstra's algorithm because every later part depends on the correct shortest path. 
After that, the recursive search will also be implemented for the relic visitation orders and finally add pruning to not go to any other paths.
Expecting the recursive search and pruning correctiveness to be hard so I plan to test using the provided graph for said implementations.

---

## Entry 2 – [May 13, 2026]: Fixing Recursive Search State

While implementing _explore, I forgot to restore the search state after recursive calls in '_explore'.
Relics removed from the remaining state stayed removed for later branches, which may cause some visitation orders to never be explored.
I fixed this by re-adding relics and popping from the visited order once recursion return.

---

## Entry 3 – [May 13, 2026]: Pruning Validation and Edge Cases

After fixing the recursive search behavior, I focused on validating the pruning logic and testing edge cases. I confirmed that pruning using 'cost_so_far >= best_cost' was safe because all edge weights are nonnegative, meaning future exploration can only increase total cost. I also tested unreachable-path cases to ensure the algorithm correctly returned '(inf, [])' when no valid exit route existed.

---

## Entry 4 – [May 14, 2026]: Post-Implementation Reflection

_The pruning strategy was correct, but fairly simple. If I had more time, I'd improve the lower bound estimates to prune more branches earlier and reduce unnecessary recursive exploration. I would also consider dynamic programming to avoid recomputing equivalent search states. Another improvement would be reconstructing the full path through intermediate nodes instead of only returning the relic visitation order._

---

## Final Entry – [May 14, 2026]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.4 |
| Part 2: Precomputation Design | 1 |
| Part 3: Algorithm Correctness | 1 |
| Part 4: Search Design | 0.5 |
| Part 5: State and Search Space | 1 |
| Part 6: Pruning | 1 |
| Part 7: Implementation | 3 |
| README and DEVLOG writing | 1.5 |
| **Total** | 9.4 |
