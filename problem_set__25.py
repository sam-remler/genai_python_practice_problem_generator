"""```python
# Title: Sliding Window Maximum
# Difficulty: Medium
# Problem Statement:
# Given an integer array nums and an integer k, return the maximum sliding window for each sliding window of size k.
# The sliding window moves from the start of the array to the end, one element at a time. The maximum of each window is collected in a result array.

# Input Format:
# - A list of integers, nums (1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4)
# - An integer k (1 <= k <= nums.length)

# Output Format:
# - A list of integers indicating the maximum value for each sliding window.

# Constraints:
# - Time complexity should be O(n) where n is the length of the array nums.
# - You may use additional space for the result but be cautious about memory usage.

# Example Test Cases:

# Test Case 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Test Case 2:
# Input: nums = [1], k = 1
# Output: [1]

# Test Case 3:
# Input: nums = [1,-1], k = 1
# Output: [1,-1]

# Additional Edge Cases:
# Test Case 4:
# Input: nums = [7, 2, 4, 3, 6, 5], k = 2
# Output: [7, 4, 6, 6, 6]

# Test Case 5:
# Input: nums = [4,3,6,1,8,2,7,5], k = 4
# Output: [6, 8, 8, 8]
```"""

def sliding_max_window(num_list : list, k : int) -> list:
    max_nums = []
    reversed_num_list = num_list[::-1]
    if len(num_list) <= k:
        return num_list
    for index in range(len(reversed_num_list)):

        max_nums.append( max ( reversed_num_list[index : index + k] ) )
    return max_nums[::-1]

nums = [7, 2, 4, 3, 6, 5]

print(sliding_max_window (nums, 2))

nums = [4,3,6,1,8,2,7,5]

print(sliding_max_window (nums, 4))