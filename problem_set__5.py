"""Here's a medium difficulty programming challenge for you:

---

### Title: Subarray Sum

**Difficulty:** Medium

**Problem Statement:**  
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return that sum. 

Write a function `max_subarray_sum(arr: List[int]) -> int` that takes an array of integers as input and returns the maximum sum of a contiguous subarray.

**Input Format:**  
- The function receives a single parameter:  
  - `arr`: A list of integers where `1 ≤ len(arr) ≤ 10^5` and `-10^4 ≤ arr[i] ≤ 10^4`.

**Output Format:**  
- The function should return a single integer representing the maximum sum of the contiguous subarray.

**Constraints:**  
- The input array may contain both positive and negative integers.
- The solution should run in O(n) time complexity and O(1) space complexity.

**Example Test Cases:**

1. **Input:**  
   `arr = [-2,1,-3,4,-1,2,1,-5,4]`  
   **Output:**  
   `6`  
   **Explanation:** The contiguous subarray `[4,-1,2,1]` has the largest sum of `6`.

2. **Input:**  
   `arr = [1]`  
   **Output:**  
   `1`  
   **Explanation:** The only subarray is the array itself.

3. **Input:**  
   `arr = [5,4,-1,7,8]`  
   **Output:**  
   `23`  
   **Explanation:** The contiguous subarray `[5,4,-1,7,8]` has the largest sum of `23`.

4. **Input:**  
   `arr = [-1,-2,-3,-4]`  
   **Output:**  
   `-1`  
   **Explanation:** The maximum subarray is `[-1]`, with a sum of `-1`.

---

You can implement this challenge in Python to test your skills in handling arrays, sum calculations, and using an efficient algorithm like Kadane's algorithm to solve it."""


