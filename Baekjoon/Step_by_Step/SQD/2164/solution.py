import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    # drop
    if q:
        q.popleft()
    
    # go back
    if len(q) > 1:
        if q:
            f = q.popleft()
            q.append(f)

if q:
    print(q[0])