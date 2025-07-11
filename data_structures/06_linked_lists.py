# -----------------------------------------
# 📦 LINKED LISTS — SINGLY & DOUBLY
# -----------------------------------------

# ✅ WHAT IT IS:
# - Node-based linear structure
# - Each node points to the next (or prev+next for doubly)
# - No indexing; must traverse to access
# - Useful for dynamic memory, pointer-based logic, and in-place ops

# 🔁 ACCESS PATTERN: sequential only → O(n)
# ❗ not a built-in Python type; implemented manually

# ------------------------
# 🧱 SINGLY LINKED LIST NODE
# ------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}"

# ------------------------
# 🧱 DOUBLY LINKED LIST NODE
# ------------------------

class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# used in: LRU cache, deque, editors

# ------------------------
# 🛠 BUILD & TRAVERSE
# ------------------------

def print_list(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print("None")

# manually build: 1 -> 2 -> 3
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

print_list(n1)

# ------------------------
# 📎 SENTINEL NODE PATTERN
# ------------------------

# dummy = ListNode(0)
# dummy.next = real head
# cur = dummy
# used to simplify head insert/delete edge cases

# ------------------------
# 🧱 LINKED LIST CLASS (WITH TAIL)
# ------------------------

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_end(self, val):
        node = ListNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_val(self, val):
        dummy = ListNode(0, self.head)
        prev, cur = dummy, self.head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                break
            prev, cur = cur, cur.next
        self.head = dummy.next

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def print(self):
        print_list(self.head)

# ------------------------
# 🔁 REVERSAL
# ------------------------

def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

# ------------------------
# 🔁 FIND MIDDLE NODE
# ------------------------

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ------------------------
# 🔁 REMOVE NTH FROM END (2-PASS)
# ------------------------

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    cur = dummy
    for _ in range(length - n):
        cur = cur.next
    cur.next = cur.next.next
    return dummy.next

# ------------------------
# 🔁 CYCLE DETECTION
# ------------------------

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# ------------------------
# 🔁 MERGE TWO SORTED LISTS
# ------------------------

def merge(l1, l2):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# ------------------------
# 🧰 UTILITIES
# ------------------------

def from_list(arr):
    dummy = ListNode()
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# - inserting tail = O(n) unless tail ptr
# - deleting head = edge case unless dummy used
# - reversal loses access to original head
# - forget breaking .next leads to memory leaks or cycles
# - no random access (head[2] ❌)
# - infinite loops if cycle present
# - dummy pattern required in many problems
# - aliasing = shared mutation

# ------------------------
# 🧵 WHEN TO USE LINKED LISTS
# ------------------------

# - dynamic/unknown size sequences
# - frequent insert/delete at head/mid
# - pointer-based manipulation (merge, reverse, reorder)
# - abstract buffer structures (queue, stack, deque)
# - LRU cache (via DLL + hashmap)

# ------------------------
# 🧠 PROBLEMS TO PRACTICE
# ------------------------

# - Reverse Linked List
# - Merge Two Sorted Lists
# - Detect Cycle
# - Remove Nth From End
# - Add Two Numbers
# - Middle of Linked List
# - Palindrome Linked List
# - Reorder List
# - Rotate List
# - LRU Cache (DLL + dict)

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# access/search:       O(n)
# insert at head:      O(1)
# insert at tail:      O(n) or O(1) with tail
# delete:              O(n)
# reverse:             O(n)
# space:               O(n)
