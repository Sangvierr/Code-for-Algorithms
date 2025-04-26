import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()
for num in lst:
    print(num)