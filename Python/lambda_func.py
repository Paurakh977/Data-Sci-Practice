from  icecream import ic
from functools import reduce
import pandas as pd

# Basics Syntax 
# lambda arguments: expression


numbers = [1, 2, 3, 4, 5]

# Using lambda with map to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

#inline 
ic((lambda *agrs:[items**2 if items% 2==0 else items for items in agrs ] )(1,2,3,4,5))


# sort students on the basics of their score.
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 70}
]
ic(sorted(students,key= lambda x:x["score"] ))

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

# in pandas

data = {
    "City": ["New York", "Los Angeles", "Chicago"],
    "Temperature_C": [22, 25, 20]
}
df = pd.DataFrame(data)

# convert celcuis to Fahrenheit
df["Temperature_F"]= df['Temperature_C'].apply(lambda C: (C * 9/5) + 32  )

ic(df)

# Categorize products based on their price in df

data = {
    "Product": ["A", "B", "C", "D","E"],
    "Price": [150, 50, 200, 80,120]
}
df = pd.DataFrame(data)

df['Category'] = df['Price'].apply(lambda price: "Expensive" if price >=150 else "Affordable" if price<150 and price >=100 else "Cheap")
ic(df)