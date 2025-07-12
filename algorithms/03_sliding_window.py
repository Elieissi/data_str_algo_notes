# -----------------------------------------
# 📏 SLIDING WINDOW
# -----------------------------------------

# ✅ WHAT IT IS:
# - Technique for processing a subset ("window") of input as you iterate
# - Reuses partial work to avoid recomputation
# - Works on arrays, strings, counters
# - Comes in fixed-size or variable-size variants

# 🔁 POINTER BEHAVIOR:
# - right expands the window
# - left contracts the window when condition is met or violated

# ------------------------
# 1️⃣ FIXED-WINDOW
# ------------------------

# max sum of any subarray of size k
def max_subarray_sum_k(nums, k):
    if len(nums) < k:
        return None                        # not enough elements

    window_sum = sum(nums[:k])            # sum of first window
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # add right, drop left
        max_sum = max(max_sum, window_sum)

    return max_sum

# running average of all k-length subarrays
def average_subarrays(nums, k):
    res = []
    window_sum = sum(nums[:k])
    res.append(window_sum / k)

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        res.append(window_sum / k)

    return res

# ------------------------
# 2️⃣ VARIABLE-SIZE WINDOW
# ------------------------

# min-length subarray with sum ≥ target
def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]             # expand window to the right

        while total >= target:           # shrink from left while still valid
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    # no valid subarray found
    return min_len if min_len != float('inf') else 0

# longest substring with ≤ k distinct characters
def longest_k_distinct(s, k):
    from collections import defaultdict
    freq = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1              # add char to window

        while len(freq) > k:             # too many distinct → shrink
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]        # remove empty keys
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

# ------------------------
# 3️⃣ MATCHING PATTERN (FREQ-BASED)
# ------------------------

# check if s contains any permutation of t
def contains_permutation(s, t):
    from collections import Counter

    if len(t) > len(s):
        return False                    # impossible if t longer

    t_count = Counter(t)                # target pattern count
    window = Counter(s[:len(t)])        # initial window

    if window == t_count:
        return True

    for i in range(len(t), len(s)):
        window[s[i]] += 1               # add new char to right
        window[s[i - len(t)]] -= 1      # remove old char from left

        if window[s[i - len(t)]] == 0:
            del window[s[i - len(t)]]   # remove zero-count entries

        if window == t_count:
            return True                 # match found

    return False                        # no match

# ------------------------
# 4️⃣ UNIQUE ELEMENT TRACKING
# ------------------------

# longest substring with no repeats
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])       # shrink until char removed
            left += 1

        seen.add(s[right])             # add current char
        max_len = max(max_len, right - left + 1)

    return max_len

# count subarrays with exactly k distinct integers
def subarrays_with_k_distinct(nums, k):
    from collections import defaultdict

    def at_most_k(k):
        count = defaultdict(int)
        res = left = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            res += right - left + 1     # count current window

        return res

    return at_most_k(k) - at_most_k(k - 1)  # exactly-k = at_most(k) - at_most(k-1)

# ------------------------
# 5️⃣ MONOTONIC QUEUE (MAX IN WINDOW)
# ------------------------

# max in every sliding window of size k
def max_sliding_window(nums, k):
    from collections import deque
    dq = deque()                        # stores indices
    res = []

    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()               # remove index outside window

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()                   # remove smaller elements

        dq.append(i)

        if i >= k - 1:
            res.append(nums[dq[0]])    # max is at front of deque

    return res

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ must shrink window properly or logic will break
# ❌ always remove zero-counts from counter/dict to avoid false mismatch
# ❌ fixed-size logic won't work on variable-size questions
# ❌ skip monotonic queue unless asked for max/min in window
# ❌ don't assume condition will *ever* be met (handle empty case)

# ------------------------
# 🧰 PYTHON TOOLS
# ------------------------

from collections import defaultdict, Counter, deque

# counter init
freq = defaultdict(int)
freq = Counter("string")

# slice window
window = s[i:i+k]

# del dict key if zero
if freq[c] == 0:
    del freq[c]

# check all window counts match
if window == target:
    ...

# ------------------------
# 🧵 WHEN TO USE
# ------------------------

# - substring, subarray with condition (sum, match, repeat)
# - count/rank/filter based on sliding range
# - min/max over range (monotonic queue)
# - anagram/permutation detection
# - longest/shortest substring with constraint

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# fixed window sum:               O(n)
# variable window shrink/expand:  O(n)
# freq map maintenance:           O(k) space
# monotonic deque:                O(n)
# nested-at-most trick:           O(n) twice
