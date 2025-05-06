from collections import deque

N, M = map(int, input().strip().split()) # 열,행
arr = []
for _ in range(M):
    row = list(input().strip())
    arr.append(row)
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

# BFS
def bfs(r, c):
    q = deque([(r, c, 0)])
    arr[r][c] = '0' # 죽임
    visited = [[-1]*N for _ in range(M)]
    visited[r][c] = 0 # 감염됨
    max_death_time = 0

    while q:
        r, c, sec = q.popleft()
        death_time = sec+3
        max_death_time=max(max_death_time, death_time)

        for dr, dc in dir_guide:
            nr=r+dr
            nc=c+dc

            if nr<0 or nc<0 or nr>=M or nc>=N: continue
            if arr[nr][nc] == '0': continue # 이미 죽음
            if visited[nr][nc] != -1: continue

            visited[nr][nc] = 0
            q.append((nr, nc, sec+1))
            arr[nr][nc] = '0'
    
    reamin=0
    for r in range(M):
        for c in range(N):
            if arr[r][c] != '0' and visited[r][c] == -1: # 살아있고 방문 안 함
                reamin+=1

    print(max_death_time)
    print(reamin)

# 시작 위치(1을 기준으로 주어짐)
c, r = map(int, input().strip().split())
bfs(r-1, c-1)