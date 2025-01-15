"""Sure! Here's a new Python coding challenge of easy-medium difficulty for you.

### Title: Calculate the Average of a List

**Difficulty:** Medium

#### Problem Statement:
Write a function that calculates the average of a list of numbers. The average should be computed as the sum of the numbers divided by the count of those numbers. Your function should handle both integer and floating-point numbers.

#### Input Format:
- A list of `n` numbers where `n` is the number of elements in the list. The elements can be either integers or floats.
  
#### Output Format:
- A single floating-point number representing the average of the list rounded to two decimal places. If the list is empty, the function should return `0.00`.

#### Constraints:
- The input list can contain up to 1000 elements.
- Each element value can range from -10^6 to 10^6.

#### Example Test Cases:

**Test Case 1:**
```python
input = [1, 2, 3, 4, 5]
output = 3.00
```

**Test Case 2:**
```python
input = [10.5, 20.75, 30.0]
output = 20.42
```

**Test Case 3:**
```python
input = []
output = 0.00
```

**Test Case 4:**
```python
input = [-1, 0, 1, 2]
output = 0.50
```

**Test Case 5:**
```python
input = [100, 200, 300, 400]
output = 250.00
```

### Function Signature:
```python
def calculate_average(numbers: List[float]) -> float:
```

Feel free to implement the above challenge and test your solution!"""

def list_average(list : list) -> float:
    return sum(list) / len(list)

input = [100, 200, 300, 400]
print(list_average(input))