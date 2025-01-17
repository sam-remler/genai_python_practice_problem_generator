"""Here is a medium difficulty coding challenge for you:

### Title: Kth Largest Element in an Array

**Difficulty:** Medium

**Problem Statement:**
Write a function that takes an unsorted array of integers and returns the kth largest element in the array. The function should be efficient and handle large input sizes optimally.

**Input Format:**
- An integer array `arr` of size `n` (1 ≤ n ≤ 10^5), where each element is an integer in the range (-10^9 ≤ arr[i] ≤ 10^9).
- An integer `k` (1 ≤ k ≤ n), where `k` indicates the position of the largest element to retrieve.

**Output Format:**
- Return an integer representing the kth largest element in the array.

**Constraints:**
- You may not use built-in sorting functions as a primary means of achieving the solution.
- Aim for a time complexity better than O(n log n).

**Example Test Cases:**

1. **Input:**
   ```python
   arr = [3, 2, 1, 5, 6, 4]
   k = 2
   ```
   **Output:**
   ```python
   5
   ```


### Notes:
- Be mindful of edge cases such as duplicates within the array.
- Aim to utilize a heap or a quickselect algorithm to find the kth largest element efficiently.
- Validate if the `k` input is within the permissible range based on the size of the array."""

def kth_largest_number(num_list : list, k : int) -> int:
    num_list.sort(reverse=True)
    
    return num_list[k-1]

arr = [3, 2, 1, 5, 6, 4]
k = 2

print  (kth_largest_number (arr, k) )