# Naive Solution 
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_efficient(a, b):
    """
    if d is the greatest common divisor of a and b, then 
        a = d * a' 
        b = d * b' 
    for some a' and b' such that they are relatively prime numbers
    Thus, lcm(a,b) = a'*b'*d = (a*b)/d
    """
    def gcd_euclidiean(a, b): 
        g, s = max(a,b), min(a,b) 
        if s == 0:
            return g 
        else:
            g_remainder = g % s 
            return gcd_euclidiean(g_remainder, s) 
    gcd = gcd_euclidiean(a, b)
    return int((a*b)/gcd)

if __name__ == '__main__':
    input = input() 
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))

