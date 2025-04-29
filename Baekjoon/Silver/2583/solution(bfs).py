import sys
from collections import deque

### 세팅
M, N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

for _ in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().rstrip().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            arr[y][x] = 1

### 너비 우선 탐색
def bfs(r, c):
    que = deque([(r, c)]) # 초기값 입력
    visited[r][c] = 1 # 초기값 방문 완료
    cnt=1

    while que: # 큐에 남은 원소가 없을 때까지 반복
        r, c = que.popleft() # 맨 처음 원소 꺼내기
        for dr, dc in dir_guide:
            nr=r+dr
            nc=c+dc

            if nr<0 or nc<0 or nr>=M or nc>=N: continue # 범위 밖은 탐색 안 함
            if visited[nr][nc]: continue # 이미 방문했다면 탐색 안 함
            if arr[nr][nc]: continue # 색이 칠해져 있다면 방문 안 함함

            que.append((nr, nc))
            visited[nr][nc] = 1
            cnt+=1

    return cnt

### 탐색 수행
cnt_lst=[]
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and visited[r][c] == 0: # 찾아야 하는 부분: 색칠 안 되어 있으면서, 아직 방문 안 함
            cnt_lst.append(bfs(r, c))

print(len(cnt_lst))
print(*sorted(cnt_lst))