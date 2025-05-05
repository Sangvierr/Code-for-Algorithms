# 상 좌 우 하 방향으로 움직임
# 조건: 가장 가까운 쥐, 그리고 거리가 같다면 가장 위쪽, 또 같다면 가장 왼쪽 쥐를 선택

from collections import deque

N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip().split())))
dir_guide = [(-1, 0), (0, -1), (0, 1), (1, 0)]

LEVEL = 2 # 고양이 레벨
CATCH = 0 # 현재까지 잡은 쥐 개수
TIME = 0 # 총 걸린 시간

R=C=-1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            R, C = r, c # 현재 고양이의 위치
            arr[r][c] = 0 # 초기 고양이 위치를 0으로 초기화

def bfs(r, c):
    q = deque([(r, c, 0)]) # 행, 열, 시간
    visited=[[0]*N for _ in range(N)]
    visited[r][c] = 1
    target = [] # 조건에 따라 거리, 행, 열 순으로 저장

    while q:
        r, c, time = q.popleft()
        for dr, dc in dir_guide:
            nr=dr+r
            nc=dc+c

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= LEVEL: # 현재 고양이 레벨보다 작거나 같아야지만 갈 수 있음
                visited[nr][nc] = 1
                if 0 < arr[nr][nc] < LEVEL: # 갈 수 있는 애들 중에서 잡을 수 있는 애들 확인
                    target.append((time+1, nr, nc))
                q.append((nr, nc, time+1))

    if target:
        target.sort() # (거리, 행, 열) 순으로 정렬 후 가장 작은 애 리턴
        return target[0]
    else:
        return None

while True:
    target = bfs(R, C)

    if not target:
        break
    time, tr, tc = target
    TIME+=time
    R, C = tr, tc
    arr[R][C] = 0
    CATCH+=1

    if CATCH==LEVEL:
        CATCH=0
        LEVEL+=1

print(TIME)