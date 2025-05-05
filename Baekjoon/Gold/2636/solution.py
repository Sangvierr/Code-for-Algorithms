import sys
from collections import deque

### 세팅
M, N = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(M):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(row)
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌
history = []
time=0

### 너비 우선 탐색
def bfs():
    que = deque([(0, 0)]) # 0, 0에서 시작
    visited = [[0]*N for _ in range(M)]
    visited[0][0] = 1
    cnt=0

    while que:
        r, c = que.popleft()
        for dr, dc in dir_guide:
            nr = r + dr
            nc = c + dc

            # 해당 조건
            if 0<=nr<M and 0<=nc<N and not visited[nr][nc]:
                visited[nr][nc] = 1 # 방문 했으니깐 체크
                if arr[nr][nc] == 0: # 가능 방향이 치즈가 아니라면
                    que.append((nr, nc)) # 그 방향도 나중에 가도록 추가
                elif arr[nr][nc] == 1: # 가능 방향이 치즈라면
                    arr[nr][nc] = 0 # 녹인다
                    cnt+=1
    return cnt

### 탐색
while True:
    cnt = bfs() # 0, 0에서 시작하기 때문에 별도 인자 없이 그냥 선언

    if cnt == 0: # 다 녹으면 끝
        print(time)
        print(history[-1])
        break
    
    history.append(sum(row.count(1) for row in arr)+cnt)
    time+=1
