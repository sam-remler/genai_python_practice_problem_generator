"""### Title: Finding the Missing Number

**Difficulty:** Medium

**Problem Statement:**
Write a function `find_missing_number(arr: List[int], n: int) -> int` that takes an array of integers `arr` containing `n` integers from 1 to `n+1` (inclusive) with one integer missing. The function should return the missing integer.

**Input Format:**
- `arr` (List[int]): A list of integers where integers are in the range from 1 to `n+1` with exactly one number missing.
- `n` (int): The number of integers that should be in the array (which means the array's length will be `n`).

**Output Format:**
- Returns a single integer representing the missing number in the sequence.

**Constraints:**
- The length of `arr` is `n` where `1 <= n <= 10^6`.
- The integers present in the array are unique.
- The integers in the array are positive integers.
  
**Example Test Cases:**

**Test Case 1:**
```python
Input: arr = [2, 3, 1, 5], n = 4
Output: 4
```

**Test Case 2:**
```python
Input: arr = [1, 2, 3], n = 3
Output: 4
```

**Test Case 3:**
```python
Input: arr = [2], n = 1
Output: 1
```

**Test Case 4:**
```python
Input: arr = [3, 7, 1, 2, 8], n = 5
Output: 4
```

### Edge Cases:
1. An empty `arr` (with n = 1) should return 1.
2. All numbers except for the last number are present in the array.

**Function Signature:**
```python
from typing import List

def find_missing_number(arr: List[int], n: int) -> int:
    pass
```

**Time Complexity Requirement:**
- The solution should ideally operate in O(n) time.

**Space Complexity Requirement:**
- The solution should ideally operate in O(1) space."""

def missing_int(lst : list) -> int:
    
    if lst == []:
        return 1
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] != lst[i+1] - 1:
            return lst[i] + 1
    
    return None

print(missing_int([1,2,3,4]))
