# -----------------------------------------
# 🔁 DFS / BFS — TREES, GRAPHS, GRIDS
# -----------------------------------------

# ✅ WHAT IT IS:
# - DFS (Depth-First Search): Go deep first, explore branches fully before backtracking (uses stack or recursion)
# - BFS (Breadth-First Search): Explore neighbors level by level (uses queue)

# 📦 Applicable to:
# - Trees
# - Graphs (cyclic/acyclic, directed/undirected)
# - Grids (2D arrays as implicit graphs)

# -----------------------------------------
# 1️⃣ DFS ON TREE — RECURSIVE
# -----------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive(root):
    if not root:
        return
    print(root.val)                # process current node
    dfs_recursive(root.left)      # go left first
    dfs_recursive(root.right)     # then right

# DFS order → preorder: root → left → right

# -----------------------------------------
# 2️⃣ INORDER / POSTORDER VARIANTS
# -----------------------------------------

def inorder(root):
    if root:
        inorder(root.left)         # left first
        print(root.val)            # visit in the middle
        inorder(root.right)        # then right

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)            # visit after children

# -----------------------------------------
# 3️⃣ DFS TREE — ITERATIVE (USING STACK)
# -----------------------------------------

def dfs_iterative(root):
    if not root: return
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)            # visit node

        # push right first so left is on top of stack
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# -----------------------------------------
# 4️⃣ BFS TREE — LEVEL ORDER
# -----------------------------------------

from collections import deque

def bfs_tree(root):
    if not root: return
    queue = deque([root])

    while queue:
        node = queue.popleft()     # remove from front of queue
        print(node.val)

        # enqueue left and right children
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# -----------------------------------------
# 5️⃣ BFS WITH LEVELS — RETURN LEVEL ORDER LIST
# -----------------------------------------

def level_order(root):
    if not root: return []
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):       # only current level nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# -----------------------------------------
# 6️⃣ DFS ON GRAPH — WITH VISITED SET
# -----------------------------------------

def dfs_graph(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs_graph(graph, neighbor, visited)

# graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: []}

# -----------------------------------------
# 7️⃣ BFS ON GRAPH — LEVEL ORDER / SHORTEST PATH STYLE
# -----------------------------------------

def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            queue.append(neighbor)

# -----------------------------------------
# 8️⃣ DFS GRID (e.g. flood fill, islands)
# -----------------------------------------

# directions for 4-way movement: up/down/left/right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if (r < 0 or c < 0 or r >= rows or c >= cols or
        (r, c) in visited or grid[r][c] == 0):
        return
    visited.add((r, c))                # mark current cell
    for dr, dc in DIRS:
        dfs_grid(grid, r + dr, c + dc, visited)

# grid = 2D list, visited = set of (r, c)

# -----------------------------------------
# 9️⃣ CYCLE DETECTION IN DIRECTED GRAPH
# -----------------------------------------

def has_cycle(graph):
    visited = set()
    path = set()  # nodes currently in recursion stack

    def dfs(node):
        if node in path: return True     # cycle detected
        if node in visited: return False # already checked
        visited.add(node)
        path.add(node)
        for nei in graph[node]:
            if dfs(nei): return True
        path.remove(node)                # backtrack
        return False

    for node in graph:
        if dfs(node): return True
    return False

# -----------------------------------------
# 🔟 TOPOLOGICAL SORT (POSTORDER DFS)
# -----------------------------------------

def topo_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for nei in graph[node]:
            dfs(nei)
        result.append(node)            # postorder append

    for node in graph:
        dfs(node)

    return result[::-1]                # reverse postorder

# DAG only. No cycles allowed.

# -----------------------------------------
# 🔁 BFS WITH PARENT TRACKING (FOR PATH RECONSTRUCTION)
# -----------------------------------------

def bfs_with_parents(graph, start):
    parent = {start: None}             # stores where each node came from
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in parent:
                parent[nei] = node     # record parent
                queue.append(nei)
    return parent

# To reconstruct path from target back to start:
# path = []
# while target:
#     path.append(target)
#     target = parent[target]
# path.reverse()

# -----------------------------------------
# ⚠️ GOTCHAS
# -----------------------------------------

# ❌ DFS on graph w/o visited set → infinite loop
# ❌ Don’t reuse mutable path lists across calls (backtrack properly)
# ❌ Grid DFS must check bounds and visited
# ❌ Topological sort assumes DAG (no cycles)
# ❌ Recursive DFS can hit stack overflow → use iterative version
# ❌ BFS requires fixed-level processing for correct layer separation

# -----------------------------------------
# 🧵 WHEN TO USE WHICH
# -----------------------------------------

# ✅ DFS:
# - explore all paths (backtracking)
# - generate permutations/combinations
# - subtree or postorder logic
# - when you want full traversal or decision tree

# ✅ BFS:
# - shortest path (unweighted)
# - level-order processing
# - problems with minimum steps
# - solving outward from a source

# -----------------------------------------
# ⏱ TIME COMPLEXITY
# -----------------------------------------

# Tree DFS/BFS:               O(n)
# Graph DFS/BFS:              O(V + E)
# Grid DFS/BFS:               O(R * C)
# BFS with levels:            O(n)
# Topological sort (DFS):     O(V + E)
# Cycle detection:            O(V + E)
# Path reconstruction:        O(n)
