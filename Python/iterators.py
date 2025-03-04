#!/usr/bin/env python3
"""
Iterator Tutorial in Python
----------------------------

This Python script provides a comprehensive guide to understanding iterators
and iterables in Python, covering concepts from basic to advanced. It explains:

1. Definitions:
   - Iterable: An object capable of returning its members one at a time. Examples
     include lists, tuples, dictionaries, sets, and strings.
   - Iterator: An object representing a stream of data; it implements the __next__()
     method and returns successive items until there are no more items, at which
     point it raises StopIteration.
   - Note: Every iterator is an iterable (since it has an __iter__() method that
     returns itself), but not every iterable is an iterator (e.g., a list is
     iterable but does not implement __next__ directly).

2. How a for Loop Works Internally:
   - When you initiate a for loop on an iterable, Python internally calls the
     iter() function to obtain an iterator.
   - The loop then repeatedly calls next() on that iterator until a StopIteration
     exception is raised, signaling that there are no further items.

3. Custom Iterators:
   - How to build your own iterator classes by implementing __iter__() and
     __next__().
   - How generator functions using the 'yield' keyword offer a concise way to
     create iterators.

4. Advanced Concepts:
   - Iterator exhaustion: Once an iterator has been fully consumed, it cannot be
     reused unless a new iterator is created.
   - Multiple iterators from a single iterable are independent.
   - Memory efficiency and lazy evaluation provided by iterators and generators.

Usage:
------
Run this script to see examples and explanations in action. Each section prints
its own demonstration output.

Author: Your Name Here
Date: YYYY-MM-DD
"""

# --------------------------
# Section 1: Basic Iterator Example
# --------------------------

def basic_iterator_example():
    """
    Demonstrates the basic use of iterators and iterables.

    A list is an iterable, but not an iterator. To iterate over it using an
    iterator, we call the built-in iter() function. The iterator has a __next__()
    method which returns each element until the list is exhausted.
    """
    print("Basic Iterator Example:")
    
    my_list = [1, 2, 3, 4]
    print("Iterable (list):", my_list)
    
    # Get an iterator from the list
    my_iter = iter(my_list)
    print("Iterator created using iter():", my_iter)
    
    # Use next() to access elements one at a time
    print("Elements obtained by next():")
    try:
        while True:
            element = next(my_iter)
            print(element)
    except StopIteration:
        print("Reached the end of the iterator.\n")

# --------------------------
# Section 2: Understanding Iterable vs Iterator
# --------------------------

def explain_iterable_vs_iterator():
    """
    Explains the difference between an iterable and an iterator.

    Iterable:
      - An object with an __iter__() method that returns an iterator.
      - Examples include list, tuple, string, dictionary, set.
    
    Iterator:
      - An object with a __next__() method that returns successive items.
      - Also implements __iter__() (which returns itself).
    
    Important:
      - Although every iterator is iterable, an iterable is not necessarily an
        iterator. For instance, a list is iterable but does not implement __next__.
    """
    print("Iterable vs Iterator Explanation:")
    
    my_list = [10, 20, 30]
    # Check if the list is an iterator by looking for the __next__ attribute
    print("Does list have __next__? :", hasattr(my_list, '__next__'))  # Expected: False
    
    # Obtain an iterator from the list
    my_iter = iter(my_list)
    print("Does iterator have __next__? :", hasattr(my_iter, '__next__'))  # Expected: True
    print()

# --------------------------
# Section 3: Custom Iterator Class
# --------------------------

class Countdown:
    """
    A custom iterator that counts down from a given number to 1.

    Implements the iterator protocol:
      - __iter__() returns the iterator object (self).
      - __next__() returns the next value in the countdown.
    
    When the countdown is complete, __next__() raises StopIteration.
    """
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

def custom_iterator_example():
    """
    Demonstrates the use of the custom Countdown iterator.
    """
    print("Custom Iterator Example (Countdown):")
    countdown = Countdown(5)
    for number in countdown:
        print(number)
    print()

# --------------------------
# Section 4: Generator Functions as Iterators
# --------------------------

def fibonacci_generator(n):
    """
    A generator function that yields the Fibonacci sequence up to n elements.

    Generators provide a simple way to create iterators using the 'yield' keyword.
    This is a memory-efficient method for iterating over potentially large sequences.

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

def generator_example():
    """
    Demonstrates the use of a generator function by printing the first 10 Fibonacci numbers.
    """
    print("Generator Example (Fibonacci Sequence):")
    for num in fibonacci_generator(10):
        print(num)
    print()

# --------------------------
# Section 5: Behind the Scenes of a For Loop
# --------------------------

def for_loop_mechanics_demo():
    """
    Explains what happens when a for loop is used on an iterable or iterator.

    Process:
      1. The for loop calls iter() on the iterable to obtain an iterator.
      2. The loop repeatedly calls next() on the iterator.
      3. When the iterator is exhausted, next() raises StopIteration, which ends the loop.
    
    This works uniformly for built-in iterables (e.g., strings, lists) and custom iterators.
    """
    print("For Loop Mechanics Demonstration:")
    
    sample_iterable = "Hello"
    print("Iterable (string):", sample_iterable)
    
    # Obtain an iterator from the string
    iterator = iter(sample_iterable)
    print("Iterator from string:", iterator)
    
    print("Iterating using next():")
    try:
        while True:
            char = next(iterator)
            print(char)
    except StopIteration:
        print("End of iterator reached.\n")

# --------------------------
# Section 6: Advanced Concepts and Best Practices
# --------------------------

def advanced_concepts():
    """
    Discusses advanced iterator concepts and best practices.

    - Iterator Exhaustion:
      Once an iterator is fully consumed, subsequent calls to next() will raise
      StopIteration. To iterate again, a new iterator must be created.
    
    - Multiple Iterators:
      Creating multiple iterators from the same iterable produces independent
      iterators with their own state.
    
    - Memory Efficiency:
      Iterators and generators process elements on the fly, offering memory
      efficiency, especially for large or infinite sequences.
    
    - Lazy Evaluation:
      Values are computed as needed, rather than all at once.
    """
    print("Advanced Concepts and Best Practices:")
    
    # Demonstrate iterator exhaustion
    print("\nIterator Exhaustion Example:")
    numbers = [1, 2, 3]
    iterator = iter(numbers)
    print("First iteration over iterator:")
    for num in iterator:
        print(num)
    print("Attempting to iterate again on the same (now exhausted) iterator:")
    for num in iterator:
        print(num)  # This will not print anything because the iterator is exhausted.
    
    # Multiple iterators from one iterable
    print("\nMultiple Iterators Example:")
    data = [10, 20, 30, 40]
    iter1 = iter(data)
    iter2 = iter(data)
    print("First iterator, first value:", next(iter1))
    print("Second iterator, first value:", next(iter2))
    print("First iterator, second value:", next(iter1))
    
    # Memory efficiency using a generator expression
    print("\nMemory Efficiency with Generators:")
    large_range = (x * x for x in range(1000000))  # A generator expression
    # Only compute and print the first 5 values to demonstrate lazy evaluation
    for _ in range(5):
        print(next(large_range))
    print()

# --------------------------
# Main function to run examples
# --------------------------

def main():
    """
    Main function that runs all iterator and iterable examples.
    """
    basic_iterator_example()
    explain_iterable_vs_iterator()
    custom_iterator_example()
    generator_example()
    for_loop_mechanics_demo()
    advanced_concepts()

if __name__ == "__main__":
    main()
