# -----------------------------------------
# 🔁 RECURSION
# -----------------------------------------

# ✅ WHAT IT IS:
# - A function calling itself with smaller subproblems
# - Needs a base case to stop, and a recursive case to progress
# - Uses the call stack to track progress (each call gets own scope)

# ------------------------
# 1️⃣ BASIC STRUCTURE
# ------------------------

# factorial: n! = n × (n-1)!
def factorial(n):
    if n == 0:                        # base case: factorial(0) = 1
        return 1
    return n * factorial(n - 1)       # recursive step: reduce problem size

# 🔎 Call stack trace for factorial(3):
# factorial(3)
# → 3 * factorial(2)
# → 3 * (2 * factorial(1))
# → 3 * (2 * (1 * factorial(0)))
# → 3 * (2 * (1 * 1)) = 6

# ------------------------
# 2️⃣ SIMPLE RECURSION
# ------------------------

# sum of first n natural numbers
def sum_n(n):
    if n == 0:
        return 0                     # base case: nothing to add
    return n + sum_n(n - 1)          # reduce problem by 1

# fibonacci (inefficient)
def fib(n):
    if n <= 1:
        return n                    # base case: fib(0)=0, fib(1)=1
    return fib(n - 1) + fib(n - 2)  # sum of previous two → exponential time

# ------------------------
# 3️⃣ STRINGS / LISTS
# ------------------------

# reverse string (list of chars) in-place
def reverse_string(s):
    def helper(left, right):
        if left >= right: return    # base case: finished reversing
        s[left], s[right] = s[right], s[left]  # swap ends
        helper(left + 1, right - 1)            # move toward center

    helper(0, len(s) - 1)

# check if string is palindrome using recursion
def is_palindrome(s, left, right):
    if left >= right: return True   # base case: checked all pairs
    if s[left] != s[right]: return False
    return is_palindrome(s, left + 1, right - 1)

# ------------------------
# 4️⃣ RECURSION + BACKTRACKING
# ------------------------

# generate all subsets (power set) of nums
def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])                # append COPY of current subset
        for i in range(start, len(nums)):
            path.append(nums[i])           # choose
            backtrack(i + 1, path)         # explore
            path.pop()                     # un-choose (backtrack)

    backtrack(0, [])
    return res

# ➕ uses: generate combinations, permutations, valid paths, etc.

# ------------------------
# 5️⃣ TREE TRAVERSAL (DFS STYLE)
# ------------------------

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# sum of all node values in tree
def tree_sum(root):
    if not root: return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

# check if any root-to-leaf path equals target sum
def has_path_sum(root, target):
    if not root: return False
    if not root.left and not root.right:    # leaf node
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))

# build binary tree from preorder + inorder (classic recursive pattern)
def build_tree(preorder, inorder):
    if not preorder or not inorder: return None
    root = TreeNode(preorder[0])             # first preorder = root
    idx = inorder.index(preorder[0])         # locate root in inorder
    root.left = build_tree(preorder[1:1+idx], inorder[:idx])
    root.right = build_tree(preorder[1+idx:], inorder[idx+1:])
    return root

# ------------------------
# 6️⃣ MEMOIZED RECURSION (TOP-DOWN DP)
# ------------------------

# fibonacci with memoization
def fib_memo(n, memo={}):
    if n in memo: return memo[n]             # return cached
    if n <= 1: return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# climb stairs: 1 or 2 steps at a time
def climb_stairs(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return 1
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]

# ------------------------
# 7️⃣ RECURSION VS ITERATION
# ------------------------

# ✅ Use recursion:
# - Trees / graphs (DFS, backtracking)
# - Generate permutations / subsets
# - Divide-and-conquer (merge sort, binary search)
# - Natural call stack behavior (traceable, undo steps)

# ❌ Use iteration:
# - When recursion depth > 1000 (stack overflow risk)
# - Simple loops / linear work
# - Space-efficiency critical (no call stack cost)

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ missing base case → infinite recursion → RecursionError
# ❌ modifying list in-place without copying in backtracking
# ❌ memo = {} is shared across calls (intentional or risky?)
# ❌ Python recursion depth ≈ 1000 (sys.setrecursionlimit() needed)
# ❌ expensive recomputation if no memo used (e.g., naive fib)

# ------------------------
# 🧰 PYTHON TOOLS
# ------------------------

# use standard lib caching
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

# increase recursion limit if needed
import sys
sys.setrecursionlimit(10**6)   # use cautiously

# ------------------------
# 🧵 WHEN TO USE
# ------------------------

# - Tree/graph DFS traversal
# - Exploring all combinations (subset/permutation)
# - Divide-and-conquer (sort, search, math)
# - When problem naturally splits into smaller parts
# - Backtracking with state exploration

# ------------------------
# ⏱ TIME COMPLEXITY (VARIES)
# ------------------------

# factorial, sum_n:               O(n)
# naive fibonacci:                O(2^n)
# memoized fibonacci:             O(n)
# tree traversal:                 O(n)
# subset generation:              O(2^n * n)
# backtracking (e.g. permutations): O(n!)
