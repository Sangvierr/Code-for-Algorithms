from collections import deque

M, N = map(int, input().strip().split()) # 열, 행
arr = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    arr.append(row)
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

# 1인 위치를 찾아서 queue에 먼저 넣어줌, 이미 1인 위치는 0일째에 익어있음
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j, 0))
            arr[i][j] = -1 # 큐에 넣어준 위치는 들어있지 않은 곳으로 간주주

def bfs():
    while q:
        r, c, time = q.popleft()

        for dr, dc in dir_guide:
            nr=r+dr
            nc=c+dc

            if nr<0 or nc<0 or nc>=M or nr>=N: continue
            if arr[nr][nc] == -1: continue

            arr[nr][nc] = -1
            q.append((nr, nc, time+1))

    for row in arr:
        if row.count(0) > 0:
            return -1
        
    return time

print(bfs())