"""### Title: Anagram Groups

**Difficulty:** Medium

**Problem Statement:**
Given a list of strings, group the strings that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. Return a list of groups, where each group contains all the strings that are anagrams.

**Input Format:**
- A list of strings `words` (1 ≤ |words| ≤ 10^4), where each string consists of only lowercase English letters and has a length of at most 100 characters.

**Output Format:**
- A list of lists, where each inner list contains strings that are anagrams of one another. The order of the groups and the order of strings within each group does not matter.

**Constraints:**
- The output should be optimized for both time and space complexity.
- Ensure that the solution has a time complexity of O(N * K log K), where N is the number of words and K is the maximum length of a word.

**Example Test Cases:**

1. **Input:**
   ```python
   ["eat", "tea", "tan", "ate", "nat", "bat"]
   ```
   **Output:**
   ```python
   [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
   ```

2. **Input:**
   ```python
   ["listen", "silent", "enlist", "inlets", "hello", "world"]
   ```
   **Output:**
   ```python
   [["listen", "silent", "enlist", "inlets"], ["hello"], ["world"]]
   ```

3. **Input:**
   ```python
   ["abc", "cba", "bca", "xyz", "zyx", "wvu"]
   ```
   **Output:**
   ```python
   [["abc", "cba", "bca"], ["xyz", "zyx"], ["wvu"]]
   ```

**Note:**
- Multiple correct outputs may exist due to the different possible orderings of groups and strings."""


"""
function to determine if its an anagram with another workd
loop through each word
if its part of an existing anagram list, add it there if not create a new list, 


"""

def is_anagram(word : str, other_word : str):
   check = True
   other_letter_list = list(other_word.lower())
   if len(word) != len(other_word):
      return False 
   
   for i in word.lower():
      if i in other_letter_list:
         other_letter_list.remove(i)
      else:
         return False
   
   return True

def anagram_groups(word_list : list):
   
   # initialize a list of empty groups
   final_list = [ [""] for _ in range(len(word_list)) ]

   for word_index in range(len(word_list)):
      
      word = word_list[word_index]

      group_index = 0

      try:
         while not is_anagram(word, final_list[group_index][0]):
            group_index += 1
      except IndexError:
         pass 
      
      if group_index == len(final_list):
         final_list[word_index][0] = word_list[word_index]
      else:
         final_list[group_index].append(word_list[word_index])
   
   
   # Remove empty lists using a simple for loop
   cleaned_list = []
   remove = ['']
   
   for group in final_list:
      if group != remove:
         cleaned_list.append(group)
   
   return cleaned_list


test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = ["listen", "silent", "enlist", "inlets", "hello", "world"]
test3 = ["abc", "cba", "bca", "xyz", "zyx", "wvu"]

test_result1 = [["eat", "tea", "ate"],["tan", "nat"],["bat"] ]
test_result2 = [["listen", "silent", "enlist", "inlets"], ["hello"], ["world"]]
test_result3 = [["abc", "cba", "bca"], ["xyz", "zyx"], ["wvu"]]


assert anagram_groups(test1) == test_result1 
assert anagram_groups(test2) == test_result2
assert anagram_groups(test3) == test_result3


from collections import defaultdict

def anagram_groups_v2(words: list) -> list:
    # Use defaultdict to automatically handle new groups
    groups = defaultdict(list)
    
    # Group words by their sorted characters
    for word in words:
        # Sort the characters to create a key - all anagrams will have the same key
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        groups[sorted_word].append(word)
        print(groups)
    
    # Convert dict values to list
    return list(groups.values())

print(anagram_groups_v2(test1))