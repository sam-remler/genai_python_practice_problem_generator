"""### Title: Maximum Product Subarray

**Difficulty:** Medium

**Problem Statement:**  
Given an integer array `nums`, find the contiguous subarray within the array (containing at least one number) which has the largest product. Return the largest product you can get.

**Input Format:**  
- An integer array `nums` where `1 <= len(nums) <= 2 * 10^4` and `-10 <= nums[i] <= 10`.

**Output Format:**  
- A single integer, the maximum product of a contiguous subarray.

**Constraints:**  
- The algorithm should have a time complexity of O(n) and space complexity of O(1).

**Example Test Cases:**

1. **Input:**  
   `nums = [2, 3, -2, 4]`  
   **Output:**  
   `6`  
   **Explanation:**  
   The subarray `[2, 3]` has the largest product of 6.

2. **Input:**  
   `nums = [-2, 0, -1]`  
   **Output:**  
   `0`  
   **Explanation:**  
   The subarray `[0]` has the largest product of 0.

3. **Input:**  
   `nums = [-2, 3, -4]`  
   **Output:**  
   `24`  
   **Explanation:**  
   The subarray `[3]` has the largest product 

**Edge Cases:**  
- Input array containing only one element: e.g., `nums = [1]` should yield a product of `1`.
- Input with all negative numbers: e.g., `nums = [-3, -1, -5, -10]` should yield the largest product as the largest negative number: `-1`. 
- Input with zeros in the array: Handling zero values properly to examine the products without including them."""

