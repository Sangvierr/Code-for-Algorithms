from collections import deque

N = int(input().strip())
arr = []
for _ in range(N):
    row = input()
    arr.append([int(n) for n in row])
visited = [[0]*N for _ in range(N)]
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc]=1
    cnt = 1

    while q:
        r, c = q.popleft()

        for dr, dc in dir_guide:
            nr=r+dr
            nc=c+dc

            if nr<0 or nr>=N or nc<0 or nc>=N: continue
            if visited[nr][nc]: continue
            if arr[nr][nc] == 0: continue

            q.append((nr, nc))
            visited[nr][nc] = 1
            cnt+=1

    return cnt

total=[]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0 and arr[r][c] == 1:
            total.append(bfs(r, c))

print(len(total))
print(*sorted(total), sep='\n')

