from icecream import ic
from math import sqrt,pow

# Scenario: You have a list of 2D points, and you need to compute the Manhattan distance between each pair.

# Task:

# Points: points = [(1, 2), (3, 4), (5, 6)]
# Calculate the Manhattan distance between every pair.
# Store results as a list of tuples: (index1, index2, distance).
# Expected output: [(0, 1, 4), (0, 2, 8), (1, 2, 4)]
# Hint: Manhattan distance between (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

points = [(1, 2), (3, 4), (5, 6)]

ic(
    [   (i,j, (lambda tup_1,tup_2: abs(tup_1[0] - tup_2[0]) + abs(tup_1[1] - tup_2[1])) (points[i], points[j]) )
        for i in range(len(points))
        for j in range(i+1,len(points))
    ]
)


# Extract Features from a List of Dictionaries
# Scenario: You’re given a list of dictionaries representing data points, and you need to extract a specific feature.

# Task:

# Input:
# data = [
#     {'age': 25, 'income': 50000, 'years_edu': 12},
#     {'age': 30, 'income': 70000, 'years_edu': 16},
#     {'age': 22, 'income': 45000, 'years_edu': 10}
# ]
# Use a list comprehension to extract the 'income' values.
# Compute the average income.
# Expected output: [50000, 70000, 45000], average = 55000

data = [
    {'age': 25, 'income': 50000, 'years_edu': 12},
    {'age': 30, 'income': 70000, 'years_edu': 16},
    {'age': 22, 'income': 45000, 'years_edu': 10}
]

ic(
    [items['income'] for items in data], ( lambda *x : int(sum(x)/len(x)) ) (*[items['income'] for items in data])
)

# Implement a Simple k-Nearest Neighbors (k-NN) Classifier
# Scenario: You have a dataset of points with labels and need to classify a new point based on its nearest neighbor.

# Task:

# Dataset: dataset = [([1, 2], 'A'), ([3, 4], 'B'), ([5, 6], 'A')]
# New point: [2, 3]
# Calculate the Euclidean distance from the new point to each dataset point.
# Return a list of label and the value of distance of the nearest point.
# Expected output: [1.414, 'A'] (since [1, 2] is closest)
# Hint: Euclidean distance = sqrt((x1 - x2)^2 + (y1 - y2)^2). Use math.sqrt() or compare squared distances.

dataset = [([1, 2], 'A'), ([3, 4], 'B'), ([5, 6], 'A')]
ic( min(
        [   
        (lambda item, new_points =[2,3]: [sqrt( sum( [ pow(p1-p2,2) for p1,p2 in zip(item[0],new_points) ] )), item[-1]] ) (item)
        for item in dataset 
        ]
        , key= lambda x: x[0]
    )
)


