"""### Title: List Intersection

**Difficulty:** Medium

**Problem Statement:**
Write a function that takes two lists of integers and returns a list of their intersection. The intersection should contain unique elements only, meaning that each element in the result should appear only once, regardless of how many times it appears in the input lists.

**Input Format:**
- Two lists of integers, `list1` and `list2`. The lengths of the lists can vary, and the integers can be positive or negative.

**Output Format:**
- A list of integers representing the intersection of the two input lists, with all duplicates removed.

**Constraints:**
- The length of `list1` and `list2` can be in the range of 0 to 10^4.
- The elements in the lists can range from -10^6 to 10^6.

**Example Test Cases:**

1. **Example 1**
   - Input:
     ```python
     list1 = [1, 2, 2, 1]
     list2 = [2, 2]
     ```
   - Output:
     ```python
     [2]
     ```

2. **Example 2**
   - Input:
     ```python
     list1 = [4, 9, 5]
     list2 = [9, 4, 9, 8, 4]
     ```
   - Output:
     ```python
     [4, 9]
     ```

3. **Example 3**
   - Input:
     ```python
     list1 = [1, 2, 3]
     list2 = [4, 5, 6]
     ```
   - Output:
     ```python
     []
     ```

**Additional Notes:**
- Consider how you can efficiently find the intersection using data structures or built-in Python capabilities.
- Aim to implement the solution with a time complexity of O(n) where n is the total number of elements in both lists combined."""

