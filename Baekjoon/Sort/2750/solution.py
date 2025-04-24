import sys

T = int(sys.stdin.readline())

lst = []
for _ in range(T):
    lst.append(int(input()))

lst.sort()
print(*lst, sep='\n')