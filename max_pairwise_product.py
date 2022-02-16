""" 
Given a sequence of non negative integers 0<= a_0, a_1, ..., a_n-1 <= 1e5, 
find the maximum pairwise product 

Input format. 
First line contains a number 2<= n <= 2e5 - number of integers
Second line contains n non-negative integers
"""

def max_pairwise_prod(integers): 
    max_1 = max(integers) 
    integers.remove(max_1)
    max_2 = max(integers)

    return max_1 * max_2


if __name__ == "__main__":
    n = map(int, input().strip())
    integers = list(map(int, input().strip().split()))
    print(max_pairwise_prod(integers))

