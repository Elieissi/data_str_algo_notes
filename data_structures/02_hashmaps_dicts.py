# -----------------------------------------
# 📦 HASHMAPS / DICTIONARIES (Python dict)
# -----------------------------------------

# ✅ WHAT IT IS:
# - Unordered key-value store using hash table
# - Keys must be hashable (str, int, tuple, etc.)
# - Values can be any type
# - Preserves insertion order (Python 3.7+)
# - Backed by open-addressed hash table in CPython
# - Allows fast updates, lookups, and deletions

# 🔁 ACCESS PATTERN: Key-based lookup → O(1) average
# ❗ Worst-case for insert/delete/search → O(n) (hash collisions)

# ------------------------
# 🛠 BASIC OPERATIONS
# ------------------------

d = {'name': 'Alice', 'age': 25}   # create dict
print(d['name'])                  # access → 'Alice'
print(d.get('job'))              # safe get → None

d['job'] = 'Engineer'            # insert new key
d['age'] = 26                    # update existing key

del d['job']                     # delete key
d.pop('age')                     # remove key and return value
d.clear()                        # remove all entries

# check length
print(len(d))

# set a default value when key might be missing
d['score'] = d.get('score', 0) + 1  # safe increment pattern

# ------------------------
# 🔁 LOOPING
# ------------------------

for k in d:
    print(k, d[k])              # key and value

for k, v in d.items():
    print(f"{k}: {v}")          # cleaner

for v in d.values():
    print(v)

# ------------------------
# 🔎 SEARCH / MEMBERSHIP
# ------------------------

print('name' in d)              # True (key lookup)
print('Alice' in d.values())   # True (value lookup)

# ------------------------
# 📐 LENGTH & EMPTY CHECK
# ------------------------

print(len(d))
if not d:
    print("empty dict")

# ------------------------
# 🧱 COPYING DICTS
# ------------------------

a = {'x': 1}
b = a.copy()                   # shallow copy
c = dict(a)                    # another shallow copy
d = a                          # ❌ reference only

# ------------------------
# ➕ MERGING & DEFAULTS
# ------------------------

# update()
a = {'x': 1}
a.update({'y': 2})             # merge new keys in-place

# union (Python 3.9+)
x = {'a': 1}
y = {'b': 2}
z = x | y                      # {'a':1, 'b':2}

# setdefault → assign default if missing
profile = {}
profile.setdefault('name', 'Unknown')  # safe insert
print(profile)

# fromkeys → create dict from list of keys
keys = ['a', 'b', 'c']
blank = dict.fromkeys(keys, 0)        # {'a':0, 'b':0, 'c':0}

# ------------------------
# 🔁 DICT COMPREHENSIONS
# ------------------------

squares = {x: x*x for x in range(5)}  # {0:0, 1:1, ..., 4:16}

# ------------------------
# 🧮 COMMON PATTERNS
# ------------------------

# 1. frequency count
def count_freq(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

# 2. two sum using hashmap
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# 3. group anagrams
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

# 4. reverse lookup (value → key)
def reverse_lookup(d, target_val):
    for k, v in d.items():
        if v == target_val:
            return k

# 5. nested defaultdict for graphs
from collections import defaultdict
graph = defaultdict(list)
graph['A'].append('B')  # safe without pre-init

# 6. manual max-2 from dict (no slicing)
def top_two_keys(d):
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    result = []
    count = 0
    for k, v in sorted_items:
        if count == 2:
            break
        result.append(k)
        count += 1
    return result

# ------------------------
# 🧰 PYTHON-SPECIFIC TOOLS
# ------------------------

# zip + dict
keys = ['a', 'b']
vals = [1, 2]
z = dict(zip(keys, vals))         # {'a':1, 'b':2}

# convert views to list
list(d.keys())                    # ['name']
list(d.values())                  # ['Alice']
list(d.items())                   # [('name', 'Alice')]

# sort keys
for k in sorted(d):
    print(k, d[k])

# tuple keys (multi-dimensional map)
coords = {(0,1): 'A', (2,3): 'B'}
print(coords[(2,3)])              # 'B'

# nested dict access
nested = {'user': {'name': 'Alice'}}
print(nested['user']['name'])

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ d['missing'] → KeyError
# ✅ d.get('missing') → None or default

# ❌ keys must be hashable (list/sets fail)
# coords = {[1,2]: 'A'} → ❌ TypeError

# mutating while looping:
# for k in d: del d[k] → ❌ RuntimeError
# for k in list(d): del d[k] → ✅

# reference aliasing
ref = {}
alias = ref
alias['x'] = 5
print(ref['x'])                  # 5

# dicts don’t auto-initialize
# d['x'] += 1 → ❌ KeyError unless pre-initialized
# use d.get('x', 0) + 1 or defaultdict

# reversing dict only works if values are unique

# ------------------------
# 🧵 WHEN TO USE DICTS
# ------------------------

# - Fast lookup / insertion / deletion
# - Count or categorize data
# - Map relationships (ID → value)
# - Track state or seen items
# - Represent graphs, adjacency, index maps
# - Cache/memoize computed results

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# access/set:     O(1) avg
# delete:         O(1) avg
# loop:           O(n)
# worst-case:     O(n) (due to collisions — rare)
