import sys
from collections import deque

### 입력값

# 열, 행
N, M = map(int, sys.stdin.readline().rstrip().split())

# 행렬
arr = []
for _ in range(M):
    row = list(sys.stdin.readline().rstrip())
    arr.append(row)

# 움직일 수 있는 범위
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

### BFS
def bfs(r, c):
    q = deque([(r, c, 0)])
    arr[r][c] = '0'
    infection_time = [[-1]*N for _ in range(M)] # 오염 시간을 기록하는 배열
    infection_time[r][c] = 0
    max_death_time = 0
    
    while q:
        r, c, sec = q.popleft()
        death_time = sec+3
        max_death_time=max(death_time, max_death_time)
        
        for dr, dc in dir_guide:
            nr=r+dr
            nc=c+dc
            
            # 예외 경우 
            if nr<0 or nr>=M or nc<0 or nc>=N: continue # 배열 범위 밖
            if arr[nr][nc]=='0': continue # 이미 죽음
            if infection_time[nr][nc] != -1: continue # 이미 오염됨(이미 방문)
            
            # 만약 저글링이 있다면
            infection_time[nr][nc] = sec+1
            q.append([nr, nc, sec+1])
            arr[nr][nc] = '0' # 방사능 오염
            
    remaining=0
    for r in range(M):
        for c in range(N):
            if arr[r][c] == '1' and infection_time[r][c] == -1: # 살아있고 감염도 안됨
                remaining+=1
    
    print(max_death_time)
    print(remaining)
    
# 시작 위치(1을 기준으로 주어짐)
c, r = map(int, sys.stdin.readline().rstrip().split())
bfs(r-1, c-1)