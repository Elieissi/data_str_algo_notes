# -----------------------------------------
# 📦 ARRAYS / LISTS (Python built-in list)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Ordered, indexed, dynamic collection
# - Mutable (can modify in-place)
# - Backed by dynamic array (amortized resize)

# 🔁 ACCESS PATTERN: Random-access by index → O(1)
# ❗ insert/delete at arbitrary position → O(n)

# ------------------------
# 🛠 BASIC OPERATIONS
# ------------------------

nums = [10, 20, 30, 40]       # create list
print(nums[0])                # access by index → 10
nums[2] = 99                  # update → [10, 20, 99, 40]

nums.append(50)              # add to end → O(1)
nums.insert(1, 15)           # insert at index 1 → O(n)
nums.pop()                   # remove last → O(1)
nums.pop(2)                  # remove index 2 → O(n)
nums.remove(99)              # remove by value → O(n)

# ------------------------
# 🔁 LOOPING
# ------------------------

for num in nums:
    print(num)

for i in range(len(nums)):
    print(i, nums[i])

for i, val in enumerate(nums):
    print(i, val)             # cleaner index+value loop

# ------------------------
# 🔎 SEARCH / MEMBERSHIP
# ------------------------

print(40 in nums)             # True
print(nums.index(40))        # get index of 40
print(nums.count(15))        # how many times 15 appears

# ------------------------
# ✂️ SLICING
# ------------------------

print(nums[1:3])              # slice index 1 to 2
print(nums[:2])               # first two elements
print(nums[::-1])             # reversed

# ------------------------
# 📐 LENGTH & EMPTY CHECK
# ------------------------

print(len(nums))              # list length
if not nums:
    print("empty list")

# ------------------------
# 🧱 COPYING LISTS
# ------------------------

a = [1, 2, 3]
b = a[:]                      # shallow copy
c = list(a)                   # another shallow copy
d = a                         # ❌ reference to same object

# ------------------------
# ➕ EXTEND VS APPEND
# ------------------------

x = [1, 2]
x.append([3, 4])              # [1, 2, [3, 4]]
x = [1, 2]
x.extend([3, 4])              # [1, 2, 3, 4]

# ------------------------
# 🔁 LIST COMPREHENSIONS
# ------------------------

squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]

# ------------------------
# 🧮 COMMON PATTERNS
# ------------------------

def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

def remove_evens(arr):
    return [x for x in arr if x % 2 != 0]

# ------------------------
# 🧱 2D LISTS (MATRICES)
# ------------------------

matrix = [[1, 2], [3, 4]]
print(matrix[1][0])           # 3

grid = [[0] * 3 for _ in range(3)]  # safe way to create 3x3 grid

# ⚠️ DON'T DO THIS:
bad_grid = [[0] * 3] * 3      # all rows reference same list

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

# zip → parallel iteration
a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b):
    print(x, y)

# all / any
print(all(x > 0 for x in a))     # True
print(any(x > 2 for x in a))     # True

# del
del a[1]                         # remove by index

# convert str to list and back
s = "hello"
chars = list(s)                 # ['h', 'e', 'l', 'l', 'o']
s2 = ''.join(chars)             # "hello"

# fill list
zeros = [0] * 5                 # [0, 0, 0, 0, 0]

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# nums = nums.sort() returns None → use sorted()
# modifying list while looping can cause skipped elements
# pop(0) is O(n) → avoid for queue-like use (use deque instead)
# [[0]*n]*m creates m refs to same list → shared mutation bug

# ------------------------
# 🧵 WHEN TO USE LISTS
# ------------------------

# - ordered, indexed data
# - fast end-insertions
# - collecting inputs/results
# - iterative filtering/transformation

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# indexing:     O(1)
# update:       O(1)
# append:       O(1) amortized
# pop():        O(1)
# insert(i,x):  O(n)
# remove(x):    O(n)
# in (search):  O(n)
