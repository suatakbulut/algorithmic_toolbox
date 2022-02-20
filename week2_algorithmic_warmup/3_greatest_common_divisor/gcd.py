# Uses python3
import sys

# Naive Solution
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# A Better Solution: 
# Euclidean Algorithm:

def gcd_euclidiean(a, b): 
    g, s = max(a,b), min(a,b) 

    if s == 0:
        return g 
    else:
        g_remainder = g % s 
        return gcd_euclidiean(g_remainder, s)

    pass 
if __name__ == "__main__":
    #input = sys.stdin.read()
    input = input() 
    a, b = map(int, input.split())
    print(gcd_euclidiean(a, b))
