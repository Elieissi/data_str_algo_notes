# -----------------------------------------
# 🌲 BINARY TREES — STRUCTURE + TRAVERSALS
# -----------------------------------------

# ✅ WHAT IT IS:
# - Recursive node-based hierarchy
# - Each node has ≤ 2 children: left + right
# - Used in recursion, search trees, hierarchical modeling

# ------------------------
# 🌱 TREE TYPES — DEFINITIONS
# ------------------------

# - Binary Tree: each node ≤ 2 children
# - BST (Binary Search Tree): left < root < right
# - Full Tree: each node has 0 or 2 children
# - Complete Tree: all levels filled left-to-right
# - Perfect Tree: full + all leaves at same depth

# ------------------------
# 🧱 NODE STRUCTURE
# ------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ------------------------
# 🔁 TRAVERSAL ORDERS
# ------------------------

# preorder:   Root → Left → Right
# inorder:    Left → Root → Right
# postorder:  Left → Right → Root
# level-order: top to bottom, left to right (BFS)

# ------------------------
# 🔁 DFS TRAVERSALS (RECURSIVE)
# ------------------------

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# ------------------------
# 🔁 BFS (LEVEL-ORDER TRAVERSAL)
# ------------------------

from collections import deque

def level_order(root):
    if not root: return []
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return res

# ------------------------
# 📦 BUILD TREE FROM ARRAY (LEETCODE FORMAT)
# ------------------------

def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

# ------------------------
# 🔁 DEPTH / HEIGHT
# ------------------------

def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# ------------------------
# 🔁 DIAMETER (LONGEST PATH)
# ------------------------

def diameter(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node: return 0
        l = dfs(node.left)
        r = dfs(node.right)
        res = max(res, l + r)
        return 1 + max(l, r)
    dfs(root)
    return res

# ------------------------
# 🔁 IS BALANCED
# ------------------------

def is_balanced(root):
    def dfs(node):
        if not node: return 0
        l = dfs(node.left)
        r = dfs(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1: return -1
        return 1 + max(l, r)
    return dfs(root) != -1

# ------------------------
# 🔁 INVERT TREE
# ------------------------

def invert(root):
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root

# ------------------------
# 🔁 PATH SUM (ROOT TO LEAF)
# ------------------------

def has_path_sum(root, target):
    if not root: return False
    if not root.left and not root.right:
        return target == root.val
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)

# ------------------------
# 🔁 LOWEST COMMON ANCESTOR (LCA)
# ------------------------

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right

# ------------------------
# 🔁 SERIALIZE / DESERIALIZE TREE
# ------------------------

def serialize(root):
    vals = []
    def dfs(node):
        if not node:
            vals.append('#')
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ' '.join(vals)

def deserialize(data):
    vals = iter(data.split())
    def dfs():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

# ------------------------
# 🔁 BINARY SEARCH TREE (BST) OPS
# ------------------------

def search_bst(root, target):
    if not root: return False
    if root.val == target: return True
    return search_bst(root.left, target) if target < root.val else search_bst(root.right, target)

def insert_bst(root, val):
    if not root: return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def delete_node(root, key):
    if not root: return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root

# ------------------------
# 🧰 UTILITIES
# ------------------------

def tree_to_list(root):
    if not root: return []
    q = deque([root])
    out = []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# - must check for None before accessing .left/.right
# - recursion returns: value vs side-effect (use nonlocal if needed)
# - incorrect base case = stack overflow
# - BFS = use deque
# - BST delete edge cases require finding in-order successor
# - forget to update .left/.right = lost subtree

# ------------------------
# 🧵 WHEN TO USE BINARY TREES
# ------------------------

# - recursive divide-and-conquer problems
# - hierarchical modeling
# - ordered search (BST)
# - segmenting ranges, intervals
# - prefix structures (e.g. tries, parsers)

# ------------------------
# 🧠 INTERVIEW PROBLEMS TO PRACTICE
# ------------------------

# - Max Depth of Binary Tree
# - Diameter of Binary Tree
# - Invert Binary Tree
# - Path Sum
# - Balanced Binary Tree
# - Lowest Common Ancestor
# - Serialize and Deserialize Binary Tree
# - Construct from Inorder + Preorder
# - Symmetric Tree
# - BST: insert/search/delete

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# traversal:          O(n)
# depth / diameter:   O(n)
# BST insert/search:  O(log n) avg, O(n) worst
# serialize/parse:    O(n)
# LCA:                O(n)
# BST delete:         O(h), h = height
