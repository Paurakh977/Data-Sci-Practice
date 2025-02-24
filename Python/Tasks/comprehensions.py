from icecream import ic
# Given a string, create a dictionary where the keys are vowels (a, e, i, o, u) and the values are the counts of each vowel in the string, using a dictionary comprehension.

def counter(string : str)-> dict[str: int]:
    return {char: string.count(char) for char in "aeiou"}

ic(counter("Paurakh"))

# without using python built in function
def counter(string : str)-> dict[str: int]:
    return { vow : sum([1 for char in string if char.lower() == vow]) for vow in "aeiou"}

ic(counter("Paurakh"))

# Description: Given a 2D list (matrix), use a list comprehension to transpose it (i.e., rows become columns and vice versa).
# Input: A matrix like [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: The transposed matrix [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# Explanation: This task deals with nested comprehensions and understanding how to access elements in a multi-dimensional list.



