"""```python
# Title: Count Distinct Subsequences

# Difficulty: Medium

# Problem Statement:
# Given a string `s`, return the number of distinct subsequences of `s`.
# A subsequence is a sequence derived from another sequence where some elements may be deleted without changing the order of the remaining elements.

# Input Format:
# - A string `s` (1 ≤ |s| ≤ 1000), which consists of English letters (both lowercase and uppercase).

# Output Format:
# - An integer representing the count of distinct subsequences.

# Constraints:
# - The output must be returned modulo 10^9 + 7 to prevent overflow.

# Example Test Cases:

# Test Case 1:
# Input: "abc"
# Output: 8
# Explanation: The distinct subsequences are "", "a", "b", "c", "ab", "ac", "bc", "abc".

# Test Case 2:
# Input: "aba"
# Output: 6
# Explanation: The distinct subsequences are "", "a", "b", "ab", "aa", "aba".

# Test Case 3:
# Input: "aaa"
# Output: 3
# Explanation: The distinct subsequences are "", "a", "aa", "aaa".

# Edge Case:
# Input: ""
# Output: 1
# Explanation: The only subsequence is the empty string.
```"""

def distinct_subsequence_count(string : str):
    chars = set(sorted(string))
    return 2**(len(chars))


print(distinct_subsequence_count("abc"))

print(distinct_subsequence_count("aba"))