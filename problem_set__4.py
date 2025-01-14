"""### Title: Subarray Sum Equals K

**Difficulty:** Medium

**Problem Statement:**  
Given an array of integers and an integer `k`, find the total number of continuous subarrays whose sum equals to `k`.

**Input Format:**  
- An integer array `nums` of length `n` (-10^5 ≤ `nums[i]` ≤ 10^5).
- An integer `k` (-10^9 ≤ `k` ≤ 10^9).

**Output Format:**  
- An integer representing the number of continuous subarrays whose sum equals `k`.

**Constraints:**  
- The length of the array `n` is between 1 and 10^5.  
- Your solution should have a time complexity of O(n).

**Example Test Cases:**

1. **Input:**  
   ```python
   nums = [1, 1, 1]
   k = 2
   ```
   **Output:**  
   ```python
   2
   ```
   **Explanation:** The subarrays [1, 1] (from index 0 to 1) and [1, 1] (from index 1 to 2) both sum to 2.

2. **Input:**  
   ```python
   nums = [1, 2, 3]
   k = 3
   ```
   **Output:**  
   ```python
   2
   ```
   **Explanation:** The subarrays [3] (index 2) and [1, 2] (indices 0 to 1) both sum to 3.

3. **Input:**  
   ```python
   nums = [-1, -1, 1]
   k = 0
   ```
   **Output:**  
   ```python
   1
   ```
   **Explanation:** The subarray [-1, -1, 1] (from index 0 to 2) sums to 0.

4. **Input:**  
   ```python
   nums = [1, 2, 3, 4, 5]
   k = 15
   ```
   **Output:**  
   ```python
   0
   ```
   **Explanation:** There are no continuous subarrays that sum up to 15.

### Implementation Hint:
To solve the problem efficiently, you may utilize a hashmap (dictionary in Python) to store the cumulative sum up to each index and track how many times each cumulative sum has been seen. This allows you to determine how many times a subarray summing to `k` ends at each index."""


def subarray_sum_equals_k(array : list, k : int): 
   count = 0
   cumulative_sum = 0

   for i in range(len(array) + 1):
      if sum(array[0:i]) == k:
         count += 1
   
   return count

nums = [1, 2, 3]
k = 3

def subarray_sum_equals_k_v2(array: list, k: int):
    # Initialize a hashmap to store cumulative sum frequencies
    # Key: cumulative sum, Value: frequency of this sum
    sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1
    
    curr_sum = 0  # Track the cumulative sum
    count = 0     # Track count of valid subarrays
    
    for num in array:
        # Add current number to running sum
        curr_sum += num

        # If (curr_sum - k) exists in hashmap, it means we have found
        # subarrays that sum to k ending at current position
        if curr_sum - k in sum_freq:
            count += sum_freq[curr_sum - k]
        
        # Update frequency of current cumulative sum
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        print (sum_freq)
        print(curr_sum)
        print(count)
    return count


print(subarray_sum_equals_k_v2(nums, k))