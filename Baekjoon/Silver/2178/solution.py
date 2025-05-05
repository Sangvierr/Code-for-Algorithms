# 최단 경로 찾기 문제 
# => visited에 거리 저장 
# => 따라서 visited 초기화는 -1로 하는게 좋음
# => 종료 조건: (M, N)에 도착

### 참고) 인접 1 개수 찾기 
### => visited에는 방문했다고만 표시
### => 따라서 visited 초기화는 0으로 하는게 좋음

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(M):
    row = sys.stdin.readline().rstrip()
    arr.append([int(r) for r in row])
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def bfs():
    q = deque([(0, 0)])
    visited = [[-1]*N for _ in range(M)]
    visited[0][0] = 1 # 시작점 거리는 1

    while q:
        r, c = q.popleft()

        # pop 하자마자 종료 조건 발동하는게 좋음
        if r == M-1 and c == N-1:
            return visited[r][c]

        for dr, dc in dir_guide:
            nr=dr+r
            nc=dc+c

            if 0<=nr<M and 0<=nc<N and visited[nr][nc] == -1:
                if arr[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1 # 이전 거리보다 1칸 더 감

dist = bfs()
print(dist)