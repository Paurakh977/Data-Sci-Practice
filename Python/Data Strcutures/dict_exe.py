from icecream import ic

# decalring dicts from iterable
ic( dict([("name", "Alice"), ("age", 25), ("city", "New York")]) )
ic(dict ({("name", "Alice"), ("age", 25), ("city", "New York")} ) ) # this is a set of tuples

# Converting a Dictionary to a List
{'a': 1, 'b': 2, 'c': 3}
ic( list({'a': 1, 'b': 2, 'c': 3}.keys()))      # getting keys only
ic( list({'a': 1, 'b': 2, 'c': 3}.values()))    # getting values only
ic( list( {'a': 1, 'b': 2, 'c': 3}.items()))    # getting list of tuples
ic(list (item for pair in {'a': 1, 'b': 2, 'c': 3}.items() for item in pair))  # flattening a dict to list elements
keys,values= zip(*{'a': 1, 'b': 2, 'c': 3}.items())
ic(keys,values)   # getting tuple of keys and values


# converting list to dictionary
ic( dict([("name", "Alice"), ("age", 25), ("city", "New York")]) )

keys = ['a', 'b', 'c']
values = [1, 2, 3]
ic(dict(zip(keys,values)))

#falttend list to dict
ic( 
   dict(zip(['a', 1, 'b', 2, 'c', 3][::2],['a', 1, 'b', 2, 'c', 3][1::2])
        )
   )



#visualzing unpakcing of dict

def show_kwargs(**kwargs):
    print(kwargs)

d = {'a': 1, 'b': 2, 'c': 3}
show_kwargs(**d)

def show_details(name,age,sex):
    ic(name,age,sex)

show_details(**{"name": "ram", "age": 10, "sex": "M"})
# this is same as
show_details(name= "ram", age= 10, sex= "M")

# so **kwargs in function means you can pass as many key words args into it k1=v1,k2=v2 etc.
# similalry ynpacking a dict using ** makes it in the form like k1=v1,k2=v2
#Basic Dictionary Operations

from collections import defaultdict, OrderedDict


# 1. Basic Dictionary Operations
ic("1. Basic Dictionary Operations:")
student = {'name': 'Alice', 'age': 23, 'major': 'Physics'}
ic(student)
# Expected Output: {'name': 'Alice', 'age': 23, 'major': 'Physics'}

# Accessing a value
ic(student['name'])
# Expected Output: Alice

# Using get() with a default value if key doesn't exist
ic(student.get('gpa', 'Not Available'))
# Expected Output: Not Available

# 2. Dictionary Methods: keys(), values(), and items()
ic("\n2. keys(), values(), and items():")
ic("Keys:", list(student.keys()))
# Expected: ['name', 'age', 'major']
ic("Values:", list(student.values()))
# Expected: ['Alice', 23, 'Physics']
ic("Items:", list(student.items()))
# Expected: [('name', 'Alice'), ('age', 23), ('major', 'Physics')]

# 3. Adding and Updating Entries
ic("\n3. Adding and Updating Entries:")
student['gpa'] = 3.8  # Add a new key-value pair
ic("After adding GPA:", student)
# Expected: {'name': 'Alice', 'age': 23, 'major': 'Physics', 'gpa': 3.8}
student['age'] = 24  # Update the existing 'age'
ic("After updating age:", student['age'])
# Expected Output: 24

# 4. Removing Items
ic("\n4. Removing Items:")
# Using del to remove a key-value pair
del student['major']
ic("After deleting major:", student)
# Expected: {'name': 'Alice', 'age': 24, 'gpa': 3.8}
# Using pop() to remove and return a value
popped_age = student.pop('age')
ic("Popped age:", popped_age)
# Expected Output: 24
ic("After popping age:", student)
# Expected: {'name': 'Alice', 'gpa': 3.8}
# Using popitem() to remove and return the last inserted key-value pair
popped_item = student.popitem()
ic("Popped item (popitem):", popped_item)
# Expected Output: ('gpa', 3.8) (or similar based on insertion order)
ic("After popitem:", student)
# Expected: {'name': 'Alice'}

# Reset student for further demonstrations
student = {'name': 'Alice', 'age': 23, 'major': 'Physics'}

