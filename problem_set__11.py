"""### Title: FizzBuzz Variation

**Difficulty:** Easy

**Problem Statement:**  
Write a function `fizz_buzz_variation(n)` that returns a list of strings representing the numbers from 1 to `n`. 
However, for multiples of 3, it should add "Fizz" instead of the number, for multiples of 5 it should add "Buzz",
and for numbers which are multiples of both 3 and 5, it should add "FizzBuzz".

**Input Format:**  
- An integer `n` (1 ≤ n ≤ 100) representing the upper limit of the range.

**Output Format:**  
- A list of strings representing the result of the FizzBuzz variation.

**Constraints:**  
- 1 ≤ n ≤ 100

**Example Test Cases:**

1. **Input:**  
   `n = 15`
   
   **Output:**  
   `['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']`

2. **Input:**  
   `n = 5`
   
   **Output:**  
   `['1', '2', 'Fizz', '4', 'Buzz']`

3. **Input:**  
   `n = 10`
   
   **Output:**  
   `['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']`

**Edge Cases:**  
- For the smallest input, `n = 1`, the output should simply be `['1']`. 
- For the largest input, `n = 100`, the function should handle iterating through 100 numbers effectively."""


def fizzbuzz(length : int) -> list:
    final_list = [0 for _ in range(length)]
    for i in range(length):
        if (i + 1) % 15 == 0:
            final_list[i] = "FizzBuzz"
        elif (i + 1) % 3 == 0:
            final_list[i] = "Fizz"
        elif (i + 1) % 5 == 0:
            final_list[i] = "Buzz"
        else:
            final_list[i] = i + 1
         
    return final_list

print(fizzbuzz(30))