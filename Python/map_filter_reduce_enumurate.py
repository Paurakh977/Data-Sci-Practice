from icecream import ic
from functools import reduce
#map(function, iterable, ...)

ic(
    tuple(map(lambda c: (c * 9/5) + 32, [0, 10, 20, 30]))
    )
# Multiple Iterables
ic(
    list(map(lambda name,score: f"{name} --> {score}",["Alice", "Bob", "Charlie"],[85, 90, 95]))
)

exchange_rate = 1.1  # Convert USD to EUR
transactions_usd = [100, 250, 80, 500]
ic(
    list(map(lambda x: round(x* exchange_rate,2),transactions_usd))
)

# filter() Function
# Purpose: Construct an iterator from those elements of an iterable for which a function returns true.
# Syntax:
# filter(function, iterable)

data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95}
]

ic(
    list(
        filter(lambda dict: dict['score']>80, data)
    )
)

logs = [
    "[INFO] System started",
    "[ERROR] Disk failure detected",
    "[WARNING] Memory usage high",
    "[ERROR] Database connection lost"
]
ic(
    tuple(filter(lambda x : "ERROR" in x, logs))
)

# function in Python does not support multiple iterables directly.

names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 40, 90, 30]
ic([ f"{names} --> {scores}"for names,scores in 
    tuple(
        filter(lambda x: x[1]>50,zip(names,scores))
    )]
)

# reduce() Function
# Purpose: Apply a rolling computation to sequential pairs of values in an iterable.
# Location: It is available in the functools module.
# Syntax:
# reduce(function, iterable[, initializer])
# Documentation
# Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

# This effectively reduces the iterable to a single value. If initial is present,
# it is placed before the items of the iterable in the calculation, and serves as
# a default when the iterable is empty.

# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# calculates ((((1 + 2) + 3) + 4) + 5).

ic(
    reduce(lambda x,y : x+y,[i for i in range(1,6)])  # 15
)
# how it works


# Step | Values of x | Values of y | Computation | Result
# ------------------------------------------------------
# 1    | 1          | 2          | 1 + 2       | 3
# 2    | 3          | 3          | 3 + 3       | 6
# 3    | 6          | 4          | 6 + 4       | 10
# 4    | 10         | 5          | 10 + 5      | 15

# Step 1:  (1 + 2) = 3
# Step 2:  (3 + 3) = 6
# Step 3:  (6 + 4) = 10
# Step 4:  (10 + 5) = 15
# Final Result: 15

# Feature	reduce()
# Purpose	Apply a function cumulatively to an iterable
# Requires?	A function with two arguments
# Output?	A single value
# Use Case	Summing, multiplying, finding max/min, factorial, etc.

ic(
    reduce(lambda x,y: x-y if x>y else x+y,[5, 12, 8, 19, 7] )
    # 27
)


ic(
    reduce(lambda x,y: x-y if x>y else x+y,[5, 12, 8, 19, 7] )
    # 27
)

ic(
    reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 10)
)
# Step | Values of x | Values of y | Computation | Result
# ------------------------------------------------------
# 1    | 10 (initial) | 1          | 10 + 1      | 11
# 2    | 11          | 2          | 11 + 2      | 13
# 3    | 13          | 3          | 13 + 3      | 16
# 4    | 16          | 4          | 16 + 4      | 20
# 5    | 20          | 5          | 20 + 5      | 25

# use cases 
print("use cases of reduce")
# calculate factorial of 5  
ic("Factorial using reduce",reduce( lambda x,y : x*y , [i for i in range(1,6)])
   )
# concatenating strings
ic(
    reduce(lambda str_1,str_2: str_1 + " " + str_2,["Hello", "World", "Pauri", "Rocks"])
)

# max/min
numbers = [5, 12, 8, 19, 7]

ic("min value", reduce(lambda x, y: x if x < y else y, numbers)
) # Output: 5


words = ["apple", "banana", "grape", "blueberry", "kiwi"]

longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
shortest_word = reduce(lambda x, y: x if len(x) < len(y) else y, words)

print(longest_word)  # Output: "blueberry"
print(shortest_word)  # Output: "kiwi"

# The enumerate() function is useful when you need to loop through an iterable while keeping track of the index.
names = ["Alice", "Bob", "Charlie", "David"]

for index, name in enumerate(names):
    if index % 2 == 0:
        print(f"{index}: {name}")

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(f"Person {index}: {name}")
    
for index, name in enumerate(names):
    if name == "Charlie":
        print(f"Charlie is at index {index}")

name_dict = {index: name for index, name in enumerate(names)}
print(name_dict)

def write_line_wit_enum():
    with open("sample.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")