# 5. setdefault() Method
ic("\n5. setdefault() Method:")
# If key 'gpa' doesn't exist, set it to 3.9 and return 3.9.
value = student.setdefault('gpa', 3.9)
ic("Value returned by setdefault for 'gpa':", value)
# Expected Output: 3.9
ic("Student after setdefault:", student)
# Expected: {'name': 'Alice', 'age': 23, 'major': 'Physics', 'gpa': 3.9}
# If the key exists, setdefault returns the current value.
existing_value = student.setdefault('major', 'Mathematics')
ic("Value returned by setdefault for existing key 'major':", existing_value)
# Expected Output: Physics

# 6. update() Method
ic("\n6. update() Method:")
# Merge new key-value pairs into the dictionary
student.update({'age': 25, 'gpa': 4.0})
ic("After update:", student)
# Expected: {'name': 'Alice', 'age': 25, 'major': 'Physics', 'gpa': 4.0}

# 7. copy() Method
ic("\n7. copy() Method:")
student_copy = student.copy()
ic("Copy of student dictionary:", student_copy)
# Expected: {'name': 'Alice', 'age': 25, 'major': 'Physics', 'gpa': 4.0}

# 8. Dictionary Comprehensions
ic("\n8. Dictionary Comprehensions:")
# Basic comprehension: numbers as keys and their squares as values.
squares = {x: x**2 for x in range(1, 6)}
ic("Squares:", squares)
# Expected: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Comprehension with a condition: only even numbers.
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
ic("Even Squares:", even_squares)
# Expected: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 9. Nesting Dictionaries
ic("\n9. Nesting Dictionaries:")
students = {
    'student1': {
        'name': 'Alice',
        'age': 23,
        'address': {'street': '123 Main St', 'city': 'New York'}
    },
    'student2': {
        'name': 'Bob',
        'age': 24,
        'address': {'street': '456 Maple Ave', 'city': 'Los Angeles'}
    }
}
ic("Nested Dictionary (students):", students)
# Access nested value
alice_city = students['student1']['address']['city']
ic("Alice's city:", alice_city)
# Expected: New York

# 10. Iterating Over Dictionaries
ic("\n10. Iterating Over Dictionaries:")
ic("Iterating over keys:")
for key in student:
    ic(key)
# Expected: keys of student (order may vary)
ic("Iterating over values:")
for value in student.values():
    ic(value)
# Expected: values of student (order may vary)
ic("Iterating over key-value pairs:")
for key, value in student.items():
    ic(f"{key}: {value}")
# Expected: each key-value pair iced

# 11. Merging Dictionaries
ic("\n11. Merging Dictionaries:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Using update()
merged_update = dict1.copy()
merged_update.update(dict2)
ic("Merged using update():", merged_update)
# Expected: {'a': 1, 'b': 3, 'c': 4}
# Using merge operator (Python 3.9+)
try:
    merged_operator = dict1 | dict2
    ic("Merged using | operator:", merged_operator)
    # Expected: {'a': 1, 'b': 3, 'c': 4}
except TypeError:
    ic("Merge operator not supported in this Python version.")
# Using unpacking (Python 3.5+)
merged_unpack = {**dict1, **dict2}
ic("Merged using unpacking:", merged_unpack)
# Expected: {'a': 1, 'b': 3, 'c': 4}

# 12. Sorting Dictionaries
ic("\n12. Sorting Dictionaries:")
unsorted = {'b': 2, 'a': 1, 'c': 3}
sorted_by_keys = dict(sorted(unsorted.items()))
ic("Sorted by keys:", sorted_by_keys)
# Expected: {'a': 1, 'b': 2, 'c': 3}
sorted_by_values = dict(sorted(unsorted.items(), key=lambda item: item[1]))
ic("Sorted by values:", sorted_by_values)
# Expected: {'a': 1, 'b': 2, 'c': 3}

# 13. Filtering Dictionaries
ic("\n13. Filtering Dictionaries:")
filtered = {k: v for k, v in unsorted.items() if v >= 2}
ic("Filtered dictionary:", filtered)
# Expected: {'b': 2, 'c': 3}

# 14. Advanced Dictionary Tools
ic("\n14. Advanced Dictionary Tools:")

# defaultdict: counting word frequencies.
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for word in words:
    word_count[word] += 1
ic("Word count using defaultdict:", dict(word_count))
# Expected: {'apple': 3, 'banana': 2, 'orange': 1}

# OrderedDict: maintains insertion order (especially useful in older Python versions).
ordered = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
ic("OrderedDict:", ordered)
# Expected: OrderedDict([('one', 1), ('two', 2), ('three', 3)])

