# Uses python3
from re import A
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
    r=0  r=1      r=2      r=3     r=4    ... r= N
    ==============================================================
    0     1        1        2       3     ... f_S      d = 0   (S)
    ==============================================================
    0     f_S     f_S     2*f_S   3*f_S   ... f_S^2    d = 1
    0     f_S^2  f_S^2  2*f_S^2  3*f_S^2  ... f_S^3    d = 2
    """
    first_sequence_until_zero = [0, 1]
    while True:
        new_fib = (first_sequence_until_zero[-1] + first_sequence_until_zero[-2]) % m 
        if new_fib:
            first_sequence_until_zero.append(new_fib % m)
        else:
            break 
    
    S = len(first_sequence_until_zero)
    f_S = first_sequence_until_zero[-1]
    d = n // S
    r = n % S
    multiplier = first_sequence_until_zero[r]
    
    return multiplier*(f_S**d)



if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_efficient(n, m))
