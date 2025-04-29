import sys

N = int(sys.stdin.readline().rstrip())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]

visited = [[0] * N for _ in range(N)] # 방문 여부 표시

dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

def dfs(r, c):
    global cnt
    cnt+=1
    visited[r][c] = 1
    
    for dr, dc in dir_guide:
        nr = r + dr
        nc = c + dc

        # 예외 처리
        if nr<0 or nr>=N or nc<0 or nc>=N: continue # 범위를 넘어서면 넘어감
        if visited[nr][nc]: continue # 이미 방문함
        if arr[nr][nc] == '0': continue # 집이 아님

        dfs(nr, nc)

cnt_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == 0: # 집이면서 아직 방문 안함(이 경우를 찾아야 함)
            cnt=0
            dfs(i, j)
            cnt_lst.append(cnt)

print(len(cnt_lst))
print(*sorted(cnt_lst), sep='\n')