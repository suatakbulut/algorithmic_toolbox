# Uses python3
import random
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_efficient(n, m):
    """
    Let S be the largest list of N numbers such that 
       S[i] = fib(i) % m and S[i] > 0 for all i>0. 
    Observe that N+i'th fibonacci number modulo m will 
    simply be S[-1] * S[i]. Using this logic, we can construct 
    the following matrix and use it to solve this problem

      r=1      r=2      r=3     r=4    ... r=S-1  r=S
    ===========================================================
       1        1        2       3     ...  f_S    0    d = 0   (S)
    ===========================================================
       f_S     f_S     2*f_S   3*f_S   ... f_S^2   0    d = 1
      f_S^2   f_S^2  2*f_S^2  3*f_S^2  ... f_S^3   0    d = 2
    """
    first_sequence_until_zero = [1, 1]
    while True:
        new_fib = (first_sequence_until_zero[-1] + first_sequence_until_zero[-2]) % m 
        first_sequence_until_zero.append(new_fib % m)
        if new_fib == 0:
            break             
    
    S = len(first_sequence_until_zero)
    f_S = first_sequence_until_zero[-2]
    d = n // S
    r = n % S
    multiplier = first_sequence_until_zero[r-1]
    res = multiplier*(f_S**d)
    return res%m


def stress_test():
    n_max = 1000
    m_max = 1000
    num_test = 100
    passed = True
    for _ in range(num_test):
        n = random.randint(2, n_max)
        m = random.randint(2, m_max)
        if get_fibonacci_huge_naive(n, m) == get_fibonacci_huge_efficient(n, m):
            print(f"for n={n} and m={m}, it passes the stress test")
        else:
            print(f"\nfor n={n} and m={m}, it FAILS the stress test\n")
            passed = False
    return passed

    
if __name__ == "__main__":
    if stress_test():        
        print(f"\n{get_fibonacci_huge_efficient.__name__} passed all the test cases. Please enter n and m to calculate nth Fibonacci in modulo m")
        input = sys.stdin.readline()
        n, m = map(int, input.split())    
        print(get_fibonacci_huge_efficient(n, m))
    else:
        print(f"\n{get_fibonacci_huge_efficient.__name__} failed some test cases. Please debug its problem")
