import sys

N = int(sys.stdin.readline().rstrip())

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(N))