import sys

N = int(sys.stdin.readline().rstrip())

memo = [0] * (N+1)

def fibo(n):
    if n < 2:
        return n
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = fibo(n-1)+fibo(n-2)

    return memo[n]