"""```python
# Title: Flatten Nested List Iterator
# Difficulty: Medium

# Problem Statement:
# You have been given a nested list of integers, where some of the integers can themselves be lists of integers. 
# Your task is to implement a function that flattens this nested list. 
# Essentially, you will generate a single list which contains all the integers in the same order they appear, 
# but without any nested structure.

# Input Format:
# A nested list of integers: List[Union[int, List]] 
# where each element can either be an integer or a list of integers. 

# Output Format:
# A single list of integers that are flattened from the nested structure: List[int]

# Constraints:
# - The input list can have a maximum length of 1000 elements.
# - Each integer in the input can be in the range of -10^6 to 10^6.
# - The nested lists can be nested to a maximum depth of 100 levels.

# Example Test Cases:
# Test Case 1:
# Input: [1, [2, [3]], 4]
# Output: [1, 2, 3, 4]

# Test Case 2:
# Input: [[1, 2], 3, [4, [5, [6]]]]
# Output: [1, 2, 3, 4, 5, 6]

# Test Case 3:
# Input: [7, [8, 9], 10, [[11], 12], 13]
# Output: [7, 8, 9, 10, 11, 12, 13]
```"""

def flatten(num_list : list) -> list:
    while not all(type(element) == int for element in num_list):
        new_list = []
        for element in num_list:
            if type(element) == int: 
                new_list.append(element)
            elif type(element) == list: 
                new_list.extend(element)
            else:
                raise ValueError("All elements must be integers")
            
        num_list = new_list.copy()
        
    return new_list

print ( flatten ([[1, 2], 3, [4, [5, [6]]]]) )