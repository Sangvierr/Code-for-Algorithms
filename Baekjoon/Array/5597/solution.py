import sys

arr = [False] * 30

for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    arr[n - 1] = True

for i in range(30):
    if not arr[i]:
        print(i + 1)