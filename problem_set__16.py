"""Sure! Here's a new Python coding challenge that meets your criteria:

---

**Title:** Count Prime Numbers in a Range

**Difficulty:** Easy

**Problem Statement:**  
Write a function called `count_primes_in_range(start: int, end: int) -> int` that takes two integers, `start` and `end`, representing the range of numbers (inclusive). The function should return the total count of prime numbers within that range.

A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The only even prime number is 2. Any number less than 2 is not prime.

**Input Format:**  
- Two integers, `start` and `end` (1 ≤ start ≤ end ≤ 10^6).

**Output Format:**  
- An integer representing the count of prime numbers in the given range.

**Example Test Cases:**

1. **Input:** `count_primes_in_range(10, 20)`  
   **Output:** `4`  
   **Explanation:** The prime numbers are 11, 13, 17, 19.

2. **Input:** `count_primes_in_range(1, 10)`  
   **Output:** `4`  
   **Explanation:** The prime numbers are 2, 3, 5, 7.

3. **Input:** `count_primes_in_range(20, 30)`  
   **Output:** `2`  
   **Explanation:** The prime numbers are 23, 29.

---

Feel free to reach out if you need further assistance or more challenges!"""

def count_primes_in_range(lower_bound : int, upper_bound : int):
    primes = set()
    for num in range(2, upper_bound+1):
        is_prime = all(num % prime != 0 for prime in primes if prime <= num**0.5)
        if is_prime:
            primes.add(num)

    valid_primes = {num for num in primes if num >= lower_bound}
    return valid_primes

print(count_primes_in_range(2,75))
print(count_primes_in_range(20,30))

