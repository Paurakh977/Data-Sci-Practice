"""
# Advanced Comprehension Examples and Documentation

This script demonstrates various advanced comprehension techniques in Python,
including dictionary, list, set, and nested comprehensions. The examples cover:

1. Counting vowels in a string (with and without built-in functions)
2. Generating Pythagorean triplets from numbers 1 to 30
3. Grouping words by their length
4. Creating a dictionary of factors for numbers 1 to 20
5. Building a nested multiplication table with only even products
6. Generating a set of ordered pairs (i, j) with specific conditions
7. Transposing a 2D matrix using list comprehensions

The `icecream` library is used for easy debugging output.
"""

from icecream import ic

# -----------------------------------------------------------------------------
# 1. Count Vowels in a String Using Dictionary Comprehension
# -----------------------------------------------------------------------------

def counter_with_builtin(string: str) -> dict[str, int]:
    """
    Returns a dictionary with vowels as keys and the count of each vowel in the string.
    This version uses the built-in .count() method.
    
    :param string: Input string to search vowels in.
    :return: Dictionary with vowels and their counts.
    """
    return {char: string.count(char) for char in "aeiou"}

# Test the function with built-in count
ic(counter_with_builtin("Paurakh"))
# Expected output (case-sensitive): {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 1}


# -----------------------------------------------------------------------------
# 2. Count Vowels in a String Without Using the Built-in .count() Method
# -----------------------------------------------------------------------------

def counter_without_builtin(string: str) -> dict[str, int]:
    """
    Returns a dictionary with vowels as keys and the count of each vowel in the string.
    This version does not use the built-in .count() method.
    
    :param string: Input string to search vowels in.
    :return: Dictionary with vowels and their counts.
    """
    # For each vowel, sum 1 for every character in the string that matches (ignoring case)
    return {vow: sum(1 for char in string if char.lower() == vow) for vow in "aeiou"}

# Test the function without using built-in count
ic(counter_without_builtin("Paurakh"))
# Expected output: {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 1}


# -----------------------------------------------------------------------------
# 3. Generate All Possible Pythagorean Triplets (1 <= a <= b <= c <= 30)
# -----------------------------------------------------------------------------
ic( [
    (a, b, c)
    for a in range(1, 31)
    for b in range(a, 31)
    for c in range(b, 31)
    if a**2 + b**2 == c**2
] )


# Expected output: A list of tuples containing the Pythagorean triplets.


# -----------------------------------------------------------------------------
# 4. Group Words by Their Length Using Dictionary Comprehension
# -----------------------------------------------------------------------------

words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

ic(
    {
    length: [word for word in words if len(word) == length]
    for length in {len(word) for word in words}
}

)
# Expected output: A dictionary where keys are word lengths and values are lists of words
# e.g., {5: ['apple'], 6: ['banana', 'cherry', 'grape'], 4: ['date', 'kiwi'], 3: ['fig']}


# -----------------------------------------------------------------------------
# 5. Create a Dictionary of Factors for Numbers 1 to 20
# -----------------------------------------------------------------------------


ic(
    {
        k: [i for i in range(1, k + 1) if k % i == 0]
        for k in range(1, 21)
    }
)
# Expected output: Dictionary mapping each number to a list of its factors.


# -----------------------------------------------------------------------------
# 6. Create a Nested Multiplication Table (1 to 10) with Even Products Only
# -----------------------------------------------------------------------------

ic(
    {
        i: {j: i * j for j in range(1, 11) if (i * j) % 2 == 0}
        for i in range(1, 11)
    }
)
# Expected output: A nested dictionary where the inner dictionary contains only even products.


# -----------------------------------------------------------------------------
# 7. Generate a Set of Ordered Pairs (i, j) Where i < j and (i+j) is Even
# -----------------------------------------------------------------------------

ic(
    {
        (i, j)
        for i in range(1, 6)
        for j in range(i, 6)
        if i < j and (i + j) % 2 == 0
    }
)
# Expected output: A set of tuples meeting the given conditions.


# -----------------------------------------------------------------------------
# 8. Transpose a 2D Matrix Using List Comprehension
# -----------------------------------------------------------------------------

# Description: Given a 2D list (matrix), this code transposes it,
# i.e., rows become columns and vice versa.
#
# Input: A matrix such as:
#   [[1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]]
#
# Output: The transposed matrix:
#   [[1, 4, 7],
#    [2, 5, 8],
#    [3, 6, 9]]
# Expected output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



