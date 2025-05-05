# 1차원 배열
# 최단거리 bfs
# visited는 -1로 초기화 후 거리로 채움

from collections import deque

subin, brother = map(int, input().split())
MAX=100001
visited = [-1]*MAX

def bfs():
    q = deque([subin])
    visited[subin] = 0

    while q:
        x = q.popleft()

        if x == brother:
            return visited[x]

        # 좌, 우, 2배 이동
        for dx in [-1, 1, 2]:
            if dx == 2:
                 nx=x*2
            else:
                nx = dx+x
            if 0<=nx<MAX and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x]+1
        
print(bfs())