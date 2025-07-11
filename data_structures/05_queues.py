# -----------------------------------------
# 📦 QUEUES (FIFO) — IMPLEMENTED WITH deque
# -----------------------------------------

# ✅ WHAT IT IS:
# - Linear data structure: First-In, First-Out (FIFO)
# - Insert at rear, remove from front
# - Used in scheduling, buffering, BFS, task processing

# 🔁 ACCESS PATTERN: enqueue (append) → right, dequeue (popleft) → left → O(1)
# ❗ Use deque — list.pop(0) is O(n), inefficient for queues

# ------------------------
# 🛠 BASIC OPERATIONS (DEQUE)
# ------------------------

from collections import deque

queue = deque()                   # create empty queue

queue.append('A')                 # enqueue
queue.append('B')

print(queue[0])                   # peek front
val = queue.popleft()             # dequeue front → 'A'

print(len(queue))                 # queue size
print(not queue)                  # is empty?

# copy
q_copy = queue.copy()

# clear
queue.clear()

# bounded queue (drops oldest on overflow)
bounded = deque(maxlen=3)
bounded.append(1)
bounded.append(2)
bounded.append(3)
bounded.append(4)                # drops 1 → [2, 3, 4]

# ------------------------
# 📎 DEQUE METHOD VARIANTS
# ------------------------

dq = deque([1])
dq.extend([2, 3])                # [1, 2, 3]
dq.extendleft([0, -1])           # [-1, 0, 1, 2, 3] (reversed input)

dq.rotate(2)                     # rotate right → [2nd last becomes front]
dq.rotate(-1)                    # rotate left → [2nd becomes last]

# reverse queue
reversed_q = deque(reversed(dq))

# ------------------------
# 🧱 CLASS IMPLEMENTATION
# ------------------------

class Queue:
    def __init__(self):
        self.data = deque()
    def enqueue(self, val):
        self.data.append(val)
    def dequeue(self):
        return self.data.popleft()
    def front(self):
        return self.data[0] if self.data else None
    def empty(self):
        return not self.data
    def size(self):
        return len(self.data)

# ------------------------
# 🔁 THREAD-SAFE QUEUES (MULTITHREADING)
# ------------------------

from queue import Queue as ThreadQueue

q = ThreadQueue()
q.put(10)                         # enqueue
val = q.get()                     # dequeue
q.qsize()
q.empty()

# ------------------------
# 🔁 BFS EXAMPLE (STANDARD)
# ------------------------

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return visited

# ------------------------
# 🔁 BFS (MULTI-SOURCE)
# ------------------------

def bfs_all_sources(grid, sources):
    visited = set(sources)
    q = deque(sources)
    while q:
        node = q.popleft()
        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return visited

# ------------------------
# 🧮 COMMON QUEUE PATTERNS
# ------------------------

# 1. BFS traversal (graph/tree)
# 2. Level-order traversal
# 3. Multi-source BFS
# 4. Topological sort (zero in-degree queue)
# 5. Rotten oranges (grid traversal)
# 6. Sliding window maximum (monotonic queue)

# ------------------------
# 🔁 MONOTONIC QUEUE (for sliding max)
# ------------------------

def sliding_window_max(nums, k):
    q = deque()  # store indices
    result = []

    for i, val in enumerate(nums):
        while q and nums[q[-1]] < val:
            q.pop()
        q.append(i)

        if q[0] == i - k:
            q.popleft()

        if i >= k - 1:
            result.append(nums[q[0]])
    return result

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

# peek safely
if queue:
    print(queue[0])

# queue aliasing
q1 = deque([1])
q2 = q1
q2.append(2)
print(q1)                         # [1, 2]

# convert to list
list(queue)

# initialize with iterable
deque('abc')                     # deque(['a', 'b', 'c'])

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# list.pop(0) is O(n) → avoid for queues
# deque[0] or popleft() on empty → IndexError
# don't mix extend/extendleft without intention — order flips
# mutation while iterating → undefined behavior

# ------------------------
# 🧵 WHEN TO USE QUEUES
# ------------------------

# - First-come-first-served processing
# - BFS / level-order graph traversal
# - Event or task scheduling
# - Multi-source propagation problems
# - Stream windows or throttling

# ------------------------
# 📊 QUEUE TYPES IN PYTHON
# ------------------------

# deque (standard use):
# ✅ O(1) appends/pops both ends
# ✅ supports maxlen, rotation
# ✅ lightweight

# queue.Queue:
# ✅ thread-safe
# ❌ slower, more overhead

# list:
# ❌ pop(0) is O(n), not suitable for queues

# ------------------------
# 🧠 QUEUE-BASED PROBLEMS TO PRACTICE
# ------------------------

# - Binary Tree Level Order Traversal
# - Number of Islands (BFS)
# - Course Schedule (Topological Sort)
# - Open the Lock
# - Rotten Oranges
# - Sliding Window Maximum
# - Moving Average from Data Stream

# ------------------------
# ⏱ TIME COMPLEXITY (DEQUE)
# ------------------------

# enqueue (append):      O(1)
# dequeue (popleft):     O(1)
# peek front:            O(1)
# search:                O(n)
# rotation:              O(k)
