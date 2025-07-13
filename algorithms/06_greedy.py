# -----------------------------------------
# 💰 GREEDY ALGORITHMS
# -----------------------------------------

# ✅ WHAT IT IS:
# - At each step, pick the BEST local option without revisiting choices
# - Greedy = no backtracking or recursion → decisions are FINAL
# - Only works if problem has:
#   1. Greedy-choice property → local = global optimum
#   2. Optimal substructure → subproblems are optimal

# ------------------------
# 1️⃣ CLASSIC EXAMPLE: Coin Selection
# ------------------------

# total up to 100 using biggest items first
def greedy_fill(items):
    items.sort(reverse=True)          # sort largest to smallest
    total = 0
    for x in items:
        if total + x <= 100:          # take it if it fits
            total += x                # add to total
    return total

# 🧠 relies on idea that bigger is better — valid if greedy-choice holds

# ------------------------
# 2️⃣ COUNTEREXAMPLE: Greedy FAILS
# ------------------------

def coin_change_fail():
    coins = [1, 3, 4]
    amount = 6
    count = 0
    coins.sort(reverse=True)          # [4, 3, 1]
    for coin in coins:
        while amount >= coin:
            amount -= coin            # subtract biggest coin
            count += 1
    return count                      # returns 3 → [4,1,1] ❌
# optimal answer is 2 → [3,3] → GREEDY FAILS

# ------------------------
# 3️⃣ INTERVAL SCHEDULING (NON-OVERLAPPING)
# ------------------------

# find max # of non-overlapping intervals
def max_non_overlap(intervals):
    intervals.sort(key=lambda x: x[1])     # sort by END time
    end = float('-inf')                    # track end of last chosen
    count = 0
    for start, stop in intervals:
        if start >= end:                   # no overlap
            count += 1
            end = stop                     # update current end
    return count

# ✅ greedy-choice: take interval that ends earliest → leaves max room

# ------------------------
# 4️⃣ ACTIVITY SELECTION (RETURN ACTUAL INTERVALS)
# ------------------------

def select_activities(intervals):
    intervals.sort(key=lambda x: x[1])
    res = []
    end = float('-inf')
    for s, e in intervals:
        if s >= end:
            res.append((s, e))             # take it
            end = e
    return res

# ------------------------
# 5️⃣ JUMP GAME (Reachability)
# ------------------------

# can you reach the last index?
def can_jump(nums):
    max_reach = 0                          # furthest we can go
    for i, steps in enumerate(nums):
        if i > max_reach: return False     # stuck at index i
        max_reach = max(max_reach, i + steps)  # update max reach
    return True

# ------------------------
# 6️⃣ MINIMUM JUMPS TO END
# ------------------------

# find minimum # of jumps to reach end
def jump(nums):
    jumps = 0
    end = 0                                # end of current jump window
    farthest = 0                           # farthest we can reach so far
    for i in range(len(nums) - 1):         # don't jump at last index
        farthest = max(farthest, i + nums[i])
        if i == end:                       # time to jump
            jumps += 1
            end = farthest                # new jump window
    return jumps

# ------------------------
# 7️⃣ GAS STATION
# ------------------------

def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost): return -1     # can't finish circuit
    total = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:                      # can't reach next station
            total = 0                      # reset buffer
            start = i + 1                  # new candidate start
    return start

# ------------------------
# 8️⃣ K-LARGEST ELEMENTS USING HEAP
# ------------------------

import heapq

# stream version: keep k largest seen so far
def k_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)           # push every number
        if len(heap) > k:
            heapq.heappop(heap)           # pop smallest if > k
    return heap                           # size-k heap of largest elements

# 🔁 greedy choice changes over time → need heap, not sorting

# ------------------------
# 9️⃣ MST: GREEDY IN GRAPHS (MENTION ONLY)
# ------------------------

# Kruskal's algorithm:
# - sort edges by weight
# - greedily pick smallest edge that doesn't form cycle

# Prim's algorithm:
# - use min heap to grow MST from seed node

# ✅ both rely on greedy edge selection → proven correct for MST

# ------------------------
# 📚 DEFINITION SUMMARY
# ------------------------

# 🧠 Greedy-choice property: local choice = global optimal
# 🧠 Optimal substructure: subproblems also optimal
# ❌ If either fails → greedy = wrong

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ greedy doesn’t guarantee optimal result unless proven
# ❌ coin change only works if coin system is canonical
# ❌ no undo → wrong choices are final
# ❌ sorting ≠ always sufficient → sometimes need heap

# ------------------------
# 🧵 WHEN TO USE GREEDY
# ------------------------

# - interval scheduling
# - jump games / ladders
# - greedy fits natural logic (earliest end, biggest gain)
# - MST, Huffman coding, Dijkstra (with modification)
# - resource allocation (greedy sort or heap)

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# greedy + sort:         O(n log n)
# jump game:             O(n)
# gas station:           O(n)
# heap-based greedy:     O(n log k)
# Kruskal/Prim MST:      O(E log V)

