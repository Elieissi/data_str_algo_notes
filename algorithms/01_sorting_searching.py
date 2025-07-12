# -----------------------------------------
# 🔍 SORTING & SEARCHING (CORE PATTERNS)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Sorting = reordering items into ascending/descending order
# - Searching = locating values or boundaries within data
# - Binary search requires sorted data
# - Sorting is often a pre-step to search or pairing logic

# 🔁 ACCESS PATTERN:
# - Binary search: O(log n)
# - Sorting: O(n log n)

# ------------------------
# 🛠 PYTHON BUILT-IN SORT
# ------------------------

arr = [5, 1, 4, 2]

sorted_arr = sorted(arr)         # ✅ returns a new sorted list (original unchanged)
arr.sort()                       # ✅ sorts the list in-place (modifies `arr`)

arr.sort(reverse=True)           # sort in descending order

# custom sort with a key
people = [('bob', 25), ('amy', 20), ('joe', 22)]
people.sort(key=lambda x: x[1])              # sort by age
people.sort(key=lambda x: (x[1], x[0]))      # sort by age, then name
people.sort(key=lambda x: x[1], reverse=True)# sort by age descending

# sort a dictionary by value
d = {'a': 3, 'b': 1}
sorted_items = sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('a', 3)]

# -----------------------------------------
# 🔬 STABILITY NOTES
# -----------------------------------------

# Python's sort is stable → relative order of equal elements is preserved
# Useful when doing multi-pass sorts (e.g., by last name, then first name)

# ------------------------
# 🔍 BINARY SEARCH (STANDARD)
# ------------------------

# search for a target value in sorted list
def binary_search(nums, target):
    left, right = 0, len(nums) - 1   # define the search space [left, right]
    while left <= right:
        mid = (left + right) // 2    # compute midpoint
        if nums[mid] == target:      # found it
            return mid
        elif nums[mid] < target:     # target in right half
            left = mid + 1
        else:                        # target in left half
            right = mid - 1
    return -1                        # not found

# ------------------------
# 🔢 LOWER / UPPER BOUND
# ------------------------

# lower_bound = first index i where nums[i] >= target
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:       # move right if too small
            left = mid + 1
        else:                        # possible match, go left
            right = mid
    return left                      # returns len(nums) if target > all elements

# upper_bound = first index i where nums[i] > target
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:      # not strictly greater → move right
            left = mid + 1
        else:
            right = mid
    return left                      # returns len(nums) if target ≥ all elements

# ------------------------
# 📈 MERGE SORT (RECURSIVE)
# ------------------------

# stable sort using divide and conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr                   # base case: already sorted
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # recursively sort left
    right = merge_sort(arr[mid:])   # recursively sort right
    return merge(left, right)       # merge sorted halves

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # walk both lists
        if left[i] <= right[j]:
            result.append(left[i])   # take from left if smaller
            i += 1
        else:
            result.append(right[j])  # take from right if smaller
            j += 1
    result.extend(left[i:])         # add leftovers
    result.extend(right[j:])
    return result

# ------------------------
# ⚡ QUICK SORT (IN-PLACE)
# ------------------------

# unstable in-place quicksort (uses last element as pivot)
def quick_sort(arr):
    def sort(low, high):
        if low < high:
            p = partition(arr, low, high)  # pivot index
            sort(low, p - 1)               # left part
            sort(p + 1, high)              # right part

    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]  # move smaller item to front
                i += 1
        arr[i], arr[high] = arr[high], arr[i]    # place pivot
        return i

    sort(0, len(arr) - 1)

# ------------------------
# 🧮 COMMON PATTERNS
# ------------------------

# check if list is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# binary search on answer (monotonic function)
def min_satisfying_val(nums, check):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if check(nums[mid]):
            right = mid              # try smaller values
        else:
            left = mid + 1           # try larger values
    return left

# two-pointer after sorting
def has_pair_sum(nums, target):
    nums.sort()                      # sort first
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

import bisect

arr = [1, 3, 5, 7]

bisect.bisect_left(arr, 4)     # → 2 (insert before 5)
bisect.bisect_right(arr, 4)    # → 2 (same for 4)

bisect.insort(arr, 4)          # arr becomes [1, 3, 4, 5, 7]

# reverse-sorted one-liner
for x in reversed(sorted(arr)):
    print(x)

# sorting dictionary items
d = {'a': 5, 'b': 2}
sorted_d = sorted(d.items(), key=lambda x: x[1])

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ list.sort() returns None → use sorted() if you want a new list
# ❌ binary search only works on sorted input
# ❌ merge sort is O(n) space
# ❌ quick sort is O(n^2) worst-case if input is already sorted
# ❌ off-by-one bugs common in lower/upper bounds
# ❌ upper_bound may return len(arr) → must check before access

# ------------------------
# 🧵 WHEN TO USE
# ------------------------

# - need sorted input for two-pointer or binary search
# - want to find boundaries for insertion
# - must sort by multiple keys or values
# - need a fast in-place sort → quick sort
# - need stable sort → merge or Python’s built-in

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# sorted() / sort():      O(n log n)
# binary search:          O(log n)
# merge sort:             O(n log n), stable, O(n) space
# quick sort:             O(n log n) avg, O(n^2) worst, in-place
# bisect:                 O(log n)
