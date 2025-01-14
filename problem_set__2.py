"""Sure! Here’s an easy difficulty programming challenge:

### Title: Count Vowels in a String

**Difficulty:** Easy

**Problem Statement:**  
Write a function that takes a string as input and returns the count of vowels (a, e, i, o, u) in that string. The function should be case insensitive, meaning it should count both uppercase and lowercase vowels.

**Input Format:**  
- A single string `s` (1 ≤ |s| ≤ 1000), which can include letters (uppercase and lowercase), digits, and special characters.

**Output Format:**  
- An integer that represents the number of vowels in the string.

**Constraints:**
- The input string will only contain printable ASCII characters.
  
**Example Test Cases:**

1. **Input:** `"Hello World!"`  
   **Output:** `3`  
   **Explanation:** The vowels in the string are 'e', 'o', and 'o'.

2. **Input:** `"Python Programming 123"`  
   **Output:** `3`  
   **Explanation:** The vowels in the string are 'o', 'o', and 'a'.

3. **Input:** `"AEIOUaeiou"`  
   **Output:** `10`  
   **Explanation:** All characters are vowels, so the count is 10.

4. **Input:** `"1234 & @#$%"`  
   **Output:** `0`  
   **Explanation:** There are no vowels in the string.

### Sample Function Signature:
```python
def count_vowels(s: str) -> int:
    pass
```

This problem is designed to test basic string manipulation and the use of loops and conditionals."""

def count_vowels(string : str, include_y: bool = False) -> int:
   vowels = ["a", "e", "i", "o", "u"]

   if include_y:
      vowels.append("y")

   vowel_count = 0

   for i in string.lower():
      if i in vowels:
         vowel_count += 1
   
   return vowel_count

tests = [
"Hello World!", #3
"Python Programming 123", #3
"AEIOUaeiou", #10
"1234 & @#$%", #0
]

for i in tests:
   print(count_vowels(i))