# Python Programming Exercises
# Complete each function according to its docstring description.
# Each section can be converted into a separate cell in your notebook.


#################################################
# Counting Vowels
#################################################

def count_vowels(s):
    """
    Write a function to count the number of vowels in the given string `s`.
    
    Example:
    count_vowels("hello world") -> 3
    """
    pass  # Your code here

# Test Cases
assert count_vowels("hello world") == 3
assert count_vowels("python") == 1
assert count_vowels("") == 0

#################################################
# String Reversal  
#################################################

def reverse_string(s):
    """
    Write a function that reverses the input string `s`.
    Do not use the built-in reverse() method or [::-1] slicing.
    
    Example:
    reverse_string("hello") -> "olleh"
    """
    pass  # Your code here

# Test Cases
assert reverse_string("hello") == "olleh"
assert reverse_string("python") == "nohtyp"
assert reverse_string("") == ""

#################################################
# Palindrome Check
#################################################

def is_palindrome(s):
    """
    Write a function that returns True if the input string `s` is a palindrome,
    False otherwise. A palindrome reads the same forwards and backwards.
    Ignore case and non-alphanumeric characters.
    
    Example:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    """
    pass  # Your code here

# Test Cases
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("race a car") == False
assert is_palindrome("") == True

#################################################
# Replace Spaces
#################################################

def replace_spaces(s):
    """
    Write a function that replaces all spaces in the input string `s` with underscores.
    
    Example:
    replace_spaces("hello world") -> "hello_world"
    """
    pass  # Your code here

# Test Cases
assert replace_spaces("hello world") == "hello_world"
assert replace_spaces("python programming") == "python_programming"
assert replace_spaces("no spaces") == "no_spaces"
assert replace_spaces("") == ""

#################################################
# Extract Unique Words
#################################################

def extract_unique_words(s):
    """
    Write a function that extracts all unique words from the input string `s`
    and returns them as a list sorted alphabetically.
    Words are case-insensitive and separated by spaces.
    Remove any punctuation from the words.
    
    Example:
    extract_unique_words("Hello world, hello Python!") -> ["hello", "python", "world"]
    """
    pass  # Your code here

# Test Cases
assert extract_unique_words("Hello world, hello Python!") == ["hello", "python", "world"]
assert extract_unique_words("The quick brown fox") == ["brown", "fox", "quick", "the"]
assert extract_unique_words("") == []
assert extract_unique_words("word") == ["word"]

#################################################
# Fibonacci Sequence
#################################################

