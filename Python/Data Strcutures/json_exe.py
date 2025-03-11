# Python provides the json module to handle JSON data. It allows you to:
# Serialize: Convert Python objects (like dictionaries) to JSON strings.

# Deserialize: Convert JSON strings back to Python objects.

import json
from icecream import ic


# Basic Serialization: json.dumps()
# The json.dumps() function converts a Python object to a JSON-formatted string.


person = {"name": "John", "age": 30, "is_student": False}
json_string = json.dumps(person)
print(json_string)  #{"name": "John", "age": 30, "is_student": false}

# Python’s False becomes JSON’s false.

# Keys and string values are automatically enclosed in double quotes.

# When to Use:
# When you need to save a dictionary to a file or send it over a network as text.


# Basic Deserialization: json.loads()
# The json.loads() function converts a JSON string to a Python object.


person_dict=json.loads(json_string)
print(person_dict)

# JSON objects become Python dictionaries.

# JSON false becomes Python False.

# The structure is intact, ready for Python manipulation.

# When to Use:
# When you receive JSON data (e.g., from an API) and need to work with it in Python.


# Example: Nested JSON


# Handling Unsupported Python Types
# JSON only supports its defined data types. Python types like tuples, sets, or custom objects need special handling.
data = {"numbers": (1, 2, 3)}
json_string = json.dumps(data)
print(json_string)      #{"numbers": [1, 2, 3]}

# Why:
# Tuples are serialized as JSON arrays (lists) because JSON lacks a tuple type.

data = {"numbers": {1, 2, 3}}
json.dumps(data)  # Raises TypeError


# Solution (Custom Serialization):


def set_serializer(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError("Type not serializable")

json_string = json.dumps(data, default=set_serializer)
print(json_string)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
# json.dumps(person)  # Raises TypeError

def person_serializer(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError

json_string = json.dumps(person, default=person_serializer)
print(json_string)

# Deserialization to Custom Object:
def person_decoder(obj):
    if "name" in obj and "age" in obj:
        return Person(obj["name"], obj["age"])
    return obj

json_string = '{"name": "John", "age": 30}'
person_obj = json.loads(json_string, object_hook=person_decoder)
print(person_obj.name)  # Output: John
