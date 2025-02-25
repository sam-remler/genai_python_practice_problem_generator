"""```python
# Title: Count Characters in a String
# Difficulty: Medium

# Problem Statement:
# Write a function that takes a string as input and returns a dictionary that maps each character 
# in the string to the number of times it appears in the string. 
# The function should be case-sensitive, meaning 'a' and 'A' should be counted as different characters.

# Input Format:
# A single string (1 <= length of string <= 10^5). The string may contain letters (uppercase and lowercase), 
# digits, punctuation, and whitespace.

# Output Format:
# A dictionary where keys are characters from the input string and values are the counts of those characters.

# Constraints:
# - The function should handle large strings efficiently.
# - Ignore any characters that are not in the printable range (ASCII 32 to 126).

# Example Test Cases:

# Test Case 1:
input_str_1 = "Hello, World!"
# Expected Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}

# Test Case 2:
input_str_2 = "Python Programming 123!"
# Expected Output: {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 2, 'r': 2, 'g': 1, 'a': 1, 'm': 1, 'i': 1, '1': 1, '2': 1, '3': 1, '!': 1}

# Test Case 3:
input_str_3 = "    "
# Expected Output: {' ': 4}
``` 

### Function Signature:
```python
def count_characters(input_str: str) -> dict:
    pass
```

### Time Complexity:
- O(n) where n is the length of the input string, as we need to traverse the string once to count characters.

### Space Complexity:
- O(k) where k is the number of distinct characters in the string, since we are storing counts in a dictionary."""

def count_char(string : str) -> dict:
    char_count = {}
    for char in string:
        char_count.setdefault(char,0)
        char_count[char] += 1
    
    return char_count

print(count_char("Hello World"))
