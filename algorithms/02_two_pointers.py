# -----------------------------------------
# 🔁 TWO POINTERS
# -----------------------------------------

# ✅ WHAT IT IS:
# - Technique using two indices moving over a sequence
# - Converts nested loops into linear passes
# - Common in arrays, strings, and linked data
# - Variants include fixed-window, variable-window, dual-end, fast/slow

# 🔁 ACCESS PATTERN:
# - Two pointers moving in same or opposite directions
# - Usually O(n), sometimes used in sliding windows or merging

# ------------------------
# 1️⃣ DUAL-END POINTERS (start + end)
# ------------------------

# Check if array has pair summing to target
def has_pair_with_sum(arr, target):
    arr.sort()                          # required if input is not sorted
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True                 # found valid pair
        elif s < target:
            left += 1                   # increase sum by moving left pointer
        else:
            right -= 1                  # decrease sum by moving right pointer
    return False                        # no such pair found

# Max area between two vertical lines (Leetcode #11)
def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        if height[left] < height[right]:
            left += 1                   # discard smaller height
        else:
            right -= 1
    return max_area

# Palindrome check
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ------------------------
# 2️⃣ SAME-DIRECTION: FAST/SLOW
# ------------------------

# Remove duplicates from sorted array (in-place)
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:     # found new unique value
            slow += 1
            nums[slow] = nums[fast]      # overwrite duplicate
    return slow + 1

# Overwrite zero values in-place (3-pointer: slow, fast, scanner)
def remove_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:              # copy only non-zero
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):              # fill remaining with zeros
        nums[slow] = 0
        slow += 1

# ------------------------
# 3️⃣ SLIDING WINDOW (FIXED + VARIABLE)
# ------------------------

# Fixed-size window: max sum of k-length subarray
def max_subarray_sum_k(nums, k):
    window = sum(nums[:k])              # first window sum
    max_sum = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k] # slide window: add new, drop oldest
        max_sum = max(max_sum, window)
    return max_sum

# Variable-size window: min subarray length with sum ≥ target
def min_subarray_len(target, nums):
    left = total = 0
    res = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:          # valid window found
            res = min(res, right - left + 1)
            total -= nums[left]         # shrink window
            left += 1
    return res if res != float('inf') else 0

# ------------------------
# 4️⃣ STRINGS (COMPRESSION / WINDOW)
# ------------------------

# Compress repeating characters: 'aaabbc' → 'a3b2c1'
def compress(s):
    i = 0
    res = []
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        res.append(s[i] + str(count))   # append char + count
        i += 1
    return ''.join(res)

# Check if s contains an anagram of t
def has_anagram(s, t):
    from collections import Counter
    if len(t) > len(s): return False

    t_count = Counter(t)
    window = Counter(s[:len(t)])
    
    if window == t_count:
        return True

    for i in range(len(t), len(s)):
        window[s[i]] += 1
        window[s[i - len(t)]] -= 1
        if window[s[i - len(t)]] == 0:
            del window[s[i - len(t)]]
        if window == t_count:
            return True
    return False

# ------------------------
# 🧮 COMMON PATTERNS
# ------------------------

# Reverse array in-place
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Merge two sorted arrays (into new list)
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# Skip duplicates after sorting
def skip_duplicates(nums):
    nums.sort()
    result = []
    i = 0
    while i < len(nums):
        if i == 0 or nums[i] != nums[i - 1]:
            result.append(nums[i])
        i += 1
    return result

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ Don’t forget to sort input if problem requires order
# ❌ Watch out for off-by-one loop errors (`while left < right` vs `<=`)
# ❌ Some problems require inclusive bounds or skipping duplicates
# ❌ Don’t modify list structure while iterating unless in-place overwrite
# ❌ Right pointer can outrun data in sliding windows

# ------------------------
# 🧰 PYTHON TOOLS
# ------------------------

# zip() to iterate two lists together
a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):
    print(x, y)

# enumerate() for index + value
for i, val in enumerate(a):
    print(i, val)

# slicing in reverse
print(a[::-1])  # reversed list

# ------------------------
# 🧵 WHEN TO USE
# ------------------------

# - sorted inputs with target constraints
# - merge, dedup, pair-finding problems
# - compression or pattern scanning in strings
# - maintaining or shrinking subarray/window
# - optimizing nested loops

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# dual-pointer scan:         O(n)
# fixed sliding window:      O(n)
# variable window:           O(n) avg
# merge sorted arrays:       O(n + m)
# most in-place logic:       O(1) space
