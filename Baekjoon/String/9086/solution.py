import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    s = sys.stdin.readline().rstrip()
    print(s[0]+s[-1])