import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    
    for s in S:
       print(s*R, end='')
    print()