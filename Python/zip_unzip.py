#!/usr/bin/env python3
"""

1. The zip() Function:
   - What it does: aggregates elements from multiple iterables into tuples.
   - How it works: stops when the shortest iterable is exhausted.
   - Example use cases.

2. Handling Different Lengths:
   - What happens when iterables are of different lengths.
   - How to handle such scenarios if needed.

3. Unzipping:
   - How to reverse a zipped sequence back to separate lists or tuples.
   - Using the unpacking operator (*) with zip().

4. Practical Examples:
   - Basic examples of zipping lists.
   - A demonstration of unzipping a list of tuples.
   - Combining zip() with list comprehensions for clarity.


"""

# --------------------------
# Section 1: Basic Usage of zip()
# --------------------------

def basic_zip_example():
    """
    Demonstrates the basic usage of zip() with lists.
    
    zip() aggregates elements from each provided iterable into tuples.
    The resulting iterator stops when the shortest iterable is exhausted.
    """
    print("Basic zip() Example:")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    
    # Zip the two lists together
    zipped = zip(names, ages)
    # Convert the zip object to a list to display its contents
    zipped_list = list(zipped)
    
    print("Names:", names)
    print("Ages:", ages)
    print("Zipped List:", zipped_list)
    print()

# --------------------------
# Section 2: zip() with Iterables of Different Lengths
# --------------------------

def different_length_zip():
    """
    Demonstrates zip() with iterables of different lengths.
    
    When iterables have different lengths, zip() stops at the shortest one.
    """
    print("zip() with Different Length Iterables:")
    names = ["Alice", "Bob", "Charlie", "David"]
    ages = [25, 30, 35]  # One element shorter than names
    
    zipped = zip(names, ages)
    zipped_list = list(zipped)
    
    print("Names:", names)
    print("Ages:", ages)
    print("Zipped (shortest length):", zipped_list)
    print()

# --------------------------
# Section 3: Unzipping a Zipped Collection
# --------------------------

def unzip_example():
    """
    Demonstrates how to unzip a zipped collection.
    
    Unzipping is the process of converting a list of tuples back into separate
    lists. This is done using the unpacking operator (*) with zip().
    """
    print("Unzipping a Zipped Collection:")
    # Example zipped list
    zipped_list = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    
    # Unzip the list of tuples into two separate tuples (names and ages)
    names, ages = zip(*zipped_list)
    
    print("Zipped List:", zipped_list)
    print("Unzipped Names:", names)
    print("Unzipped Ages:", ages)
    print()

# --------------------------
# Section 4: Advanced Usage and Best Practices
# --------------------------

def advanced_zip_usage():
    """
    Provides advanced examples and best practices using zip().
    
    - Combining more than two iterables.
    - Using list comprehensions with zip() for compact code.
    - Demonstrating that zip() returns an iterator (in Python 3).
    """
    print("Advanced zip() Usage:")
    
    # Example: Zipping three iterables together
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "Los Angeles", "Chicago"]
    
    zipped = list(zip(names, ages, cities))
    print("Zipped with three iterables:", zipped)
    
    # Using list comprehension with zip() to create a formatted string for each person
    formatted = [f"{name} is {age} years old and lives in {city}" 
                 for name, age, city in zip(names, ages, cities)]
    print("Formatted Output:")
    for entry in formatted:
        print(entry)
    
    # Demonstrate that zip() returns an iterator
    zipped_iterator = zip(names, ages)
    print("Type of zip() output:", type(zipped_iterator))
    # Converting to list to display the content
    print("Converted to list:", list(zipped_iterator))
    
    print()

# --------------------------
# Main function to run all examples
# --------------------------

def main():
    """
    Main function that runs all zip and unzip demonstrations.
    """
    basic_zip_example()
    different_length_zip()
    unzip_example()
    advanced_zip_usage()

if __name__ == "__main__":
    main()
