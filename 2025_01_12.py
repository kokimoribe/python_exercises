#################################################
# Add Tuples to Set
#################################################

def tuples_to_set(tuple_list):
    """
    Write a function that takes a list of tuples and adds them to a set.
    Return the resulting set.
    
    Example:
    tuples_to_set([(1, 2), (3, 4), (1, 2)]) -> {(1, 2), (3, 4)}
    """
    pass

def test_tuples_to_set():
    assert tuples_to_set([(1, 2), (3, 4), (1, 2)]) == {(1, 2), (3, 4)}
    assert tuples_to_set([]) == set()
    assert tuples_to_set([(1, 1), (1, 1)]) == {(1, 1)}
    assert tuples_to_set([(1,), (2,), (3,)]) == {(1,), (2,), (3,)}

#################################################
# Convert Tuples to Lists
#################################################

def tuples_to_lists(tuple_list):
    """
    Write a function that converts a list of tuples to a list of lists.
    
    Example:
    tuples_to_lists([(1, 2), (3, 4)]) -> [[1, 2], [3, 4]]
    """
    pass

def test_tuples_to_lists():
    assert tuples_to_lists([(1, 2), (3, 4)]) == [[1, 2], [3, 4]]
    assert tuples_to_lists([]) == []
    assert tuples_to_lists([(1,)]) == [[1]]
    assert tuples_to_lists([(1, 2, 3), (4, 5, 6)]) == [[1, 2, 3], [4, 5, 6]]

#################################################
# Sort Tuple Elements
#################################################

def sort_tuple_elements(tuple_list):
    """
    Write a function that sorts each tuple within a list of tuples.
    Return a new list containing the sorted tuples.
    
    Example:
    sort_tuple_elements([(3, 1, 2), (5, 4, 6)]) -> [(1, 2, 3), (4, 5, 6)]
    """
    pass

def test_sort_tuple_elements():
    assert sort_tuple_elements([(3, 1, 2), (5, 4, 6)]) == [(1, 2, 3), (4, 5, 6)]
    assert sort_tuple_elements([]) == []
    assert sort_tuple_elements([(1,)]) == [(1,)]
    assert sort_tuple_elements([(2, 1), (4, 3)]) == [(1, 2), (3, 4)]

#################################################
# Tuple Iteration
#################################################

def process_tuples(tuple_list):
    """
    Write a function that takes a list of tuples and returns a new list containing
    the sum of elements in each tuple.
    
    Example:
    process_tuples([(1, 2), (3, 4), (5, 6)]) -> [3, 7, 11]
    """
    pass

def test_process_tuples():
    assert process_tuples([(1, 2), (3, 4), (5, 6)]) == [3, 7, 11]
    assert process_tuples([(1, 1, 1), (2, 2, 2)]) == [3, 6]
    assert process_tuples([]) == []
    assert process_tuples([(5,)]) == [5]


#################################################
# Basic Data Structures
#################################################

def create_empty_structures():
    """
    Write a function that returns a tuple containing three empty data structures:
    a dictionary, a set, and a tuple, in that order.
    
    Example:
    create_empty_structures() -> ({}, set(), ())
    """
    pass

def test_create_empty_structures():
    assert len(create_empty_structures()) == 3
    assert isinstance(create_empty_structures()[0], dict)
    assert isinstance(create_empty_structures()[1], set)
    assert isinstance(create_empty_structures()[2], tuple)
    assert len(create_empty_structures()[0]) == 0
    assert len(create_empty_structures()[1]) == 0
    assert len(create_empty_structures()[2]) == 0

#################################################
# Remove Element at Index
#################################################

def remove_at_index(lst, index):
    """
    Write a function that takes a list and an index, and returns a new list
    with the element at the given index removed.
    
    Example:
    remove_at_index([1, 2, 3, 4], 1) -> [1, 3, 4]
    """
    pass

def test_remove_at_index():
    assert remove_at_index([1, 2, 3, 4], 1) == [1, 3, 4]
    assert remove_at_index([1], 0) == []
    assert remove_at_index([1, 2, 3], 2) == [1, 2]
    assert remove_at_index([1, 2, 3], 0) == [2, 3]

#################################################
# Insert Element at Index
#################################################

def insert_at_index(lst, index, value):
    """
    Write a function that takes a list, an index, and a value, and returns
    a new list with the value inserted at the given index.
    
    Example:
    insert_at_index([1, 2, 3], 1, 4) -> [1, 4, 2, 3]
    """
    pass

def test_insert_at_index():
    assert insert_at_index([1, 2, 3], 1, 4) == [1, 4, 2, 3]
    assert insert_at_index([], 0, 1) == [1]
    assert insert_at_index([1, 2], 2, 3) == [1, 2, 3]
    assert insert_at_index([1, 2], 0, 0) == [0, 1, 2]

#################################################
# Create Range
#################################################

def create_range(n):
    """
    Write a function that takes an integer n and returns a list containing
    all integers from 0 up to (but not including) n.
    
    Example:
    create_range(4) -> [0, 1, 2, 3]
    """
    pass

def test_create_range():
    assert create_range(4) == [0, 1, 2, 3]
    assert create_range(0) == []
    assert create_range(1) == [0]
    assert create_range(2) == [0, 1]

#################################################
# Get Dictionary Keys
#################################################

def get_dict_keys(d):
    """
    Write a function that takes a dictionary and returns its keys as a sorted list.
    
    Example:
    get_dict_keys({'b': 1, 'a': 2, 'c': 3}) -> ['a', 'b', 'c']
    """
    pass

def test_get_dict_keys():
    assert get_dict_keys({'b': 1, 'a': 2, 'c': 3}) == ['a', 'b', 'c']
    assert get_dict_keys({}) == []
    assert get_dict_keys({'x': 1}) == ['x']
    assert get_dict_keys({1: 'a', 2: 'b'}) == [1, 2]
