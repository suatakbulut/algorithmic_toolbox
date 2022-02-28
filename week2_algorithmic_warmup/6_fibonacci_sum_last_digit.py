# Uses python3
import random
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum_efficient(n):
    """ 
    Let's utilize our observation in the previous question. 
    """
    first_sequence_until_zero = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7]
    S = len(first_sequence_until_zero) # S =  15
    total = sum(first_sequence_until_zero) % 10  # total = 6

    f_S = first_sequence_until_zero[-1] # f_S = 7
    d = (n+1) // S
    r = (n+1) % S

    tot = ((f_S ** d - 1) / (f_S - 1))  % 10
    rem = sum(first_sequence_until_zero[:r]) % 10

    return int( (tot*total+ (f_S**(d))*rem) % 10 )
    

def stress_test():
    n_max = 50
    num_test = 25
    passed = True
    for _ in range(num_test):
        n = random.randint(2, n_max)
        if fibonacci_sum_efficient(n) == fibonacci_sum_naive(n):
            print(f"for n={n}, it passes the stress test")
        else:
            print(f"\nfor n={n}, it FAILS the stress test\n")
            passed = False
    return passed


if __name__ == "__main__":
    if stress_test():        
        print(f"\n{fibonacci_sum_efficient.__name__} passed all the test cases.")
        print("Please enter n to calculate the last digit of sum of first n Fibonaccis")
        input = sys.stdin.readline()
        n = int(input.strip())    
        print(fibonacci_sum_efficient(n))
    else:
        print(f"\n{fibonacci_sum_efficient.__name__} failed some test cases. Please debug its problem")
