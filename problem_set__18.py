"""```python
# Title: Longest Substring Without Repeating Characters
# Difficulty: Medium

# Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters.

# Input Format:
# A single string s where 1 <= len(s) <= 10^4. The string consists of printable ASCII characters.

# Output Format:
# An integer that represents the length of the longest substring without repeating characters.

# Constraints:
# - The input string s can have a length ranging from 1 to 10,000.
# - The characters in the string are case-sensitive (i.e., 'a' is different from 'A').

# Example Test Cases:
# Test Case 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3.

# Test Case 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Test Case 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Edge Case:
# Test Case 4:
# Input: ""
# Output: 0
# Explanation: An empty string has a length of 0.

# Test Case 5:
# Input: "dvdf"
# Output: 3
# Explanation: The answer is "vdf", with the length of 3.
```"""

def longest_substring_without_repeating_chars(string : str):

    chars = set()
    count = 0
    max_count = 0
    for index, char in enumerate(string):
        if char in chars:
            max_count = max(count, max_count)
            count = 0
        else:
            count += 1
            chars.add(char)

    return max_count

#this implementation doesnt work because it doesnt look at a rolling window, only at the ones so far

def longest_substring_without_repeating_chars(string : str):
    
    #tracks the most recent time we've seen a character
    dict = {
    }
    max_score = 0 #tracks the largest window since we've seen the same character
    score = 0

    for index, char in enumerate(string):
        
        if dict.get(char):
            score = index - dict[char] 
        
        dict[char] = index # updates the map to have the most recent location of a letter

        max_score = max(score,max_score)

    return max_score


def longest_substring_without_repeating_chars(string : str):
    
    #tracks the most recent time we've seen a character
    dict = {}
    start_position = 0
    max_score = 0 #tracks the largest window since we've seen the same character

    for index, char in enumerate(string):

        if char in dict and dict[char] > start_position: 
             # if the character has been seen before AND
             # the last time it was seen was within our view window we need to move our window up
             start_position = dict[char] + 1
        else: 
             max_score = max(max_score, index - start_position) # update our running best  
        
        dict[char] = index # updates the map to have the most recent location of a letter

    return max_score

print(longest_substring_without_repeating_chars("abcabcbb")) #3
print(longest_substring_without_repeating_chars("bbbbb")) #1
print(longest_substring_without_repeating_chars("pwwkew")) #3
