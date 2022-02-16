"""
In this very first programming challenge, your goal is to implement a program that 
reads two digits from the standard input and prints their sum to the standard output
"""

def sum_two_digits():
    try:
        a,b = map(int, input().strip().split())
    except:
        print("please enter two digits separated by a space")
        sum_two_digits()
    print(a+b) 

if __name__ == "__main__":
    sum_two_digits()
