import sys

N = int(sys.stdin.readline().rstrip())

take=0
while N >= 0:
    if N % 5 == 0:
        take += (N//5)
        print(take)
        break
    N -= 3
    take += 1
else:
    print(-1)