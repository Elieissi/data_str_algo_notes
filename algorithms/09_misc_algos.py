# -----------------------------------------
# ⚙️ MISCELLANEOUS ESSENTIAL ALGORITHMS 
# -----------------------------------------

# ✅ These are fundamental tools and patterns often used in coding interviews.
# - Don't belong to core categories like recursion/graphs/greedy/DP
# - Appear across many domains: arrays, math, scheduling, streams, optimization

# -----------------------------------------
# 1️⃣ BINARY SEARCH (INTEGER, CLASSIC)
# -----------------------------------------

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2      # middle index
        if arr[mid] == target:
            return mid                 # found target
        elif arr[mid] < target:
            left = mid + 1            # move right
        else:
            right = mid - 1           # move left
    return -1                          # not found

# Requires sorted array
# Time: O(log n)

# -----------------------------------------
# 2️⃣ BINARY SEARCH (FLOAT / EPSILON BASED)
# -----------------------------------------

def binary_search_float(low, high, condition, eps=1e-6):
    while high - low > eps:                   # precision loop
        mid = (low + high) / 2
        if condition(mid):
            high = mid                        # narrow left
        else:
            low = mid                         # narrow right
    return low

# Example usage:
# - Find square root
# - Minimize/maximize under constraint
# - Use when working with decimals

# -----------------------------------------
# 3️⃣ LOWER BOUND (FIRST ELEMENT ≥ TARGET)
# -----------------------------------------

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left    # index of first ≥ target

# Used in insert position, range queries

# -----------------------------------------
# 4️⃣ PREFIX SUM (1D ARRAY)
# -----------------------------------------

def prefix_sum(arr):
    n = len(arr)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i+1] = pre[i] + arr[i]     # build cumulative total
    return pre

# Range sum [l, r] = pre[r+1] - pre[l]

# -----------------------------------------
# 5️⃣ PREFIX SUM (2D GRID)
# -----------------------------------------

def prefix_sum_2d(grid):
    rows, cols = len(grid), len(grid[0])
    pre = [[0] * (cols + 1) for _ in range(rows + 1)]

    for r in range(rows):
        for c in range(cols):
            pre[r+1][c+1] = (grid[r][c]
                            + pre[r][c+1]
                            + pre[r+1][c]
                            - pre[r][c])  # inclusion-exclusion
    return pre

# Query (r1,c1) to (r2,c2) with 1-based prefix:
# pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]

# -----------------------------------------
# 6️⃣ DIFFERENCE ARRAY (RANGE UPDATES)
# -----------------------------------------

def range_add(diff, l, r, val):
    diff[l] += val
    if r + 1 < len(diff):
        diff[r + 1] -= val

def apply_diff(diff):
    for i in range(1, len(diff)):
        diff[i] += diff[i - 1]
    return diff

# Good for multiple range adds, then 1 pass application

# -----------------------------------------
# 7️⃣ KADANE'S ALGORITHM (MAX SUBARRAY)
# -----------------------------------------

def max_subarray(arr):
    curr = res = arr[0]
    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])  # extend or restart
        res = max(res, curr)               # track max
    return res

# Time: O(n)
# Use: find most profitable contiguous range

# -----------------------------------------
# 8️⃣ UNION FIND (DISJOINT SET UNION)
# -----------------------------------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))     # parent[i] = i
        self.rank = [0] * n              # depth info for optimization

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # compress path
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False        # already connected
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# Used for: connected components, Kruskal MST, cycle detection

# -----------------------------------------
# 9️⃣ BIT TRICKS
# -----------------------------------------

x & 1           # check odd
x & (x - 1)     # clear lowest 1-bit
x ^ x           # 0
x ^ 0           # x
x >> 1          # divide by 2
x << 1          # multiply by 2

# Count set bits:
def count_bits(x):
    count = 0
    while x:
        x &= (x - 1)   # drop lowest 1
        count += 1
    return count

# -----------------------------------------
# 🔟 BITMASKING — SUBSET GENERATION
# -----------------------------------------

def all_subsets(arr):
    n = len(arr)
    for mask in range(1 << n):            # 2^n masks
        subset = [arr[i] for i in range(n) if mask & (1 << i)]
        print(subset)

# Key for:
# - knapsack problems
# - subset enumeration
# - state compression

# -----------------------------------------
# 1️⃣1️⃣ SLIDING WINDOW MAX (MONOTONIC QUEUE)
# -----------------------------------------

from collections import deque

def max_sliding_window(nums, k):
    q = deque()  # stores indices of useful elements
    res = []

    for i, num in enumerate(nums):
        # pop elements smaller than current from back
        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        # pop out-of-window index from front
        if q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            res.append(nums[q[0]])  # max in window
    return res

# Time: O(n)

# -----------------------------------------
# 1️⃣2️⃣ COORDINATE COMPRESSION
# -----------------------------------------

def compress(arr):
    sorted_unique = sorted(set(arr))          # dedupe + sort
    mapping = {val: i for i, val in enumerate(sorted_unique)}
    return [mapping[x] for x in arr]          # replace with index

# Use: transform large-range values into dense index space

# -----------------------------------------
# 1️⃣3️⃣ MOORE’S VOTING ALGORITHM (MAJORITY ELEMENT)
# -----------------------------------------

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# Finds element that occurs > n//2 times
# Time: O(n), Space: O(1)

# -----------------------------------------
# 1️⃣4️⃣ RESERVOIR SAMPLING (RANDOM PICK FROM STREAM)
# -----------------------------------------

import random

def reservoir_sample(stream):
    result = None
    for i, val in enumerate(stream):
        if random.randint(0, i) == 0:      # replace with prob 1/(i+1)
            result = val
    return result

# Use when:
# - input size unknown
# - can't store full input
# Time: O(n), Space: O(1)

# -----------------------------------------
# 1️⃣5️⃣ FISHER-YATES SHUFFLE
# -----------------------------------------

def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)           # swap with earlier index
        arr[i], arr[j] = arr[j], arr[i]

# Uniform unbiased shuffle

# -----------------------------------------
# 1️⃣6️⃣ SWEEP LINE — INTERVAL MERGING
# -----------------------------------------

def merge_intervals(intervals):
    intervals.sort()               # sort by start
    res = []

    for start, end in intervals:
        if not res or res[-1][1] < start:
            res.append([start, end])           # new interval
        else:
            res[-1][1] = max(res[-1][1], end)  # merge with previous
    return res

# Used for:
# - merging meetings
# - detecting conflicts
# - active ranges

# -----------------------------------------
# ⚠️ GOTCHAS
# -----------------------------------------

# ❌ Binary search assumes sorted input
# ❌ Bitmasking works only for small n (≤ 20)
# ❌ Union-Find needs compression for efficiency
# ❌ Reservoir sampling is for unknown-size streams
# ❌ Difference array requires careful boundary handling
# ❌ Sliding window max fails if you forget to clear out-of-range index

# -----------------------------------------
# ⏱ TIME COMPLEXITY SUMMARY
# -----------------------------------------

# Binary search:              O(log n)
# Prefix sum build:           O(n)
# Prefix query:               O(1)
# Kadane’s:                   O(n)
# Bit tricks:                 O(log x)
# Bitmask subsets:            O(2^n)
# Union-Find ops:             O(α(n)) amortized
# Reservoir sampling:         O(n)
# Shuffle (Fisher-Yates):     O(n)
# Merge intervals:            O(n log n)
# Sliding window max:         O(n)
