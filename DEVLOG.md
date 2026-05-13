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

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
