"""### Title: Group Anagrams

**Difficulty:** Medium

**Problem Statement:**  
Given a list of strings, group the anagrams together. An anagram is a word formed by rearranging the letters of a different word, typically using all the original letters exactly once. Return the result as a list of lists, where each sublist contains words that are anagrams of each other.

**Input Format:**  
- A list of strings, `words`, where 1 ≤ len(words) ≤ 1000 and 1 ≤ len(words[i]) ≤ 100 (each word is non-empty).

**Output Format:**  
- A list of lists, where each inner list contains strings that are anagrams of each other.

**Constraints:**  
- All input strings consist of lowercase English letters.
- The output should maintain the order of the first appearance of the anagrams in the input list.

**Example Test Cases:**

1.  
   **Input:**  
   `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`  
   **Output:**  
   `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`
   
2.  
   **Input:**  
   `words = [""]`  
   **Output:**  
   `[[""]]`

3.  
   **Input:**  
   `words = ["a"]`  
   **Output:**  
   `[["a"]]`

4.  
   **Input:**  
   `words = ["race", "care", "acer", "hello"]`  
   **Output:**  
   `[["race", "care", "acer"], ["hello"]]`

**Time Complexity Requirement:**  
- The solution should ideally run in O(N * K log K), where N is the number of words, and K is the maximum length of a word. This accounts for sorting each word in the list.

**Space Complexity Requirement:**  
- The space complexity should be O(N * K) to store the anagram groups."""


# sort every word
# every anagram is the same word sorted
# if the word sorted isnt in hash, add it to keys
# if it is, add it to values
# 

def group_anagrams(word_list):
    hash = {}

    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in hash.keys():
            hash[sorted_word] = [word]
        else:
            hash[sorted_word].append(word)
    
    return list(hash.values())


words = ["race", "care", "acer", "hello"]



#print (sorted ("Hello"))
print (group_anagrams (words) )