# Naive Recursive Fibonacci
def calc_fib(n):
    if n <= 1:
        return n
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

# Efficient Fibonacci 
def efficient_calc_fib(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]

if __name__ == "__main__":
    n = int(input().strip())
    print(efficient_calc_fib(n))
