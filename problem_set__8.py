"""### Title: Longest Consecutive Sequence

**Difficulty:** Medium

**Problem Statement:**
Given an unsorted array of integers, write a function that finds the length of the longest consecutive elements sequence. The numbers in the sequence do not need to be sorted or contiguous in the original array; they just need to be consecutive values.

Implement a function `longest_consecutive_sequence(nums: List[int]) -> int` that takes an integer array `nums` and returns the length of the longest consecutive sequence.

**Input Format:**
- A list of integers `nums` (0 ≤ |nums| ≤ 10^5), where each element can be an integer between -10^9 and 10^9.

**Output Format:**
- An integer representing the length of the longest consecutive elements sequence.

**Constraints:**
- Time complexity should be O(n).
- Space complexity should be O(n) to account for storing elements in a set.

**Example Test Cases:**

1. 
   **Input:**
   ```python
   nums = [100, 4, 200, 1, 3, 2]
   ```
   **Output:**
   ```python
   4
   ```
   **Explanation:** The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

2. 
   **Input:**
   ```python
   nums = [0, 0, 1, 1, 2, 2]
   ```
   **Output:**
   ```python
   3
   ```
   **Explanation:** The longest consecutive sequence is [0, 1, 2]. Its length is 3.

3. 
   **Input:**
   ```python
   nums = []
   ```
   **Output:**
   ```python
   0
   ```
   **Explanation:** There are no elements in the array, so the longest consecutive sequence length is 0.

4. 
   **Input:**
   ```python
   nums = [1, 2, 0, 1]
   ```
   **Output:**
   ```python
   3
   ```
   **Explanation:** The longest consecutive sequence is [0, 1, 2]. Its length is 3. 

**Note:**
- The input can contain duplicates, but they do not affect the length of the consecutive sequence. 
- The order of the input does not matter; it only needs to contain the required numbers."""

from collections import defaultdict
"""
sort the list
if the number before it is in the table add 1 to count
if not, add number to a dictionary with the count and reset the count

"""
def longest_consecutive_sequence(nums: list[int]) -> int:
    # Handle empty input
    if not nums:
        return 0
        
    # Convert list to set for O(1) lookups
    num_set = set(nums)
    print(num_set)
    max_length = 0
    
    # Check each possible sequence
    for num in num_set:
        # Only start counting if this is the start of a sequence
        # (i.e., num-1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            # Update max_length if current sequence is longer
            max_length = max(max_length, current_length)
    
    return max_length


print(longest_consecutive_sequence([1,3,3,4,5]))