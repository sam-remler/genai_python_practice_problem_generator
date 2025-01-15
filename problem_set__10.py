"""### Title: Unique Paths in a Grid

**Difficulty:** Medium

**Problem Statement:**  
You are given a grid of size `m x n` representing a field. 
Your task is to count the number of unique paths from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1) of the grid. 
You can only move either down or right at any point in time. 

Write a function `unique_paths(m: int, n: int) -> int` that returns the number of unique paths.

**Input Format:**  
- An integer `m` (1 ≤ m ≤ 100) representing the number of rows in the grid.
- An integer `n` (1 ≤ n ≤ 100) representing the number of columns in the grid.

**Output Format:**  
- Return an integer representing the number of unique paths from the top-left to the bottom-right of the grid.

**Constraints:**  
- The function should have a time complexity of O(m*n) and a space complexity of O(n) if using a dynamic programming approach, or O(1) if using an optimized approach.

**Example Test Cases:**

1. **Input:** `m = 3, n = 7`  
   **Output:** `28`  
   **Explanation:** There are 28 unique paths in a 3x7 grid.

2. **Input:** `m = 3, n = 2`  
   **Output:** `3`  
   **Explanation:** There are 3 unique paths in a 3x2 grid.

3. **Input:** `m = 1, n = 1`  
   **Output:** `1`  
   **Explanation:** There is only 1 unique path in a grid of size 1x1.

4. **Input:** `m = 5, n = 5`  
   **Output:** `70`  
   **Explanation:** There are 70 unique paths in a 5x5 grid.

Feel free to implement the function to solve the problem!"""

def unique_paths_dp_2d(m: int, n: int) -> int:
    """
    Solution using 2D DP array
    Time: O(m*n)
    Space: O(m*n)
    """
    # Create a 2D DP array
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]