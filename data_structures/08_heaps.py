# -----------------------------------------
# 🔺 HEAPS — PRIORITY QUEUES (BINARY HEAP)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Complete binary tree stored as array
# - Min-heap: parent ≤ children (default in Python)
# - Max-heap: parent ≥ children (use negation)
# - Used for always getting/removing min/max in O(log n)
# - Not a full sort — only root is guaranteed smallest/largest

# ------------------------
# 🔁 INDEX FORMULAS
# ------------------------

# - Parent(i) = (i - 1) // 2
# - Left(i)   = 2 * i + 1
# - Right(i)  = 2 * i + 2

# ------------------------
# 📦 PYTHON HEAP BASICS (MIN-HEAP)
# ------------------------

import heapq

nums = [4, 1, 7, 3, 8, 5]
heapq.heapify(nums)              # convert list to min-heap in-place
print(nums[0])                   # peek min → 1

heapq.heappush(nums, 2)          # insert new item → O(log n)
print(heapq.heappop(nums))       # pop min item → O(log n)

heapq.heappushpop(nums, 6)       # push then pop → more efficient than separate
heapq.heapreplace(nums, 9)       # pop root, then push 9 → O(log n)

# ------------------------
# 🔺 MAX-HEAP (SIMULATED)
# ------------------------

nums = [4, 1, 7]
maxheap = [-x for x in nums]
heapq.heapify(maxheap)

print(-heapq.heappop(maxheap))   # max = -min → 7
heapq.heappush(maxheap, -10)     # insert new max

# ⚠️ -0 == 0, can cause subtle bugs

# ------------------------
# 🧮 K LARGEST / SMALLEST ELEMENTS
# ------------------------

nums = [9, 4, 1, 7, 3, 6]
print(heapq.nlargest(3, nums))   # → [9, 7, 6]
print(heapq.nsmallest(2, nums))  # → [1, 3]

# ------------------------
# 🧱 CUSTOM OBJECTS IN HEAP
# ------------------------

# wrap object as (priority, value) for comparison
tasks = [(2, 'task A'), (1, 'task B'), (3, 'task C')]
heapq.heapify(tasks)
print(heapq.heappop(tasks))      # → (1, 'task B')

# ------------------------
# 🛠 TIEBREAKER WITH SEQUENCE
# ------------------------

import itertools

counter = itertools.count()      # ensures unique tiebreak
task_heap = []
heapq.heappush(task_heap, (2, next(counter), 'task A'))
heapq.heappush(task_heap, (2, next(counter), 'task B'))
# avoids compare error if objects are non-comparable

# ------------------------
# 🔁 HEAP SORT
# ------------------------

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# ------------------------
# 🛠 MANUAL MIN-HEAP CLASS
# ------------------------

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        out = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return out

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# - only root is ordered; rest is partial
# - no decrease-key / update-in-place → must re-heapify or use (priority, count, obj)
# - modifying item values outside breaks the heap silently
# - pop(0) is O(n); use heapq.heappop() only
# - for max-heap, negate all values but watch out for -0 == 0
# - same-priority elements: insertion order not guaranteed

# ------------------------
# 🧵 WHEN TO USE HEAPS
# ------------------------

# - dynamically track top/bottom values (k-largest, median stream)
# - greedy selection (always grab best/worst next)
# - task scheduling / real-time processing
# - Dijkstra, Prim, Huffman coding, A* pathfinding
# - merge K sorted lists

# ------------------------
# 🧠 INTERVIEW PROBLEMS TO PRACTICE
# ------------------------

# - Kth Largest Element in Stream
# - Top K Frequent Elements
# - Median from Data Stream
# - Sliding Window Maximum
# - Merge K Sorted Lists
# - Connect Sticks for Min Cost
# - Reorganize String

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# heapify():        O(n)
# push/pop:         O(log n)
# peek (min/max):   O(1)
# heap sort:        O(n log n)
# nlargest/nsmallest: O(n log k)
