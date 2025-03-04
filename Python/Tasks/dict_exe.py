from icecream import ic
import re
import numpy as np
# Group Data by a Key
# Scenario: You have data points with categories and need to group them accordingly.

# Task:

# Input: [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana'), ('vegetable', 'broccoli')]
# Use a dictionary to group items by category.
# Expected output: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']}

data= [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana'), ('vegetable', 'broccoli')]
ic({k: [v2 for k2, v2 in data if k2 == k] for k in {k for k, v in data}})

# Problem: You work for an e-commerce company and are given a list of sales transactions. Each transaction is a dictionary containing the product name, quantity sold, and price per unit. Write a function that aggregates the data into a dictionary where the keys are product names, and the values are the total revenue (quantity * price) for each product.

# expected output {
#     "Laptop": 3000,    
#     "Mouse": 300,      
#     "Keyboard": 150    
# }


transactions = [
    {"product": "Laptop", "quantity": 2, "price": 1000},
    {"product": "Mouse", "quantity": 5, "price": 20},
    {"product": "Laptop", "quantity": 1, "price": 1000},
    {"product": "Keyboard", "quantity": 3, "price": 50},
    {"product": "Mouse", "quantity": 10, "price": 20}
]
ic(
    { item['product'] : sum(it['price']* it['quantity'] for it in transactions if it['product'] == item['product'] )
        for item in transactions
    }
)

# Problem: You’re a data analyst at a company analyzing customer reviews. Given a list of review strings, write a function that returns a dictionary with the frequency of each word across all reviews (case-insensitive). Ignore punctuation and treat words like "The" and "the" as the same.

# Expected Output:

# {
#     "the": 2,
#     "product": 2,
#     "is": 1,
#     "great": 2,
#     "service": 1,
#     "was": 1,
#     "slow": 2,
#     "but": 1,
#     "delivery": 1
# }
 


reviews = [
    "The product is great!",
    "The service was slow, but great product.",
    "Slow delivery."
]
# first filter the list to remove the punctuations.
ic(
    { word.lower(): sum( 1 for sent in [re.sub(r'[^\w\s]', '',w) for w in reviews] for wrd in sent.split() if wrd.lower() == word.lower())
        for sentence in [re.sub(r'[^\w\s]', '',w) for w in reviews] for word in sentence.split()
    }
)

# Problem: You’re tasked with summarizing employee data for a company. Given a list of dictionaries where each dictionary contains an employee’s name, department, and salary, write a function that returns a dictionary summarizing the total salary and number of employees per department.
# expected output:
# {
#     "HR": {"total_salary": 105000, "count": 2},
#     "Engineering": {"total_salary": 170000, "count": 2}
# }

employees = [
    {"name": "Alice", "dept": "HR", "salary": 50000},
    {"name": "Bob", "dept": "Engineering", "salary": 80000},
    {"name": "Charlie", "dept": "HR", "salary": 55000},
    {"name": "David", "dept": "Engineering", "salary": 90000}
]

ic(
    { item['dept']: {"total_salaray": sum(it['salary'] for it in employees if it['dept'] == item['dept']) ,"count": sum(1 for it in employees if it['dept'] == item['dept'])}
        for item in employees
    }
)
# Problem: You’re working on IoT data for a data science project. Given a list of sensor readings as dictionaries (with timestamp and value), write a function that detects anomalies and returns a dictionary mapping each timestamp to whether its value is anomalous (i.e., more than 2 standard deviations from the mean). Assume the data is normally distributed.

# Expected Output:

# {
#     "2023-01-01 10:00": False,
#     "2023-01-01 10:01": False,
#     "2023-01-01 10:02": False,
#     "2023-01-01 10:03": True,  # ture if outlier 
#     "2023-01-01 10:04": False
# }


readings = [
    {"timestamp": "2023-01-01 10:00", "value": 10},
    {"timestamp": "2023-01-01 10:01", "value": 12},
    {"timestamp": "2023-01-01 10:02", "value": 11},
    {"timestamp": "2023-01-01 10:03", "value": 21},
    {"timestamp": "2023-01-01 10:04", "value": 9}
]

mean, std = np.mean([r["value"] for r in readings]), np.std([r["value"] for r in readings])
print(mean,std)
ic(dict(map(lambda x: (x[0], bool(abs(x[1] - mean) > (2 * std))), [(r["timestamp"], r["value"]) for r in readings])))