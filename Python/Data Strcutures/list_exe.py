# Some common list methods
numbers = [4, 1, 3, 2, 1]
numbers.append(5)  # [4, 1, 3, 2, 1, 5]
numbers.remove(1)  # [4, 3, 2, 1, 5] (removes first 1)
numbers.index(3)  # Output: 1 (index of first occurrence of 3)
numbers.count(
    1
)  # Output: 1 (must be wondering there are two 1s but one of the 1 is removed above)
numbers.sort()  # [1, 2, 3, 4, 5]
numbers.reverse()  # [5, 4, 3, 2, 1]
numbers.pop()  # removes the last element of the list
numbers.pop(2)  # removes the item in the 2nd index
numbers.extend([4, 5])  # [5, 4, 2, 4, 5]
numbers.insert(2, 3)  # Inserts 3 at index 2

from icecream import ic
import numpy as np
# transposing a matrix
matrix= [   [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]

ic(
    [
        [ row[i] for row in matrix ]
        for i in range( len(matrix[0]) )
    ]
) 

# creating a multi-dimensonal matrix

rows,colns= 4,3
# create a matrix of this dimensons with numbers only even
 
ic(
    [
        [int(np.random.choice([i for i in range(0,51,2)])) for colns in range(colns) ]
        for rows in range(rows)
    ]
)

# unpacking list elements
a, b, *rest = [1, 2, 3, 4, 5]
ic( a, b, rest)