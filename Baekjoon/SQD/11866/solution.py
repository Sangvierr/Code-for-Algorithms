import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque()
for i in range(1, N+1):
    q.append(i)

result = [0]*N

for i in range(N):
    for j in range(K-1):
        temp = q.popleft()
        q.append(temp)
    f = q.popleft()
    result[i] = f

print("<" + ", ".join(str(x) for x in result) + ">")