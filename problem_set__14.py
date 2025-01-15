"""### Title: Count Distinct Characters in a String

**Difficulty:** Easy

**Problem Statement:**  
Write a function that counts the number of distinct characters in a given string. Consider only alphabetical characters for the count (ignore digits, punctuation, and whitespace). Both uppercase and lowercase letters should be treated as the same character (i.e., 'A' is the same as 'a').

**Input Format:**  
- A single string `s` (1 ≤ len(s) ≤ 1000), which may contain uppercase and lowercase letters, digits, punctuation, and whitespace.

**Output Format:**  
- An integer representing the count of distinct alphabetical characters in the string.

**Constraints:**  
- The input string may contain any printable ASCII characters, but your function should only count a-z and A-Z characters.

**Example Test Cases:**

1. **Input:** `"Hello, World!"`  
   **Output:** `7`  
   **Explanation:** The distinct characters are H, e, l, o, W, r, d (total of 7 unique characters).

2. **Input:** `"Python & 3.8"`  
   **Output:** `5`  
   **Explanation:** The distinct characters are P, y, t, h, o, n (total of 6 unique characters).

3. **Input:** `"    "`  
   **Output:** `0`  
   **Explanation:** There are no alphabetical characters in the string.

4. **Input:** `"abcABC! 123"`  
   **Output:** `3`  
   **Explanation:** The distinct characters are a, b, c (total of 3 unique characters counting A and a as the same).
"""

def distinct_chars(string : str) -> int:
    chars = set()
    for char in string.lower().replace(" ",""):
        if char in chars:
            pass
        elif not char.isalpha():
            pass
        else:
            chars.add(char)

    return len(chars)

print(distinct_chars("hello world"))
print(distinct_chars("Python & 3.8"))
print(distinct_chars("   "))
print(distinct_chars("abcABC! 123"))
