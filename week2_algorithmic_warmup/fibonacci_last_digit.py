
def fibonacci_last_digit(n):
    last_digits = [0, 1]
    for _ in range(2, n+1):
        next_last_digit = last_digits[-1] + last_digits[-2] 
        last_digits.append(next_last_digit %10)
    
    return last_digits[-1]


if __name__ == '__main__':
    n = int(input().strip())
    print(fibonacci_last_digit(n))
