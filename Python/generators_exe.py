#!/usr/bin/env python3
"""
Generators in Python: A Comprehensive Guide
--------------------------------------------

This script explains generators in Python with thorough examples and documentation,
covering the following topics:

1. What is a Generator?
   - A generator is a special kind of iterator that yields values one at a time,
     allowing for lazy evaluation and memory efficiency.
   - Generators can be implemented via generator functions (using 'yield') or
     generator expressions (similar to list comprehensions, but with parentheses).

2. Generator Functions:
   - How to define a generator function using the 'yield' keyword.
   - How generators work: each call to next() resumes execution from the last yield.
   - An example using a simple counter and a Fibonacci sequence generator.

3. Generator Expressions:
   - Creating generators using compact syntax.
   - Example: generating squares of numbers on the fly.

4. Built-in Functions with Generators:
   - next(): Retrieve the next value from a generator.
   - any(): Returns True if at least one element in the generator is True.
   - all(): Returns True only if all elements in the generator are True.

5. Advanced Concepts and Best Practices:
   - Generator exhaustion: once a generator is fully consumed, it cannot be reused.
   - Memory efficiency: generators are ideal for handling large or infinite sequences.
   - Best practices when using generators in real-world applications.

Usage:
------
Run this script to see detailed demonstrations of generator concepts in action.

Author: Your Name Here
Date: YYYY-MM-DD
"""

# --------------------------
# Section 1: Basic Generator Function Example
# --------------------------

def simple_counter(n):
    """
    A simple generator function that counts from 0 to n-1.
    
    Args:
        n (int): The upper limit (non-inclusive) for the count.
        
    Yields:
        int: The next number in the sequence.
        
    Note:
        Once the generator is exhausted, subsequent calls to next() will
        raise StopIteration.
    """
    print("Starting simple_counter generator")
    for i in range(n):
        yield i
    print("simple_counter generator finished")

def demo_simple_counter():
    """
    Demonstrates the usage of the simple_counter generator function with next().
    """
    print("Demo: simple_counter generator")
    counter = simple_counter(5)
    # Using next() to fetch individual values
    print("First call to next():", next(counter))  # Output: 0
    print("Second call to next():", next(counter))  # Output: 1
    
    # Consume the rest of the generator using a for loop
    print("Remaining values:")
    for number in counter:
        print(number)
    print()

# --------------------------
# Section 2: Generator Function for Fibonacci Sequence
# --------------------------

def fibonacci_generator(n):
    """
    A generator function that yields the Fibonacci sequence up to n elements.
    
    Args:
        n (int): Number of Fibonacci numbers to generate.
        
    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def demo_fibonacci():
    """
    Demonstrates the Fibonacci generator function.
    """
    print("Demo: Fibonacci Generator")
    for num in fibonacci_generator(10):
        print(num)
    print()

# --------------------------
# Section 3: Generator Expressions
# --------------------------

def demo_generator_expression():
    """
    Demonstrates the use of generator expressions.
    
    Generator expressions provide a concise way to create generators.
    They use similar syntax to list comprehensions but use parentheses.
    """
    print("Demo: Generator Expression")
    # Create a generator expression that yields squares of numbers from 0 to 9
    squares = (x * x for x in range(10))
    
    # Use next() to get the first value from the generator expression
    print("First square using next():", next(squares))
    
    # Consume the rest of the squares using a for loop
    print("Remaining squares:")
    for sq in squares:
        print(sq)
    print()

# --------------------------
# Section 4: Built-in Functions with Generators (any(), all(), next())
# --------------------------

def demo_any_all():
    """
    Demonstrates the use of any() and all() with generators.
    
    - any(generator) returns True if at least one element in the generator is True.
    - all(generator) returns True only if every element in the generator is True.
    """
    print("Demo: any() and all() with Generators")
    
    # Create a generator that yields boolean values.
    # For x in range(5): (x % 2 == 0) produces: True, False, True, False, True
    bool_values = (x % 2 == 0 for x in range(5))
    
    # Using any(): should return True since there are True values in the sequence.
    result_any = any(bool_values)
    print("Result of any() on generator:", result_any)
    
    # For all(), we need to recreate the generator since it was exhausted by any()
    bool_values = (x % 2 == 0 for x in range(5))
    result_all = all(bool_values)
    print("Result of all() on generator:", result_all)
    
    # Demonstrate next() on a generator expression directly
    numbers = (x for x in range(3))
    print("Using next() on generator expression:")
    print(next(numbers))  # Output: 0
    print(next(numbers))  # Output: 1
    print(next(numbers))  # Output: 2
    try:
        print(next(numbers))  # This will raise StopIteration
    except StopIteration:
        print("Generator exhausted using next().")
    print()

# --------------------------
# Section 5: Advanced Generator Use Cases and Best Practices
# --------------------------

def demo_advanced_usage():
    """
    Demonstrates advanced generator usage and best practices.
    
    - Generator Exhaustion: A generator, once consumed, cannot be reused.
    - Memory Efficiency: Ideal for handling large or infinite sequences.
    - Infinite Generators: Example of a generator that can produce an infinite sequence.
    """
    print("Demo: Advanced Generator Usage")
    
    # Example of generator exhaustion with a generator expression
    gen_expr = (i for i in range(3))
    print("Values from generator expression:")
    for value in gen_expr:
        print(value)
    
    print("Trying to iterate over exhausted generator:")
    for value in gen_expr:
        print(value)  # Nothing will print here because the generator is exhausted.
    
    # Example of an infinite generator (use with caution)
    def infinite_numbers():
        n = 0
        while True:
            yield n
            n += 1
    
    # Demonstrate infinite generator by taking first 5 values only
    inf_gen = infinite_numbers()
    print("First 5 values from infinite_numbers generator:")
    for _ in range(5):
        print(next(inf_gen))
    print()

# --------------------------
# Main function to run all generator demos
# --------------------------

def main():
    """
    Main function that runs all generator demonstrations.
    """
    demo_simple_counter()
    demo_fibonacci()
    demo_generator_expression()
    demo_any_all()
    demo_advanced_usage()

if __name__ == "__main__":
    main()