def fibonacci(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    The Fibonacci sequence starts with [0, 1, 1, 2, 3, 5, 8, 13, ...].
    Each number is the sum of the two preceding ones.
    Assume n >= 0.
    
    Example:
    fibonacci(6) -> 8
    """
    pass  # Your code here

# Test Cases
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(6) == 8
assert fibonacci(7) == 13

#################################################
# Finding Duplicates
#################################################

def find_duplicates(nums):
    """
    Write a function that finds all duplicates in the input list `nums`.
    Return a list of all numbers that appear more than once, in any order.
    
    Example:
    find_duplicates([1, 2, 3, 2, 1]) -> [1, 2]
    """
    pass  # Your code here

# Test Cases
assert sorted(find_duplicates([1, 2, 3, 2, 1])) == [1, 2]
assert sorted(find_duplicates([1, 2, 3, 4, 5])) == []
assert sorted(find_duplicates([1, 1, 1, 1])) == [1]

#################################################
# Prime Number Check
#################################################

def is_prime(n):
    """
    Write a function that returns True if the input number `n` is a prime number,
    False otherwise. A prime number is a number greater than 1 that has no divisors
    other than 1 and itself.
    """
    pass  # Your code here

# Test Cases
assert is_prime(2) == True
assert is_prime(17) == True
assert is_prime(1) == False
assert is_prime(4) == False

#################################################
# Find Min and Max
#################################################

def find_min_max(nums):
    """
    Write a function that finds the minimum and maximum values in the input list.
    Return them as a tuple: (min_value, max_value).
    Assume the list is non-empty.
    
    Example:
    find_min_max([3, 1, 5, 2, 4]) -> (1, 5)
    """
    pass  # Your code here

# Test Cases
assert find_min_max([3, 1, 5, 2, 4]) == (1, 5)
assert find_min_max([1, 1, 1, 1]) == (1, 1)
assert find_min_max([10]) == (10, 10)
assert find_min_max([-5, 0, 5, 10]) == (-5, 10)

#################################################
# Rotate List
#################################################

def rotate_list(nums, n):
    """
    Write a function that rotates the list to the right by n positions.
    For negative n, rotate to the left.
    
    Example:
    rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    rotate_list([1, 2, 3, 4, 5], -1) -> [2, 3, 4, 5, 1]
    """
    pass  # Your code here

# Test Cases
assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate_list([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]
assert rotate_list([1, 2, 3], 3) == [1, 2, 3]
assert rotate_list([1], 5) == [1]

#################################################
# Remove Duplicates Preserve Order
#################################################

def remove_duplicates(nums):
    """
    Write a function that removes all duplicate elements from the list
    while preserving the original order of elements.
    
    Example:
    remove_duplicates([1, 3, 3, 4, 1, 2, 2]) -> [1, 3, 4, 2]
    """
    pass  # Your code here

# Test Cases
assert remove_duplicates([1, 3, 3, 4, 1, 2, 2]) == [1, 3, 4, 2]
assert remove_duplicates([1, 1, 1, 1]) == [1]
assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
assert remove_duplicates([]) == []

#################################################
# Second Largest Number
#################################################

def find_second_largest(nums):
    """
    Write a function that finds the second-largest number in the list.
    If there is no second-largest number (empty list, list with 1 element,
    or all elements are the same), return None.
    
    Example:
    find_second_largest([3, 1, 5, 2, 4]) -> 4
    """
    pass  # Your code here

# Test Cases
assert find_second_largest([3, 1, 5, 2, 4]) == 4
assert find_second_largest([1, 1, 1, 1]) == None
assert find_second_largest([1]) == None
assert find_second_largest([2, 2, 1]) == 1

#################################################
# Flatten Nested List
#################################################

def flatten_list(nested_list):
    """
    Write a function that flattens a nested list into a single-level list.
    The input list can contain both numbers and lists of numbers.
    Preserve the order of elements.
    
    Example:
    flatten_list([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    """
    pass  # Your code here

# Test Cases
assert flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
assert flatten_list([[1, [2, 3]], [4], [], [5, 6]]) == [1, 2, 3, 4, 5, 6]
assert flatten_list([]) == []
assert flatten_list([[1], [2], [3]]) == [1, 2, 3]

#################################################
# Character Frequency
#################################################

def count_characters(s):
    """
    Write a function that counts the frequency of each character in the input string
    and returns a dictionary where keys are characters and values are their frequencies.
    Consider the count to be case-sensitive.
    
    Example:
    count_characters("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    pass  # Your code here

# Test Cases
assert count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert count_characters("aaa") == {'a': 3}
assert count_characters("") == {}
assert count_characters("Python!") == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}

#################################################
# Merge Dictionaries
#################################################

def merge_dicts(dict1, dict2):
    """
    Write a function that merges two dictionaries by summing the values of common keys.
    For keys that exist in only one dictionary, include them as is.
    
    Example:
    merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) -> {'a': 1, 'b': 5, 'c': 4}
    """
    pass  # Your code here

# Test Cases
assert merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4}
assert merge_dicts({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}
assert merge_dicts({'a': 1}, {}) == {'a': 1}
assert merge_dicts({'x': 10, 'y': 20}, {'y': 30, 'x': 40}) == {'x': 50, 'y': 50}

#################################################
# Find Maximum Value Keys
#################################################

def find_max_value_keys(d):
    """
    Write a function that returns a list of keys that correspond to the maximum value
    in the dictionary. If multiple keys share the maximum value, return all of them
    in any order.
    
    Example:
    find_max_value_keys({'a': 5, 'b': 3, 'c': 5}) -> ['a', 'c']
    """
    pass  # Your code here

# Test Cases
assert sorted(find_max_value_keys({'a': 5, 'b': 3, 'c': 5})) == ['a', 'c']
assert find_max_value_keys({'x': 1}) == ['x']
assert sorted(find_max_value_keys({'a': 10, 'b': 10, 'c': 10})) == ['a', 'b', 'c']
assert find_max_value_keys({'a': 1, 'b': 2, 'c': 3}) == ['c']

#################################################
# Invert Dictionary
#################################################

def invert_dict(d):
    """
    Write a function that inverts a dictionary, making the values keys and vice versa.
    Assume all values in the input dictionary are unique and immutable.
    
    Example:
    invert_dict({1: 'a', 2: 'b'}) -> {'a': 1, 'b': 2}
    """
    pass  # Your code here

# Test Cases
assert invert_dict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}
assert invert_dict({'hello': 123}) == {123: 'hello'}
assert invert_dict({}) == {}
assert invert_dict({True: 'yes', False: 'no'}) == {'yes': True, 'no': False}

#################################################
# Create Dictionary from Pairs
#################################################

def dict_from_pairs(pairs):
    """
    Write a function that creates a dictionary from a list of tuples,
    where each tuple contains a key-value pair.
    If a key appears multiple times, use the last occurrence.
    
    Example:
    dict_from_pairs([('a', 1), ('b', 2), ('a', 3)]) -> {'a': 3, 'b': 2}
    """
    pass  # Your code here

# Test Cases
assert dict_from_pairs([('a', 1), ('b', 2), ('a', 3)]) == {'a': 3, 'b': 2}
assert dict_from_pairs([]) == {}
assert dict_from_pairs([('x', 1)]) == {'x': 1}
assert dict_from_pairs([('a', 1), ('a', 2), ('a', 3)]) == {'a': 3}
