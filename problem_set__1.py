"""Sure! Here's an easy-level Python coding challenge for you:

---

**Title:** Palindrome Checker

**Difficulty:** Easy

**Problem Statement:**  
Write a function called `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome (it reads the same forward and backward), ignoring spaces, punctuation, and letter casing. Otherwise, return `False`.

**Input Format:**  
- A single string `s` (1 ≤ len(s) ≤ 1000), which may include letters, digits, punctuation, and spaces.

**Output Format:**  
- Return a boolean value (`True` or `False`).

**Constraints:**  
- The function should handle mixed case (e.g., "A" and "a" are considered the same) and ignore spaces and punctuation.

**Example Test Cases:**

1. **Input:** `"A man, a plan, a canal, Panama"`  
   **Output:** `True`  
   **Explanation:** Ignoring spaces and punctuation, the string reads "amanaplanacanalpanama", which is a palindrome.

2. **Input:** `"Was it a car or a cat I saw?"`  
   **Output:** `True`  
   **Explanation:** Ignoring spaces and punctuation, it reads "wasitacaroracatisaw", which is a palindrome.

3. **Input:** `"Hello"`  
   **Output:** `False`  
   **Explanation:** The string does not read the same forward and backward.

4. **Input:** `"No 'x' in Nixon"`  
   **Output:** `True`  
   **Explanation:** Ignoring spaces and punctuation, it reads "noxinixon", which is a palindrome.

---

Feel free to use or modify this challenge as needed!"""


def is_palandrome(string : str) -> bool:
    
   punctuations = [" " , "," , "'" , "/" , ".", "?", "!"]
   for i in punctuations:
      string = string.replace(i,"").lower()
   
   if string == string[::-1]:
      return True
   else:
      return False

tests = [
"A man, a plan, a canal, Panama",
"Was it a car or a cat I saw?",
"Hello",
"No 'x' in Nixon",
]

for i in tests:
   print(is_palandrome(i))