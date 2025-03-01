# A decorator is essentially a function that takes another function (or class) as input and returns a modified version of that function.

#NOTE
# When you use a decorator (with the @ syntax), Python applies it immediately at function definition time—not when you later call the function. This is why you see the print statements (like those in your Retry decorator) executed even though you're not explicitly calling the decorated function.
import functools
from icecream import ic
def my_decorator(func):
    @functools.wraps(func)  # Preserves the metadata of the original function
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")

# say_hello()


# Using @functools.wraps(func) in your decorator preserves the original function's metadata.
# print(say_hello.__name__,say_hello.__doc__) 
# Output: wrapper if you remove functools.wraps and say_hellow if you add it 

# Without Syntactic Sugar: Applying a decorator manually looks like this:
# def say_hello():
#     print("Hello!")
    
# say_hello = my_decorator(say_hello)
# With @ Syntax: Python’s decorator syntax is a shorthand for the above assignment, making your code cleaner and more readable.


# Decorators with Arguments

def repeat(num_of_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            ic(args)
            ic(kwargs)
            for _ in range(num_of_times):
                func(*args,**kwargs)
                
            return wrapper
        
        return wrapper
    
    return decorator        

 
@repeat(3)
def greet(name,msg="congrats",**kwargs):
    print(f"hello {name} {msg}")
    
greet("Paurakh","go go",home="ktm",age="21")
                

# When you write @repeat(3), Python first calls repeat(3), which returns the actual decorator function (decorator).
# inner function(decorator) receives the function to be decorated (in our case, greet). Then it returns the wrapper func that calls the original fucntion-func (greet) num times

# The use of *args and **kwargs means that wrapper can accept any number of positional and keyword arguments. This is important for flexibility—if greet later had a different signature (more or fewer arguments), the wrapper would still work.


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@logger # then this is invoked in logger
@uppercase #first this called from logger
def greet(name):
    return f"Hello, {name}!"


# print(greet("Alice"))

 
# NOTE
# understaingint he flow
# it is  something like: greet = logger(uppercase(greet))
# Definition & Decoration:
# The original function greet is first passed to the uppercase decorator, which returns a wrapper (let’s call it uppercase.wrapper) that calls greet and converts its result to uppercase.

# Call: greet("Alice")
#   ↓
#   Actually calls: logger's wrapper("Alice")
#     ↓
#     1. Prints: "Calling greet with args: ('Alice',), kwargs: {}"
#     ↓
#     2. Needs to call the original function, which is now uppercase's wrapper
#       ↓
#       3. Calls: uppercase's wrapper("Alice")
#         ↓
#         4. Calls the original greet("Alice")
#           ↓
#           5. Original greet returns: "Hello, Alice!"
#         ↓
#         6. uppercase's wrapper converts to: "HELLO, ALICE!"
#       ↓
#       7. Returns "HELLO, ALICE!" back to logger's wrapper
#     ↓
#     8. Prints: "greet returned HELLO, ALICE!"
#     ↓
#     9. Returns "HELLO, ALICE!" as the final result


# Class Decorators
# Decorators aren’t limited to functions. They can also be applied to classes to modify or enhance their behavior.
def add_attribute(cls):
    cls.extra_attribute = "I am an extra attribute!"
    return cls

@add_attribute
class MyClass:
    def __init__(self, value):
        self.value = value

instance = MyClass(10)
print(instance.value)          # Output: 10
print(MyClass.extra_attribute) # Output: I am an extra attribute!


import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def process_data(n):
    time.sleep(n)
    return "Processing done!"

print(process_data(2))


# Decorators for Input Validation
def validate_inputs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Example: Check if all arguments are non-negative
        if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("All numerical arguments must be non-negative!")
        return func(*args, **kwargs)
    return wrapper

@validate_inputs
def calculate_square_root(x):
    return x ** 0.5

print(calculate_square_root(9))

