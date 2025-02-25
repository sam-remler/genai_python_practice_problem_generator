"""```python
# Title: Capitalize Palindromes

# Difficulty: Medium

```
"""

def is_palindrome(string : str) -> bool:
    return string == string[::-1]

def capitalize_palindrome(sentence : str) -> str:
    new_sentence = []
    for word in sentence.split(" "):
        if is_palindrome(word):
            new_sentence.append(word.upper())
        else:
            new_sentence.append(word)
    
    return " ".join(new_sentence)

print (capitalize_palindrome ("Hey mom and dad how are you?"))