# -----------------------------------------
# 🧠 DYNAMIC PROGRAMMING (DP)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Solves problems by breaking them into overlapping subproblems.
# - Saves subproblem results to avoid redundant work.
# - Requires two properties:
#   1. Optimal Substructure → subproblems combine into global solution
#   2. Overlapping Subproblems → same subproblems repeat

# 🧠 TWO STYLES:
# - Top-down = Recursion + Memoization
# - Bottom-up = Tabulation (iterative build-up)

# -----------------------------------------
# 🧠 HOW TO RECOGNIZE A DP PROBLEM
# -----------------------------------------

# - Brute-force is recursive with repeated calls
# - Problem asks for: max/min/count/ways/true-false
# - You're making choices → take/skip, split, match
# - Input size small (≤ 10^4), recursion gives TLE
# - Greedy doesn't guarantee correctness

# -----------------------------------------
# 🔁 CALL TREE EXAMPLE (FIBONACCI)
# -----------------------------------------

# Brute-force: fib(5)
#       f(5)
#      /    \
#   f(4)    f(3)
#   / \      / \
# f(3)f(2) f(2)f(1)
# ... repeated calls → EXPONENTIAL work

# Memoization stores answers to avoid recomputation

# -----------------------------------------
# 1️⃣ TOP-DOWN FIB (MEMOIZATION)
# -----------------------------------------

def fib(n, memo={}):
    if n in memo: return memo[n]          # use cached result
    if n <= 1: return n                    # base case
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # recurse & store
    return memo[n]

# ✅ avoids recomputation
# ⚠️ dict default param is shared across calls (ok here, risky elsewhere)

# ✅ Alternative using Python’s built-in cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib2(n):
    if n <= 1:
        return n
    return fib2(n-1) + fib2(n-2)

# -----------------------------------------
# 2️⃣ BOTTOM-UP FIB (TABULATION)
# -----------------------------------------

def fib_tab(n):
    if n <= 1: return n
    dp = [0] * (n + 1)         # dp[i] stores fib(i)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 🧠 NO recursion → avoids stack overflow

# -----------------------------------------
# 3️⃣ SPACE OPTIMIZED FIB (ROLLING ARRAY)
# -----------------------------------------

def fib_rolling(n):
    a, b = 0, 1                # only store last 2 values
    for _ in range(n):
        a, b = b, a + b
    return a

# ✅ memory: O(1) instead of O(n)

# -----------------------------------------
# 4️⃣ CLIMBING STAIRS (LEETCODE 70)
# -----------------------------------------

def climb_stairs(n):
    if n <= 1: return 1
    a, b = 1, 1                # dp[0] = 1, dp[1] = 1
    for _ in range(2, n + 1):
        a, b = b, a + b        # rolling: dp[i] = dp[i-1] + dp[i-2]
    return b

# -----------------------------------------
# 5️⃣ COIN CHANGE (MIN COINS TO REACH AMOUNT)
# -----------------------------------------

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)  # dp[i] = min coins to make i
    dp[0] = 0                           # base case

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# -----------------------------------------
# 6️⃣ 0/1 KNAPSACK
# -----------------------------------------

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]  # dp[i][w] = max val with i items, w weight

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]           # can't take item i
            else:
                dp[i][w] = max(
                    dp[i-1][w],                 # don't take it
                    values[i-1] + dp[i-1][w - weights[i-1]]  # take it
                )
    return dp[n][W]

# -----------------------------------------
# 7️⃣ SUBSET SUM / PARTITION EQUAL SUBSET SUM
# -----------------------------------------

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0: return False             # odd total = can't split evenly
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True                                # base case

    for num in nums:
        for i in range(target, num - 1, -1):    # go backwards
            dp[i] = dp[i] or dp[i - num]        # take or not

    return dp[target]

# -----------------------------------------
# 8️⃣ LONGEST COMMON SUBSEQUENCE (LCS)
# -----------------------------------------

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:              # chars match
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # skip one

    return dp[m][n]

# -----------------------------------------
# 9️⃣ EDIT DISTANCE (LEETCODE 72)
# -----------------------------------------

def edit_distance(w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1): dp[i][0] = i          # delete all
    for j in range(n+1): dp[0][j] = j          # insert all

    for i in range(1, m+1):
        for j in range(1, n+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]        # match
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],               # delete
                    dp[i][j-1],               # insert
                    dp[i-1][j-1]              # replace
                )

    return dp[m][n]

# -----------------------------------------
# 🔟 UNIQUE PATHS IN GRID (LEETCODE 62)
# -----------------------------------------

def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]             # only 1 path in top row / left col

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] # from top + left

    return dp[m-1][n-1]

# -----------------------------------------
# 🧵 COMMON PATTERNS (NAME RECOGNITION)
# -----------------------------------------

# - Fibonacci-style (linear recurrence)
# - Grid traversal (m x n)
# - Subset / knapsack (dp[i][j])
# - Subsequence DP (strings: LCS, edit distance)
# - Decision trees (take/skip)
# - Partition-based (palindromes, cuts)

# -----------------------------------------
# ⚠️ GOTCHAS
# -----------------------------------------

# ❌ Forgetting base cases (like dp[0])
# ❌ Off-by-one indexing bugs
# ❌ Mutable default args (memo = {})
# ❌ Missing cache in top-down → exponential
# ❌ Wrong direction in tabulation (e.g., backwards needed for space-opt)

# -----------------------------------------
# 📚 ADVANCED (FYI ONLY)
# -----------------------------------------

# - DP on trees (postorder traversal)
# - DP on DAGs (topo order)
# - Digit DP (number constraints)
# - Bitmask DP (states = subsets)

# -----------------------------------------
# ⏱ TIME COMPLEXITY SUMMARY
# -----------------------------------------

# fib (memo):                O(n)
# coin change:               O(n * coins)
# knapsack:                  O(n * W)
# subset sum:                O(n * target)
# edit distance / LCS:       O(m * n)
# grid DP:                   O(m * n)
