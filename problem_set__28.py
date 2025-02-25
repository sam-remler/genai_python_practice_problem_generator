"""
#Title: Fib with write to another file
"""
def fib(n : int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n -1) + fib(n-2)


with open('fib.txt', 'w') as f:
    for n in range(20):
        fib_num = fib(n)
        f.write(f"{n} : {fib_num} \n")