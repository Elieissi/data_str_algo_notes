# -----------------------------------------
# 📦 STACKS (LIFO) — IMPLEMENTED WITH LIST/DEQUE
# -----------------------------------------

# ✅ WHAT IT IS:
# - Linear data structure: Last-In, First-Out (LIFO)
# - Only top is accessible
# - Push to top, pop from top
# - Used in parsing, undo systems, recursion, DFS

# 🔁 ACCESS PATTERN: push/pop from end → O(1)
# ❗ Not a built-in type — implemented using list or deque

# ------------------------
# 🛠 BASIC OPERATIONS (LIST-BASED)
# ------------------------

stack = []                      # create stack

stack.append(10)                # push
stack.append(20)

top = stack[-1]                 # peek (no pop)
val = stack.pop()               # pop

print(len(stack))               # size
print(not stack)                # is empty?

backup = stack.copy()           # shallow copy

# ------------------------
# 🧱 CLASS IMPLEMENTATION
# ------------------------

class Stack:
    def __init__(self):
        self.data = []
    def push(self, val):
        self.data.append(val)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1] if self.data else None
    def empty(self):
        return not self.data

# ------------------------
# 🧱 ALT: DEQUE IMPLEMENTATION
# ------------------------

from collections import deque
stack = deque()
stack.append('a')              # push
stack.pop()                    # pop
peek = stack[-1]               # peek
stack.clear()

# bounded stack
stack = deque(maxlen=1000)     # auto-trims oldest items

# ------------------------
# 🔁 LOOPING / DEBUG
# ------------------------

# top to bottom
for val in reversed(stack):
    print(val)

# ------------------------
# 🔁 DFS ITERATIVE (CLASSIC STACK USE)
# ------------------------

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)
    return visited

# ------------------------
# 🧮 COMMON STACK PATTERNS
# ------------------------

# 1. Valid Parentheses
def is_valid(s):
    stack = []
    match = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in match.values():
            stack.append(c)
        elif c in match:
            if not stack or stack[-1] != match[c]:
                return False
            stack.pop()
    return not stack

# 2. Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))
    return stack[0]

# 3. Next Greater Element
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []
    for i, val in enumerate(nums):
        while stack and val > nums[stack[-1]]:
            j = stack.pop()
            res[j] = val
        stack.append(i)
    return res

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

# peek safely
if stack:
    print(stack[-1])

# clear entire stack
stack.clear()

# simulate undo
history = []
history.append("action1")
history.append("action2")
history.pop()

# bounded stack
s = deque(maxlen=5)
for i in range(10):
    s.append(i)                # only last 5 remain

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# pop on empty stack → IndexError
# stack[-1] on empty → IndexError
# avoid accessing/setting mid-stack
# list.pop(0) is O(n) — use deque for queue-like ops
# mutation during iteration = unpredictable

# list vs deque:
# list is slightly faster for push/pop at end
# deque better for large or two-ended ops

# reference aliasing
s1 = []
s2 = s1
s2.append(5)
print(s1)                      # [5]

# ------------------------
# 🧵 WHEN TO USE STACKS
# ------------------------

# - Reversing/backtracking logic
# - Parsing expressions, parentheses
# - Evaluating RPN
# - DFS traversal (iterative)
# - Undo/redo history
# - Monotonic problems (e.g., next greater)

# ------------------------
# 📊 LIST vs DEQUE for STACKS
# ------------------------

# list:
# ✅ fast push/pop at end
# ✅ familiar syntax
# ❌ inefficient for double-ended ops

# deque:
# ✅ consistent O(1) appends/pops at both ends
# ✅ supports maxlen
# ✅ memory safe for large stacks

# → use list unless scale or dual-ended logic is needed

# ------------------------
# 🧠 STACK-BASED PROBLEMS TO PRACTICE
# ------------------------

# - Valid Parentheses
# - Min Stack
# - Evaluate Reverse Polish Notation
# - Next Greater Element
# - Largest Rectangle in Histogram
# - Daily Temperatures
# - Decode String
# - Simplify Path
# - Asteroid Collision
# - DFS (Iterative)

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# push (append):       O(1)
# pop:                 O(1)
# peek ([-1]):         O(1)
# search/lookup:       O(n)
# insert/remove mid:   O(n)
