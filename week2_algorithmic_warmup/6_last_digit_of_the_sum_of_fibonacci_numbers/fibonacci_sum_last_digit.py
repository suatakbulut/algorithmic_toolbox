# Uses python3
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
    

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_efficient(n))
