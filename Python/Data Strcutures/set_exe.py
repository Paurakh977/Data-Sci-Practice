from icecream import ic

# 1. Creating Sets
# Using curly braces to define a set (order is not guaranteed)
set1 = {1, 2, 3, 4, 5}
# Using the set() constructor from an iterable (duplicates are removed)
set2 = set([3, 4, 5, 6, 7])
# Creating a set from a string (each unique character)
set3 = set("hello")  #set3: {'h', 'e', 'l', 'o'}

# 2. Converting a List to a Set (removing duplicates)
lst = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(lst)

# Converting back to a list if needed
unique_list = list(set_from_list)

# 3. Basic Set Operations: Union, Intersection, Difference, Symmetric Difference
union_set = set1 | set2  # or set1.union(set2)
intersection_set = set1 & set2  # or set1.intersection(set2)
difference_set = set1 - set2  # or set1.difference(set2)
ic("Difference (set1 - set2):", difference_set)
difference_set2 = set2 - set1  
ic("Difference (set2 - set1):", difference_set2)

symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
ic("Symmetric Difference between set1 and set2:", symmetric_diff)

# 4. Set Methods: add(), update(), remove(), discard(), pop(), clear()
a = {1, 2, 3}
a.add(4)
a.update([5, 6])  #a: {1, 2, 3, 4, 5, 6}
# remove() raises an error if the element is not found
a.remove(2)
# discard() does not raise an error if the element is missing
a.discard(10)
# pop() removes and returns an arbitrary element (since sets are unordered)
popped = a.pop()
# clear() empties the set
a.clear()



# 6. Set Comprehensions
# Creating a set of squares from 1 to 10
squares = {x**2 for x in range(1, 11)}
# Creating a set of even numbers between 1 and 20
evens = {x for x in range(1, 21) if x % 2 == 0}

# 7. Frozen Sets (Immutable Sets)
frozen = frozenset([1, 2, 3, 2, 1])
# Frozen sets support methods like union and intersection but cannot be modified.
frozen_union = frozen.union({4, 5})

# 8. Subset, Superset, and Disjoint Checks
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
ic("Is a a subset of b?", a.issubset(b))  # true
ic("Is b a superset of a?", b.issuperset(a))  #true
c = {6, 7, 8}
ic("Are a and c disjoint?", a.isdisjoint(c)) #true
ic("Are b and c disjoint?", b.isdisjoint(c)) #true

# 9. Set Operations Using Methods

# Union using method
union_method = set1.union(set2)
# Intersection using method
intersection_method = set1.intersection(set2)
# Difference using method
difference_method = set1.difference(set2)
# Symmetric difference using method
sym_diff_method = set1.symmetric_difference(set2)
