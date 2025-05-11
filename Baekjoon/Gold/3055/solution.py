# 최단 거리를 찾는 문제 => BFS
# visited는 -1로 초기화 후 거리로 갱신
# sr, sc, er, ec 등을 미리 찾아두기
# 종료조건은 'D'에 도착하면, 다 돌아도 못 찾으면 "KAKTUS"

from collections import deque

# 입력값
R, C = map(int, input().strip().split())
arr = []
for _ in range(R):
    row = input().strip()
    arr.append([s for s in row])

# 상우하좌
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# BFS
def bfs(sr, sc, er, ec):
    q = deque() # 시작 행, 시작 열, 물 여부 (0은 또치, 1은 물)
    
    # 물을 먼저 인큐해서 확산되도록 함
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '*':
                q.append((r, c, 1))

    q.append((sr, sc, 0))
    visited = [[-1]*C for _ in range(R)]
    visited[sr][sc] = 0

    while q:
        r, c, is_water = q.popleft()

        # 도착 여부 확인
        if not is_water and (r, c) == (er, ec):
            return visited[r][c]

        for dr, dc in dir_guide:
            nr=dr+r
            nc=dc+c

            if 0<=nr<R and 0<=nc<C: # 범위 내에 있다면
                if not is_water: # 또치
                    if (arr[nr][nc] == 'D' or arr[nr][nc] == '.'):
                        if visited[nr][nc] == -1: # 아직 방문 안 함
                            q.append((nr, nc, 0))
                            visited[nr][nc] = visited[r][c]+1
                elif is_water: # 물
                    if (arr[nr][nc]=='.' or arr[nr][nc] == 'S'):
                        if arr[nr][nc] == 'S':
                            arr[nr][nc] = '*'
                        else:
                            arr[nr][nc] = '*'
                        q.append((nr, nc, 1))

    return "KAKTUS"

# sr, sc, er, ec 탐색
sr, sc, er, ec = -1, -1, -1, -1
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'S': # 또치
            sr, sc = r, c
        elif arr[r][c] == 'D': # 도착
            er, ec = r, c
        
print(bfs(sr, sc, er, ec))