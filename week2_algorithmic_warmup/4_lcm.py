import random
import sys


# Naive Solution 
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


# Better Solution
def lcm_efficient(a, b):
    """
    if d is the greatest common divisor of a and b, then 
        a = d * a' 
        b = d * b' 
    for some a' and b' such that they are relatively prime numbers
    Thus, lcm(a,b) = a'*b'*d = (a*b)/d
    """
    from gcd import gcd_euclidiean
    gcd = gcd_euclidiean(a, b)
    return int((a*b)/gcd)


def stress_test(N = 1000):
    num_test = 1000
    passed = True
    for _ in range(num_test):
        a = random.randint(1, N)
        b = random.randint(1, N)
        if lcm_naive(a, b) == lcm_efficient(a, b):
            print(f"for {a} and {b}, it passes the stress test")
        else:
            print(f"\nfor {a} and {b}, it FAILS the stress test\n")
            passed = False
    return passed

    
if __name__ == "__main__":
    if stress_test():        
        print(f"\n{lcm_efficient.__name__} passed all the test cases. Please enter a and b to calculate gcd(a,b)")
        input = sys.stdin.readline()
        a, b = map(int, input.split())    
        print(lcm_efficient(a, b))
    else:
        print(f"\n{lcm_efficient.__name__} failed some test cases. Please debug its problem")

