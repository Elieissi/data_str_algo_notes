# -----------------------------------------
# #️⃣ HASHING TECHNIQUES
# -----------------------------------------

# ✅ WHAT IT IS:
# - Use of hash functions to map keys → index for fast access
# - Enables constant-time avg access for insert, delete, lookup
# - Backing structure for dict, set, defaultdict, Counter, etc.

# 🔁 ACCESS PATTERN:
# - Unordered
# - Direct access by key → O(1) avg
# - No indexing or slicing

# ------------------------
# 1️⃣ DICTIONARY (key → value)
# ------------------------

# basic dict usage
d = {}
d["a"] = 1                            # add key-value pair
d["a"] += 1                           # update value
print(d["a"])                         # access value by key

# safe access
print(d.get("x", 0))                  # returns 0 if key missing

# check presence
if "a" in d:
    print("key exists")

# iterate keys/values/pairs
for k in d: print(k)
for v in d.values(): print(v)
for k, v in d.items(): print(k, v)

# dictionary comprehension
squares = {x: x**2 for x in range(4)}  # {0:0, 1:1, 2:4, 3:9}

# setdefault: lazy init if key doesn't exist
d = {}
d.setdefault("x", []).append(10)     # init to [] then append

# ------------------------
# 2️⃣ SETS (value only)
# ------------------------

# sets store only keys, no values
s = set()
s.add("x")                            # add value
s.discard("y")                        # safe remove (no error)
print("x" in s)                       # fast O(1) membership test

# deduplication
unique = set([1, 2, 2, 3])            # {1, 2, 3}

# set operations (math style)
a, b = {1,2,3}, {2,3,4}
print(a & b)                          # intersection
print(a | b)                          # union
print(a - b)                          # difference

# set comprehension
evens = {x for x in range(10) if x % 2 == 0}

# ------------------------
# 3️⃣ DEFAULTDICT (auto-init)
# ------------------------

from collections import defaultdict

# no need to check if key exists
count = defaultdict(int)
count["a"] += 1                       # auto-initialized to 0

# group values by key
group = defaultdict(list)
group["fruit"].append("apple")       # auto-initialized to []

# nested dicts
nested = defaultdict(lambda: defaultdict(int))
nested["a"]["b"] += 1

# ------------------------
# 4️⃣ COUNTER (frequency map)
# ------------------------

from collections import Counter

# count characters in string
freq = Counter("banana")             # {'b':1, 'a':3, 'n':2}
print(freq["a"])                     # → 3

# top-k frequent
print(freq.most_common(2))           # [('a', 3), ('n', 2)]

# subtract counters
c1 = Counter("abbc")
c2 = Counter("abc")
c1.subtract(c2)                      # modifies in-place → {'b': 1, 'c': 0}

# create from list
nums = [1, 2, 2, 3]
print(Counter(nums))                 # {2:2, 1:1, 3:1}

# ------------------------
# 5️⃣ ADVANCED TRICKS
# ------------------------

# 1. check duplicates
def has_dup(arr):
    return len(arr) != len(set(arr))  # O(n)

# 2. first duplicate
def first_dup(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return x
        seen.add(x)
    return None

# 3. frequency count (manual)
def freq_map(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

# 4. invert dict
original = {'a': 1, 'b': 2}
inverse = {v: k for k, v in original.items()}

# 5. anagram check
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# 6. tuple as hashmap key
grid_state = {}
grid_state[(0, 1)] = True            # valid since tuple is hashable

# 7. frozenset as dict key
cache = {}
key = frozenset([1, 2])
cache[key] = "valid"                 # works since frozenset is immutable

# ------------------------
# 6️⃣ ORDERED HASHMAP
# ------------------------

from collections import OrderedDict

# preserves insertion order
od = OrderedDict()
od["x"] = 1
od["y"] = 2

# move to end (LRU cache pattern)
od.move_to_end("x")

# delete oldest entry
od.popitem(last=False)

# ------------------------
# 7️⃣ HASHING CUSTOM OBJECTS
# ------------------------

class Node:
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(self.val)         # hash by value

    def __eq__(self, other):
        return self.val == other.val  # define equality

visited = set()
visited.add(Node(5))                 # ✅ works in set

# ------------------------
# ⚠️ GOTCHAS
# ------------------------

# ❌ dict keys must be hashable:
# - ✅: int, str, tuple of immutables, frozenset
# - ❌: list, dict, set

# ❌ Counter keys with zero still remain unless manually deleted
# ❌ set.remove(x) errors if x not present → use discard
# ❌ dict[key] errors if key not present → use .get() or defaultdict
# ❌ subtracting Counters may yield negative values
# ❌ tuple is only hashable if ALL its elements are hashable

# ❗ CPython dict resolves collisions via chaining
#    → Worst-case O(n), but avg case is O(1)

# ------------------------
# 🧰 PYTHON TOOLS
# ------------------------

# dictionary from list of pairs
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)

# filtering dict
filtered = {k: v for k, v in d.items() if v > 1}

# sorting by value
sorted_items = sorted(d.items(), key=lambda x: x[1])

# copying dict
copy = dict(d)

# clean Counter
if c[key] == 0:
    del c[key]

# ------------------------
# 🧵 WHEN TO USE HASHING
# ------------------------

# - fast presence checks
# - deduplication
# - frequency counting
# - group by property
# - anagram / pattern match
# - track visited states (search / recursion)

# ------------------------
# ⏱ TIME COMPLEXITY
# ------------------------

# insert / access / delete: O(1) avg, O(n) worst
# Counter / defaultdict access: O(1)
# set/dict lookup: O(1)
# iteration over n items: O(n)
