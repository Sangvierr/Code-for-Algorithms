# 인접 영역의 개수를 구하는 문제 => bfs
# 최단 거리가 아니기 때문에 visited를 0으로 초기화 후 방문하면 1
# 이때 경계가 유동적으로 바뀌기 때문에 이를 for문으로 확인하면 됨

from collections import deque

N = int(input())
MAX = float('-inf')
MAP = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    MAX = max(MAX, max(row))
    MAP.append(row)

#print('MAX:', MAX)

dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

# BFS
def bfs(sr, sc, arr, visited):

    q = deque([(sr, sc)])
    visited[sr][sc]=0
    cnt=1

    while q:
        r, c = q.popleft()

        for dr, dc in dir_guide:
            nr=dr+r
            nc=dc+c

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if not arr[nr][nc]: # 0이면 안전지대
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt+=1
    return cnt

area_lst = []
for i in range(0, MAX+1):
    arr = [[0]*N for _ in range(N)] # 지도

    for r in range(N):
        for c in range(N):
            if MAP[r][c] <= i: # 지대의 높이가 비 온 만큼보다 낮다면
                arr[r][c] = 1 # 잠김

    result=[]
    visited = [[0]*N for _ in range(N)] # BFS용 방문 체크
    for r in range(N):
        for c in range(N):
            if not arr[r][c] and not visited[r][c]:
                result.append(bfs(r, c, arr, visited))

    area = len(result) # 리스트의 각 원소는 인접 지대의 개수, 리스트의 길이는 인접된 지대의 총 개수
    #print(f'{i}:', area)
    area_lst.append(area) # max 쓰기 위해 첫번째 loop을 돌면서 append

print(max(area_lst))