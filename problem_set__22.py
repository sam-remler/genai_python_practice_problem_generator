"""Certainly! Here's a medium difficulty coding challenge for you.

---

### Title: Balanced Parentheses Checker

**Difficulty:** Medium

**Problem Statement:**  
Write a function `is_balanced_parentheses(s: str) -> bool` that checks if the input string `s` contains a valid combination of parentheses. The string may include the characters '(', ')', '{', '}', '[' and ']'. A string is considered balanced if:
1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets are closed in the correct order.

For example, the string `{[()()]}` is balanced, while the string `{{[(])}}` is not.

**Input Format:**  
- A string `s` (1 ≤ |s| ≤ 1000) which consists only of characters '(', ')', '{', '}', '[' and ']'.

**Output Format:**  
- Return `True` if the input string `s` is balanced, otherwise return `False`.

**Constraints:**  
- The input string will only consist of the specified characters.
- The function should run with a time complexity of O(n) and a space complexity of O(n) in the worst case.

**Example Test Cases:**

1. **Input:**
   ```python
   is_balanced_parentheses("{[()()]}")
   ```
   **Output:**
   ```python
   True
   ```

2. **Input:**
   ```python
   is_balanced_parentheses("{{[(])}}")
   ```
   **Output:**
   ```python
   False
   ```

3. **Input:**
   ```python
   is_balanced_parentheses("(){}[]")
   ```
   **Output:**
   ```python
   True
   ```

4. **Input:**
   ```python
   is_balanced_parentheses("([{}])")
   ```
   **Output:**
   ```python
   True
   ```

5. **Input:**
   ```python
   is_balanced_parentheses("((())")
   ```
   **Output:**
   ```python
   False
   ```

---

This problem covers concepts of stack data structure and is suitable for intermediate-level programmers. The solution requires an understanding of how to manage opening and closing brackets effectively."""

def is_balanced_parentheses(string : str) -> bool:
    openings = {"[" : "]",
                "{" : "}",
                "(" : ")"}
    
    closings = {"]" : "[",
                "}" : "{",
                ")" : "("}
    
    open_parentheses = []
    for char in string:
        if char in openings.keys(): # if its an opening parantheses add to our open list
            open_parentheses.append(char)
        elif char in closings.keys() and len(open_parentheses) == 0: # if its a closing with no openings, not valid
            return False
        elif char in closings.keys() and closings[char] == open_parentheses[-1]: # if its a closing one and there is an opening one that works, remove the opening one
            open_parentheses.pop()
        else:
            return False 

    if len(open_parentheses) != 0: # if there are still open parantheses at the end, not valid
        return False
    
    return True

test = "([{}])"

print ( is_balanced_parentheses( test) ) # True

test = "{[()()]}"

print ( is_balanced_parentheses( test) )  # True


test = "{{[(])}}"

print ( is_balanced_parentheses( test) )  # False

test = "){[(])}}"

print ( is_balanced_parentheses( test) )  # False
