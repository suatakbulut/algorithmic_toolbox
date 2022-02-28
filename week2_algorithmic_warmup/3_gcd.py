import random
import sys


# Naive Solution
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


# A Better Solution: Euclidean Algorithm
def gcd_euclidiean(a, b): 
    """ 
    let a > b and a = d*b + a' for some integer d
    then gcd(a,b) = g(a',b)
    """
    g, s = max(a,b), min(a,b) 

    if s == 0:
        return g 
    else:
        g_remainder = g % s 
        return gcd_euclidiean(g_remainder, s)


def stress_test(N = 10000):
    num_test = 1000
    passed = True
    for _ in range(num_test):
        a = random.randint(1, N)
        b = random.randint(1, N)
        if gcd_naive(a, b) == gcd_euclidiean(a, b):
            print(f"for {a} and {b}, it passes the stress test")
        else:
            print(f"\nfor {a} and {b}, it FAILS the stress test\n")
            passed = False
    return passed


if __name__ == "__main__":
    if stress_test():        
        print(f"\n{gcd_euclidiean.__name__} passed all the test cases. Please enter a and b to calculate gcd(a,b)")
        input = sys.stdin.readline()
        a, b = map(int, input.split())    
        print(gcd_euclidiean(a, b))
    else:
        print(f"\n{gcd_euclidiean.__name__} failed some test cases. Please debug its problem")

