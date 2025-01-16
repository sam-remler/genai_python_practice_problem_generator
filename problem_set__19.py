"""Here is a medium difficulty programming challenge for you:

---

**Title:** Find All Pairs With a Given Sum

**Difficulty:** Medium

**Problem Statement:**  
Given a list of integers and a target sum, find all unique pairs of integers in the list that add up to the target sum. Each pair should be reported as a tuple in ascending order of the integers, and the output should not contain duplicate pairs.

**Input Format:**  
- A list of integers, `nums`, where each integer can appear multiple times.  
- An integer, `target`, representing the target sum.

**Output Format:**  
- A list of tuples, where each tuple represents a unique pair of integers that add up to the target sum. Each tuple should be sorted in ascending order, and the result list should not have any duplicate pairs.

**Constraints:**
- The length of the list `nums` can be between 1 and 10^5.
- The integer values in `nums` can range from -10^9 to 10^9.
- The target sum, `target`, can also be between -10^9 to 10^9.

**Example Test Cases:**

1. **Input:**  
   ```python
   nums = [1, 2, 3, 2, 3, 4]  
   target = 5  
   ```  
   **Output:**  
   ```python
   [(1, 4), (2, 3)]
   ```

2. **Input:**  
   ```python
   nums = [-1, 0, 1, 2, -1, -4]  
   target = 0  
   ```  
   **Output:**  
   ```python
   [(-1, 1)]
   ```

3. **Input:**  
   ```python
   nums = [1, 1, 1, 1, 2, 2, 2]  
   target = 3  
   ```  
   **Output:**  
   ```python
   [(1, 2)]
   ```

---

This challenge tests the ability to effectively utilize data structures to find pairs, manage duplicates, and implement the logic to check for the given condition."""


def all_pairs_given_sum(number_list: list, target: int) -> list:
    seen = set()
    pairs = []
    
    for number in number_list:
        complement = target - number
        
        if complement in seen:
            # Ensure smaller number comes first in pair
            pair = (min(number, complement), max(number, complement))
            if pair not in pairs:  # Avoid duplicates
                pairs.append(pair)
        
        seen.add(number)
    
    return pairs


nums = [1, 2, 3, 2, 3, 4]  
target = 5 

print ( all_pairs_given_sum(nums , target) )

nums = [-1, 0, 1, 2, -1, -4]  
target = 0 

print ( all_pairs_given_sum(nums , target) )

nums = [1, 1, 1, 1, 2, 2, 2]  
target = 3  

print ( all_pairs_given_sum(nums , target) )

