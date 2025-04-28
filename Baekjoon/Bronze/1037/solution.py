import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

if N == 1:
    print(lst[0]**2)
else:
    lst.sort()
    print(lst[0]*lst[-1])