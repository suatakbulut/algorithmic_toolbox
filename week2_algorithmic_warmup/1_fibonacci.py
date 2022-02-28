import random
import sys


# Naive Recursive Fibonacci
def fib_naive_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_naive_recursive(n - 1) + fib_naive_recursive(n - 2)


# Efficient Fibonacci 
def fib_array(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]


def stress_test(N = 30):
    num_test = 100
    passed = True
    for _ in range(num_test):
        n = random.randint(1, N)
        if fib_naive_recursive(n) == fib_array(n):
            print(f"for n={n}, it passes the stress test")
        else:
            print(f"\nfor {n}, it FAILS the stress test\n")
            passed = False
    return passed

    
if __name__ == "__main__":
    if stress_test():        
        print(f"\n{fib_array.__name__} passed all the test cases. Please enter n to calculate nth Fibonacci")
        n = int(input().strip())
        print(fib_array(n))
    else:
        print(f"\n{fib_array.__name__} failed some test cases. Please debug its problem")
