import sys
sys.setrecursionlimit(10**6)

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

### 깊이 우선 탐색
def dfs(r, c):
    cnt=1
    visited[r][c] = 1

    for dr, dc in dir_guide:
        nr = r + dr
        nc = c + dc
        
        # 예외조건
        if nr<0 or nc<0 or nr>=M or nc>=N: continue # 범위 밖
        if visited[nr][nc]: continue # 이미 방문
        if arr[nr][nc]: continue # 색칠 되어 있음

        cnt+=dfs(nr, nc)
    
    return cnt

### 탐색 수행
cnt_lst=[]
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and visited[r][c] == 0: # 찾아야 하는 부분: 색칠 안 되어 있으면서, 아직 방문 안 함
            cnt_lst.append(dfs(r, c))

print(len(cnt_lst))
print(*sorted(cnt_lst))