"""### Title: Find the Second Largest Number in a List

**Difficulty:** Easy

**Problem Statement:**  
Write a function that takes a list of integers and returns the second largest unique number in the list. If the list has fewer than two unique numbers, return `None`.

**Input Format:**  
- A list of integers `nums` where \( 1 \leq len(nums) \leq 10^5 \) and \( -10^9 \leq nums[i] \leq 10^9 \).

**Output Format:**  
- Return an integer representing the second largest unique number in the list, or `None` if it does not exist.

**Constraints:**  
- The function should run in linear time, O(n), and use O(1) additional space complexity (aside from the input).

**Example Test Cases:**

1. **Input:**  
   `find_second_largest([3, 1, 4, 4, 2])`  
   **Output:**  
   `3`

2. **Input:**  
   `find_second_largest([5, 5, 5, 5])`  
   **Output:**  
   `None`

3. **Input:**  
   `find_second_largest([-7, -5, -1, -1])`  
   **Output:**  
   `-5`

4. **Input:**  
   `find_second_largest([10])`  
   **Output:**  
   `None`

### Function Signature:

```python
def find_second_largest(nums: List[int]) -> Optional[int]:
    pass
``` 

This structure provides a clear problem definition suitable for beginners to intermediate levels, focusing on basic data handling with a condition to account for unique values."""


def find_second_largest(nums):
    max_num = max(nums)
    second_largest = -10**10
    for num in nums:
        if (num > second_largest) & (num < max_num):
            second_largest = num
    if second_largest == -10**10:
        return None
    return second_largest

print(find_second_largest([-7, -5, -1, -1]))