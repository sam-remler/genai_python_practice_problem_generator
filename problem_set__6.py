"""## Title: Sum of Even Numbers in a List

### Difficulty: Easy

### Problem Statement:
You are tasked with writing a function that takes a list of integers and returns the sum of all even numbers in the list. An even number is any integer that is divisible by 2 without a remainder.

### Input Format:
- A list of integers, which can include positive, negative, and zero values. The list may contain between 1 and 1000 integers.

### Output Format:
- An integer representing the sum of all even numbers in the input list.

### Constraints:
- The input list can have a maximum length of 1000 elements.
- Each integer in the list should be within the range of -10^6 to 10^6.

### Example Test Cases:

1. **Test Case 1:**
   - Input: `[1, 2, 3, 4, 5]`
   - Output: `6`
   - Explanation: The even numbers are 2 and 4, and their sum is 6.

2. **Test Case 2:**
   - Input: `[-2, -3, -4, 0, 5]`
   - Output: `-6`
   - Explanation: The even numbers are -2, -4, and 0, and their sum is -6.

3. **Test Case 3:**
   - Input: `[7, 11, 13]`
   - Output: `0`
   - Explanation: There are no even numbers in the list, so the sum is 0.

### Function Signature:
```python
def sum_of_even_numbers(numbers: list) -> int:
    pass  # Implement the function
```"""


def sum_even(lst : list) -> int:
   cum_sum = 0
   for i in lst:
      if i % 2 == 0:
         cum_sum += i
   return cum_sum
