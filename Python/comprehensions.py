from icecream import ic
# list Comprehension

# Basic List Comprehension
# Syntax : [expression for item in iterable]

ic([num for num in range(5)])

#  List Comprehension with if statement
# Syntax : [expression for item in iterable if condition]

ic([num for num in range(5) if num % 2 == 0])

#  List Comprehension with if-else  statement
# Syntax : [expression_if_true if condition else expression_if_false for item in iterable]

ic([num if num % 2 == 0 else None for num in range(5)])

ic("".join([char.upper() if char.lower() in "aeiou" else char for char in "PAuRakh"]))

# Tuple compression

# Python does not have tuple comprehension, but you can use a generator expression inside tuple(), which behaves similarly.
#  syntax : (expression for item in iterable if condition)

ic(tuple(x**2 for x in range(5)))

# Set Comprehension

ic({x**2 for x in [1, 2, 2, 3, 4, 4, 5]})


# Dictionary Comprehension

# from a list
ic({num: num**2 for num in [n for n in range(1, 11)]})


# swapping keys and values of dict
original = {"a": 1, "b": 2, "c": 3}
ic({v: k for k, v in original.items()})


keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

ic({k: v for k, v in zip(keys, values)})

# Nested if-else
ic( [ i if i%2 ==0 else (i**2) if i>=20 else 0  for i in range(1,31)] )

# Nested Dictionary Comprehension

# to print : {1: {1: 1, 2: 2, 3: 3},
#  2: {1: 2, 2: 4, 3: 6},
#  3: {1: 3, 2: 6, 3: 9}}

ic({k: {i: k * i for i in range(1, 4)} for k in range(1, 4)})
ic({k: v for num in range(1, 6) for k, v in [(f"num_{num}", num), (f"square_{num}", num**2)]})
# Conditional Assignment in Dictionary Comprehension
ic({k: "even" if k % 2 == 0 else "odd" for k in range(1, 7)})

# Count Frequency of Characters in a String
ic({char: "banana".count(char) for char in "banana"})

# using enumurate
names = ["Alice", "Bob", "Charlie"]
ic({i: name for i, name in enumerate(names, start=1)})

# Use Cases
# 1)  Flattening a 2D List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ic([num for row in matrix for num in row])

# 2) Cartesian Product (Nested Loops)

ic(tuple((x, y) for x in range(3) for y in range(3)))

# Comprehension	Type	Use Case

# List [x for x in ...]	Ordered, allows duplicates	When you need a list of values

# Tuple tuple(x for x in ...)	Immutable, ordered	When an immutable collection is needed

# Set {x for x in ...}	Unordered, unique values	When duplicate removal is needed

# Generator (x for x in ...)	Lazy evaluation	When memory efficiency is important
