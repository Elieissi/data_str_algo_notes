# -----------------------------------------
# 📦 SETS (Python built-in set)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Unordered collection of unique, hashable elements
# - Backed by a hash table (like dict keys)
# - Mutable (add/remove items)
# - No duplicates, no indexing, no slicing

# 🔁 ACCESS PATTERN: membership check → O(1) avg
# ❗ unordered → iteration order not guaranteed

# ------------------------
# 🛠 BASIC OPERATIONS
# ------------------------

s = {1, 2, 3}                     # define literal set
s2 = set([2, 3, 4])               # convert list to set

s.add(4)                          # add one item
s.remove(2)                      # remove item (❌ error if missing)
s.discard(10)                    # remove safely if exists (no error)
s.pop()                          # remove arbitrary element
s.clear()                        # empty the set

print(3 in s)                    # True
print(len(s))                    # size

# ------------------------
# 🔁 LOOPING
# ------------------------

for val in s:
    print(val)

# ------------------------
# ✂️ CONVERSION & CREATION
# ------------------------

nums = [1, 2, 2, 3]
unique = set(nums)               # deduplicate → {1, 2, 3}
lst = list(unique)               # convert back to list

chars = set("banana")            # {'b', 'a', 'n'} — from string

# frozen set (immutable)
frozen = frozenset([1, 2])
# frozen.add(3) → ❌ AttributeError

# ------------------------
# 🔁 SET OPERATIONS
# ------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)                     # union → {1,2,3,4,5}
print(a & b)                     # intersection → {3}
print(a - b)                     # difference → {1,2}
print(a ^ b)                     # symmetric diff → {1,2,4,5}

# in-place variants
a |= b                           # union into a
a &= b                           # intersection into a
a -= b                           # difference from a
a ^= b                           # symmetric diff into a

# method form
a = {1, 2, 3}
b = {2, 3}
a.update([4, 5])                 # add multiple values
a.intersection_update(b)        # keep only shared values
a.difference_update(b)          # remove values in b
a.symmetric_difference_update(b)

# relations
print(a.issubset(b))            # ⊆ check
print(a.issuperset(b))          # ⊇ check
print(a.isdisjoint(b))          # no overlap?

# ------------------------
# 🧮 COMMON PATTERNS
# ------------------------

# 1. deduplicate
def dedup(arr):
    return list(set(arr))

# 2. check for duplicates
def has_duplicates(arr):
    return len(arr) != len(set(arr))

# 3. fast membership test
seen = set()
if x not in seen:
    seen.add(x)

# 4. list diff
def missing_from_b(a, b):
    return list(set(a) - set(b))

# 5. any common elements?
def shares_any(a, b):
    return bool(set(a) & set(b))

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

# set comprehension
evens = {x for x in range(10) if x % 2 == 0}

# copy
s1 = {1, 2}
s2 = s1.copy()

# convert views to list
vals = list(s1)

# performance tip
# use set for lookups, not list
lookup = set(big_list)
if x in lookup:
    ...

# frozen set use case
# use as dict key or set element
cache = {}
key = frozenset([1, 2])
cache[key] = "value"

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ indexing/slicing → TypeError
# s[0], s[:2] → invalid

# ❌ unhashable elements
# set([1, [2,3]]) → TypeError

# pop() removes arbitrary element, not "last"
# remove(x) crashes if x not present → use discard

# set math returns new set unless using *_update methods
# sets don’t preserve order (even if they seem to)

# reference aliasing
a = set([1, 2])
b = a
b.add(3)
print(a)    # {1, 2, 3} → same object

# ------------------------
# 🧵 WHEN TO USE SETS
# ------------------------

# - need fast membership test
# - eliminate duplicates
# - compare two datasets
# - track seen/visited elements
# - use set math (union, diff, etc.)

# ------------------------
# 🧠 HASHABLE TYPES
# ------------------------

# ✅ allowed: int, str, float, bool, tuple (if contents are hashable)
# ❌ disallowed: list, dict, set (mutable = unhashable)

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# x in set:               O(1) avg
# add(x), discard(x):     O(1) avg
# remove(x):              O(1) avg
# loop:                   O(n)
# set ops (union, etc.):  O(n)
# worst-case:             O(n) (collision-heavy)
